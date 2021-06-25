

# Ayit_Connect_Net

## 安阳工学院自动连接校园网

随便摸了个py，  宿舍测试可用，回头去教室试试

更新：教室也可用  不过好像没用的必要。。。

# [post版](https://github.com/caravaned/Ayit_Connect_Net/blob/main/Connect_Net.py)

**需要用一下requests包**

**安装 requests:  cmd运行**

```
pip install requests
```

**<u>使用soket检查网络连接情况，没有联网就执行一次Post</u>**

~~header咱也不知道要的啥(可能不用加就行~~   -_-  ~~能用就行~~

### 开机自启

测试成功了可以扔到启动文件夹  默认应用选择python


```
文件夹地址： C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
```

也可以用bat去启动  就不用设置默认程序了：

​	新建txt填入下面一行，后缀改为bat或cmd，把bat/cmd文件丢到上面的启动文件夹

```
start pythonw X:\你的py文件路径\Connect_Net.py
```



# [selenium版](#)

利用selenium配合chromedrive 进行模拟操作

因为自动化打开的窗口都是无cookie无session的   所以不会有打开时已登录的情况 就很舒服

~~文件手贱删了 待提交~~



# 关联

摸完了才看见有大佬写过 

~~啊这    早知道直接拿来用就不写了~~

[SjyCoding大佬的python项目](https://github.com/SjyCoding/ayit_autologin)

[1281926469大佬的bat/sh项目](https://github.com/1281926469/Ayit_Autologin_CampusNetwork)

