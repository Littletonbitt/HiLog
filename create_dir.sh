#!/bin/bash

current="$PWD"

path=$current+"/my_syslog"

if [ ! -d $DIRECTORY ]; then
	mkdir $DIRECTORY
fi
