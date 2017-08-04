import java.io.*;
import java.util.*;
//https://www.hackerrank.com/challenges/java-anagrams
//DONE
public class JavaAnagrams {
	static boolean isAnagram(String a, String b) {
		a = a.toLowerCase();
		b = b.toLowerCase();
		java.util.List<Character> stringA = new ArrayList<Character>();
		java.util.List<Character> stringB = new ArrayList<Character>();
		
		for(int i=0; i < a.length(); i++)
			stringA.add(a.charAt(i));
		for(int i=0; i < b.length(); i++)
			stringB.add(b.charAt(i));
		
		Collections.sort(stringA);
		Collections.sort(stringB);
		if(stringA.equals(stringB)) return true; else return false;

	}

	public static void main(String[] args) {

		Scanner scan = new Scanner(System.in);
		String a = scan.next();
		String b = scan.next();
		scan.close();
		boolean ret = isAnagram(a, b);
		System.out.println((ret) ? "Anagrams" : "Not Anagrams");
	}
}