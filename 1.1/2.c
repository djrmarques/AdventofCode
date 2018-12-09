#include<stdio.h>
#include<stdlib.h>

#define INPUT "input"
#define BUFFSIZE 10
/* cat INPUT | wc -l */
#define FREQSTORESIZE 1028

/* Check if frequency is in list */
int checkfreqlist(int *, int, int); 

void printbuffer(int*, int);

int main(){
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
  fp = fopen(INPUT, "r");

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

        /* Sums value to sum one by one */
        while (dfreq != 0){

          /* printf("midsum: %d\n", sum); */
          /* Checks if it is negative or positive */
          if(dfreq < 0){
            sum -= 1;
            dfreq +=1;
          }else{
            sum += 1;
            dfreq -=1;
          }

          /* printf("  midsum: %d\n", sum); */
          /* Checks if freq is repeated */
          /* j is the size of the frquency store buffer */
          ENDFLAG = checkfreqlist(freqstore, sum, j);

          if (ENDFLAG){
            break;
          }
        }

        /* printf("sum: %d\n", sum); */
        *(freqstore+j) = sum;
        /* printbuffer(freqstore, j); */
        j++;                     
      }
    }

      /* Reads File again  */
      /* There is probably a better way to do this */
      fp -= FREQSTORESIZE;
  }

  /* Prints answer */
  printf("ANSWER: %d\n", sum);
  /* free(buff); */
  /* free(freqstore); */
  return 1;
}

int checkfreqlist(int* freqstore, int sum, int j){ 
    /* Returns boolean */
    int i = 0;

    /* Checks */
    while(i < j){
      if (*(freqstore+i) == sum){
        printf("found ans: %d == %d\n", sum, *(freqstore+i));
        return 1;
      }
      i++;
    }
    return 0;
  }

void printbuffer(int* freqstore, int j){
    /* Returns boolean */
    int i = 0;

    printf("BUFFER: ");
    /* Checks */
    while(i <= j){
      printf("%d ", *(freqstore+i));
      i++;
    }
    printf("\n");
  }

