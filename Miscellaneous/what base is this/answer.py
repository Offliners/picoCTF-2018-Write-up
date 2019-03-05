#!/usr/bin/python
from pwn import * 

s = remote('2018shell1.picoctf.com', 31711) 

binary = s.recvuntil('word.') 
binary = re.findall(r'(\d+)', binary) 
ans = ''
for i in binary:
	ans += chr(int(i, 2)) 
s.sendline(ans) 

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

print s.recvuntil('}\n') 

s.close() 
