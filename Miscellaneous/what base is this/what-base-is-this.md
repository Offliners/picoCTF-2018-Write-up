## What base is this?
To be successful on your mission, you must be able read data represented in different ways, such as hexadecimal or binary. 

Can you get the flag from this program to prove you are ready? 

Connect with nc 2018shell.picoctf.com 31711.

Points : 200

## Category
Miscellaneous

## Solution
這題如果直接nc過去的話會發現...
```shell
root@DESKTOP-54M2H0F:/mnt/c/Users/ASUS# nc 2018shell.picoctf.com 31711
We are going to start at the very beginning and make sure you understand how data is stored.
table
Please give me the 01110100 01100001 01100010 01101100 01100101 as a word.
To make things interesting, you have 30 seconds.
Input:
```
如果解太慢，就會...
```shell
root@DESKTOP-54M2H0F:/mnt/c/Users/ASUS# nc 2018shell.picoctf.com 31711
We are going to start at the very beginning and make sure you understand how data is stored.
table
Please give me the 01110100 01100001 01100010 01101100 01100101 as a word.
To make things interesting, you have 30 seconds.
Input:
Too slow!
```

## Useful Link
pwntools安裝 : https://pwntoolsdocinzh-cn.readthedocs.io/en/master/install.html

sublime Text3安裝 : https://www.sublimetext.com/3
