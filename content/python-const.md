Title: python const
Date: 2015-06-10 16:55
Modified: 2015-06-10 16:55
Category: it
Tags: python
Slug: python-const
Author: caimaoy


- python 没有const 这样的语法，但是在项目中可能会有这样的需求？
- 自己动手丰衣足食！！！

###const.py

- 首先创建一个const.py文件，代码如下

```
# -*- coding: UTF-8 -*-

'''
Last modified time: 2015-06-09 09:49:29
Edit time: 2015-06-09 09:55:07
File name: const.py
Edit by caimaoy
'''

__author__ = 'caimaoy'

class _const(object):
    class ConstError(TypeError): pass
    class ConstCaseError(TypeError): pass

    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self.ConstError, "Can't change const. %s" % name
        if not name.isupper():
            raise self.ConstCaseError, \
                    'const name "%s" is not all uppercase' % name
        self.__dict__[name] = value


import sys
sys.modules[__name__] = _const()
```

- 使用代理模式，代理类的\_\_setattr\_\_方法
- 判断是否键值，抛出自定义的Error类
- 判断键值格式是否符合要求，抛出自定义的Error类

```
import sys
sys.modules[__name__] = _const()  # <<<使加载此模块指向_const()类
```

###test_const.py

```
# -*- coding: UTF-8 -*-

'''
Last modified time: 2015-06-10 17:14:54
Edit time: 2015-06-10 17:15:21
File name: test_cosnt.py
Edit by caimaoy
'''

__author__ = 'caimaoy'

import const

def test_cosnt_error():
    const.NAME = 'caimaoy'
    const.NAME = 'jessie'  # <<< ConstError("Can't change const. NAME",)

def test_cosnt_case_error():
    const.name = 'caimaoy' # <<< ConstCaseError('const name "name" is not all uppercase',)

def catch_error():
    try:
        test_cosnt_error()
    except Exception as e:
        print repr(e)

    try:
        test_cosnt_case_error()
    except Exception as e:
        print repr(e)

if __name__ == '__main__':
    catch_error()
```

- 对于const.py的测试
- 运行结果如下,符合预期
```
ConstError("Can't change const. NAME",)
ConstCaseError('const name "name" is not all uppercase',)
```
- 如果有需求可以代理\_\_del\_\_方法，保证常量不会被del


###constant.py

- 当然我们通常把所有的常量写入一个文件，方便管理

```
# -*- coding: UTF-8 -*-

'''
Last modified time: 2015-06-10 17:38:12
Edit time: 2015-06-10 17:38:17
File name: constant.py
Edit by caimaoy
'''

__author__ = 'caimaoy'

import const

const.NAME = 'caimaoy'
const.GAME = 'Monster Hunter'

```
- 使用的方法如下

```
# -*- coding: UTF-8 -*-

'''
Last modified time: 2015-06-10 17:40:28
Edit time: 2015-06-10 17:40:35
File name: use_const.py
Edit by caimaoy
'''

__author__ = 'caimaoy'

from constant import const

def use_const():
    print 'const.NAME is %s' % const.NAME
    print 'const.GAME is %s' % const.GAME

if __name__ == '__main__':
    use_const()
```
- 结果当然是预期的情况

```
const.NAME is caimaoy
const.GAME is Monster Hunter
```
