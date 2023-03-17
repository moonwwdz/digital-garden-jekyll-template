#!/bin/bash


for file in _notes/4\ 书籍阅读/*.md
do
    book_title=$(grep -oP '(?<=《)[^》]+' <<< "$file")
    echo "- [[《"$book_title"》]]" >> _notes/阅读目录.md
done
