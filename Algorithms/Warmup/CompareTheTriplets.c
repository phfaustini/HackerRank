#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int a0; 
    int a1; 
    int a2; 
    scanf("%d %d %d",&a0,&a1,&a2);
    int b0; 
    int b1; 
    int b2; 
    scanf("%d %d %d",&b0,&b1,&b2);
    int alice = 0;
    int bob = 0;
    if (a0 > b0) alice++;
    if (a1 > b1) alice++;
    if (a2 > b2) alice++;
    if (b0 > a0) bob++;
    if (b1 > a1) bob++;
    if (b2 > a2) bob++;
    printf("%i %i", alice, bob);
    
    return 0;
}
