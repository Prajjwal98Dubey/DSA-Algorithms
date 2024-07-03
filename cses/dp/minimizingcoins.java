package cses.dp;
import java.util.Scanner;

public class minimizingcoins {
    public static int findMinimumCoins(int[] nums, int target) {
        int[] dp = new int[target + 1];
        for (int i = 0; i < target + 1; i++) {
            dp[i] = 1000001;
        }
        dp[0] = 0;
        for (int i = 1; i < target + 1; i++) {
            for (int j = 0; j < nums.length; j++) {
                if (i - nums[j] >= 0) {
                    dp[i] = Math.min(dp[i], 1 + dp[i - nums[j]]);
                }
            }
        }
        int res = dp[target] == 1000001 ? -1 : dp[target];
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String inputString = sc.nextLine();
        String[] numbers = inputString.split(" ");
        int n = Integer.parseInt(numbers[0]);
        int x = Integer.parseInt(numbers[1]);
        String coinsString = sc.nextLine();
        String[] coinsStringArr = coinsString.split(" ");
        int[] coins = new int[n];
        for (int i = 0; i < coins.length; i++) {
            coins[i] = Integer.parseInt(coinsStringArr[i]);
        }
        System.out.println(findMinimumCoins(coins, x));
        sc.close();
    }

}
