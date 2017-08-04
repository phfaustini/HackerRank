import java.util.*;

public class JavaDequeue {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int m = in.nextInt();
		Deque deque = new ArrayDeque<>(m);

		for (int i = 0; i < n; i++) {
			int num = in.nextInt();
			if(deque.size() < m){
				deque.addLast(num));
			}
			else{
				
			}
		}
	}
}
