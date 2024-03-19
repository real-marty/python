import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt
from math import sqrt


ti = [5.0, 8.0, 11.0, 14.0, 17.0]
ti5 = [20.0, 23.0, 26.0, 29.0, 32.0]
 


ri = [8.17, 8.26, 8.34, 8.45, 8.57]
ri5 = [8.65, 8.76, 8.85, 8.95, 9.06]

ai = []
aiAverage = 0
aiSquared = []

for i in range(5):
  numerator = ri5[i] - ri[i]
  denominator = ri[i] * ti5[i] - ri5[i] * ti[i]
  if denominator != 0:
      alpha = numerator / denominator
      ai.append(alpha)
  else:
      print("Error: Division by zero at index", i)


print(f"Ai values: {ai}")
print (f"Sum of Ai: {sum(ai)}")
aiAverage = sum(ai) / len(ai)
print(f"a Average - {aiAverage} \n")

for i in range(5):
  print(f"A({i}) - Average({ aiAverage}) = {ai[i] - aiAverage}")
  squared = (ai[i] - aiAverage)**2
  aiSquared.append(squared)
  print(f"({ai[i] - aiAverage})^2 = {squared}")
  print("\n")

print(f"Sum of Ai Squared: {sum(aiSquared)}")


# Assuming aiSquared is a list defined elsewhere in your code

print(f"chyba {sqrt(sum(aiSquared) / 20)}")




regT = ti.copy()
regT.extend(ti5)
regR = ri.copy()
regR.extend(ri5)
xConductor = np.array(regT)
yConductor = np.array(regR)

slope, intercept, r_value, p_value, std_err = linregress(xConductor, yConductor)

# Calculate predicted values
y_predicted = slope * xConductor + intercept

print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
equation = f"y = {slope:.6f}x + {intercept:.6f}"
print("slope / intercept", (slope / intercept))
#graph

# Plot the data and regression line
plt.scatter(xConductor, yConductor, label='Data')
plt.plot(xConductor, y_predicted, color='red', label='Linear Regression')
plt.xlabel('t[°C]')
plt.ylabel('R[Ω]')
plt.title('Linear Regression Electrical Resistance on the Temperature')
plt.legend()


# Annotate the equation on the plot
plt.text(30, 8.2, equation, fontsize=10, color='blue', horizontalalignment='right')


plt.show()
