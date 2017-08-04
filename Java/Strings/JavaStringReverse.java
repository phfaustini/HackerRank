import java.io.*;
import java.util.*;

//https://www.hackerrank.com/challenges/java-string-reverse
//DONE
public class JavaStringReverse {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        Boolean output = true;
        /* Enter your code here. Print output to STDOUT. */
        for (int i=A.length()-1, j=0; i>=0; i--, j++){
        	if (A.charAt(i) != A.charAt(j)){
        		output = false;
        		break;
        	}
        }
        if(output) System.out.println("Yes"); else System.out.println("No");
        
    }
}
