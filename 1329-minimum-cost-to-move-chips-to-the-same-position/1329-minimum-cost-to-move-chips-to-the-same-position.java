class Solution {
    public int minCostToMoveChips(int[] chips) {
        int even = 0;
        for(int i:chips)
            if(i%2==0)
                even++;
        return Math.min(even,chips.length-even);
    }
}