## ssh-keyz
As nice as it is to use our webshell, sometimes its helpful to connect directly to our machine. 

To do so, please add your own public key to ~/.ssh/authorized_keys, using the webshell. 

The flag is in the ssh banner which will be displayed when you login remotely with ssh to with your username. 

Points : 150

## Category
Miscellaneous

## Solution
這題是希望我們去遠端登入其他台電腦

如果兩台都是自己的電腦，還要輸入帳號密碼就十分的麻煩

在linux上就可以把另一台電腦記錄在白名單中

只要電腦有在這白名單中，就不用登入

首先就要先生成電腦專屬的金鑰

照著下面的流程即可生成，詳細說明有在下方的連結中
```shell
offliner@ubuntu:~$ ssh-keygen -t rsa -C "eric21904@gmail.com"
Generating public/private rsa key pair.
Enter file in which to save the key (/home/offliner/.ssh/id_rsa): 
/home/offliner/.ssh/id_rsa already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/offliner/.ssh/id_rsa.
Your public key has been saved in /home/offliner/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:RMiI+PPwajIQkC23W/yy3rBDi93GqvOfBO9+TvnCKIw eric21904@gmail.com
The key's randomart image is:
+---[RSA 2048]----+
| + . o ..        |
|= + . o.         |
|.+ o    .        |
|. = o  .         |
| . B..  S        |
|. . =o.  .       |
|.  B.*ooo        |
|o E B*=o+.       |
| +.==B*o...      |
+----[SHA256]-----+
```

生成後的金鑰會儲存在`.ssh/id_rsa.pub`中
```shell
offliner@ubuntu:~$ cd .ssh
offliner@ubuntu:~/.ssh$ ls
id_rsa  id_rsa.pub  known_hosts
offliner@ubuntu:~/.ssh$ cat id_rsa.pub
```


## Useful Link
如何生成ssh金鑰 : https://confluence.atlassian.com/bitbucketserver/creating-ssh-keys-776639788.html
