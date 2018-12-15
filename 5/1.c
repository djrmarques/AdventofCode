#include<stdio.h>

/* cat input | wc -c */
#define BUFFSIZE 500001

void remove_pol(char *, int);

int main(){
  FILE *fp;
  fp = fopen("input", "r");

  char buff[BUFFSIZE];
  int i=0, FLAG=1;

  fgets(buff, BUFFSIZE, fp);

  printf("%c\n", 'a'-32);

}
