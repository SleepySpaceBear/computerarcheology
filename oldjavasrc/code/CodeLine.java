package code;

import java.util.ArrayList;
import java.util.List;

import util.CU;

public class CodeLine {
			
	/**
	 * This function does a simple checksum over all data in the
	 * code lines.
	 * @param code the list of code lines
	 * @return the simple checksum
	 */
	public static long simpleDataChecksum(List<CodeLine> code) {
		long ret = 0;
		for(CodeLine line : code) {
			if(line.data!=null) {
				for(int i : line.data) {
					ret = ret + i;
				}
			}
		}		
		return ret;
	}	
	
	
	public String originalText;
				
	public int address = -1;
	public List<Integer> data = null;
	public String opcode = null;
	public int opcodePos = -1;	
	public String comment = null;
	public int commentPos = -1;
	
	public String label = null;
				
	// PrintChar:
	// 4000: 01 02 03  LDA  $500   ; This is a comment
	//
	// PureAssembly:
	// PrintChar:
	//    STA tmp1 ; This is a comment
	
	/**
	 * This creates a new CodeLine object from the given line of text.
	 * @param originalText the line of text (usually from a text file)
	 * @param filename the name of the file (for error reporting)
	 * @param line the line number (for error reporting)
	 */
	public CodeLine(String originalText) {
		
		originalText = originalText.replaceAll("(\\t|\\r?\\n)+", " ");
		
		this.originalText = originalText;
				
		// comment		
		commentPos = originalText.indexOf(";");
		if(commentPos>=0) {
			comment = originalText.substring(commentPos+1);
			originalText = originalText.substring(0,commentPos);
		}
		
		int pos = 0; // Where we are moving across the string		
		
		// label
		String [] words = originalText.trim().split(" ");
		if(words.length>0 && words[0].endsWith(":")) {
			String lab = words[0].substring(0,words[0].length()-1);
			int i = originalText.indexOf(":");
			pos = i+1;
			if(CU.isNumeric(lab,16)) {
				this.address = CU.parseInt(lab, 16);
			} else {
				this.label = lab;				
			}
		}
		
		// data
		List<Integer> dat = new ArrayList<Integer>();
		while(pos<originalText.length()) {
			if(originalText.charAt(pos)==' ') {
				pos = pos + 1;
				continue;
			}
			if(pos > originalText.length()-2) { // Can't be valid
				break;
			}
			if(pos == originalText.length()-2) { // Right on the end
				if(CU.isNumeric(originalText.substring(pos,pos+2), 16)) {
					dat.add(CU.parseInt(originalText.substring(pos,pos+2), 16));
					pos = pos + 2;
					break;
				}
			}			
			if(originalText.charAt(pos+2)!=' ') { // Not a two digit value
				break;
			}
			if(CU.isNumeric(originalText.substring(pos,pos+2), 16)) {
				dat.add(CU.parseInt(originalText.substring(pos,pos+2), 16));
				pos = pos + 2;
			} else {
				break;
			}
		}
		if(dat.size()>0) {
			this.data = dat;
		}
		
		// opcode
		this.opcode = originalText.substring(pos).trim();
		if(this.opcode.length()>0) {
			this.opcodePos = pos;			
		} else {
			this.opcode = null;
		}		
		
	}	
		
}
