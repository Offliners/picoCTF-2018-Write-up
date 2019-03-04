## grep 2
This one is a little bit harder. 

Can you find the flag in /problems/grep-2_0_783d3e2c8ea2ebd3799ca6a5d28fc742/files on the shell server? Remember, grep is your friend.

Points : 125

## Category
Miscellaneous

## Solution
題目直接叫我們使用網站提供的shell到/problems/grep-2_0_783d3e2c8ea2ebd3799ca6a5d28fc742/files此目錄下去尋找flag

到此目錄中看到有10個files要找

不過只要下此指令

`grep -r picoCTF`

`-r`是linux的循環指令，他會grep所有的檔案

所以flag就能輕鬆得到

## Useful Link
grep詳細用法 : https://ryanstutorials.net/linuxtutorial/grep.php
