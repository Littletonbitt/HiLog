#!/bin/bash

current="$PWD"
count=$(cd ~/HiLog/my_syslog && ls -1 | wc -l)

if [[ $count -ge 10 ]] 
then
	$(cd ~/HiLog && tar -czf my_syslog.tar.gz my_syslog)
	rm -rf my_syslog
	mkdir my_syslog
fi
