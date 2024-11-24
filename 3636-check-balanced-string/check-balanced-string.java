class Solution {
    public boolean isBalanced(String num) {
        int evenSum=0;
        int oddSum=0;
        char[] num1 = num.toCharArray();      

        for ( int i =0 ; i < num1.length ; i++){  //24123
            int x = Character.getNumericValue(num1[i]);

            if ((i+1) % 2 == 0){
                oddSum += x;          //oddsum = 4
            }else {
                evenSum += x;         //  evensum = 3
            }
        }

        return evenSum == oddSum;
        
    }
}