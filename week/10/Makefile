CC=gcc
CFLAGS=-g -fno-stack-protector -fno-pie -fPIC -m32
LDFLAGS=-lcrypto
TARGETS=ledger crack

ledger: ledger.o $(OBJECTS)

crack: crack.o $(OBJECTS)

clean:
	rm -rf *.o $(TARGETS) *.bin

all: ledger crack

.PHONY=clean
.DEFAULT_GOAL=all
