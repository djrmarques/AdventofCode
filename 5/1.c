#include<stdio.h>
#include<stdlib.h>

/* cat input | wc -c */
#define BUFFSIZE 500001

int is_related(char, char);

int main(int argc, char **argv){
  FILE *fp;
  fp = fopen(argv[1], "r");

  char buff[BUFFSIZE] = "";
  int i=0, FLAG=1;

  fgets(buff, BUFFSIZE, fp);

  while(FLAG){
    FLAG = 0;
    while (buff[i] != '\n'){
      if(buff[i] != 0){
        if (is_related(buff[i], buff[i+1])){
          buff[i] = '0';
          buff[i+1] = '0';
          FLAG = 1;
        }
      }
      i++;
    }
    /* Delete 0 from flag */
    for (int c=0; buff[c] != '\n'; c++){
      while(buff[c] == '0'){
        for (int l=c; buff[l] != '\n'; l++){
          buff[l] = buff[l+1];
        }
      }
    }
    i=0;
  }

  int count = 0;
  while (buff[count] != '\n'){
    count++;
  }
  buff[count+1] = '\0';

  FILE *fp2;
  fp2 = fopen("output", "w+");

  fprintf(fp2, "%s", buff);

  printf("%d\n", count);
}

int is_related(char c1, char c2){
  if (abs(c1 - c2) == 32){return 1;}
  else{return 0;}
}
