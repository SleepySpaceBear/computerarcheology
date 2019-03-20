package cleans;


import java.io.PrintStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

import code.CodeLine;
import util.CU;
import web.LineOfMarkup;
import web.MarkupToHTML;

public class ColumnSpacing {

	public static void main(String[] args) throws Exception {
		
		//List<String> lines = Files.readAllLines(Paths.get("content/arcade/defender/BankFIxed.mark"));
		List<String> lines = Files.readAllLines(Paths.get("content/coco/daggorath/code.mark"));
		
		List<LineOfMarkup> marks = LineOfMarkup.convert(lines, "");
		
		for(int pos=0;pos<marks.size();++pos) {
			LineOfMarkup mark = marks.get(pos);
			if(MarkupToHTML.isCodeLine(marks, pos)) {
				mark.codeLine = new CodeLine(mark.line);				
			}			
		}
		
		PrintStream ps = new PrintStream("out.txt");		
		
		for(LineOfMarkup mark : marks) {
			
			if(mark.codeLine!=null) {
				if(mark.codeLine.opcode!=null) {
					String s = mark.line;
					int i = s.indexOf(";");
					if(i>0) {
						String before = s.substring(0,i).trim();
						String after = s.substring(i);
						s = CU.padTo(before, 51) + after;						
					}						
					ps.println(s);
					continue;
				}
			}
			
			ps.println(mark.line);
			
			
			/*
			if(line.length()>5 && line.charAt(4)==':') {
				int i = line.indexOf(";");
				if(i<0) {
					ps.println(line);
				} else {
					String a = line.substring(0, i);
					String b = line.substring(i);
					while(a.length()<45) {
						a = a + " ";
					}
					ps.println(a+b);
				}
			} else {
				ps.println(line);
			}
			*/
			
		}
		
		ps.flush();
		ps.close();
		
	}

}
