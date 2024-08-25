from statistics import mean #METHOD1
from scipy import stats #METHOD2
#METHOD1 PROCEDURE
est=[1,3,2,1,2,3,2,3,2,1,4,5,6,7,5,4,5,6,8,5,4,8]
est.sort()
tv=int(0.1*len(est))
est=est[tv:]
est=est[:len(est)-tv]
print(mean(est))
#METHOD2 PROCEDURE
est1=[1,3,2,1,2,3,2,3,2,1,4,5,6,7,5,4,5,6,8,5,4,8]
est1.sort()
m=stats.trim_mean(est1,0.1)
print(m)

