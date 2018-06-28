#!/bin/bash

for i in a b c; do
    echo $i
done

count=0
for i in $(cat ~/.bashrc); do
    count=$((count+1))
done
echo $count

for i in "$@"; do
    echo $i
done

a=0
until [ $a -eq 5 ]; do
    a=$((a+1))
    echo $a
done
