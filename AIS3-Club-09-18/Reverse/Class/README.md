# 第一堂咖啡課

## Description

ㄚ喵經過逆向驗證密碼的檔案後，成功進入了後台，但是目前還沒看到什麼有趣的資料，或許這個放在咖啡旁邊的 .class 檔案很有價值  

Released : [ClassChallenge.class](./ClassChallenge.class)

## Task

跟上一題類似 只是從 .pyc 換成了 .class  
.class 是 .java compile 過後的產物 一樣可以透過 decompiler 回推

## Solve

這邊使用的是 [.JAR and .Class to Java decompiler](http://www.javadecompilers.com/)  
上傳檔案後就會回傳 decompile 的結果

![](https://i.imgur.com/g5XZpZf.png)

經果美化並擷取重點會得到這段

```java
		return pass.substring(22,26).equals("3_ch") && 
		       pass.substring(24,27).equals("ch4") && 
		       pass.substring(1,3).equals("IS") && 
		       pass.substring(7,11).equals("_w0w") && 
		       pass.substring(8,11).equals("w0w") && 
		       pass.substring(38,41).equals("Ez_") && 
		       pass.substring(14,19).equals("3ms_t") && 
		       pass.substring(33,37).equals("_t0O") && 
		       pass.substring(45,49).equals("YoU}") && 
		       pass.substring(30,34).equals("_15_") && 
		       pass.substring(13,17).equals("e3ms") && 
		       pass.substring(15,17).equals("ms") && 
		       pass.substring(12,17).equals("se3ms") && 
		       pass.substring(24,29).equals("ch4l1") && 
		       pass.substring(41,44).equals("f0r") && 
		       pass.substring(2,6).equals("S3{0") && 
		       pass.substring(5,10).equals("0h_w0") && 
		       pass.substring(15,18).equals("ms_") && 
		       pass.substring(23,26).equals("_ch") && 
		       pass.substring(10,15).equals("w_se3") && 
		       pass.substring(4,6).equals("{0") && 
		       pass.substring(47,49).equals("U}") && 
		       pass.substring(41,45).equals("f0r_") && 
		       pass.substring(24,29).equals("ch4l1") && 
		       pass.substring(34,38).equals("t0O_") && 
		       pass.substring(41,43).equals("f0") && 
		       pass.substring(30,35).equals("_15_t") && 
		       pass.substring(27,30).equals("l1s") && 
		       pass.substring(11,16).equals("_se3m") && 
		       pass.substring(8,13).equals("w0w_s") && 
		       pass.substring(0,4).equals("AIS3") && 
		       pass.substring(0,5).equals("AIS3{") && 
		       pass.substring(42,46).equals("0r_Y") && 
		       pass.substring(35,39).equals("0O_E") && 
		       pass.substring(17,22).equals("_theS") && 
		       pass.substring(9,12).equals("0w_") && 
		       pass.substring(21,23).equals("S3");
```

這段是由 [gen_flag.py](./gen_flag.py) 生成的  
接下來就是手動或是自動把字串拼接上去即可  
或是用 regex 的方式抓出這樣比較好處理的資料  

[data](./data)

接著用程式直接拼接就好

```python
#!/usr/bin/python

f = open("data" , "r").read().strip().split("\n")
f = map(lambda i : i.split(",") , f)

ls = list("?" * 49)

for i in f:
    for j in range(int(i[0]) , int(i[1])):
        ls[j] = i[2][j - int(i[0])]

    print("".join(ls))
```

