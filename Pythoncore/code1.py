#50 No. Video, 51, 52
# Implicit Wait = Globally apply for all steps and waait for 5 sec each, it will not waste  the time if page loads in 1.5 sec
# Explicit Wait = Video 53 - This is PENDING
# Pause the test for few seconds using time class
# 'str1 = 'abcdef'
#  str2 = 'defghia''
import pickle
car=['audi','maruti','skoda']
file= 'car.txt'
fileobj=open(file,'wb')
car1=pickle.dump(car,fileobj)

fileobj.close()

fileobj=open(file,'rb')
mycar=pickle.load(fileobj)
print("---",mycar)





