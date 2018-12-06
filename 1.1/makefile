# the compiler: gcc for C program, define as g++ for C++
CC = gcc

# compiler flags:
#  -g    adds debugging information to the executable file
#  -Wall turns on most, but not all, compiler warnings
CFLAGS  = -g -Wall

# the build target executable:
FIRST=1
SECOND=2

f: $(FIRST).c
	$(CC) $(CFLAGS) -o $(FIRST) $(FIRST).c

s: $(SECOND).c
	$(CC) $(CFLAGS) -o $(SECOND) $(SECOND).c
