#include <arpa/inet.h>
#include <sys/socket.h>
#include <stdio.h>
#include <unistd.h>
#include <assert.h>
#include <string.h>

#define HOST "112.137.129.129"
#define PORT 27001

int f(char x) {
  return x < 0 ? x + 256 : x;
}

unsigned int parse_int(char *buf) {
  return (f(buf[0]) << 0) + (f(buf[1]) << 8) + (f(buf[2]) << 16) + (f(buf[3]) << 24);
}

void pack_int(char* buf, unsigned int x) {
  char res[4] = {0, 0, 0, 0};
  for (int i = 0; i < 4; i++) {
    res[i] = (x >> (8 * i)) % (1 << 8);
  }
  for (int i = 0; i < 4; i++) {
    *(buf + i) = res[i];
  }
}

int main(int argc, char **argv) {
  int status = 0, read_status, client_fd;
  struct sockaddr_in serv_addr;
  char buffer[64] = {0};

  if ((client_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
    fprintf(stderr, "Socket error\n");
    return 0;
  }

  serv_addr.sin_family = AF_INET;
  serv_addr.sin_port = htons(PORT);

  if (inet_pton(AF_INET, HOST, &serv_addr.sin_addr) <= 0) {
    fprintf(stderr, "Address not supported\n");
    return 0;
  }

  if ((status = connect(client_fd, (struct sockaddr *)&serv_addr, sizeof(serv_addr))) < 0) {
    fprintf(stderr, "Connect failed\n");
    return 0;
  }

  char packet_0[64] = {0, 0, 0, 0, 8, 0, 0, 0};
  char* msv = "22021105";
  for (int i = 0; i < 8; i++) {
    packet_0[i + 8] = msv[i];
  }
  printf("Sending packet 0\n");
  send(client_fd, packet_0, 16, 0);

  read_status = read(client_fd, buffer,
                   59);
  
  if (buffer[0] != 1) {
    fprintf(stderr, "Failed to send packet 0!\n");
  }
  while (1) {
    unsigned int a = parse_int(buffer + 8);
    unsigned int b = parse_int(buffer + 12);

    char packet_2[15] = {2, 0, 0, 0, 4, 0, 0, 0};
    pack_int(packet_2 + 8, a + b);
    // printf("Sending packet 2\n");
    send(client_fd, packet_2, 12, 0);
    
    for (int i = 0; i < 32; i++) {
      buffer[i] = 0;
    }
    
    read_status = read(client_fd, buffer, 64);

    if (buffer[0] == 1) {
      continue;
    } else if (buffer[0] == 4) {
      for (int i = 0; i < 64; i++) {
        if (buffer[i] > 45) {
          printf("%c", buffer[i]);
        }
      }
      return 0;
    } else {
      assert(buffer[0] == 3);
      printf("Wrong answer!\n");
      return 0;
    }
  }
}