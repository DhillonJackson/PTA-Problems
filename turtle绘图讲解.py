
import turtle
turtle.setup(width,height,startx,starty)
 
# turtle.setup(width=_CFG["width"], height=_CFG["height"], startx=_CFG["leftright"], starty=_CFG["topbottom"])
import turtle, time
turtle.screensize(800, 600, "pink")
turtle.screensize() #返回默认大小(400, 300)
time.sleep(3)
turtle.screensize(canvwidth, canvheight, bg)
 
# turtle.screensize(canvwidth=None, canvheight=None, bg=None)
turtle.penup()   # 抬起画笔，之后移动画笔不绘制形状。
turtle.pendown() # 落下画笔，之后移动画笔将绘制形状。
turtle.pensize() # 用来设置画笔尺寸；turtle.width()设置画笔宽度，当无参数输入时返回当前画笔宽度。
turtle.pencolor()# 没有参数传入返回当前画笔颜色。turtle.pencolor((r,g,b))设置当前画笔颜色。
turtle.speed()   # 设置画笔移动速度，画笔绘制的速度范围[0,10]整数，数字越大越快。
# 颜色字符串
turtle.pencolor('purple')  # 小写
# RGB小数值
turtle.pencolor(0.63,0.13,0.94) #三个小数值
# RGB数值元组  
turtle.pencolor((0.63,0.13,0.94))  # 一个三元素元组
