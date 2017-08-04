import java.util.*;
class JavaStack{
//https://www.hackerrank.com/challenges/java-stack
//DONE
   public static void main(String []argh)
   {
      Scanner sc = new Scanner(System.in);
      
      while (sc.hasNext()) {
         String input=sc.next();
         ArrayDeque<Character> po = new ArrayDeque<Character>();
         ArrayDeque<Character> pc = new ArrayDeque<Character>();
         ArrayDeque<Character> bo = new ArrayDeque<Character>();
         ArrayDeque<Character> bc = new ArrayDeque<Character>();
         ArrayDeque<Character> co = new ArrayDeque<Character>();
         ArrayDeque<Character> cc = new ArrayDeque<Character>();
         
         boolean answer = true;
         for (int i=0; i < input.length(); i++){
        	 if(input.charAt(i) == '(') {
        		 po.push('(');
        	 }
        	 else if(input.charAt(i) == '[') {
        		 bo.push('[');
        	 }
        	 else if(input.charAt(i) == '{') {
        		 co.push('{');
        	 }
        	 else if(input.charAt(i) == ')'){
        		 if (! po.isEmpty())
        			 po.pop();
        		 else{
        			 answer = false;
        			 break;
        		 }
        	 }
        	 else if(input.charAt(i) == ']'){
        		 if (! bo.isEmpty())
        			 bo.pop();
        		 else{
        			 answer = false;
        			 break;
        		 }
        	 }
        	 else if(input.charAt(i) == '}') {
        		 if (! co.isEmpty())
        			 co.pop();
        		 else{
        			 answer = false;
        			 break;
        		 }
        	 }
         }
         if(answer && po.isEmpty() && pc.isEmpty() && bo.isEmpty() && bc.isEmpty() && co.isEmpty() && cc.isEmpty())
        	 answer = true;
         else answer = false;
         System.out.println(answer);
      }
      sc.close();
      
   }
}
