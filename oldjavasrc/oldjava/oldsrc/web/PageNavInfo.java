package web;

import java.util.ArrayList;
import java.util.List;

public class PageNavInfo {
	
	
	public static String idFromText(String text) {
		String ret = "";
		for(int x=0;x<text.length();++x) {
			char c = text.charAt(x);
			if(c>='a' && c<='z') ret = ret + c;
			if(c>='A' && c<='Z') ret = ret + c;
		}
		return ret;
	}
	
	public int level;
	public String link;
	public String text;
	
	public PageNavInfo parent;
	
	public List<PageNavInfo> subs = new ArrayList<PageNavInfo>();

}
