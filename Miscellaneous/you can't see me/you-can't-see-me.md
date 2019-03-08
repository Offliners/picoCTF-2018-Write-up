## you can't see me
'...reading transmission... Y.O.U. .C.A.N.'.T. .S.E.E. .M.E. ...transmission ended...' 

Maybe something lies in /problems/you-can-t-see-me_4_8bd1412e56df49a3c3757ebeb7ead77f.

Points : 200

## Category
Miscellaneous

## Solution
首先開啟網站的shell，然後到題目指定的位址

`cd /problems/you-can-t-see-me_4_8bd1412e56df49a3c3757ebeb7ead77f`

第一步當然先`ls`看一下裡面有什麼，結果發現...什麼都沒有

那麼必須先知道一些重要的linux的`ls`指令

`-a` 顯示所有文件與目錄(但文件名與目錄開頭為.視為隱藏檔，不會顯示出來)

`-l` 顯示文件名稱外，也會將文件的權限、型態、檔案大小...等顯示出來

所以`-al`就可以先是所有完件與目錄，並把權限、型態、檔案大小...等都一併顯示出來

接著就開始找flag吧~

```shell
Offliner123@pico-2018-shell:~$ cd /problems/you-can-t-see-me_4_8bd1412e56df49a3c3757ebeb7ead77f                            
Offliner123@pico-2018-shell:/problems/you-can-t-see-me_4_8bd1412e56df49a3c3757ebeb7ead77f$ ls                              
Offliner123@pico-2018-shell:/problems/you-can-t-see-me_4_8bd1412e56df49a3c3757ebeb7ead77f$ ls -al                          
total 60                                                                                                                   
drwxr-xr-x   2 root       root        4096 Nov 15 02:40 .
-rw-rw-r--   1 hacksports hacksports    57 Nov 15 02:40 .                                                                  
drwxr-x--x 566 root       root       53248 Nov 15 04:28 ..
Offliner123@pico-2018-shell:/problems/you-can-t-see-me_4_8bd1412e56df49a3c3757ebeb7ead77f$ cat .*                          
cat: .: Is a directory                                                                                                     
picoCTF{j0hn_c3na_paparapaaaaaaa_paparapaaaaaa_22f627d9}                                                                   
cat: ..: Permission denied                                                                                                 
Offliner123@pico-2018-shell:/problems/you-can-t-see-me_4_8bd1412e56df49a3c3757ebeb7ead77f$   
```

## Useful Link
Linux指令大全 : http://www.runoob.com/linux/linux-command-manual.html
