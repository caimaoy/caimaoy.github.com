Title: python re.sub
Date: 2015-07-13 11:17
Modified: 2015-07-13 11:17
Category: it
Tags: python
Slug: python-re-sub
Author: caimaoy


- 经常遇到使用re.sub的情况，但经常忘记，所以记录一下
- 首先还是看看大神的简介：[crifan【整理】详解Python中re.sub](http://www.crifan.com/python_re_sub_detailed_introduction/)

```
sub(pattern, repl, string, count=0, flags=0)
    Return the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in string by the
    replacement repl.  repl can be either a string or a callable;
    if a string, backslash escapes in it are processed.  If it is
    a callable, it's passed the match object and must return
    a replacement string to be used.
```
- [re.sub官方文档](https://docs.python.org/2/library/re.html#re.sub)


- 用法和功能我就不详述了，下面看看一些奇葩需求
- 首先是换位的需求

```
def change_place(s):
    '''
    >>> change_place('caimaoy&jessie')
    'jessie&caimaoy'
    '''
    return re.sub(r'(caimaoy)(&)(jessie)', r'\3\2\1', s)
```
- 然后是换位换字符的需求

```
def change_place_and_joiner(s):
    '''
    >>> change_place_and_joiner('caimaoy&jessie')
    'jessie with caimaoy'
    '''
    return re.sub(r'(caimaoy)(&)(jessie)', r'\3 with \1', s)
```

- 看起来不错，但是如果我要换的字符是数值，会发生什么？

```
def change_place_and_joiner_with_number(s):
    '''
    >>> change_place_and_joiner_with_number('caimaoy&jessie')
    'jessie0caimaoy'
    '''
    return re.sub(r'(caimaoy)(&)(jessie)', r'\30\1', s)
```
```
File "test_doc_test.py", line 37, in __main__.change_place_and_joiner_with_numbe
r
Failed example:
    change_place_and_joiner_with_number('caimaoy&jessie')
Exception raised:
    Traceback (most recent call last):
      File "D:\Python27\lib\doctest.py", line 1289, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.change_place_and_joiner_with_number[0]>", line 1,
in <module>
        change_place_and_joiner_with_number('caimaoy&jessie')
      File "test_doc_test.py", line 40, in change_place_and_joiner_with_number
        return re.sub(r'(caimaoy)(&)(jessie)', r'\30\1', s)
      File "D:\Python27\lib\re.py", line 151, in sub
        return _compile(pattern, flags).sub(repl, string, count)
      File "D:\Python27\lib\re.py", line 275, in filter
        return sre_parse.expand_template(template, match)
      File "D:\Python27\lib\sre_parse.py", line 789, in expand_template
        raise error, "invalid group reference"
    error: invalid group reference
```

- 报错了！大概的描述就是我们根本就没有30这个组
- 如何解决？看看文档，下面是解决方案，__用\g<n>来替代\n__

```
def change_place_and_joiner_with_number(s):
    '''
    >>> change_place_and_joiner_with_number('caimaoy&jessie')
    'jessie0caimaoy'
    '''
    return re.sub(r'(caimaoy)(&)(jessie)', r'\g<3>0\g<1>', s)
```

- 好像没有进一步的需求了，其实上面的需求re.sub的第二个参数传入一个函数是可以解决的
- 不过就是懒（优秀品质）
- 最后给一个传入函数的例子
- 要replace为大写

```
def change_place_and_upper(s):
    '''
    >>> change_place_and_upper('caimaoy&jessie')
    'JESSIE&CAIMAOY'
    '''
    def _upper(matched):
        return matched.group(3).upper() + matched.group(2) + matched.group(1).upper()
    return re.sub(r'(caimaoy)(&)(jessie)', _upper, s)
```

- 看看以后还有什么需求，估计传入函数基本都能解决


