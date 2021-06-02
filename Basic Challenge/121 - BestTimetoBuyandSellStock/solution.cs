public class Solution {
    public int MaxProfit(int[] prices) {
        int profit = 0;
        int minPrice = prices[0];
        int n = prices.Length;
        for(int i = 0; i < n; i++) {
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            } else if ((prices[i]-minPrice) > profit) {
                profit = prices[i]-minPrice;
            }
        }
        return profit;
    }
}
