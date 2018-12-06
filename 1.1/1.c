#include<stdio.h>
#include<stdlib.h>

#define INPUT "input"

int main(){
  int sum=0, ch, i=0;
  char *buff;
  FILE *fp;

  fp = fopen(INPUT, "r");

  while ((ch = fgetc(fp)) != EOF){
    if(ch != '\n'){

      *buff++ = ch;
      i++;
    }
    else{
      /* Decrements Pointer to first position*/
      *buff = '\0';
      buff -= i;

      sum += atoi(buff);

      /* Sets i back to 0 */
      i = 0;
    }
  }
  printf("%d\n", sum);
  return sum;
}
