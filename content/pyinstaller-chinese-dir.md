Title: pyinstaller生成exe中文路径无法运行解决方案
Date: 2015-04-15 20:14
Modified: 2015-04-15 20:14
Category: it
Tags: pyinstaller, python
Slug: pyinstaller-chinese-dir
Author: caimaoy


>pyinstaller生成的exe中文路径不能运行，错误信息如下:

```
D:\测试>"D:\测试\caimaoy_tool.exe"
Traceback (most recent call last):
  File "<string>", line 21, in <module>
  File "D:\Python27\Lib\site-packages\PyInstaller\loader\pyi_importers.py", line
 507, in install
  File "D:\Python27\Lib\site-packages\PyInstaller\loader\pyi_importers.py", line
 156, in __init__
ImportError: Can't load frozen modules.
```

- 直接上[解决方案](http://hi.baidu.com/domhow/item/341817d1afd5a558ddf9bee9)
- 在此[安装pyinstaller](https://github.com/dkw72n/pyinstaller/tree/develop)
- 但是介于他是百度空间的东西我还是备份一下的好，以下内容摘抄自解决方案

###原文
> 想修改windows的默认字符集为 utf8 的  
>
>
> 请参考这篇 <http://superuser.com/questions/239810/setting-utf8-as-default-character-encoding-in-windows-7>  

>本质问题是他把我们的目录当成是utf8编码的.  

> 然后, 只能看代码了. 发现 bootloader 里有个 stb\_to\_utf8 和 stb\_from\_utf8  
>
> 而且是 放在 #ifdef \_WIN32 里的! =.= 里面正经地实现了 UTF16 <-> UTF8 .
>于是. 把这两个函数用 MultiByteToWideChar WideCharToMultiByte 改了.重新编译.好了.  

>然后我 fork 过来改了. <https://github.com/dkw72n/pyinstaller/tree/develop> 有需要的可以来取.  


> (顺便整理下走过的弯路, 开始时已经知道是是模块加载的时候编码不对了, 只是一直纠结在''我怎么在模块加载的时候强行把他    的错误编码掰过来''. 无果. 可能的原因是那个阶段编码相关模块没被加载.)  

> 另外: 感谢 ikadog 同学两度把这个链接贴到了官方的ticket[[1](http://trac.pyinstaller.org/ticket/901),[2](http://trac.pyinstaller.org/ticket/824)]. 不过貌似他们没打算处理.  
>
> \# update(2014\_09\_01): 之前没有编译64位的bootloader，用64位的同学直接取下来会发现还是不能用，今天补上了，之前不行的可以再试试。  
