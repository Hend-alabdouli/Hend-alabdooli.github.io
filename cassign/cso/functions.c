#include <stdio.h>
#include <string.h>
#include <stdlib.h>


// ------------------ First Exercise ------------------ //


// function that converts a float to a binary string
char* float_to_binary(float value)  {
    char* binary = malloc(33);
    
    unsigned int bits;
    memcpy(&bits, &value, sizeof(bits));

    // convert the bits to a binary string
    for (int i = 31; i >= 0; i--) {
        binary[i] = (bits & 1) ? '1' : '0';
        bits >>= 1;
    }
    binary[32] = '\0';
    return binary;
}

// function that switches the significand and exponent positions in string representation of float
char* switch_significand_exponent_string(char* value) {
    char* switched_value = malloc(33);
    // copy the sign
    switched_value[0] = value[0];
    
    char exponent[8];
    // copy the significand
    for (int i = 1; i < 9; i++) {
        exponent[i - 1] = value[i];
    }
    
    int i;
    for (i = 1; i < 24; i++) {
        switched_value[i] = value[i + 8];
    }

    for (int j = 0; j < 8; j++) {
        switched_value[i + j] = exponent[j];
    }

    switched_value[32] = '\0';
    return switched_value;
}

// expand the significand to 52 bits and the exponent to 11 bits
char* expand_switched_significand_exponent(char* switched_value) {
    char* expanded = malloc(65);
    // copy the sign
    expanded[0] = switched_value[0];

    char exponent[11];
    exponent[0] = switched_value[24];
    int index = 10;
    for (int i = 31; i > 24; i--) {
        exponent[index--] = switched_value[i];
    }
    while (index > 0) {
        exponent[index--] = '0';
    }

    for (int i = 1; i <= 23; i++) {
        expanded[i] = switched_value[i];
    }
    int i = 23;
    for (i = 23; i < 53; i++) {
        expanded[i] = '0';
    }

    for (int j = 0; j < 11; j++) {
        expanded[i + j] = exponent[j];
    }

    expanded[64] = '\0';
    return expanded;
}


// ------------------ Second Exercise ------------------ //
//print the value of a variable in binary
void print_binary(unsigned int  value) {
    for (int i = 31; i >= 0; i--) {
        printf("%d", (value >> i) & 1);
    }
    printf("\n");
}

// function that extracts the significand from float using bit operations
// A function that extracts the significand from the input float using bit manipulation. The function takes a float as input and returns an unsigned int containing the significand.
unsigned int get_significand(float value) {
    unsigned int bits;
    memcpy(&bits, &value, sizeof(bits));
    unsigned int significand = bits & 0x007FFFFF;
    return significand;

}

// function that extracts the exponent from float using bit operations
unsigned int get_exponent(float value) {
    unsigned int bits;
    memcpy(&bits, &value, sizeof(bits));
    unsigned int exponent = (bits & 0x7F800000);
    return exponent;
}

// function that extracts the sign from float using bit operations
unsigned int get_sign(float value) {
    unsigned int bits;
    memcpy(&bits, &value, sizeof(bits));
    unsigned int sign = (bits & 0x80000000);
    return sign;
}

// function that switches the significand and exponent positions in float using bit operations using previous functions
unsigned int switch_significand_exponent(float value) {
    unsigned int significand = get_significand(value);
    unsigned int exponent = get_exponent(value);
    unsigned int sign = get_sign(value);
    unsigned int switched = (significand << 8) | (exponent >> 23) | sign;
    return switched;
}




