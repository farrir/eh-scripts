#!/bin/bash
# sends a ping w/ 1 packet to each ip address in the given X.X.X net
# prints out all IP that are reachable

if [ -n $1 ]; then
    echo "net missing for ipsweep (format X.X.X)"
else
    for ip in `seq 1 254` ; do
        ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
    done
fi