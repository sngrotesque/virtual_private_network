#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <winsock2.h>
#include <windows.h>
#include <unistd.h>
#include <stdint.h>
#define HOST   "0.0.0.0"
#define PORT   1080
#define RECV_N 4096
typedef SOCKADDR_IN sockaddr_in;
typedef struct {
    char    *host;
    uint16_t port;
    char    *sbuf;
    char    *rbuf;
} sn_sock;

static char *htoi(char *host)
{
    WSADATA ws;
    WSAStartup(MAKEWORD(2,2), &ws);
    struct sockaddr_in s;
    struct hostent *H = gethostbyname(host);
    if (H == NULL) {return NULL;}
    char **p = H->h_addr_list;
    memcpy(&s.sin_addr, *p, sizeof(p));
    return inet_ntoa(s.sin_addr);
}

static int _Client(sn_sock *data)
{
    WSADATA ws;
    WSAStartup(MAKEWORD(2,2), &ws);
    SOCKET s = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in server;

    server.sin_addr.S_un.S_addr = inet_addr(HOST);
    server.sin_port             = htons(PORT);
    server.sin_family           = AF_INET;

    int c  = connect(s, (struct sockaddr *)&server, sizeof(server));
    if (c == EOF) {return -1;}

    while(TRUE) {
        send(s, data->sbuf, strlen(data->sbuf), 0);
        send(s, data->rbuf, RECV_N, 0);
    }

    closesocket(s), closesocket(c);
    WSACleanup();
    return 0;
}

static int _Server(void)
{
    WSADATA ws;
    WSAStartup(MAKEWORD(2,2), &ws);
    SOCKET s, c;
    struct sockaddr_in server, client;
    uint32_t TIMEOUT = 100, clientlen = sizeof(client);

    s = socket(AF_INET, SOCK_STREAM, 0);

    server.sin_addr.S_un.S_addr = inet_addr(HOST);
    server.sin_port             = htons(PORT);
    server.sin_family           = AF_INET;

    setsockopt(s, SOL_SOCKET, SO_REUSEADDR, (char *)&TIMEOUT, sizeof(TIMEOUT));
    bind(s, (struct sockaddr *)&server, sizeof(server));
    listen(s, 5);

    c = accept(s, (struct sockaddr *)&client, &clientlen);

    char *rbuf = (char *)malloc(4096);
    while(TRUE) {
        memset(rbuf, 0, 4096);
        recv(c, rbuf, RECV_N, 0);
        printf("%s\n", rbuf);
    }

    closesocket(s), closesocket(c);
    WSACleanup();
    return 0;
}

int main(int argc, char **argv)
{
    _Server();

    return 0;
}
















