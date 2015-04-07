Title: python print
Date: 2015-04-07 13:58
Modified: 2015-04-07 13:58
Category: it 
Tags: python
Slug: python-print
Author: caimaoy


今天突然想到要聊一下这个话题  

在实际的使用当中我们经常用到print来显示一些状态比如：

```
In [2]: print 'caimaoy'
caimaoy

In [3]: print 'caimaoy\n'
caimaoy


In [4]:
```
__注意一下空行数__  


这里面有个隐藏的参数，就是print会在每次输出后再输出一个'\n'，那如果我们是读取的
文本的文件一行一行print操作，其实每一行会打印两个'\n', 其中一个来自文本，另外一
个来自print的默认参数，如果我们只想要一个'\n'如何解决这个问题？


#解决方案#

##1. 使用''.join把需要的内容拼接起来然后一次性打印

大概可以得到这样的效果：
```
In [4]: a = ['caimaoy\n', 'caimaoy1\n', 'caimaoy3\n']

In [5]: print ''.join(a)
caimaoy
caimaoy1
caimaoy3


In [6]:
```

##2. 使用print中的参数end
```
In [6]: print ('caimaoy', end='')
  File "<ipython-input-6-dfd4986b6077>", line 1
    print ('caimaoy', end='')
                         ^
SyntaxError: invalid syntax
```
但是不幸的是在python2中我们好像不能只是这样做，

```
In [7]: from __future__ import print_function

In [8]: print ('caimaoy', end='')
caimaoy
In [9]:
```
我们需要做<pre>from __future__ import print_function</pre>这个操作可以正常使用。
