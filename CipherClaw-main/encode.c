#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char **argv) {
    if (argc != 3) {
        printf("Usage %s <text to encode> <file>\xA", argv[0]);
        exit(1);
    }
    char *string = argv[1];
    int i, j, length = strlen(argv[1]);
    FILE *toFile = fopen(argv[2], "w");
    for (i = 0; i < length; i++) {
        char currentChar = string[i];
        for (j = 0; j < (int)currentChar; j++){ 
            fprintf(toFile, "\x20");
        }
        fprintf(toFile, "\xA");
    }
}

