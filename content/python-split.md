Title: python split
Date: 2015-05-07 10:14
Modified: 2015-05-07 10:14
Category: it
Tags: python
Slug: python-split
Author: caimaoy


###str.split


```
Help on method_descriptor:

split(...)
    S.split([sep [,maxsplit]]) -> list of strings

    Return a list of the words in the string S, using sep as the
    delimiter string.  If maxsplit is given, at most maxsplit
    splits are done. If sep is not specified or is None, any
    whitespace string is a separator and empty strings are removed
    from the result.
```

####基本用法

```
In [5]: 'caimaoy jessie HHKB Tesla'.split(' ')
Out[5]: ['caimaoy', 'jessie', 'HHKB', 'Tesla']
```

###re.split

```
Help on function split in module re:

split(pattern, string, maxsplit=0, flags=0)
    Split the source string by the occurrences of the pattern,
    returning a list containing the resulting substrings.
```

####基本用法

```
In [14]: re.split(r'\d', 'caimaoy1jessie2HHKB3Tesla')
Out[14]: ['caimaoy', 'jessie', 'HHKB', 'Tesla']
```


####迷惑用法

```
In [15]: re.split('o(o)', 'foobar')
Out[15]: ['f', 'o', 'bar']
```

- 这是发生了什么啊？
- 书里面的解释

> 如果模式包括小括号，那么括起来的字符组合会散布在分割后的字字符串之间

- 不过上面的例子还是很让人迷惑，还是自己写几个


```
In [19]: re.split('(and)', 'caimaoyandjessie')
Out[19]: ['caimaoy', 'and', 'jessie']

In [20]: re.split('o(and)o', 'caimaoyoandojessie')
Out[20]: ['caimaoy', 'and', 'jessie']

In [21]: re.split(r'(\d)', 'caimaoy3jessie')
Out[21]: ['caimaoy', '3', 'jessie']
```

- 相信这几个例子写了之后就没有那么迷惑了






