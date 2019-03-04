## environ
Sometimes you have to configure environment variables before executing a program. 

Can you find the flag we've hidden in an environment variable on the shell server?

Points : 150

## Category
Miscellaneous

## Solution
題目問我們是否能了解環境變數，所以我們需要到網站提供的shell來看其環境

想要了解，就必須下此指令

`printenv`

結果發現跑出一堆東西，根據以往的經驗，flag就藏在其中，所以...

`printenv | grep pico`

果不其然，flag就藏在其中
## Useful Link
env詳細用法 : https://www.tutorialspoint.com/unix/unix-environment.htm
