Title: 修复pelican 3.6 后没有标签云
Date: 2015-09-27 16:55
Modified: 2015-09-27 16:55
Category: it
Tags: python pelican
Slug: pelican-tag-cloud
Author: caimaoy

### 提问：我的标签咋不见了？

- 换了新的电脑 pelican 还是要先安装
- 使用了如下的命令：
```
pip install pelican
```
- 好像一切正常，拉取一下仓库，make 一下，发现标签云没有了
- 为什么？

### 回答：pelican 版本升级，标签云 tag_cloud 被移除了
- 看看官网的 faq 吧—— [http://docs.getpelican.com/en/3.6.3/faq.html](http://docs.getpelican.com/en/3.6.3/faq.html?#my-tag-cloud-is-missing-broken-since-i-upgraded-pelican)

> My tag-cloud is missing/broken since I upgraded Pelican
> In an ongoing effort to steamline Pelican, tag_cloud generation has been moved out of the pelican core and into a separate plugin. See the Plugins documentation further information about the Pelican plugin system.

### 解决：添加插件

- [pelican 的插件库地址](https://github.com/getpelican/pelican-plugins)
- 拉取仓库下来，修改 pelicanconf.py 或者 publishconf.py 文件
- 添加类似于如下的配置
```
# 插件路径
PLUGIN_PATHS = ['pelican-plugins']
# 添加插件
PLUGINS = ['tag_cloud',]

# tag_cloud 配置(自己个性配置)
DISPLAY_TAGS_INLINE = True
DISPLAY_TAGS_ON_SIDEBAR = True
TAG_CLOUD_STEPS = 4
```
