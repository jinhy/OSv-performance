#!/bin/sh
export OSV_BRIDGE=virbr0
brctl stp $OSV_BRIDGE off
brctl addif $OSV_BRIDGE $1
ifconfig $1 up
