# 逆向首戰

## Description

ㄚ喵發現某公司的後端居然是用 Python 寫的，而且還因為檔案處理不當，留下了一個可能是驗證密碼的 Pyc 檔，快趁這機會打下他ㄅㄅㄅ  

Released : [task.pyc](./task.pyc)

## Task

這是一題提供了 .pyc 檔案的題目  
雖然直接打開會看到很多亂碼 但是 .pyc 是可以被 decompile 回 .py 的  
所以打開一些線上 decompiler 工具就好  

## Solve

這邊使用的是 [pyc 反編譯](https://www.toolnb.com/tools-lang-zh-TW/pyc.html)  
上傳檔案後就會回傳 decompile 的結果

![](https://i.imgur.com/2yyVi3a.png)

接著 code review 後就會發現  
你只需要輸入一個 16 進位並且用 `, ` 分隔每個字元的字串  
只要字串全部 XOR 31 後等於 ls 就可以通過驗證了  
並且 `assert s.startswith` 這行有提示字串開頭應該怎麼寫  
所以就可以寫一個簡單的程式來解  

```python
#!/usr/bin/python

ls = [94, 86, 76, 44, 100, 72, 44, 115, 92, 47, 114, 122, 64, 126, 123, 114, 46, 113, 64, 86, 42, 64, 75, 119, 44, 109, 90, 64, 43, 113, 102, 64, 119, 43, 92, 116, 44, 109, 42, 32, 98]
res = ""

for i in ls:
    res += chr(i ^ 31)

print(res)

```

如果是在 Linux 環境下的話  
可以使用 uncompyle6 直接離線 decompile  
安裝 : sudo pip3 install uncompyle6

