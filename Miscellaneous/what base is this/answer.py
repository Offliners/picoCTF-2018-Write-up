#!/usr/bin/python
from pwn import * 

r = remote('2018shell1.picoctf.com', 31711) 

binary = r.recvuntil('word.') 
binary = re.findall(r'(\d+)', binary) 
ans = ''
for i in binary:
	ans += chr(int(i, 2)) 
r.sendline(ans) 

hexa = r.recvuntil('word').strip()
hexa = re.findall(r'([0-9a-f]+) as ', hexa)[0]
ans = hexa.decode('hex')
r.sendline(ans)

octal = r.recvuntil('word.')[2:]
octal = re.findall(r'[0-9]+', octal)
ans = ''
for i in octal:
	ans += chr(int(i, 8))
r.sendline(ans)

print r.recvuntil('}\n') 

r.close() 
