Title: pelican 如何添加404页面
Date: 2015-04-14 19:26
Modified: 2015-04-14 19:26
Category: it
Tags: github, pelican
Slug: pelican-add-404-page
Author: caimaoy



> pelican 已经挂在了github上面了但是如何挂上一个404 页面

```
Title: Not Found
Status: hidden
Save_as: 404.html

<script type="text/javascript" src="http://www.qq.com/404/search_children.js" charset="utf-8" homePageUrl="http://www.caimaoy.com" homePageName="Back to Home Page"></script>

```


###源码里面要说的几点

- 添加Status: hidden这个元信息
- Save_as为404.html，这样的话就满足了github的要求
- 挂上这一段js，出自我旁边的[鹅厂](http://www.qq.com/404/)这样的事业还是要支持一下的
- 最后看一看:[效果图](http://caimaoy.github.io/404/)


###TODO

- 当然也是因为我没有找到pelican直接挂原始页面的办法，如果你知道下面disqus我


#####乱七八糟
- 我说了我今天要去跑步，不能再做一个颓废的胖纸了！！！
- 另外今天在H亏成狗了，可以去天台了~
