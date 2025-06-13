#!/bin/bash

ARCH=amd64
SONAME=libcaaplus.so

mkdir -p $ARCH

g++ -DCWRAPPER -Isrc src/*.cpp -std=gnu++17 -Wall -fpic -c
g++ -shared -fPIC -Wl,-soname,$SONAME -o ./$ARCH/$SONAME *.o
rm -vf *.o
