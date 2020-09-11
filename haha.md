# 网页模板列表

+ 404.html：404报错，功能有一个搜索框，发起的请求是get参数s={参数}
+ author.html:个人信息，元素包含头像和介绍，还有一个输入框，以及一些信息展示，不需要可以删掉
+ author-no-sidebar.html：还是个人信息，不包含侧边栏
+ category~6：展示信息的页面，5和6还可以
+ contact.html：个人联系方式，联系方式展示，还有一个留言板
+ home1~5:个人主页，建议用1，比较好看
+ index.html:指标页面
+ page.html：大片的文字展示和评论，评论可以去掉，样式也可以更改，不需要右边的信息
page-no-sidebar.html：没有侧边栏的page页面，这个ok
search.html：搜索页面，建议不用
single.html：静态页面，展示信息用的，建议用4
single-gallery.html：有相册插件，展示相册用的，建议用4
single-video.html：有视屏播放的插件，播放视频用的，建议用4
tag.html：列表页面
typography.html：字体的说明

要用到的（需要新建路由）：
主页：home1
个人介绍：author-no-sidebar.html
联系方式：contact.html
信息展示（日志列表）：category5
page页面：page-no-sidebar
详情：single4.html
详情，相册：single4-gallery.html
详情，视屏：single4-video.html
列表样式：tag.html
404：404.html

实现步骤：
1.修改每个页面的元素展示，改成自己想要的，去掉多余的展示
通用部分
1)注释掉顶部导航栏<!-- Top bar -->，
2)将页面导航栏修改成自己想要的，去掉原来的
3)套用jinjia2模板，优化html文件
2.定义好这些页面各自的url，编写视函数，再去梳理html页面的跳转，修改对应的超链接

3.后端编写，能正常展示，这是最简陋的1.0版

最终效果：
网站构成：
导航栏：主页，笔记，照片，视频，留言板，个人信息
1.导航栏去调用接口加载放到数据库里面的详情页面
2.数据放到数据库，建立表结构，前端页面信息通过数据库里面的数据进行渲染

