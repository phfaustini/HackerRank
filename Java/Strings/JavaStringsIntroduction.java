import java.io.*;
import java.util.*;
//https://www.hackerrank.com/challenges/java-strings-introduction
//DONE
public class JavaStringsIntroduction {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        
        System.out.println(A.length() + B.length());
        int order = B.compareTo(A);
        if (order < 0) System.out.println("Yes"); else System.out.println("No");
        System.out.println(Character.toUpperCase(A.charAt(0))+A.substring(1)+" "+Character.toUpperCase(B.charAt(0))+B.substring(1));
    }
}
