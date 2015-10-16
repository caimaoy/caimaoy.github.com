Title: python list implementation
Date: 2015-10-16 17:47
Modified: 2015-10-16 17:47
Category: it
Tags: python, list, implementation
Slug: python-list-implementation
Author: caimaoy


# Python list implementation
# 深入 Python 列表的内部实现

 
This post describes the CPython implementation of the list object. CPython is the most used Python implementation.  

Lists in Python are powerful and it is interesting to see how they are implemented internally.  

Following is a simple Python script appending some integers to a list and printing them.  


Cpython 是 Python 最为常见的实现。 Python 中的列表非常强大，本文介绍了列表在 CPython 内部是如何实现的，一定非常有趣。  

下面是一段 Python 脚本，在列表中添加几个整数，然后打印列表。  


```
>>> l = []
>>> l.append(1)
>>> l.append(2)
>>> l.append(3)
>>> l
[1, 2, 3]
>>> for e in l:
...   print e
...
1
2
3
```
As you can see, lists are iterable.  

可以发现，列表是一个迭代器。

## List object C structure
## 列表对象的 C 语言结构体

A list object in CPython is represented by the following C structure. ob_item is a list of pointers to the list elements. allocated is the number of slots allocated in memory.  

Cpython 中的列表实现类似于下面的 C 结构体。ob_item 是指向列表对象的指针数组。allocated 是申请内存的槽的个数。

```
typedef struct {
    PyObject_VAR_HEAD
    PyObject **ob_item;
    Py_ssize_t allocated;
} PyListObject;
```
## List initialization
## 列表初始化

Let’s look at what happens when we initialize an empty list. e.g. l = [].  

看看列表初始化的时候发生了什么，例如：l = []。

```
arguments: size of the list = 0
returns: list object = []
PyListNew:
    nbytes = size * size of global Python object = 0
    allocate new list object
    allocate list of pointers (ob_item) of size nbytes = 0
    clear ob_item
    set list's allocated var to 0 = 0 slots
    return list object
```

It is important to notice the difference between allocated slots and the size of the list. The size of a list is the same as len(l). The number of allocated slots is what has been allocated in memory. Often, you will see that allocated can be greater than size. This is to avoid needing calling realloc each time a new elements is appended to the list. We will see more about that later.  

要分清列表大小和分配的槽大小，这很重要。列表的大小和 len(l) 的大小相同。分配槽的大小是指已经在内存中已经分配了的槽空间数。通常分配的槽的大小要大于列表大小，这是为了避免每次列表添加元素的时候都调用分配内存的函数。下面会具体介绍。

## Append
## Append 操作


We append an integer to the list: l.append(1). What happens? The internal C function app1() is called:  

向列表添加一个整数：l.append(1) 时发生了什么？调用了底层的 C 函数 app1()。

```
arguments: list object, new element
returns: 0 if OK, -1 if not
app1:
    n = size of list
    call list_resize() to resize the list to size n+1 = 0 + 1 = 1
    list[n] = list[0] = new element
    return 0
```

Let’s look at list_resize(). It over-allocates memory to avoid calling list_resize too many time. The growth pattern of the list is: 0, 4, 8, 16, 25, 35, 46, 58, 72, 88, …  

下面是 list_resize() 函数。它会多申请一些内存，避免频繁调用 list_resize() 函数。列表的增长系列为：0，4，8，16，25，35，46，58，72，88……

```
arguments: list object, new size
returns: 0 if OK, -1 if not
list_resize:
    new_allocated = (newsize >> 3) + (newsize < 9 ? 3 : 6) = 3
    new_allocated += newsize = 3 + 1 = 4
    resize ob_item (list of pointers) to size new_allocated
    return 0
```

4 slots are now allocated to contain elements and the first one is the integer 1. You can see on the following diagram that l[0] points to the integer object that we just appended. The dashed squares represent the slots allocated but not used yet.  

现在分配了 4 个用来装列表元素的槽空间，并且第一个空间中为整数 1。如下图显示 l[0] 指向我们新添加的整数对象。虚线的方框表示已经分配但没有使用的槽空间。

Append operation amortized complexity is O(1).  

列表追加元素操作的平均复杂度为 O(1)。


![](http://ww4.sinaimg.cn/large/61203d71gw1ex3418lleoj204h05twef.jpg)

We continue by adding one more element: l.append(2). list_resize is called with n+1 = 2 but because the allocated size is 4, there is no need to allocate more memory. Same thing happens when we add 2 more integers: l.append(3), l.append(4). The following diagram shows what we have so far.  

继续添加新的元素：l.append(2)。调用 list_resize 函数，参数为 n+1 = 2， 但是因为已经申请了 4 个槽空间，所以不需要再申请内存空间。再添加两个整数的情况也是一样的：l.append(2)，l.append(2)。下图显示了我们现在的情况。

![](http://ww3.sinaimg.cn/mw690/61203d71gw1ex3418cf9uj204h07gjrf.jpg)

## Insert
## Insert 操作


Let’s insert a new integer (5) at position 1: l.insert(1,5) and look at what happens internally. ins1() is called:  

在列表偏移量 1 的位置插入新元素，整数 5：l.insert(1,5)，内部调用ins1() 函数。

```
arguments: list object, where, new element
returns: 0 if OK, -1 if not
ins1:
    resize list to size n+1 = 5 -> 4 more slots will be allocated
    starting at the last element up to the offset where, right shift each element
    set new element at offset where
    return 0
```

![](http://ww4.sinaimg.cn/mw690/61203d71gw1ex34198im9j20ht0ad0tn.jpg)

The dashed squares represent the slots allocated but not used yet. Here, 8 slots are allocated but the size or length of the list is only 5.  

虚线的方框依旧表示已经分配但没有使用的槽空间。现在分配了 8 个槽空间，但是列表的大小却只是 5。

Insert operation complexity is O(n).  

列表插入操作的平均复杂度为 O(n)。

## Pop
## Pop 操作


When you pop the last element: l.pop(), listpop() is called. list_resize is called inside listpop() and if the new size is less than half of the allocated size then the list is shrunk.  

弹出列表最后一个元素：调用 listpop() 函数。在 listpop() 函数中会调用 list_resize 函数，如果弹出元素后列表的大小小于分配的槽空间数的一半，将会缩减列表的大小。


```
arguments: list object
returns: element popped
listpop:
    if list empty:
        return null
    resize list with size 5 - 1 = 4. 4 is not less than 8/2 so no shrinkage
    set list object size to 4
    return last element
```


Pop operation complexity is O(1).  
列表 pop 操作的平均复杂度为 O(1)。

![](http://ww2.sinaimg.cn/mw690/61203d71gw1ex3419wrvaj20fg0adwf9.jpg)

You can observe that slot 4 still points to the integer but the important thing is the size of the list which is now 4.  

可以看到 pop 操作后槽空间 4 依然指向原先的整数对象，但是最为关键的是现在列表的大小已经变为 4。  

Let’s pop one more element. In list_resize(), size – 1 = 4 – 1 = 3 is less than half of the allocated slots so the list is shrunk to 6 slots and the new size of the list is now 3.  

继续 pop 一个元素。在 list_resize() 函数中，size – 1 = 4 – 1 = 3 已经小于所分配的槽空间大小的一半，所以缩减分配的槽空间为 6，同时现在列表的大小为 3。  

You can observe that slot 3 and 4 still point to some integers but the important thing is the size of the list which is now 3.  

可以看到槽空间 3 和 4 依然指向原先的整数，但是现在列表的大小已经变为 3。  

![](http://ww1.sinaimg.cn/mw690/61203d71gw1ex3419ln7uj20fc0aa3zb.jpg)

## Remove
## Remove 操作

Python list object has a method to remove a specific element: l.remove(5). listremove() is called.  

Python 的列表对象有个方法，删除指定的元素： l.remove(5)。底层调用 listremove() 函数。  

```
arguments: list object, element to remove
returns none if OK, null if not
listremove:
    loop through each list element:
        if correct element:
            slice list between element's slot and element's slot + 1
            return none
    return null
```

To slice the list and remove the element, list_ass_slice() is called and it is interesting to see how it works. Here, low offset is 1 and high offset is 2 as we are removing the element 5 at position 1.  

为了做列表的切片并且删除元素，调用了 list_ass_slice() 函数，它的实现方法比较有趣。我们在删除列表位置 1 的元素 5 的时候，低位的偏移量为 1 同时高位的偏移量为 2.  

```
arguments: list object, low offset, high offset
returns: 0 if OK
list_ass_slice:
    copy integer 5 to recycle list to dereference it
    shift elements from slot 2 to slot 1
    resize list to 5 slots
    return 0
```
Remove operation complexity is O(n).  

列表 remove 操作的复杂度为 O(n)。  

![](http://ww3.sinaimg.cn/mw690/61203d71gw1ex341ajn3fj20c9096wf2.jpg)

文章翻译自：[http://www.laurentluce.com/posts/python-list-implementation/](http://www.laurentluce.com/posts/python-list-implementation/)
