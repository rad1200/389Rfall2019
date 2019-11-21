#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>

#include <openssl/rand.h>

#include "crypto.h"
#include "common.h"

#define LEDGER_FILE "ledger.bin"
#define PERMISSIONS (S_IRUSR | S_IWUSR)

const int NUM=62;

int main(int argc, char **argv) {
    char alpha[62]= {'A','B','C','D','E','F','G','H','I','J','K','L',
	 'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    	'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
    	'q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5',
    	'6','7','8','9'};
    char key[9];
    char *pass_hash, *key_hash;
    char fd_key_hash[16];
    int rand_val,x=0, y=0,fd;
    int worked=0;
    fd= open(LEDGER_FILE, O_RDONLY, PERMISSIONS);
    read(fd, fd_key_hash, 16);
   while (worked==0){ //change condition once u understand how ledger is working with this
    	key[0]=alpha[rand() % NUM];
    	key[1]=alpha[rand() % NUM];
	key[2]=alpha[rand() % NUM];
	key[3]=alpha[rand() % NUM];
	key[4]=alpha[rand() % NUM];
    	key[5]=alpha[rand() % NUM];
	key[6]=alpha[rand() % NUM];
	key[7]=alpha[rand() % NUM];
	key[8]=0;
	pass_hash=md5_hash(key, strlen(key));
	memset(pass_hash+2, 0, 14);
	key_hash= md5_hash(pass_hash, 2);
   	if(memcmp(key_hash, fd_key_hash, 16) != 0){
		/*printf("%s\n",key);*/
		worked=0;
		/*printf("%d\n",worked);*/
	} else{
		printf("%s\n",key);
		worked=1;
		free(pass_hash);
		free(key_hash);
	}

    }
}
