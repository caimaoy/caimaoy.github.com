Title: VIM 去掉重复行
Date: 2015-05-06 10:57
Modified: 2015-05-06 10:57
Category: it
Tags: vim
Slug: vim-removing-duplicate-lines
Author: caimaoy


###不难理解的方法

- 先想想思路:
    - 先排序
    - 然后去掉重复的行
- 看看具体命令

```
:sort u
g/^\(.*\)\n\1$/d
```

####下面讲解一下：

```
:sort u             <-- 排序
g/^\(.*\)\n\1$/d    <-- kjkj
g/            /d    <-- g命令delete 满足要求的行
  ^\(.*\)\n         <-- 一行的开始到换行
           \1$      <-- \1 是前面(.*\)的内容，也就是说和前面的行内容相等
             $      <-- 结束符，两行相等是匹配条件
```

###一些高级vim语法的操作

[参考博文](http://vim.wikia.com/wiki/Uniq_-_Removing_duplicate_lines)

- 先看一下命令

```
g/\%(^\1\n\)\@<=\(.*\)$/d
g/\v%(^\1\n)@<=(.*)$/d
```

#### 看一下原本博客中的解释

```
g/\%(^\1\n\)\@<=\(.*\)$/d
g/                     /d  <-- Delete the lines matching the regexp
            \@<=           <-- If the bit following matches, make sure the bit preceding this symbol directly precedes the match
                \(.*\)$    <-- Match the line into subst register 1
  \%(     \)               <-- Group without placing in a subst register.
     ^\1\n                 <-- Match subst register 1 followed the new line between the 2 lines
```

- 这里面有一个reg的知识点：__环视__
- \@<= 这是一个逆向环视
- 所以建议大家还是用第一种方法就好了
