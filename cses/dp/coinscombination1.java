package cses.dp;
import java.util.Scanner;
public class coinscombination1 {
    public static long solve(int[] nums, int target) {
        // dp[x] -> number of ways to construct sum x.
        long MOD = 1000000007;
        long[] dp = new long[target + 1];
        dp[0] = 1;
        for (int i = 1; i < target + 1; i++) {
            for (int j = 0; j < nums.length; j++) {
                if (i - nums[j] >= 0) {
                    dp[i] += dp[i - nums[j]];
                    dp[i]%=MOD;
                }
            }
        }
        return dp[target];
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
        System.out.println(solve(coins, x));
        sc.close();
    }

}