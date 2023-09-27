#include <stdio.h>
#include "functions.c"

// main for the first exercise
int main() {
    float test = 203.5;
    printf("Original value: %f\n", test);
    printf("Original value in binary representation as a string: ");
    //    print the value in binary
    char* binary = float_to_binary(test);
    printf("%s\n", binary);

    //    switch the significand and exponent in string representation
    char* switched = switch_significand_exponent_string(binary);

    //    print the switched value
    printf("Switched Value: %s\n", switched);

    //    expand the switched string to 64 bits
    char* expanded = expand_switched_significand_exponent(switched);

    //    print the expanded value
    printf("Expanded Value: %s\n", expanded);

    return 0;
}

