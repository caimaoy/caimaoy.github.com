Title: 使用Pelican在Github上建立个人博客
Date: 2015-04-01 09:51
Modified: 2015-04-01 09:51
Category: IT
Tags: python, github, pelican
Slug: build-blog-on-github-with-pelican
Author: caimaoy

#相关连接
- [基础篇](http://www.xycoding.com/articles/2013/11/21/blog-create)
- [进阶篇](http://www.xycoding.com/articles/2013/11/22/blog-advance)  
- 有以上的链接我就不再赘述了，讲讲一些其他的坑


#基础知识
- python
- git
- github


#配置文件
>这个应该是说得比较多的一部分了，因为使用windows(我也不想用！！！)不得不改动一下配置文件  
重点修改如下


##Makefile

对于windows用户你可能要敢以下几件事

1. 下载make.exe, 并且添加到环境变量中
2. 修改Makefile文件关键是一些路径，具体忘记是哪些了，你可以去看这个blog的[源代码](http://github.com/caimaoy)对比一下


##pelicanconfig.py

```shell
git: publish
    git push origin $(GITHUB_PAGES_BRANCH)
	ghp-import -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR) -p
```

其中git的部分你懂就应该懂，说一下ghp-import  
ghp-import 是用于分支发布的，也就是说你的源码是在一个分支，而生成的页面是在另外一个分支发布

##ghp-import on Windows

[Until ghp-import Pull Request #25 is accepted,you will need to install a custom build of ghp-import:](http://docs.getpelican.com/en/latest/tips.html#publishing-to-github)  

```
pip install https://github.com/chevah/ghp-import/archive/win-support.zip
```

可以使用上面的pip安装  
如果你安装不上可以先卸载

```
pip uninstall ghp-import
```
如果你无法用下面的方法安装，请下载[zip包](https://github.com/chevah/ghp-import/archive/win-support.zip)后安装:
```
python setup.py install
```
