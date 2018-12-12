#include<stdio.h>

#define BUFFSIZE 30
/*Number of diferent letters in the same position*/
int diffchars(char *buff1, char *buff2);

int main(int argc, char **argv){

  /* There is probably a better way to do this */
  FILE *fp1, *fp2;
  fp1 = fopen(argv[1], "r");
  fp2 = fopen(argv[1], "r");

  /* Stores the two chars */
  char buff1[BUFFSIZE], buff2[BUFFSIZE];

  while (fgets(buff1, BUFFSIZE, fp1) != NULL){
    while (fgets(buff2, BUFFSIZE, fp2) != NULL){
      if(diffchars(buff1, buff2) == 1){goto end;}
    }
    rewind(fp2);
  }


  /* Print the buffers after they are found */
  end:
  printf("%s\n%s\n", buff1, buff2);
  fclose(fp1);
  fclose(fp2);
}

int diffchars(char *buff1, char *buff2){
  /* Counter for different characters */
  int i=0, j=0;

  while(buff1[i] != '\n'){
    if (buff1[i] != buff2[i]){
      j++;
    }

    if(j > 1){return 0;}
    i++;
  }
  return j;
}
