#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>

#include <openssl/rand.h>

#include "crypto.h"
#include "common.h"

const int NUM=26;

int main(int argc, char **argv) {
    char alpha[26]= {'A','B','C','D','E','F','G','H','I','J','K','L',
	 'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
    char key[3];
    int rand_val,x=0, y=0;
    key[0]=0;
   while (x<26){ //change condition once u understand how ledger is working with this
     while(y<26){
    	key[0]=alpha[x];
    	rand_val=rand() % NUM;
    	key[1]=alpha[y];
	key[2]=0;
    	printf("%s\n",key);
	key[0]=0;
	y=y+1;
    }
    x=x+1;
    y=0;
   }

}
