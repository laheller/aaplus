#!/bin/bash

ARCH=i386
SONAME=libcaaplus.so

mkdir -p $ARCH

g++ -m32 -DCWRAPPER -Isrc src/*.cpp -std=gnu++17 -Wall -fpic -c
g++ -m32 -shared -fPIC -Wl,-soname,$SONAME -o ./$ARCH/$SONAME *.o
rm -vf *.o
