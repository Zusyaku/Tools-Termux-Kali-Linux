#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char **argv) {
    if (argc != 2){ 
        printf("Usage %s <file to decode>\xA", argv[0]);
        exit(1);
    }

    FILE *fromFile = fopen(argv[1], "r");
    int ch;
    int count = 0;
    printf("[*] Variables ready to go!\xA");
    printf("[*] File handled successfully!\xA");
    printf("[~] WORD: ");
    while ((ch = fgetc(fromFile)) != EOF) {
        if (ch == '\x20') {
            count++;
        } else {
            printf("%c", count);
            count = 0;
        }
    }
    printf("\n[!] DONE\xA");
}
