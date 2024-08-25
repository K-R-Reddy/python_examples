import statistics
import matplotlib.pyplot as plt
est=[1,3,2,1,2,3,2,3,2,1,4,5,6,7,5,4,5,6,8,5,4,8]
y=[]
est.sort()
tv=int(0.1*(len(est)))
est=est[tv:]
est=est[:len(est)-tv]
for i in range(len(est)):
    y.append(5)
plt.plot(est,y,'r--')
plt.plot([3.7],[5],'ro')
plt.plot(statistics.mean(est),[5],'bs')
plt.plot(statistics.median(est),[5],'g^')