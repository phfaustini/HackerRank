import java.io.*;
import java.util.*;
//https://www.hackerrank.com/challenges/mark-and-toys
// DONE
public class MarkandToys {

    public static void main(String[] args) {
    	Scanner scanner = new Scanner(System.in);
    	String s;
    	int n = -1;
    	int k = -1;
    	do {
    		s=scanner.nextLine();
    		if (n == -1){
    			n = Integer.parseInt(s.split(" ")[0]);
    			k = Integer.parseInt(s.split(" ")[1]);
    		}
    		else{
    			int[] toys = new int[n];
    			int value = 0;
    			int bought = 0;
    			String[] t = s.split(" ");
    			for(int i = 0; i < n; i++){
    				toys[i]= Integer.parseInt(t[i]); 
    			}
    			
    			Arrays.parallelSort(toys);
    			for (int i =0; i< n; i++)
    			{
    				if(value + toys[i] <= k){
    					bought+=1;
    					value += toys[i];
    				}
    			}
    			System.out.println(bought);
    		}
		} while (! s.isEmpty());
    }
}
