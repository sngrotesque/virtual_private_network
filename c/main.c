#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <winsock2.h>
#include <windows.h>
#include <unistd.h>
#include <stdint.h>

#define LOCAL_HOST "0.0.0.0"
#define LOCAL_PORT 1080

typedef SOCKADDR_IN sockaddr_in;
typedef struct {
    char *host;
    int port;
} sn_vpn;

static void _Server()
{
    WSADATA ws;
    WSAStartup(MAKEWORD(2, 2), &ws);
    SOCKET s_s = socket(AF_INET, SOCK_STREAM, 0);
    SOCKET s_c = socket(AF_INET, SOCK_STREAM, 0);
    SOCKET c = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in server, client;
    uint32_t clientlen = sizeof(client);

    server.sin_addr.S_un.S_addr = inet_addr(LOCAL_HOST);
    server.sin_port             = htons(LOCAL_PORT);
    server.sin_family           = AF_INET;

    int b = bind(s_s, (struct sockaddr *)&server, sizeof(server));
    if (b == EOF) {printf("bind error.\n"); exit(0);}
    listen(s_s, 5);

    s_c = accept(s_s, (struct sockaddr *)&client, &clientlen);

    char recvbuf[4100];
    while (TRUE) {
        memset(recvbuf, 0, 4100);
        recv(s_c, recvbuf, 4096, 0);
        printf("%s\n", recvbuf);
    }

    WSACleanup();
    closesocket(s_s);
    closesocket(s_c);
    closesocket(c);
}


int main(int argc, char **argv)
{
    _Server();

    return 0;
}



