#!/bin/sh

COOKIE=$(cat ~/.aoc-session-cookie)
YEAR=$1
DAY=$2

curl -sH "Cookie: session=$COOKIE" "https://adventofcode.com/$YEAR/day/$DAY/input" > data/input-$DAY.txt
