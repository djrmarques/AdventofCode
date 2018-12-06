#include<stdio.h>
#include<stdlib.h>

#define INPUT "input"
#define BUFFSIZE 10
/* cat INPUT | wc -l */
#define FREQSTORESIZE 1028

int repeatedfreq(int *, int, int); 

int main(){
  /* i and j are two counters */
  /* ch stores the character of a file */
  int ch, i=0, j=0, sum=0;

  /* Buffer that stores the character  */
  char *buff;
  buff = (char *) malloc(BUFFSIZE);

  /* Store the frequency values */
  int *freqstore;
  freqstore = (int *) malloc(FREQSTORESIZE);

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

      /* Stores Frequency */
      sum += atoi(buff); 
      printf("%d\n", sum);
      *freqstore++ = sum;
      j++;                     

      /* Checks if freq already exists */
      if (repeatedfreq(freqstore-j, j, sum)){
        printf("%d\n", sum);
        return 1;
      }

      /* Sets i back to 0 */
      i = 0;
    }
  }
  return 0;
}

int repeatedfreq(int *freqstore, int j, int freq){
  int i = 0;
  while(i++ < j-1){
    if (*freqstore++ == freq){return 1;}
  }
  return 0;
}
