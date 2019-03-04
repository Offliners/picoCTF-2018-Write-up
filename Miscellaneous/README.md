# General Warmup 1
題目提示答案是將0x41(十六進位)轉換成ASCII表中代表的即可得到flag

0x41 = 4 * 16 + 1 = 65

ASCII表單連結 : https://zh.wikipedia.org/wiki/ASCII

查表即可知道為 A

所以flag為 `picoCTF{A}`

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

grep詳細用法 : https://ryanstutorials.net/linuxtutorial/grep.php

開啟後會發現一堆亂碼，但尋找關鍵字pico即可發現

flag為 `picoCTF{grep_and_you_will_find_52e63a9f}`

# net cat 
此題目是要我們了解如何使用netcat去連線到題目指定的伺服器

此時開啟linux的終端機，下此指令

`nc 2018shell.picoctf.com 49387`

flag就馬上跳出來

flag為 `picoCTF{NEtcat_iS_a_NEcESSiTy_8b6a1fbc}`

# strings
此題目給了我們一個名叫strings的檔案，按照前面步驟開啟發現一大堆的字串

於是，這次開啟linux的終端機，並先下此指令

`strings strings`

此指令是將strings的檔案以文字呈現，果不其然跑出一堆的字串

接著下

`strings strings | grep pico`

這個指令是將檔案以文字檔開啟，然後尋找pico

strings詳細用法 : https://linux.die.net/man/1/strings

則flag就跑了出來

flag為 `picoCTF{sTrIngS_sAVeS_Time_c09b1444}`

# pipe
題目又給了域名和port，二話不說先nc連線看看

結果噴出了一堆的英文句子

學過剛剛的教訓，就用grep來找看看吧

`nc 2018shell.picoctf.com 44310 | grep pico`

就馬上找到了flag `picoCTF{almost_like_mario_a13e5b27}`

# grep 2
題目直接叫我們使用網站提供的shell到/problems/grep-2_0_783d3e2c8ea2ebd3799ca6a5d28fc742/files此目錄下去尋找flag

到此目錄中看到有10個files要找

不過只要下此指令

`grep -r picoCTF`

`-r`是linux的循環指令，他會grep所有的檔案

grep詳細用法 : https://ryanstutorials.net/linuxtutorial/grep.php

所以flag就能輕鬆得到 `picoCTF{grep_r_and_you_will_find_24c911ab}`
