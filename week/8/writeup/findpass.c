#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#define BUFF_SIZE 32
#define FLAG_SIZE 32
#define PASS_SIZE 16

int main(void) {
    int i, prompt_response;
    /* password for admin to provide to dump flag */
    char *password;
    /* true if user is admin */
    uint8_t admin;
    int n=5;
    /* seed random with time so that we can password */
    while (n>0){
    srand(time(0));
    admin = 0;
    password = calloc(1, PASS_SIZE+1);
    for (i = 0; i < PASS_SIZE; i++) {
        password[i] = rand() % ('z'-' ') + ' ';
    }
    password[PASS_SIZE] = 0;

    printf("%s\n", password);
    /*free(password);*/
    n=n-1;
    sleep(1);
    }
    return 0;
}
