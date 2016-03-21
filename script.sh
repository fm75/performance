#! /bin/bash

for n in 1000 10000 100000 1000000 10000000;do
  time ./processor.py $n
done
