import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt
from math import sqrt


ti = [4.0, 7.0, 10.0, 13.0, 16.0]
ti5 = [19.0, 22.0, 25.0, 28.0, 31.0]
 


ri = [7.87, 7.94, 8.07, 8.15, 8.24]
ri5 = [8.31, 8.37, 8.5, 8.61, 8.72]

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

print(f"Sum of Ai Squared: {sum(aiSquared)} * 10^(-3)")


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
plt.xlabel('t [°C]')
plt.ylabel('R [Ω]')
plt.title('Linear Regression Electrical Resistance on the Temperature')
plt.legend()


# Annotate the equation on the plot
plt.text(30, 8.2, equation, fontsize=10, color='blue', horizontalalignment='right')


plt.show()


# section halfconductors


t = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44]
r = [4.32, 4.08, 3.82, 3.46, 3.3, 3.08, 2.88, 2.7, 2.54, 2.39, 2.24, 2.1, 1.98, 1.86, 1.75, 1.65, 1.56, 1.47, 1.39, 1.31]


# Regrese
(slope, intercept, r_value, p_value, std_err) = linregress(t, r)

# Přímka regrese
y_pred = [slope * x + intercept for x in t]

# Korelační koeficient
r_squared = r_value**2

# Vizualizace
# Visualization
plt.plot(t, r, 'o', label='Measured values')
plt.xlabel('Temperature [°C]')
plt.ylabel('Resistance [kΩ]')
plt.legend()

# Information about regression analysis
print(f'Slope: {slope:.3f}')
print(f'Intercept: {intercept:.3f}')
print(f'Correlation coefficient: {r_squared:.3f}')
plt.show()


# Linear Regression
(slope, intercept, r_value, p_value, std_err) = linregress(t, r)
y_pred = [slope * x + intercept for x in t]
r_squared = r_value**2

# Visualization
plt.plot(t, r, 'o', label='Measured values')
plt.plot(t, y_pred, label='Linear Regression')  # Add line for regression
plt.xlabel('Temperature [°C]')
plt.ylabel('Resistance [kΩ]')
plt.legend()

# Information about regression analysis
print(f'Slope: {slope:.3f}')
print(f'Intercept: {intercept:.3f}')
print(f'Correlation coefficient (R^2): {r_squared:.3f}') 
plt.show()

# Transformation to lnR and 1/T
temp_K = [x + 273.15 for x in t]  # Convert to Kelvin
temp_inv = [1 / x for x in temp_K]  # Calculate 1/T
lnR = [np.log(x * 1000) for x in r]  # Calculate ln(R)


# Linear Regression on transformed data
(slope_ln, intercept_ln, r_value_ln, p_value_ln, std_err_ln) = linregress(temp_inv, lnR)
y_pred_ln = [slope_ln * x + intercept_ln for x in temp_inv]

# Plotting lnR vs 1/T
plt.figure()  # Create a new plot
plt.plot(temp_inv, lnR, 'o', label='Measured values')
plt.plot(temp_inv, y_pred_ln, label='Linear Regression') 
plt.xlabel('1/T (K^-1)')
plt.ylabel('ln(R)')
plt.legend()

# Annotate the equation on the plot
equation = f"y = {slope_ln:.6f}x + {intercept_ln:.6f}"
plt.text(0.0036, 7.3, equation, fontsize=10, color='green', horizontalalignment='right')

# Information about regression analysis on transformed data
print(f'Slope (lnR vs 1/T): {slope_ln:.3f}')
print(f'Intercept (lnR vs 1/T): {intercept_ln:.3f}')
print(f'Correlation coefficient (lnR vs 1/T): {r_value_ln**2:.3f}') 
print(f'Standard error of the estimate: {std_err_ln:.3f}')
print(f"equation {equation}")
plt.show()


print(temp_inv)
print(lnR)