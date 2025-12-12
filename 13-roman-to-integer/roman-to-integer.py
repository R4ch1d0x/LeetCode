class Solution:
    def romanToInt(self, s: str) -> int:
        sum1 = 0
        i=0
        while i < len(s) :
            if s[i] == "I" :
                if i != len(s)-1 and s[i+1] == "V":
                    sum1 =sum1 + 4
                    i+=1
                elif i != len(s)-1 and s[i+1] == "X":
                    sum1= sum1 + 9
                    i+=1
                else: 
                    sum1= sum1 +1


            elif s[i] == "X" :
                if i != len(s)-1 and s[i+1] == "L":
                    sum1=sum1+40 
                    i+=1
                elif i != len(s)-1 and s[i+1] == "C":
                    sum1=sum1+90
                    i+=1
                else :
                    sum1=sum1 + 10


            elif s[i] == "C":
                if  i != len(s)-1 and s[i+1] == "D":
                    sum1=sum1+400
                    i+=1
                elif i != len(s)-1 and s[i+1] == "M":
                    sum1=sum1+900
                    i+=1
                else: 
                    sum1=sum1+100

            
            elif s[i] == "V":
                sum1 =sum1+5

            elif s[i] == "L":
                sum1 =sum1+50

            elif s[i] == "D":
                sum1 =sum1+500

            elif s[i] == "M":
                sum1=sum1+1000
            
            i+=1
            
            
        return sum1
        
        