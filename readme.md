## 简介 ##
这是一个本人无聊时写的一个命令行下Python的动画&美化库，目前有进度条，滚动条，仿metasploit大小写切换动画，多彩字体，动态彩色字体，渐变字体，动态渐变字体等功能，支持修改动画速度，动画样式。动画效果参见demo.py
## 用法 ##
下载project_sandsugar.py，把它放在你的python项目的目录下（高级玩家可以直接复制粘贴源代码），在你的python主程序中添加

`from project_sandsugar import *`
## 动画和特效的调用 ##

### 仿MSF大小写字体滚动效果 ###
使用以下代码

`text_scroll(text,delay)`

参数：
- text：显示的字符
- delay：（可选）动画速度，数值越小越快，建议0.15

示例：

`text_scroll("[*] starting patasploit framework",0.1)`

### 进度条 ###
使用以下代码

`progress_bar(prog,total,fin,unfin,arrow)`

参数：
- prog：进度变量
- total：进度条总长度
- fin：(可选）进度条风格，默认为=
- unfin：（可选）空白进度条风格，默认为空格
- arrow：（可选）箭头风格，默认为>

示例：

`progress_bar(j,30,"#","_","")`

### 滚动条 ###
使用以下代码

`scroll_bar(length,total,delay,text)`

参数：
- length：滚动条长度
- total：滚动条总长度
- delay：（可选）动画速度，数值越小越快，建议0.05
- text：（可选）显示的文字，默认为空

示例：

`scroll_bar(6,30,0.1,"Windows is searching for the solution...")`

### 旋转棒 ###
使用以下代码

`spin_bar(text,delay)`

参数：
- text：显示的文字
- delay：（可选）动画速度，数值越小越快，建议0.1

示例：

`spin_bar("[*] Firing the BFG10000",0.1)`

### 彩色字体 ###
使用以下代码

`color_text(text,color)`

参数：
- text：显示的文字
- color：文字颜色，默认为红色

颜色列表：
- red：红色
- green：绿色
- yellow：黄色
- blue：蓝色
- magenta：洋红
- light_blue：青色

示例：

`color_text("[*] Leaving the MCRN ship",'yellow')`

### 动态彩色字体 ###
使用以下代码

`dycolor_text(text,delay)`

参数：
- text：显示的文字
- delay：（可选）颜色切换速度，数值越小越快，建议0.15

示例：

`dycolor_text("[*] Entering zero gravity",0.15)`

### 渐变彩色字体 ###
使用以下代码

`gradient_text(text,color)`

参数：
- text：显示的文字
- color：（可选）渐变颜色码，参考Xterm 256 色图，以列表形式输入

示例：

`gradient_text("[*] Senpai of the pool, what's your wisdom?",["166","172","178"])`

### 动态渐变彩色字体 ###
使用以下代码

`dygradient_text(text,delay,color_plate)`

参数：
- text：显示的文字
- delay：（可选）动画速度，数值越小越快，建议0.15
- color_plate：（可选）渐变颜色模板，默认为0，输入Xterm 256 色图中每行开头颜色的代码和93之间的差值即可选择此行颜色作为渐变动画，比如例子中的-72就是以颜色代号为21开头的那一行作为渐变动画颜色模板的。

示例：

`dygradient_text("[*] Listen, I don't have much time",0.1,-72)`

### Xterm 256 色图 ###

![色图](https://github.com/arandintday/project_sandsugar/blob/master/IMG/color_pic.png)

