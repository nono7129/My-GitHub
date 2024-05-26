from random import *
a = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if time <= 15:
      print("[O] {}번째 손님 (소요시간 : {})분)".format(i, time))
      a += 1
    else:
      print("[] {}번째 손님 (소요시간 : {})분)".format(i, time))
      a += 0
print("총 탑승객 수 :", a)