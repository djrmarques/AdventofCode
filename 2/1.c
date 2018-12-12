#include<stdio.h>
#include<string.h>

#define SIZEOFBUFF 30

/* Counts the number of threes and fours */
void count(char *, int*, int*);

/* Gets the name of the input file from argv */
int main(int argc, char **argv){

  /* Stores twos and threes */
  int n2=0, n3=0;

  FILE *fp;
  fp = fopen(argv[1], "r");

  /* Stores Line*/
  char buf[SIZEOFBUFF];

  while(fgets(buf, sizeof(buf), fp) != NULL){
    count(buf, &n2, &n3);
  }

  fclose(fp);
  printf("Answer: %d * %d = %d\n", n2, n3, n2 * n3);
  return 0;
}

void count(char *buff, int *n2, int *n3){

  /* Stores letters that were already evaluated */
  char invalid[30] = "";

  char current_char;

  int i=0, j=0, current_count=0, f2=0, f3=0;

  while(*buff != '\n'){

    current_char = *buff;

    if(!strchr(invalid, *buff)){
      invalid[i++] = *buff;

      /* Repeat loop */
      while(*buff != '\n'){
        if(*buff == current_char){
          current_count++;
        }
        j++;
        buff++;
      }
      }

    /* Increments the buffer by one */
    buff -= (j - 1);
    /* Resets j */
    j = 0;

    /* Increments counter */
    if ((current_count == 2) && !f2){
      (*n2)++;
      f2 = 1;
    }
    else if ((current_count == 3) && !f3){
      (*n3)++;
      f3 = 1;
    }

    /* Breaks out of cicle of already found twos and threes */
    if(f3 & f2){break;}

    /* Resets the count! */
    current_count=0;
  }
}
