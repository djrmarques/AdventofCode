/* Awk and sed were used to filter the intput file  */
/* dl  dt  w  h */
/* 333 27  15 24 */
/* 107 608 16 18 */
/* 695 587 18 16 */
/* 435 778 25 13 */
/* 562 221 12 16 */

#include<stdio.h>

/* No reason why its 30 */
#define BUFFERSIZE 30
#define MATSIZE 1001

int main(int argc, char **argv){

  FILE *fp;
  fp = fopen(argv[1], "r");

  int mat[MATSIZE][MATSIZE] = {0};

  int dl=0, dt=0, w=0, h=0;

  int ystart=0, yend=0, xstart=0, xend=0;

  int common=0;

  /* Stores lines */
  char buff[BUFFERSIZE]="";

  while(fgets(buff, BUFFERSIZE, fp) != NULL){
    sscanf(buff, "%d %d %d %d\n", &dl, &dt, &w, &h);
    /* printf("%d %d %d %d\n", dl, dt, w, h); */

    /* Start and end Y coordinate */
    ystart = MATSIZE - dt;
    yend = ystart - h;

    /* Start and end X coordinate */
    xstart = dl;
    xend = xstart + w;

    /* Populates the matrix */
    while (ystart > yend){
      while(xstart < xend){
        mat[xstart][ystart]++;
        xstart++;
      }
    ystart--;
    xstart -= w;
    }
  }

  /* Count the common square inches */
  for(int i = 0; i < MATSIZE; i++){
    for(int j = MATSIZE; j > 0; j--){
      if (mat[i][j] >= 2){
        common++;
      }
    }
  }
  printf("%d\n", common);
}
