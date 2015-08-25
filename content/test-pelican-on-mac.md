Title: windows 迁移 pelican 到 Mac 机器测试
Date: 2015-08-25 18:36
Modified: 2015-08-25 18:36
Category: it
Tags: test, mac, pelican, python
Slug: test-pelican-on-mac
Author: caimaoy


- 就是一个测试
- 在Mac机器上面使用pelican，很多的配置都有更改，如果测试通过了，我会把diff贴在下面的
- 先看看一下 diff Makefile
```
diff --git a/Makefile b/Makefile
index e69e9c8..c98df1f 100644
--- a/Makefile
+++ b/Makefile
@@ -107,6 +107,12 @@ cf_upload: publish
        cd $(OUTPUTDIR) && swift -v -A https://auth.api.rackspacecloud.com/v1.0 -U $(CLOUDFILES_USERNAME) -K $(CLOUDFILES_API_KEY) upload -c $(CLOUDFILES_CONTAINER) .

 github: publish
+       git add .
+       git ci -a -m "update"
+       git push origin source
+       echo caimaoy.com > $(OUTPUTDIR)/CNAME
+       cp googledabe3ca1b7fa15.html  $(OUTPUTDIR)/googledabe3ca1b7fa15.html
        ghp-import -m "Generate Pelican site" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
        git push origin $(GITHUB_PAGES_BRANCH)
```

- 使用上面的命令进行提交

- 因为是从 windows 迁移到mac机器上面，所以配置文件的分隔符要修改一下

```
diff --git a/publishconf.py b/publishconf.py
index 30d0156..bfb60d8 100644
--- a/publishconf.py
+++ b/publishconf.py
@@ -88,7 +88,7 @@ USE_FOLDER_AS_CATEGORY = True

 # plugin config
 # PLUGIN_PATHS = ['./plugins']
-PLUGIN_PATHS = [r'.\pelican-plugins']
+PLUGIN_PATHS = [r'./pelican-plugins']
 PLUGINS = [
     #'pandoc_reader',
     #'gzip_cache',
@@ -121,4 +121,4 @@ SITEMAP = {

 # THEME = r'.\pelican-themes\bootstrap2-dark'
 # THEME = r'.\pelican-themes\SoMA'
-THEME = r'.\pelican-themes\pelican-bootstrap3'
+THEME = r'./pelican-themes/pelican-bootstrap3'
```

- 主题文件和插件文件因为是在另外的两个git仓库里面，不需要修改
- 一切看起来还很美好？！
- NO！ Tags 不见了！
- 生产过程中没有报错，目前还在排查中！
- 囧！但是我已经上线了，又不想回滚 555

