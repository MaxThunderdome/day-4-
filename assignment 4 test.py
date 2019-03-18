import numpy as np
from statistics import mean
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
Polynomial = np.polynomial.Polynomial
# location = input("Select file location")
infile = open("DataForAssignment4.txt", "r")
content = infile.readlines()
k=len(content)
while k<20:
   contents.append("\n")
   k+=1
titleLine = content[0]
title = " ".join(titleLine.split()[1:])
print(title)
dateLine = content[2]
i = 6
blankData = []
while(1):
    if content[i] == "\n":
        break
    print(content[i])
    blankData.append(float(content[i].split("\n")[0]))
    i+=1
j = i + 4
#print(blankData)
print("blank deviation=", np.std(blankData))
print("LOD = ", np.std(blankData)*3)
while(1):
    if content[i] == "Concentration	Readings\n" or i >= j:
        break
    i+=1
i+=1
xArray = []
yArray = []
while(len(content)>i):
    pts = content[i].split("\t")
    #print(pts)
    m=0
    while m<3:
        xArray.append(pts[0])
        yArray.append(pts[m+2].strip("\n"))
        m+=1
    i+=1
print("xArray: ",xArray)
print("yArray: ",yArray)
x = np.array(xArray, dtype=np.float64)
y = np.array(yArray, dtype=np.float64)
def best_fit_slope_and_intercept(xArray, yArray):
    m = (((mean(xArray) * mean(yArray)) - mean(yArray * xArray)) /
         ((mean(xArray) * mean(xArray)) - mean(xArray * xArray)))

    b = mean(yArray) - m * mean(xArray)

    return m, b
print("best_fit result: ", best_fit_slope_and_intercept(x, y))
m,b=best_fit_slope_and_intercept(x, y)

Fit_line = [(m*xpt)+b for xpt in x]
plt.scatter(x,y,color='#003F72')
plt.plot(x, Fit_line)
plt.show()