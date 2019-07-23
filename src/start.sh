#!/bin/bash
filename="./name.txt"
while read line; do
    if [ "$line" == "" ]; then
        echo "finish"
    else
        del=$IFS
        IFS=',' read -a n <<< $line
        array=(${n[@]})
        echo $array
        size=$((${#array[@]}/20))
        echo $size

        for index in $(seq 0 $size)
        do
            a=$(($index*20))
            #b=$(($a+19))
            ar=${array[@]:$a:20}
            ar=${ar// /,}
            echo $ar
            eval "scrapy crawl_many -a $ar -o output.json -t json"
        done
   fi
done < $filename



