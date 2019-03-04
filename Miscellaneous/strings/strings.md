## strings
Can you find the flag in this file without actually running it? 

You can also find the [file](https://2018shell.picoctf.com/static/e78981e684a62559baaef12a27f0e918/strings) in /problems/strings_0_bf57524acf558aca2081eb97ece8e2ee on the shell server.

Points : 100

## Category
Miscellaneous

## Solution
此題目給了我們一個名叫strings的檔案，按照前面步驟開啟發現一大堆的字串

於是，這次開啟linux的終端機，並先下此指令

`strings strings`

此指令是將strings的檔案以文字呈現，果不其然跑出一堆的字串

接著下

`strings strings | grep pico`

這個指令是將檔案以文字檔開啟，然後尋找pico

則flag就跑了出來

## Useful Link
Downloads file : https://2018shell.picoctf.com/static/e78981e684a62559baaef12a27f0e918/strings
strings詳細用法 : https://linux.die.net/man/1/strings
