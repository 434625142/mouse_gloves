import pyautogui
#点击过快时会导致失控，所以禁用
pyautogui.FAILSAFE = False
width,hight=pyautogui.size()
print(width,hight)
#获取鼠标的当前位置
x, y = pyautogui.position()
print(x,y)
#duration是移动的时间
pyautogui.moveTo(300,300,duration=1)
x, y = pyautogui.position()
print(x,y)
#用键盘输入，第二个入口参数时延时的时间
pyautogui.typewrite('Hello world!', 0.25)
pyautogui.alert("oh,you did it!")
