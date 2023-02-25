
from datetime import datetime
import time

calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
# dailyBounds1 = ['9:00', '20:00']
calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
# dailyBounds2 = ['10:00', '18:30']
# meetingDuration = 30
# Sample_Output = [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]


timeszones=['00:00', '00:30', '01:00', '01:30', '02:00', '02:30', '03:00', '03:30', '04:00', '04:30', '05:00', '05:30', '06:00', '06:30', '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30', '22:00','22:30','23:00','23:30']


#times = ["00:00","00:30","01:00","01:30","02:00","02:30","03:00","0"]
#  print(times)

# print()

# start = datetime.datetime.now()
# sleep(10)
# end = datetime.datetime.now()
# duration = end - start

# lst1=[]
# for i in calendar1:
#     for j in i:
#         t1 = datetime.strptime(j, "%H:%M")
#         lst1.append(t1.time())
#         print(len(lst1))
#         if len(lst1)==2:
#             print(lst1[1] - lst1[0])
#             lst1.clear()
          
                
                


t1 = datetime.strptime(calendar1[0][0], "%H:%M")
print('Start time:', t1.time())

t2 = datetime.strptime(calendar1[0][1], "%H:%M")
print('End time:', t2.time())

t3 = datetime.strptime(calendar1[1][0], "%H:%M")
print('End time:', t3.time())

t4 = datetime.strptime(calendar1[1][1], "%H:%M")
print('End time:', t4.time())

t5 = datetime.strptime(calendar1[2][0], "%H:%M")
print('End time:', t5.time())

t6 = datetime.strptime(calendar1[2][1], "%H:%M")
print('End time:', t6.time())

if t5 in timeszones:
    print(timeszones[t5])
# t7 = datetime.strptime(calendar1[3][0], "%H:%M")
# print('End time:', t7.time())

# t8 = datetime.strptime(calendar1[3][1], "%H:%M")
# print('End time:', t8.time())

# get difference
delta = t2 - t1   
print(t4-t3)
print(t6-t5)
print(delta)     
        
# print('Start time:', t1.time())

# t2 = datetime.strptime(endtime, "%H:%M:%S")
# print('End time:', t2.time())

# # get difference
# delta = t2 - t1

# for i in calendar1:
#     for j in i:
#         lst2=[]
#         datedeatils=datetime.strptime(j,"%H:%M")
#         lst2.append(datedeatils.hour)
#         lst2.append(datedeatils.minute)
#         print(lst2)
#         for i in lst2:
#             if i 
        


