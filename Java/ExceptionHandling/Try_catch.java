import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

//https://www.hackerrank.com/challenges/java-exception-handling-try-catch
//DONE
public class Try_catch {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        try {
        	long x = s.nextInt();
        	long y = s.nextInt();
        	System.out.println(x/y);
		} catch (java.util.InputMismatchException e) {
			System.out.println(e.getClass().toString().split(" ")[1]);
		}
        catch (java.lang.ArithmeticException e) {
        	System.out.println(e.toString());
		}
        s.close();
    }
}