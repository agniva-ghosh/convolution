libconv.so : conv.o
	gcc -shared -o libconv.so conv.o

conv.o : conv.c
	gcc -c -fPIC conv.c -o conv.o