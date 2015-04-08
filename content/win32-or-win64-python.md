Title: python 判断windows系统是32位还是64位
Date: 2015-04-08 10:24
Modified: 2015-04-08 10:24
Category: it
Tags: python, windows
Slug: win32-or-win64-python
Author: caimaoy


###首先来看看错误方法：  

- 以下是在64位机器下使用32位python得到的结果

```
In [14]: sys.version
Out[14]: '2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)]'
```
- 这里看到的其实是python的版本，而不是系统的版本

```
In [15]: platform.architecture()
Out[15]: ('32bit', 'WindowsPE')
```
- 这个运行的结果也是不正确的


```
In [16]: print sys.maxint
2147483647
```
- 数字是2\*\*31-1的话就是32位(这是错误的！！！)
- 数字式2\*\*64-1的话就是64位(这也是错误的！！！)

上面引述的方法也是不正确的，因为使用的是sys库


###正确方法

####1. 通过环境变量进行判断
```
def is_64_windows():
    return 'PROGRAMFILES(X86)' in os.environ
```
####2. 通过注册表进行判断
```
aReg = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, \
"SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Run")
```
- 存在即为64bits
- 如果不存在会抛出异常，进行捕获判断返回32bits


个人观点到此结束，如果有其他方法可以评论回复我，THX
