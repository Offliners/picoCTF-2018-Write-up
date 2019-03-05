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
因此，我們就必須寫程式去給電腦去高速運算

而我也在下方附上自己寫程式的IDE與程式碼(有註解方便理解)
```python
#!/usr/bin/python
from pwn import * //使用pwntools

s = remote('2018shell1.picoctf.com', 31711) //連線到題目指定的伺服器

binary = s.recvuntil('word.') //讀取字串並停止在word
binary = re.findall(r'(\d+)', binary) //使用pwntools內建模組re的findall函式庫，findall可以指定的字串
ans = ''
for i in binary:
	ans += chr(int(i, 2)) //將binary一個個轉成10進位，在轉成ASCII
s.sendline(ans) //將答案送出

hexa = s.recvuntil('word').strip()
hexa = re.findall(r'([0-9a-f]+) as ', hexa)[0]
ans = hexa.decode('hex')
s.sendline(ans)

octal = s.recvuntil('word.')[2:]
octal = re.findall(r'[0-9]+', octal)
ans = ''
for i in octal:
	ans += chr(int(i, 8))
s.sendline(ans)

print s.recvuntil('}\n') //印出flag

s.close() //關閉程式
```
接著在終端機下此指令即可執行這程式

`python answer.py`

flag就會跑出來~

## Useful Link
pwntools安裝 : https://pwntoolsdocinzh-cn.readthedocs.io/en/master/install.html

sublime Text3安裝 : https://www.sublimetext.com/3

[My code](answer.py)
