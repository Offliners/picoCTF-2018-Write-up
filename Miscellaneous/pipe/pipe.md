## pipe
During your adventure, you will likely encounter a situation where you need to process data that you receive over the network rather than through a file.

Can you find a way to save the output from this program and search for the flag? 

Connect with 2018shell.picoctf.com 44310.


Points : 110

## Category
Miscellaneous

## Solution
題目又給了域名和port，二話不說先nc連線看看

結果噴出了一堆的英文句子

學過剛剛的教訓，就用grep來找看看吧

`nc 2018shell.picoctf.com 44310 | grep pico`

就馬上找到了flag 

## Useful Link
grep詳細用法 : https://ryanstutorials.net/linuxtutorial/grep.php
