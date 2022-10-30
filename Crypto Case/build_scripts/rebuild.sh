#!/bin/sh
clear
premake4 gmake
make -j 100 config=release clean
make -j 100 config=release