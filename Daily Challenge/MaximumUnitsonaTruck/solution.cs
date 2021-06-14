public class Solution {
    public int MaximumUnits(int[][] boxTypes, int truckSize) {
        int len = boxTypes.Length;
        int[] boxNumber = new int[len];
        int[] boxUnits = new int[len];
        int index = 0,res = 0,boxTotal = 0,unitTotal = 0;
        foreach (int[] boxType in boxTypes) {
            boxNumber[index] = boxType[0];
            boxUnits[index] = boxType[1];
            index++;
            boxTotal += boxType[0];
            unitTotal += boxType[0] * boxType[1];
        }
        if (truckSize > boxTotal) return unitTotal;
                                 
        Array.Sort(boxUnits,boxNumber);
        index = len-1;
        while(truckSize > 0 && index >= 0) {
            truckSize--;
            boxNumber[index]--;
            res += boxUnits[index];
            if (boxNumber[index] == 0) index--;
        }
        return res;
    }
}
