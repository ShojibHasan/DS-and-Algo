// # x = str(56565)
// def isPalindrome(n: int) -> bool:
        
//     temp=n
//     rev=0
//     while(n>0):
//         dig=n%10
//         rev=rev*10+dig
//         n=n//10
//     if(temp==rev):
//         return True
//     else:
//         return False
        
// a = isPalindrome(1000021)
// print(a)
package main

import (
    "fmt" 
    "math"
)
func main() {
    var temp,rev,dig,x int
    x = 1000021
    
    rev =0
    temp=x
    for(x>0){
        dig=x%10
        rev =rev*10+dig
        x = math.Remainder(x, 10)

    }
    if (temp==rev){
        return True
    }
    else{
        return False
    }
}

