#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int n; 
    int primary=0, secondary=0, sec_index_c, sec_index_r=0, output;
    scanf("%d",&n);
    sec_index_c = n-1;
    int a[n][n];
    for(int a_i = 0; a_i < n; a_i++){
       for(int a_j = 0; a_j < n; a_j++){
          scanf("%d",&a[a_i][a_j]);
          if(a_i == a_j) primary+=a[a_i][a_j];
          
          if(a_j == sec_index_c && sec_index_r == a_i)
          {
              sec_index_c--;
              sec_index_r++;
              secondary+=a[a_i][a_j];
          }
       }
    }
    output = primary - secondary;
    if (output < 1) output*=-1;
    printf("%i", output);
    return 0;
}

