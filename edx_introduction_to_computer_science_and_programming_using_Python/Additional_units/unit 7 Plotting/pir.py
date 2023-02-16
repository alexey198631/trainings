import pylab as plt
#import matplotlib


mySample = []
myLinear = []
myQuad  = []

for i in range(0,30):
    mySample.append(i)
    myLinear.append(i)
    myQuad.append(i**2)

plt.clf()
plt.figure('lin')
#plt.clf()
plt.xlabel('numbers')
plt.ylabel('linear')
plt.ylim(0, 50)
plt.plot(mySample, myLinear, '-b' ,label = "linear",linewidth = 2.0)
plt.plot(mySample, myQuad,'r--' ,label = 'quadratic',linewidth = 3.0)
plt.title('linear vs quadratic')
plt.legend(loc='upper left')



#plt.figure('quad')
#plt.title('quadratic')
#plt.xlabel('numbers')
#plt.ylabel('quadratic')
#plt.plot(mySample, myQuad)


