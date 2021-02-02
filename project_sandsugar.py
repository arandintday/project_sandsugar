import time
#MSF like boot ascii animation仿MSF大小写字体滚动效果
def text_scroll(text="text",delay=0.15):
    for i in range(0,len(text)):
        time.sleep(delay)#Animation speed动画速度
        print("{}{}{}".format(text[:i],text[i].upper(),text[i+1:]),end="\r")
    return 0
#Progress bar进度条
def progress_bar(prog=0,total=50,fin="=",unfin=" ",arrow=">"):
    print("[{}{}{}]{}%".format(fin*prog,arrow,unfin*(total-prog-1),int((prog+1)/total*100)),end="\r")
    return 0
#Scrolling bar滚动条
def scroll_bar(length=5,total=50,delay=0.1,text=""):
    fin="="#Finished progress bar style进度条风格
    unfin=" "#Unfinished progress bar style空白进度条风格
    for m in range(0,total-length):
        print("[{}{}{}]{}".format(unfin*m,fin*length,unfin*(total-m-length),text),end="\r")
        time.sleep(delay)
    for m in range(total-length,0,-1):
        print("[{}{}{}]{}".format(unfin*m,fin*length,unfin*(total-m-length),text),end="\r")
        time.sleep(delay)
    return 0
#Classic spin bar旋转棒
def spin_bar(text="Text",delay=0.1):
    spin="-\|/"
    for k in range(0,len(spin)):
        time.sleep(delay)#Animation speed动画速度
        print("{}...{}".format(text,spin[k]),end="\r")
    return 0
#Colorful fonts多彩字体
def color_text(text="Text",color="red"):
    if color=="red":
        print("\033[0;31m{}\033[0m".format(text))#RED红色
    elif color=="green":
        print("\033[0;32m{}\033[0m".format(text))#GREEN绿色
    elif color=="yellow":
        print("\033[0;33m{}\033[0m".format(text))#YELLOW黄色
    elif color=="blue":
        print("\033[0;34m{}\033[0m".format(text))#BLUE蓝色
    elif color=="magenta":
        print("\033[0;35m{}\033[0m".format(text))#MAGENTA洋红
    elif color=="light_blue":
        print("\033[0;36m{}\033[0m".format(text))#LIGHT BLUE青色
    else:
        print(text)
    return 0
#Dynamic color font动态彩色字体
def dycolor_text(text="Text",delay=0.15):
    for color in range(31,38):
        time.sleep(delay)
        print("\033[0;{}m{}\033[0m".format(color,text),end="\r")
    return 0
#Gradient font渐变彩色字体
def gradient_text(text="Text",color=["34","40","46"]):
    display_text=""
    split=len(text)//len(color)
    for i in range(0,len(text),split):
        num=i//split
        if num>(len(color)-1):
            num-=1
        display_text+="\033[38;5;{}m{}\033[0m".format(color[num],text[i:i+split])
    print(display_text)
    return 0
#Dynamic gradient font动态渐变彩色字体
def dygradient_text(text="Text",delay=0.15,color_plate=0):
    color=[[93,99,105],[99,105,111],[105,111,117],[111,117,123],[117,123,159],[123,159,153],[159,153,147],[153,147,141],[147,141,135],[141,135,129],[135,129,93],[129,93,99]]
    for i in range(0,len(color)):
        for j in range(0,len(color[i])):
            color[i][j]=color_plate+color[i][j]
    split=len(text)//len(color[0])
    for i in range(0,len(color)):
        display_text=""
        for j in range(0,len(text),split):
            num=j//split
            if num>(len(color[i])-1):
                num-=1
            display_text+="\033[38;5;{}m{}\033[0m".format(color[i][num],text[j:j+split])
        print(display_text,end="\r")
        time.sleep(delay)
    return 0
