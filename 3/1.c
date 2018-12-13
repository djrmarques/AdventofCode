#include<stdio.h>

/* No reason why its 30 */
#define BUFFERSIZE 30
#define MATSIZE 1000

/* Gets height and other stuff from the string */
void evalstring(char *buff);

/* Increments values in the matrix */
void populmatrix(int dl, int dt, int w,  int h);

int main(int argc, char **argv){

  FILE *fp;
  fp = fopen(argv[1], "r");

  int mat[MATSIZE][MATSIZE];

  /* Stores lines */
  char buff[BUFFERSIZE];

  while(fgets(buff, BUFFERSIZE, fp) != NULL){
    printf("%s", buff);
  }
}
