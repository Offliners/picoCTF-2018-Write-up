# General Warmup 1
題目提示答案是將0x41(十六進位)轉換成ASCII表中代表的即可得到flag

0x41 = 4 * 16 + 1 = 65

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

通常就會用Notepad或用文字檔開啟

開啟後會發現一堆亂碼，但尋找關鍵字pico即可發現

flag為 `picoCTF{grep_and_you_will_find_52e63a9f}`

# net cat 
此題目是要我們了解如何使用netcat去連線到題目指定的伺服器

此時開啟linux的終端機，下此指令

`nc 2018shell.picoctf.com 49387`

flag就馬上跳出來

flag為 `picoCTF{NEtcat_iS_a_NEcESSiTy_8b6a1fbc}`
