#include <stdio.h>

int clamp_c(int value, int minimum, int maximum) {
    if (value < minimum) {
        return minimum;
    }
    if (value > maximum) {
        return maximum;
    }
    return value;
}

int main(void) {
    int failed = 0;
    if (clamp_c(5, 0, 1) != 1) {
        failed = 1;
    }
    if (clamp_c(-2, 0, 10) != 0) {
        failed = 1;
    }
    if (clamp_c(4, 0, 10) != 4) {
        failed = 1;
    }
    if (failed) {
        printf("C clamp cases failed\n");
        return 1;
    }
    printf("C clamp cases passed\n");
    return 0;
}
