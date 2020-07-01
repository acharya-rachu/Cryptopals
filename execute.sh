#! /bin/bash
while  ! inotifywait -e modify Challenge3.py
	do clear;
	python3 Challenge3.py;
done;
