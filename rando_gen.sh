#!/usr/bin/bash

for i in $(seq 1 100000)
do
	./random.sh >> /tmp/testfile
done
