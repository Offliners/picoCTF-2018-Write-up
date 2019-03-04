# General Warmup 1
題目提示答案是將0x41(十六進位)轉換成ASCII表中代表的即可得到flag

0x41 = 4 * 16 + 1 = 65

查表即可知道為 A

所以flag為 `picoCTF{A}`

ASCII表單連結 : https://zh.wikipedia.org/wiki/ASCII

# General Warmup 2
題目提示答案是將27(十進位)轉換成二進位

所以 27 => 11011

flag即為 `picoCTF{11011}`

# General Warmup 3
這題只要將0x3D(十六進位)轉換成十進位即可得到flag

0x3D = 3 * 16 + 13 = 61

flag即為 `picoCTF{61}`

# Resources
題目給了一個連結，並提示答案藏在此網頁中，第一個想法就是...

讀網頁的原始碼

不出乎所料就藏在裡頭

flag為 `picoCTF{xiexie_ni_lai_zheli}`

# grep 1
下載題目給的檔案file，會發現無法辨識此為什麼檔案

通常就會用Notepad或用文字檔開啟，也可在linux的終端機使用grep尋找

開啟後會發現一堆亂碼，但尋找關鍵字pico即可發現

flag為 `picoCTF{grep_and_you_will_find_52e63a9f}`

grep詳細用法 : https://ryanstutorials.net/linuxtutorial/grep.php

# net cat 
此題目是要我們了解如何使用netcat去連線到題目指定的伺服器

此時開啟linux的終端機，下此指令

`nc 2018shell.picoctf.com 49387`

flag就馬上跳出來

flag為 `picoCTF{NEtcat_iS_a_NEcESSiTy_8b6a1fbc}`

net cat詳細用法 : https://linux.die.net/man/1/nc

# strings
此題目給了我們一個名叫strings的檔案，按照前面步驟開啟發現一大堆的字串

於是，這次開啟linux的終端機，並先下此指令

`strings strings`

此指令是將strings的檔案以文字呈現，果不其然跑出一堆的字串

接著下

`strings strings | grep pico`

這個指令是將檔案以文字檔開啟，然後尋找pico

則flag就跑了出來

flag為 `picoCTF{sTrIngS_sAVeS_Time_c09b1444}`

strings詳細用法 : https://linux.die.net/man/1/strings

# pipe
題目又給了域名和port，二話不說先nc連線看看

結果噴出了一堆的英文句子

學過剛剛的教訓，就用grep來找看看吧

`nc 2018shell.picoctf.com 44310 | grep pico`

就馬上找到了flag `picoCTF{almost_like_mario_a13e5b27}`

grep詳細用法 : https://ryanstutorials.net/linuxtutorial/grep.php

# grep 2
題目直接叫我們使用網站提供的shell到/problems/grep-2_0_783d3e2c8ea2ebd3799ca6a5d28fc742/files此目錄下去尋找flag

到此目錄中看到有10個files要找

不過只要下此指令

`grep -r picoCTF`

`-r`是linux的循環指令，他會grep所有的檔案

所以flag就能輕鬆得到 `picoCTF{grep_r_and_you_will_find_24c911ab}`

grep詳細用法 : https://ryanstutorials.net/linuxtutorial/grep.php

# Aca-Shell-A
這題考驗我們對linux指令的熟悉度，linux常用指令有

`cd`      變換目錄

`ls`      列出該目錄的檔案

`cat`     直接檢視檔案內容

`cp`      複製檔案或目錄

`rm`      移除檔案或目錄

`echo`    字符、字串輸出

`./`      執行檔案

了解這些指令後就來解這題吧~

```shell
Sweet! We have gotten access into the system but we aren't root.
It's some sort of restricted shell! I can't see what you are typing
but I can see your output. I'll be here to help you along.
If you need help, type "echo 'Help Me!'" and I'll see what I can do
There is not much time left!
~/$ ls
blackmail
executables
passwords
photos
secret
~/$ cd secret
Now we are cookin'! Take a look around there and tell me what you find!
~/secret$ ls
intel_1
intel_2
intel_3
intel_4
intel_5
profile_ahqueith5aekongieP4ahzugi
profile_ahShaighaxahMooshuP1johgo
profile_aik4hah9ilie9foru0Phoaph0
profile_AipieG5Ua9aewei5ieSoh7aph
profile_bah9Ech9oa4xaicohphahfaiG
profile_ie7sheiP7su2At2ahw6iRikoe
profile_of0Nee4laith8odaeLachoonu
profile_poh9eij4Choophaweiwev6eev
profile_poo3ipohGohThi9Cohverai7e
profile_Xei2uu5suwangohceedaifohs
Sabatoge them! Get rid of all their intel files!
~/secret$ rm intel*
Nice! Once they are all gone, I think I can drop you a file of an exploit!
Just type "echo 'Drop it in!' " and we can give it a whirl!
~/secret$ echo 'Drop it in!'
Drop it in!
I placed a file in the executables folder as it looks like the only place we can execute from!
Run the script I wrote to have a little more impact on the system!
~/secret$ cd ..
~/$ ls
blackmail
executables
passwords
photos
secret
~/$ cd executables
~/executables$ ls
dontLookHere
~/executables$ ./dontLookHere
 a504 9276 1b65 6f04 e3b5 9d15 2a54 ead8 5543 eecd 6d08 35f5 3f46 e453 f696 8377 c4d3 bf60 e3a5 3a1a 3221 21ad 20d6 cbc2 e4ee
 3da3 9122 8154 d4e3 b25c dc90 37ef ead5 8dce efc0 8a01 0d8b 4fe2 53dd b739 388d 4ef0 1a03 5611 fa29 c2fa 285f f49e 49fb 9389
 b8b6 9c9d 371c d8eb 8f41 ca24 1160 1b6e df1d f014 63f9 4e54 b539 41fe 8f42 c1b8 fdfd 5809 492c 7ba5 9777 fd26 9a04 8e03 b762
 6e4a faf9 e793 1e36 43bc f0dd a4df ef6b 42c6 8d91 34ed be19 0449 4c5d bded c2f3 9213 5375 f79c 512b c370 fff9 0a69 bb1d 7043
 1e0e 80a3 e9b4 385e 0c08 206b bc41 ab01 7573 078a 04d6 8c6a ddfa 190a 50cf e128 9bf9 01d6 8110 447c 10ac 25d0 dbeb b9e7 b672
 8984 c752 cb42 5781 42fb 9343 80c4 b236 9a5a b6ff 29cd f93d b6da b202 5544 e4bf 6ee2 3c7e c7d9 46a0 f3a3 966c 7ecc 7854 ab6e
 e51e b8d5 02f6 0d58 ef04 26cf 6401 e5c0 4ce8 e4d3 efb0 9733 b00b a85a f414 a50d 27aa 585b 2883 24a7 9f1e 90b1 bbde d3ee d439
 ddbc 9f49 72f4 b382 8476 a1ce 7ad1 26e7 2312 b896 d2de 6ed8 7252 9488 aada 9b02 b90c b1b4 05df 13ae 7834 e163 ec44 6cef b4ac
 499c 30f5 e7d7 41f4 4302 dfdc b2c1 a7bc d83e e0ab 6014 919b 96a9 f6e9 8639 9273 8b60 8cbb 3bc0 163f dc6d 1ff7 6987 c5b4 7362
 c6f1 9603 d34e b13b 8464 9f52 4901 112e 9dec 17bf 5f57 91b7 bf64 657e 5333 a0ef bc3e dc1e d45d f759 80ca 3db2 f29e 6d7a f6b1
 b579 40da 895b 2826 5422 b5c4 1455 e144 78fb 7fe2 e8f6 40e3 6073 c084 40df 9241 fd64 0663 0272 b02e 7392 453a a423 131f 7612
 5d2e 40c5 3c83 c0ed a864 4aa9 0ec8 77d0 c00a a4c8 cae9 362e 0358 8e3a 672c 3e74 5b19 94e6 6154 30dd 66ae b6eb d08f 5d95 f9d0
 1127 cc55 43fe 1876 f23b daa1 37d9 826f fa28 ffcc 6616 9b8c a9bf 251b 2e75 52bf cee1 1b11 9031 c4fa fdc4 6305 e1c6 91bb 97f4
 54e4 44e2 933e 2e50 4d31 6e71 1139 607d a923 7604 6d77 f5a9 b9b4 31fb 4dbd fe24 b137 cdff bae0 38ca c01e 2bac a460 b9dd 9337
 44f9 c891 ba8c 4e2b 07bb 8612 3a30 e704 384b 8cb4 9aeb bd1c 9df5 7c44 38a6 d2b9 0fc4 d492 725a d9e3 c55b 6189 2ea7 42ac d21c
 f680 42f1 b400 10f8 8b41 16ea 48fc f755 67e5 8c5f 10da cab1 c729 b07b a959 ca9d 7d06 bf69 f6b8 8aff 4663 a8e3 f618 ade9 431e
 b41f c9d7 5577 7d16 776f c787 286f 5397 0a85 f5ee 2d2e 893b f091 72fd 0b25 a18f b123 36db a085 e5b0 ed90 8cd9 ea3a 7396 975b
 4fbe c128 4a90 0428 dcaa 8f14 7410 0680 259c 2a40 52e2 4e82 82d7 8d49 9481 3968 bc60 6376 3243 eb25 f2a2 63df fc44 2183 9ced
 db52 c400 ee1a ac22 741b f5b3 f367 9f08 67e0 00d0 d269 42b3 6656 325e 707f 7434 180f d300 266a 461b 89ae fd61 23c1 8c86 a11c
 010a c226 eb12 e006 379c d03d 3ae7 8085 3625 7e59 0f25 8122 d7bf 5363 4f85 bd60 6f87 ae84 b9de 70be f390 04ab a92f 3690 b6d8
 0547 c3f0 47c0 0a15 1652 0d89 701d 95f8 6c38 d28e 17de 1d7d 04d2 f9d1 7620 b892 bf65 2616 be07 c8d1 951a b553 a56a 2522 c4f5
 5b1f ea44 824c 112a c26e 2e35 f2be f0d9 f61f 583b 787e 9031 847a fb55 4228 984f 7fc2 1cac 86b4 70a0 6084 1f53 4914 0247 cf32
 1acb 2d50 60e7 31ac 50dd a600 b1ab 584c ca46 720e d777 4a98 9c24 a29a 5cba 10d8 e8a2 234c 734e bdc0 3001 2bea 8147 e0fb 83ee
 0b12 9a5a 445b 1836 fda9 0fdc 4c27 1230 5d8d 9042 3507 6f6d da76 4592 a515 71af fce6 7e18 2cc2 12cb 7f4e 98c7 9f7b a049 e9a6
 165c c6b3 da76 627a 3f55 9935 c86b 7348 d4d2 b004 8786 33c4 0b36 dd45 4187 965d a84a 0574 788b 4b93 904f 4c66 43b9 d168 399f
 2c34 3274 6549 5b07 1abe 430b 2f76 e355 f86b 650a fbb1 ec02 db23 b2e2 63e8 6b1a dc93 574e 016a fa58 2c06 0e6b b7fe 98c0 1f3d
 a645 f6b5 2e09 a1cd d1f3 f3c2 a239 b379 2558 b761 8c17 2cb4 8c5d dff2 926c 0e87 08f8 f1f6 8e9f 4b87 a7ab 8985 7ed4 4b57 84f7
 7335 b7e9 e8b3 3b14 e29a 935a c921 8321 7abe 875d 794e fb83 9faa 90fb 7bad 0bec b834 78a8 080a 2488 8e81 53d4 8dc2 8013 4c82
 0817 803a b4c1 3cb3 9c24 5ea9 c693 3849 f86b db76 0d6f cec0 d077 b81a 354f 59e1 6021 2a24 4320 35cb 74e1 0921 b7d0 ee0b 953b
 9c2c badc b3b2 8f88 6ee7 ccb7 66b0 ddab 6f23 fdd3 9a64 8a08 8b40 df9a 1e30 6d7a ca05 1a19 79b9 02af 5a66 ed4d 48a4 f8ae 3968
 68a1 12d7 a5a6 4e87 f5fb e7bf a6c7 5b14 461a 0218 ad11 bc09 12ba c8d4 8e5e d37c 3e06 f8d6 e998 5413 0692 6d6e b41b c4d2 a074
 8a67 8f74 b268 e0b8 3d46 611f 3659 25c1 c327 509d 0fd9 7114 7bad c87c c499 303f 2726 6726 8892 10fb f2d0 6a84 c87a a136 7558
 9876 f7de 921a 934c 8f1d f8be ec4a c7f4 7679 fd3a 9fdf f710 03f7 8775 e52d 1e13 84ac 4424 a30e 7145 1cb0 1329 738a e2f7 742f
 8494 3a88 ce27 8954 340a 7127 b3cd b90e b8a8 89c4 1738 7da0 c5b4 2fd2 ee08 38ac 3163 d6ed 4ce3 e437 5bbb f767 6b70 5a36 4c20
 6c9f a9f3 fa73 bca2 3b35 9c53 c8f0 d6fa d611 652f 9835 5e62 dcdb 9ecf 0526 8df0 5ebd 3640 295c 3ff6 3bb1 0d23 3fe6 60f0 b7bd
 11d9 af34 1810 7738 09b8 033a 633b ce55 b76c 7ebf e999 c7f4 8f21 31b2 4715 c169 17f5 0d48 fffd 8262 96e8 8572 c092 2228 b592
Looking through the text above, I think I have found the password. I am just having trouble with a username.
Oh drats! They are onto us! We could get kicked out soon!
Quick! Print the username to the screen so we can close are backdoor and log into the account directly!
You have to find another way other than echo!
~/executables$ whoami
l33th4x0r
Perfect! One second!
Okay, I think I have got what we are looking for. I just need to to copy the file to a place we can read.
Try copying the file called TopSecret in tmp directory into the passwords folder.
~/executables$ cp /tmp/TopSecret passwords
Server shutdown in 10 seconds...
Quick! go read the file before we lose our connection!
~/executables$ cd ..
~/$ cd passwords
~/passwords$ ls
TopSecret
~/passwords$ cat TopSecret
Major General John M. Schofield's graduation address to the graduating class of 1879 at West Point is as follows: The discipline which makes the soldiers of a free country reliable in battle is not to be gained by harsh or tyrannical treatment.On the contrary, such treatment is far more likely to destroy than to make an army.It is possible to impart instruction and give commands in such a manner and such a tone of voice as to inspire in the soldier no feeling butan intense desire to obey, while the opposite manner and tone of voice cannot fail to excite strong resentment and a desire to disobey.The one mode or other of dealing with subordinates springs from a corresponding spirit in the breast of the commander.He who feels the respect which is due to others, cannot fail to inspire in them respect for himself, while he who feels,and hence manifests disrespect towards others, especially his subordinates, cannot fail to inspire hatred against himself.
picoCTF{CrUsHeD_It_4e355279}
```

所以flag就是 `picoCTF{CrUsHeD_It_4e355279}`

linux詳細網站 : https://maker.pro/linux/tutorial/basic-linux-commands-for-beginners

# environ
題目問我們是否能了解環境變數，所以我們需要到網站提供的shell來看其環境

想要了解，就必須下此指令

`printenv`

結果發現跑出一堆東西，根據以往的經驗，flag就藏在其中，所以...

`printenv | grep pico`

果不其然，flag就是 `picoCTF{eNv1r0nM3nT_v4r14Bl3_fL4g_3758492}`

env詳細用法 : https://www.tutorialspoint.com/unix/unix-environment.htm

# ssh-keyz

# what base is this?

# you can't see me

# absolutely relative

# in out error

# learn gdb

# store

# script me

