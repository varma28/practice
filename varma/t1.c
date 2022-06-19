#include<stdio.h>

void main()
{
    int n=4;
    if((n&(n-1)) == 0 && (n&(0xAA))==0)
     printf("yes");
    else
     printf("no");
    
}




