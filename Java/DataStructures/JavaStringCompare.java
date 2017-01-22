import java.io.*;
import java.util.*;

import javax.swing.text.StyleContext.SmallAttributeSet;

//https://www.hackerrank.com/challenges/java-string-compare
// DONE
public class JavaStringCompare {

	public static void main(String[] args) {
    	/* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    	Scanner in = new Scanner(System.in);
    	String line = in.nextLine();
    	int substringSize = in.nextInt();
    	String smallest = "zzz", biggest = "A";
    	
    	for(int i = 0; i<line.length()-substringSize+1; i++){
    		if (line.substring(i, i+substringSize).compareTo(smallest) < 0){
    			smallest = line.substring(i, i+substringSize);
    		}
    		if (line.substring(i, i+substringSize).compareTo(biggest) > 0){
    			biggest = line.substring(i, i+substringSize);
    		}
    	}
    	System.out.println(smallest);
    	System.out.println(biggest);
    }
}