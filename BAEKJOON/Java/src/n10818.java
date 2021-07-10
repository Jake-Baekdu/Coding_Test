import java.io.*;
import java.util.StringTokenizer;

public class n10818 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		int max = Integer.MIN_VALUE;
		int min = Integer.MAX_VALUE;
		
		while(st.hasMoreTokens()) {
			int val = Integer.parseInt(st.nextToken());
			if (val > max) {
				max = val;
			}
			if (val < min) {
				min = val;
			}
		}
		System.out.println(min + " " + max);

	}

}

