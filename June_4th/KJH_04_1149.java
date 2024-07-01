// 백준 1149. RGB 거리


import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {

        // 입력을 받기 위한 BufferedReader 초기화
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        //    색칠할 집 갯수 n 입력
        int n = Integer.parseInt(bf.readLine());

        // 비용 (n X 3) 배열 초기화
        int[][] costs = new int[n][3];
        // dp ( n X 3) 배열 초기화
        int[][] dp = new int[n][3];

        // n을 순회하며 문자열을 입력
        for (int i = 0; i < n; i ++) {
            String str = bf.readLine();
            // 문자열을 공백 기준으로 분리
            String[] dataArr = str.split(" ");
            // 공배 기준으로 분리한 문자열을 정수형으로 변환하며 costs 배열 값을 변환
            for (int j = 0; j < 3; j++) {
                costs[i][j] = Integer.parseInt(dataArr[j]);
            }
        }
        // n 순회
        for (int i = 0; i < n; i++) {
            // 0, 1, 2 순회 (이중 반복문)
            for (int j = 0; j < 3; j++) {
                // 첫 번째 dp에는 이전 값이 없기 때문에 costs 배열 값 자체를 dp 배열에 저장
                if (i == 0) {
                    dp[i][j] = costs[i][j];
                } else {
                    // 두 번째 dp 부터는 이전 dp 배열에서 본인과 값이 다른 경우 중 최소값에 현재 j값을 더함
                    int minPreDp;
                    int preDp1 = dp[i-1][(j+1) % 3];
                    int preDp2 = dp[i-1][(j+2) % 3];
                    minPreDp = Math.min(preDp1, preDp2);
                    dp[i][j] = minPreDp + costs[i][j];
                }
            }
        }

        int result = 1000000;

        // 최종 dp 배열을 순회하면서 최소값 출력
        for (int i = 0; i < 3; i++) {
            int resultDp = dp[n - 1][i];
            result = Math.min(resultDp, result);
        }

        System.out.println(result);

    }
}