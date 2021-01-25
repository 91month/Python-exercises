import turtle
'''
t = turtle.Pen()
for x in range(360):
    t.forward(x)
    t.left(59)
'''
#六边形
'''t = turtle.Pen()
turtle.bgcolor("black")
sides = 6
colors = ["red", "yellow", "green", "blue", "orange", "purple"]
for x in range(360):
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides / 200)
'''

#自定义边框
'''t = turtle.Pen()
turtle.bgcolor("black")
sides = eval(input("输入要绘制的边的数目（2-6）！"))
colors = ["red", "yellow", "green", "blue", "orange", "purple"]
for x in range(100):
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides / 200)
'''

#带有文字的图形绘制
'''t = turtle.Pen()
turtle.bgcolor("black")

my_name = turtle.textinput("输入你的姓名", "你的名字？")
colors = ["red", "yellow", "purple", "blue"]
for x in range(100):
    t.pencolor(colors[x % 4])
    t.penup()
    t.forward(x * 4)
    t.pendown()
    t.write(my_name, font=("Arial", int((x + 4) / 4), "bold"))
    t.left(92)
'''


#绘制雪花
'''from turtle import *
from random import *
def ground():
    hideturtle()
    speed(100)
    for i in range(400):
        pensize(randint(5, 10))
        x = randint(-400, 350)
        y = randint(-280, -1)
        r = -y / 280
        g = -y / 280
        b = -y / 280
        pencolor(r, g, b)
        penup()
        goto(x, y)
        pendown()
        forward(randint(40, 100))


def snow():
    hideturtle()
    speed(100)
    pensize(2)
    for i in range(100):
        r = random()
        g = random()
        b = random()
        pencolor(r, g, b)
        penup()
        setx(randint(-350, 350))
        sety(randint(1, 270))
        pendown()
        dens = randint(8, 12)
        snowsize = randint(10, 14)
        for j in range(dens):
            forward(snowsize)
            backward(snowsize)
            right(360 / dens)


def main():
    setup(800, 600, 0, 0)
    tracer(False)
    bgcolor("black")
    snow()
    ground()
    tracer(True)
    mainloop()

main()
'''

#绘制科赫雪花
'''def coch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            coch(size / 3, n - 1)

def main():
    turtle.setup(600, 600)
    turtle.penup()
    turtle.bgcolor("white")
    turtle.pensize(2)
    turtle.goto(-200, 100)
    turtle.pendown()
    level = 3
    coch(400, level)
    turtle.right(120)
    coch(400, level)
    turtle.right(120)
    coch(400, level)
    turtle.hideturtle()

main()
'''

#绘制七彩线条
'''import turtle as t

t.setup(1000, 1000)
t.pen(shown=False, pendown=False, pensize=10, speed=0)

colorlist = [(255, 0, 0), (255, 165, 0), (255, 255, 0), \
             (0, 255, 0), (0, 255, 255), (0, 0, 255), (139, 0, 255)]
colorlist.reverse()

t.fd(-250)
t.seth(-40)

t.colormode(255)

t.pendown()
for color in colorlist[:-1]:
    t.pencolor(color)
    t.circle(30, 80)
    t.circle(-30, 80)

t.pencolor(colorlist[-1])
t.circle(30, 80 / 2)
t.fd(40)
t.circle(25, 180)
t.fd(40 * 2 / 3)
t.done()
'''


# 绘制太极图函数
'''def draw_TJT(R):
    turtle.screensize(800, 600, "blue")  # 画布长、宽、背景色 长宽单位为像素
    turtle.pensize(1)  # 画笔宽度
    turtle.pencolor('black')  # 画笔颜色
    turtle.speed(10)  # 画笔移动速度

    TJT_color = {1: 'white', -1: 'black'}  # 太极图填充色 1 白色 -1 黑色
    color_list = [1, -1]

    """
    先画半边，再画另一边
    """
    for c in color_list:
        turtle.fillcolor(TJT_color.get(c))  # 获取该半边的填充色
        turtle.begin_fill()  # 开始填充

        # 开始画出半边的轮廓
        turtle.circle(R / 2, 180)
        turtle.circle(R, 180)
        turtle.circle(R / 2, -180)

        turtle.end_fill()  # 结束填充 上色完成

        # 绘制该半边的鱼眼
        turtle.penup()  # 提起画笔，移动不留痕
        turtle.goto(0, R / 3 * c)  # 移动到该半边的鱼眼的圆上 R/3*c 表示移动到哪边
        turtle.pendown()  # 放下画笔，移动留痕
        turtle.fillcolor(TJT_color.get(-c))  # 获取鱼眼填充色, 与该半边相反
        turtle.begin_fill()
        turtle.circle(-R / 6, 360)
        turtle.end_fill()

        # 回到原点，为下一循环的开始做准备
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()

    # 绘制文本
    turtle.penup()
    turtle.goto(0, -R - 50)
    turtle.pendown()
    turtle.write("太极图 made by kjshen", font=('Arial', 12, 'normal'))


if __name__ == '__main__':
    R = 100  # 太极图半径
    draw_TJT(R)
    input('Press Enter to exit...')  # 防止程序运行完成后就自动关闭窗口
'''


'''
turtle.setup(2000, 2000, 0, 0)
turtle.pensize(20)
turtle.pencolor("black")
turtle.seth(0)
turtle.fd(400)
turtle.seth(-144)
turtle.fd(400)
turtle.seth(-144 - 144)
turtle.fd(400)
turtle.seth(-144 - 144 - 144)
turtle.fd(400)
turtle.seth(-144 - 144 - 144 - 144)
turtle.fd(400)
input("")

'''



'''书写汉字王'''
'''import turtle as t
t.pensize(20)
t.colormode(255)
t.color("red", "black")
t.setup(800, 600)
t.speed(10)
 
 
t.pu()
t.goto(-100, 100)
t.pd()
t.seth(0)
t.fd(200)
 
 
t.color("yellow")
t.pu()
t.goto(-100, 10)
t.pd()
t.seth(0)
t.fd(200)
 
 
t.color((0,255,0))
t.pu()
t.goto(-150, -80)
t.pd()
t.seth(0)
t.fd(300)
 
 
t.color((255,0,255))
t.pu()
t.goto(0, 100)
t.pd()
t.seth(-90)
t.fd(180)
t.done()
'''

#新年快乐
'''
penup简称up --------- t.up()就是抬起笔
pendown简称down --------t.down()就是落下笔
forward简称fd------------t.fd()就是向前画
backward----------t.backward()向后画
goto----------t.goto(二维坐标)箭头到此地
pensize--------t.pensize(笔的粗细（像素）)
pencolor简称color----t.color(“red”)参数也可为rgb小数值或元组值
left---------t.left(）箭头左转，里面写度数，可正可负
right-----右转
setup-----t.setup(width,height,startx,starty)设置窗口大小及位置
begin_fill------开始填充
end_fill---------结束填充
fillcolor----------填充颜色
circle---------一个参数是圆，二个（半径，角度（对应弧度）），另外，circle（40，steps=3）为三角形边长40像素，多边形可以改steps值。
'''

'''
import turtle as t
t.pensize(10)
t.color("red")
t.up()
t.goto(-200,150)
t.pendown()
t.left(-135)
t.fd(30)
t.up()
t.goto(-250,130)
t.pendown()
t.left(135)
t.fd(80)
t.up()
t.goto(-235,120)
t.down()
t.left(-45)
t.fd(28)
t.up()
t.goto(-185,120)
t.down()
t.left(-90)
t.fd(25)
t.up()
t.goto(-250,100)
t.down()
t.left(135)
t.fd(80)
t.up()
t.goto(-250,80)
t.down()
t.fd(80)
t.up()
t.goto(-205,100)
t.down()
t.left(-90)
t.fd(100)
t.left(-135)
t.fd(30)
t.up()
t.goto(-220,60)
t.down()
t.left(90)
t.fd(40)
t.up()
t.goto(-190,60)
t.down()
t.left(90)
t.fd(30)
t.up()
t.goto(-100,150)
t.down()
t.left(-100)
t.fd(60)
t.left(50)
t.fd(120)
t.backward(95)
t.left(95)
t.fd(70)
t.up()
t.goto(-115,90)
t.down()
t.left(-90)
t.fd(93)
#年
t.up()
t.color("orange")
t.goto(100,135)
t.left(-45)
t.down()
t.fd(45)
t.backward(22)
t.left(135)
t.fd(100)
t.up()
t.goto(97,95)
t.down()
t.fd(80)
t.backward(80)
t.left(-90)
t.fd(30)
t.left(-90)
t.fd(15)
t.backward(112)
t.up()
t.goto(140,115)
t.down()
t.left(90)
t.fd(110)
#kuai
t.up()
t.color("pink")
t.goto(-230,-55)
t.down()
t.fd(160)
t.up()
t.goto(-233,-95)
t.down()
t.left(-40)
t.fd(27)
t.pensize(3)
t.backward(30)
t.left(76)
t.pensize(10)
t.fd(20)
t.up()
t.goto(-190,-90)
t.left(55)
t.down()
t.fd(80)
t.left(-90)
t.fd(40)
t.left(90)
t.fd(20)
t.backward(110)
t.up()
t.goto(-150,-50)
t.left(-90)
t.down()
t.fd(80)
t.circle(-150,40)
t.up()
t.goto(-150,-140)
t.down()
t.left(50)
t.circle(150,35)
#le
t.up()
t.goto(100,-80)
t.color("yellow")
t.down()
t.left(50)
t.circle(180,30)
t.up()
t.goto(100,-80)
t.down()
t.left(-127)
t.fd(45)
t.left(90)
t.fd(90)
t.up()
t.goto(140,-85)
t.down()
t.left(-90)
t.fd(130)
t.left(-135)
t.fd(40)
t.up()
t.goto(124,-155)
t.down()
t.left(90)
t.fd(50)
t.up()
t.goto(158,-160)
t.down()
t.left(80)
t.fd(46)
#tuan
t.up()
t.goto(-50,-160)
t.down()
t.pensize(5)
t.color("bloown")
t.begin_fill()
t.fillcolor("yellow")
t.circle(50)
t.end_fill()
t.up()
t.goto(-35,-130)
t.down()
t.color("black")
t.circle(7)
t.up()
t.goto(5,-130)
t.down()
t.circle(7)
t.up()
t.goto(-20,-150)
t.down()
t.circle(20,130)
#xin
t.up()
t.goto(-30,80)
t.pensize(60)
t.color("red")
t.left(-120)
t.down()
t.fd(50)
t.left(90)
t.fd(50)
#ok   over

'''

import turtle as t
for i in range(4):
    t.circle(90,90)
    t.right(180)
    










