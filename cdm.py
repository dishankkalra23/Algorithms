import numpy as np
from statistics import variance as var
x = np.array([[0.0347, 0.0897, 0.0912, -73.3024, 6.2152],
              [0.0814, 0.2727, 0.0857, -62.5844, 3.1832],
              [0.0115, 0.2736, 0.0844, -65.2353, 2.7950]])

y = np.array([[0, 1, 1],
              [1, 0, 0],
              [0, 1, 0]])

cdm = []
for i in range(len(x[0])):
    fea = x[:,i]
    meanf = sum(fea)/len(fea)
    corr = []
    for j in range(len(y[0])):
        lab = y[:,j]
        print()
        meanl = sum(lab)/len(lab)
        varx = (var(fea,meanf)*var(lab,meanl))**0.5
        print(varx)
        covx = np.cov(fea,lab)[0,1]
        corr.append((1-(covx/varx)))
    cdm.append(corr)
print(cdm)
