import time
import winsound
from datetime import datetime


class Alarm:
    def __init__(self, h, m, replay):
        self.h = h
        self.m = m
        self.replay = replay


    def signal(self):
        N = ["0","1","2","3","4","5","6","7","8","9"]
        while True:
            date = datetime.now()
            now_hour = str(date.hour)
            now_minute = str(date.minute)
            for x in N:
                if now_hour == x:
                    now_hour = "0" + now_hour
                if now_minute == x:
                    now_minute = "0" + now_minute
            if now_hour == h and now_minute == m:
                for i in  range(0, replay + 1, 1):
                    winsound.Beep(2500,1500)
                    time.sleep(0.1)
                time.sleep(60)

# Ввод времени
t = input("Enter time:\n hh:mm\n\n ")
# Ввод количества сигналов
replay = int(input("Enter signal replay: "))
set_hour = True
h = ""
m = ""
for char in t:
    if set_hour:
        if char != ":":
            h += char
        else:
            set_hour = False
    else:
        m += char
# Вызов класса
a = Alarm(h,m,replay)
a.signal()
