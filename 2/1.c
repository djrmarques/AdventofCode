#include<stdio.h>

#define SIZEOFBUFF 40

int main(int argc, char **argv){

  FILE *fp;
  fp = fopen(argv[1], "r");

  /* Stores Line*/
  char buf[SIZEOFBUFF];

  while(fgets(buf, sizeof(buf), fp) != NULL){

  }
  fclose(fp);
  return 0;
}
