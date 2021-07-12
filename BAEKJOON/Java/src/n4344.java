import java.util.*;
import java.io.*;
import java.util.StringTokenizer;

public class n4344 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		System.out.println();
		int c = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < c; i++) {
			String[] sarr = br.readLine().split(" ");
			double sCnt = Integer.parseInt(sarr[0]);
			double overAgvCnt = 0;
			int[] iarr = new int[(int)sCnt];
			int sum = 0;
			for(int j = 1; j <= sCnt; j++) {
				iarr[j-1] = Integer.parseInt(sarr[j]);
				sum += iarr[j-1];
				}
			double avg = sum/sCnt;
			for(int j = 0; j < sCnt; j++) {
				if (avg < iarr[j]) {
					overAgvCnt++;
				}
			}
			
			System.out.printf("%.3f%%\n",(overAgvCnt/sCnt)*100);
			
		}
		
		
	}
}
