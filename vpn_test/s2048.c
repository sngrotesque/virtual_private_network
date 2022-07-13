#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <unistd.h>
#include <sys/stat.h>

#define BLOCKSIZE 256

static int encrypt(uint8_t *data, size_t len);
static int decrypt(uint8_t *data, size_t len);
static int key_padding(uint8_t *key, size_t len);
static long getfileSize(FILE *stream);
static uint8_t *file_read(FILE *stream);

static inline int encrypt(uint8_t *data, size_t len)
{
    size_t x;
    uint8_t key;
    for(x = 0; x < len; ++x) {
        data[x] = data[x] ^ 0xFF;
    }
    return 0;
}

static inline int decrypt(uint8_t *data, size_t len)
{
    return 0;
}

static inline int key_padding(uint8_t *key, size_t len)
{
    return 0;
}

static inline long getfileSize(FILE *stream)
{
	long file_size = -1;
	long cur_offset = ftell(stream);
	if (cur_offset == -1) {return -1;}
	if (fseek(stream, 0, SEEK_END) != 0) {return -1;}
	file_size = ftell(stream);
	if (file_size == -1) {return -1;}
	fseek(stream, cur_offset, SEEK_SET);
	return file_size;
}

static inline uint8_t *file_read(FILE *stream)
{
    long len = getfileSize(stream);
    uint8_t *data = (uint8_t *)malloc(len);
    for(size_t x = 0; x < len; ++x) {data[x] = fgetc(stream);}
    return data;
}

int main(int argc, char **argv)
{
    return 0;
}

