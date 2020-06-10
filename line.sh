#!/bin/bash
content=""
for j in seq 1 $3
do
for i in seq 1 $2
do
content="$content$1"
done
content="$content\n"
done
echo -e $content
