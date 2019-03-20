package web;

import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import code.CU;
import files.LineFromFile;

public class MarkupToHTML {
	
	enum BlockType {
		NONE,
		PRE,
		PLAYME,
		HTML,
		CODE
	}
	
	Map<String,String> variables; // Any %% variables in the markup
	PageNavInfo rootPageNav;      // The navigation tree for the page
	List<String> ids;             // Unique IDs on the page
	StringBuffer body;	
	PageNavInfo navCursor;        // For moving up and down the navigation tree as we build it
	List<LineFromFile> lines;
	int pos;
	BlockType blockType = BlockType.NONE;
		
	/**
	 * We keep a list of unique IDs on the page. This method ensures the
	 * id is unique by modifying it until it is. 
	 * @param org the original (requested) id
	 * @return the actual (maybe modified) id
	 */
	String addID(String org) {
		if(!ids.contains(org)) {
			ids.add(org);
			return org;
		}		
		int un = 2;
		while(ids.contains(org+un)) {
			++un;
		}
		ids.add(org+un);
		return org+un;		
	}
	
	/**
	 * Parse the set-variable line from the markup.
	 * @param com the markup text
	 */
	void setVariable(String com) {
		int i = com.indexOf("=");
		if(i<0) {
			throw new MarkupException("Expected '=' in '"+com+"'");
		}
		String key = com.substring(2,i).trim();
		String value = com.substring(i+1).trim();
		variables.put(key,value );
		//System.out.println(":"+key+":"+value+":");
	}
	
	/**
	 * Parse all markdown links in the string and replace with HTML
	 * @param line the markdown line
	 * @return the modified line
	 */
	String fixLinks(String line) {
		while(true) {
			int i = line.indexOf('[');
			if(i<0) return line;
			int j = line.indexOf(']',i);
			if(j<0) return line;
			String text = line.substring(i+1, j);
			String link = text;
			if(j+1<line.length() && line.charAt(j+1)=='(') {
				int k = line.indexOf(')',j+1);
				if(k<0) return line;
				link = line.substring(j+2,k);
				j = k;
			}
			String rep = "<a href='"+link+"'>"+text+"</a>";
			//System.out.println(rep);
			line = line.substring(0,i)+rep+line.substring(j+1);
		}		
	}
	
	/**
	 * Parse the header and create a navigation link
	 * @param lineTrim the header line
	 */
	void parseHeader(String lineTrim) {
		int level = 0;
		while(level<lineTrim.length() && lineTrim.charAt(level)=='#') {
			++level;
		}
		
		PageNavInfo ni = new PageNavInfo();
		
		if(level>navCursor.level) {
			if(navCursor.level+1 != level) {
				throw new MarkupException("Header skipped a sublevel '"+lineTrim+"'");
			}								
			navCursor.subs.add(ni);
			navCursor = ni;					
		} else {
			for(int x=1;x<level;++x) {
				navCursor = navCursor.parent;
			}					
			navCursor.subs.add(ni);
		}
		
		ni.level = level;
		ni.parent = navCursor;
		ni.text = lineTrim.substring(level).trim();
		ni.link = addID(PageNavInfo.idFromText(ni.text));	
		
		body.append("<h"+(level+1)+" id='"+ni.link+"'>"+ni.text+"</h"+(level+1)+">\n");
	}
	
	/**
	 * Parse a list of bullets
	 * @param lineTrim the first bullet
	 */
	void parseBullet(String lineTrim) {
		// TODO multi-levels if ever needed
		--pos; // Back up to this one
		body.append("<ul>\n");
		while(pos<lines.size()) {
			lineTrim = lines.get(pos++).line.trim();			
			if(!lineTrim.startsWith("*")) break;
			lineTrim = lineTrim.substring(1).trim();
			//System.out.println(">>"+lineTrim+"<<");
			body.append("<li>"+fixHTMLText(lineTrim)+"</li>\n");
		}		
		body.append("</ul>\n");
		if(pos<lines.size()) {
			--pos;
		}
	}
	
	/**
	 * Processes links and entities.
	 * @param line the line to be HTML
	 * @return the modified line
	 */
	String fixHTMLText(String line) {
		line = fixLinks(line);
		// TODO entize
		return line;
	}
	
	/**
	 * Expand all include directives
	 * @param lines the current list of lines
	 * @param inFile the name of the input file
	 * @throws IOException file errors
	 */
	void expandIncludes(List<LineFromFile> lines,String inFile) throws IOException {
		for(int x=lines.size()-1;x>=0;--x) {
			String s = lines.get(x).line.trim();
			if(s.startsWith("%%include ")) {
				int i = inFile.lastIndexOf("/");
				List<String> inc = Files.readAllLines(Paths.get(inFile.substring(0,i+1)+s.substring(10).trim()));
				lines.remove(x);
				lines.addAll(x,LineFromFile.convert(inc, "INCLUDED FROM '"+s.substring(10).trim()));				
			}
		}
	}
	
	protected String makePageNav(String inFile, List<PageNavInfo> pageNav) {
		if(pageNav.size()<1) {
			return "";
		}
		
		int tlev = (int) pageNav.get(0).level;
		if(tlev != 1) {
			throw new RuntimeException("File '"+inFile+"' Headers must start at level 1.");
		}
		
		List<PageNavInfo> pret = new ArrayList<PageNavInfo>();
		PageNavInfo p = new PageNavInfo();
		p.level = 0;
		pret.add(p);
		
		makePageNavRecurse(inFile, pret,1,0,pageNav);
		
		List<String> lines = new ArrayList<String>();
		makePageNavHTMLRecurse(pret.get(0).subs, lines);
		
				
		return CU.listToString(lines);		
		
	}
	
	private void makePageNavHTMLRecurse(List<PageNavInfo> cur, List<String> lines) {
		for(PageNavInfo c : cur) {						
			
			String li = "<li><a href=\"#"+c.link+"\">"+c.text+"</a>";
			lines.add(li);
			
			if(c.subs!=null) {
				lines.add("<ul>");
				makePageNavHTMLRecurse(c.subs,lines);
				lines.add("</ul>");
			}
			
			lines.add("</i>");
			
		}
	}
	
	private int makePageNavRecurse(String fileName, List<PageNavInfo> parent, int level, int pos, List<PageNavInfo> pageNav) {		
		List<PageNavInfo> ret = new ArrayList<PageNavInfo>();
		while(true) {
			if(pos==pageNav.size() || pageNav.get(pos).level<level) {
				parent.get(parent.size()-1).subs = ret;
				return pos;
			}
			if(pageNav.get(pos).level == level) {
				ret.add(pageNav.get(pos));
				pos = pos + 1;
				continue;
			}
			if(pageNav.get(pos).level != (level+1)) {
				throw new RuntimeException("In '"+fileName+"' Missing header level");
			}
			pos = makePageNavRecurse(fileName, ret,level+1,pos,pageNav);		
		}				
	}
	
	private void parseBlockOpen(String lineTrim) {
		if(blockType!=BlockType.NONE) {
			System.out.println(pos);
			throw new MarkupException("No nested blocks allowed");
		}
		if(lineTrim.toUpperCase().contains("PLAYME")) {
			blockType = BlockType.PLAYME;
			body.append("<div class='playMe'><div>\n");
			return;
		}
		if(lineTrim.toUpperCase().contains("HTML")) {
			blockType = BlockType.HTML;
			return;
		}		
		if(lineTrim.toUpperCase().contains("CODE")) {
			blockType = BlockType.CODE;
			body.append("<div class='codePreStyle'><pre>\n");
			return;
		}
		if(lineTrim.length()!=3) {
			System.out.println(pos);
			throw new MarkupException("Unknown block type: "+lineTrim);
		}		
		blockType = BlockType.PRE;
		body.append("<pre>\n");
		return;				
	}
	
	private void parseBlockClose(String lineTrim) {		
		switch(blockType) {
		case PLAYME:
			body.append("</div></div>\n");
			break;
		case HTML:
			break;			
		case NONE:
			System.out.println(pos);
			throw new MarkupException("Found a close-block but wasn't in a block");		
		case PRE:
			body.append("</pre>\n");
			break;			
		case CODE:
			body.append("</pre></div>\n");
			break;
		}
		blockType = BlockType.NONE;		
	}
	
	/**
	 * Parse the given input markup file and write the HTML to the given
	 * output file.
	 * @param contentRoot the root path of the content (we may pull in other files)
	 * @param inFile the name of the input markup file 
	 * @param outFile the output file to generate
	 * @param breadCrumbs the breadcrumb string for this page
	 * @param siteNav the site navigation string (common to all pages)
	 * @param title default page title
	 * @param lines the lines of markdown
	 * @throws IOException with file operation exceptions
	 */
	public void translate(String contentRoot, String inFile, String outFile, String breadCrumbs, String siteNav,
			String title, List<LineFromFile> lines) throws IOException {
		
		this.lines = lines;
				
		int x = 0;
		boolean isCodeBlock = false;
		while(x<lines.size()) {
			boolean ic = isCodeLine(x);
			if(ic) {
				if(!isCodeBlock) {
					lines.add(x,new LineFromFile("{{{CODE","",-1));					
					isCodeBlock = true;
					x=x+1; // Skip over the newly created
				}				
			} else {
				if(isCodeBlock) {
					lines.add(x,new LineFromFile("}}}","",-1));
					isCodeBlock = false;
					x=x+1; // Skip over the newly created
				}							
			}			
			++x;
		}
								
		ids = new ArrayList<String>();
		variables = new HashMap<String,String>();
		variables.put("template", "master.template"); // Default page template
		variables.put("title", title);
		rootPageNav = new PageNavInfo();		
		rootPageNav.level = 1;		
		navCursor = rootPageNav;		
		
		body = new StringBuffer();
		
		boolean startedPElement  = false;
		
		pos = 0;
		while(pos<lines.size()) {
			String line = lines.get(pos++).line;			
			String lineTrim = line.trim();			
			
			// Set a variable's value
			if(lineTrim.startsWith("%%")) {
				setVariable(lineTrim);
				continue;
			}
			
			// Header
			if(lineTrim.startsWith("#")) {				
				parseHeader(lineTrim);							
				continue;
			}
			
			if(lineTrim.startsWith("*")) {				
				parseBullet(lineTrim);
				continue;				
			}
			
			if(lineTrim.startsWith("{{{")) {
				parseBlockOpen(lineTrim);				
				continue;				
			}
			
			if(lineTrim.startsWith("}}}")) {
				parseBlockClose(lineTrim);
				continue;
			}
			
			// TODO Tables
			
			
			if(blockType==BlockType.CODE) {
				System.out.println(lineTrim);
				// TODO				
			}
						
			if(blockType!=BlockType.HTML) { // if we are in HTML then don't do any fixing
				if(blockType!=BlockType.PRE && blockType!=BlockType.CODE) { // PRE and CODE are wrapped in <pre> ... no need to <p>
					if(lineTrim.isEmpty()) {
						// We are prepared for adjacent blank lines
						if(startedPElement) {
							body.append("</p>\n");
							startedPElement = false;
						}
					} else {
						// TODO this logic will change with <pre> and <html> elements
						if(!startedPElement) {
							body.append("<p>\n");
							startedPElement=true;
						}
					}
				}
				line = fixHTMLText(line);
			}
									
			body.append(line);
			
			body.append("\n"); // This was stripped off the original line
			continue;
			
		}
							
		// Load the template
		String templateFile = variables.get("template");		
		String template = "<!-- %%BODY%% -->";
		Path p = Paths.get(contentRoot+"/"+templateFile);
		List<String> tlines = Files.readAllLines(p);
		template = CU.listToString(tlines);		
		
		// Get page_nav fillin		
		String pageTree = makePageNav(inFile,rootPageNav.subs);
						
		// Fill in the template substitutions
		template = CU.replaceAll(template, "<!-- %%title=%% -->", variables.get("title"));		
		template = CU.replaceAll(template, "<!-- %%CONTENT_TITLE%% -->", variables.get("title"));
		template = CU.replaceAll(template, "<!-- %%BREAD_CRUMBS%% -->", breadCrumbs);
		template = CU.replaceAll(template, "<!-- %%PAGE_TREE%% -->", pageTree);
		template = CU.replaceAll(template, "<!-- %%SITE_TREE%% -->", siteNav);
		template = CU.replaceAll(template, "<!-- %%CONTENT%% -->", body.toString());
		template = CU.replaceAll(template, "<!-- %%IMAGE%% -->", variables.get("image"));
				
		// Write the output file
		PrintWriter pw = new PrintWriter(outFile);
		pw.print(template);
		pw.flush();
		pw.close();					
						
	}
	
	// A line that begins with ";" is a code line.
	// A line of the form "1234:" is a code line.
	// A blank line is code if the next line is code (a recursive check).
	// A line that starts with "Label:" is a label (a code line) if the next line
	//   is code (a recursive check).
	boolean isCodeLine(int pos) {
		if(pos>=lines.size()) return false;
		String lineTrim = lines.get(pos).line.trim();
		if(lineTrim.startsWith(";")) return true; // Code comment is code
		if(lineTrim.length()>4 && CU.isNumeric(lineTrim.substring(0, 4), 16)  && lineTrim.charAt(4)==':') {
			return true;
		}
		if(lineTrim.isEmpty()) {				
			// Blank line could be code if next line is
			// DANGEROUS RECURSION HERE			
			boolean is = isCodeLine(pos+1);
			return is;
		}
		// It could be a label
		int i = lineTrim.indexOf(":");
		if(i<0) return false; // Must have a colon
		int j = lineTrim.indexOf(" ");
		if(j>=0 && j<i) return false; // No spaces in labels		
		// It is only a label if the next line is code
		// DANGEROUS RECURSION HERE
		boolean is = isCodeLine(pos+1);
		return is;
	}
	
	// Address and Code derived classes use this
	protected void translate(String contentRoot, String inFile, String outFile, 
			String breadCrumbs, String siteNav, String nav) throws IOException 
	{
		Path ip = Paths.get(inFile);
		List<String> lines = Files.readAllLines(ip);
		List<LineFromFile> ls = LineFromFile.convert(lines, inFile);
		expandIncludes(ls,inFile);
		translate(contentRoot, inFile, outFile, breadCrumbs, siteNav, nav, ls);
	}
	
	public static void main(String [] args) throws Exception {
		MarkupToHTML m = new MarkupToHTML();
		m.translate("content/","content/Arcade/SpaceInvaders/code.cmark","test.html", "CRUMBS", "SITENAV", "NAV");
	}
	
}
