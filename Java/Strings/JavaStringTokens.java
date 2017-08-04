import java.io.*;
import java.util.*;

//https://www.hackerrank.com/challenges/java-string-tokens
//DONE
public class JavaStringTokens {

	public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        if(!scan.hasNext()) { System.out.print(0);return;}
        String s = scan.nextLine();
        s = s.trim();
        int counter = 0;
        String[] tokens = s.split("[^A-Za-z]+");
        System.out.println(tokens.length);
        for (String t : tokens){
        	System.out.println(t);
        }
        scan.close();
    }
}
