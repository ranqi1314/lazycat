## 第01课：初识Python

### Python简介

Python是由荷兰人吉多·范罗苏姆（Guido von Rossum）发明的一种编程语言，是目前世界上最受欢迎和拥有最多用户群体的编程语言。

<img src="https://gitee.com/jackfrued/mypic/raw/master/20210816232538.png" width="85%">

![QQ截图20220325143606](C:\WorkSpace\lazycat\0-python基础\Python-Core-50-Courses\新建文件夹\QQ截图20220325143606.png)

#### Python的历史

1. 1989年圣诞节：Guido开始写Python语言的编译器。
2. 1991年2月：第一个Python解释器诞生，它是用C语言实现的，可以调用C语言的库函数。
3. 1994年1月：Python 1.0正式发布。
4. 2000年10月：Python 2.0发布，Python的整个开发过程更加透明，生态圈开始慢慢形成。
5. 2008年12月：Python 3.0发布，引入了诸多现代编程语言的新特性，但并不完全兼容之前的Python代码。
6. 2020年1月：在Python 2和Python 3共存了11年之后，官方停止了对Python 2的更新和维护，希望用户尽快过渡到Python 3。

> **说明**：大多数软件的版本号一般分为三段，形如A.B.C，其中A表示大版本号，当软件整体重写升级或出现不向后兼容的改变时，才会增加A；B表示功能更新，出现新功能时增加B；C表示小的改动（例如：修复了某个Bug），只要有修改就增加C。

#### Python的优缺点

Python的优点很多，简单为大家列出几点。

1. 简单明确，跟其他很多语言相比，Python更容易上手。
2. 能用更少的代码做更多的事情，提升开发效率。
3. 开放源代码，拥有强大的社区和生态圈。
4. 能够做的事情非常多，有极强的适应性。
5. 能够在Windows、macOS、Linux等各种系统上运行。

Python最主要的缺点是执行效率低，但是当我们更看重产品的开发效率而不是执行效率的时候，Python就是很好的选择。

#### Python的应用领域

目前Python在Web服务器应用开发、云基础设施开发、**网络数据采集**（爬虫）、**数据分析**、量化交易、**机器学习**、**深度学习**、自动化测试、自动化运维等领域都有用武之地。

#### 人生苦短我用python

![QQ截图20220325142158](C:\WorkSpace\lazycat\0-python基础\Python-Core-50-Courses\新建文件夹\QQ截图20220325142158.png)

### 安装Python环境

想要开始你的Python编程之旅，首先得在计算机上安装Python环境，简单的说就是得安装运行Python程序的工具，通常也称之为Python解释器。我们强烈建议大家安装Python 3的环境，很明显它是目前更好的选择。

#### Windows环境

可以在[Python官方网站](https://www.python.org/downloads/)找到下载链接并下载Python 3的安装程序。

![QQ截图20220324142215](L:\WorkSpace\lazycat\0-python基础\Python-Core-50-Courses\新建文件夹\QQ截图20220324142215.png)

安装完成后可以打开Windows的“命令行提示符”工具（或“PowerShell”）并输入`python --version`或`python -V`来检查安装是否成功，命令行提示符可以在“运行”中输入`cmd`来打开或者在“开始菜单”的附件中找到它。如果看了Python解释器对应的版本号（如：Python 3.7.8），说明你的安装已经成功了，如下图所示。

<img src="L:\WorkSpace\lazycat\0-python基础\Python-Core-50-Courses\新建文件夹\QQ截图20220324142357.png" alt="QQ截图20220324142357" style="zoom:67%;" />

你还应该检查一下Python的包管理工具是否已经可用，对应的命令是`pip --version`。

![QQ截图20220324142601](L:\WorkSpace\lazycat\0-python基础\Python-Core-50-Courses\新建文件夹\QQ截图20220324142601.png)

Python语言可以做很多的事情，也值得我们去学习。要使用Python语言，首先需要在自己的计算机上安装Python环境，也就是运行Python程序的Python解释器。
