#include<stdio.h>
#include<stdlib.h>              /* For atoi */

#define BUFFSIZE 10

/* cat INPUT | wc -l */
#define FREQSTORESIZE 10280000

/* Check if frequency is in list */
int checkfreqlist(int *, int, int); 

int main(int argc, char **argv){

  /* i and j are two counters */
  /* ch stores the character of a file */
  int ch, i=0, j=0, sum=0, dfreq, ENDFLAG=0;

  /* Buffer that stores the character  */
  char *buff;
  buff = (char *) malloc(BUFFSIZE);

  /* Store the frequency values */
  int *freqstore;
  freqstore = (int *) malloc(FREQSTORESIZE);

  FILE *fp;
  fp = fopen(argv[1], "r");

  /* Reads File continuously */
  while (ENDFLAG==0){
    while (((ch = fgetc(fp)) != EOF) && (ENDFLAG==0)){
        /* If finds a new line */
        if(ch != '\n'){

        *buff++ = ch;
        i++;
        }
        else{
        /* Adds null terminator */
        *buff = '\0';

        /* Decrements pointer to original position */
        buff -= i;
        /* Sets i back to 0 */
        i = 0;

        /* Stores Frequency */
        dfreq = atoi(buff); 

        sum += dfreq;

        ENDFLAG = checkfreqlist(freqstore, sum, j);

        if (ENDFLAG){
        break;
        }

        *(freqstore+j) = sum;
        j++;                     
      }
    }

    /* Re-read file */
    rewind(fp);
  }

  /* Prints answer */
  printf("ANSWER: %d\n", sum);
  return 1;
}

int checkfreqlist(int* freqstore, int sum, int j){ 
    /* Returns boolean */
    int i = 0;

    /* Checks */
    while(i < j){
      if (*(freqstore+i) == sum){
        return 1;
      }
      i++;
    }
    return 0;
  }
