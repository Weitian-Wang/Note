#include <stdio.h>
#include <stdint.h>
/**
 * Searching for first set bit index in a bitmap.
 *
 * [bitmap example]         [expected return value]
 * 0x0000 0000 0000 0000 --> -1
 * 0x0000 0000 0000 0001 --> 0
 * 0x0000 0000 0000 0002 --> 1
 * 0x0000 0000 0000 0003 --> 0
 * 0xFFFF FFFF FFFF FFFF --> 0
 * 0x0000 0100 0000 0000 --> 40
 *
 * @param[in] bitmap input
 * @return return index of the first set bit close to LSB
 */

int index_search(uint64_t bitmap)
{
    if(!bitmap) return -1;
    int rst = 0, len = 32;
    uint64_t mask = 0xFFFFFFFF;
    while(!(0x1 & bitmap)){
        if(!(mask & bitmap)){
            rst+=len;
            bitmap = bitmap>>len;
        }
        len = len/2;
        mask = mask>>len;
    }
    return rst;
}

int main(int argc, char **argv)
{
	printf("***** index_search ******\n");
	printf("%d\n", index_search(0x0000000000000000));
	printf("%d\n", index_search(0x0000000000000001));
    printf("%d\n", index_search(0x0000000000000003));
	printf("%d\n", index_search(0x0000000000000005));
	printf("%d\n", index_search(0x0000000000000002));
	printf("%d\n", index_search(0x0000000000000004));
    printf("%d\n", index_search(0x0000000000000006));
	printf("%d\n", index_search(0x0000000000000008));
	printf("%d\n", index_search(0x1000000000000000));
	printf("%d\n", index_search(0x2000000000000000));
	printf("%d\n", index_search(0x4000000000000000));
	printf("%d\n", index_search(0x8000000000000000));
	printf("%d\n", index_search(0x0000010000000000));
	/* 
    -1
    0
    0
    0
    1
    2
    1
    3
    60
    61
    62
    63
    40
     */
    return 0;
}