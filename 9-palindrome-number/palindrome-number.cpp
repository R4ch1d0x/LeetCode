class Solution {
public:
    bool isPalindrome(int x) {
        unsigned int remainder = 0,x2=0,x3=x;
        if (x< 0 ){
           return false; 
        }
        else {
            while(x> 0){
               remainder = x %10 ;
               x /=10;
               x2 = x2 *10 +remainder;
            }
            if (x2 == x3){
                return true;
            }
            else return false;
        }
        
        
    }
};