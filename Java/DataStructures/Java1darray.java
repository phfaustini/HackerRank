import java.io.*;
import java.util.*;
//https://www.hackerrank.com/challenges/java-1d-array
//DONE

public class Java1darray {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int tests = s.nextInt();
		while (tests > 0) {
			tests--;
			int l = s.nextInt();
			int m = s.nextInt();
			int a[] = new int[l];
			for (int i = 0; i < l; i++)
				a[i] = s.nextInt();

			Deque<Integer> toVisit = new ArrayDeque<Integer>(l);
			Deque<Integer> visited = new ArrayDeque<Integer>(l);
			toVisit.add(0);

			boolean answer = false;
			while (!toVisit.isEmpty()) {
				int current = toVisit.pop();
				visited.add(current);
				if (current == (l - 1)) {
					answer = true;
					break;
				}
				if (current > 0){
					if (!visited.contains(current - 1) && a[current - 1] == 0){
						toVisit.add(current - 1);
					}
				}
				if (!visited.contains(current + 1) && a[current + 1] == 0){
					toVisit.add(current + 1);
				}
				if ((current + m) < (l)){
					if (!visited.contains(current + m) && a[current + m] == 0){
						toVisit.add(current + m);
					}
				}
				if ((current + m) >= (l)) {
					answer = true;
					break;
				}
			}
			if (answer)
				System.out.println("YES");
			else
				System.out.println("NO");

		}
		s.close();
	}
}