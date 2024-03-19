import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

# Your data
# x = np.array([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5])
x = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3])
# y = np.array([15.7, 36.2, 58.5, 79.7, 102.1])
y = np.array([[6.5, 23.5, 41.0, 58.2, 75.7, 92.8, 110.3] ])
# y = np.array([7, 16.7, 26.7, 36.2, 45.8, 55.7, 65.1, 74.8, 84.5, 94, 103.7, 113.4])
# y = np.array([5, 22.5, 40.0, 57.5, 74.8, 92.2, 109.6])
# y = np.array([2.5, 13.4, 25.6, 37.2, 48.7, 60.2, 71.7, 83.3, 94.4, 106.5])
# y = np.array([0.1, 9.5, 18.5, 26.7, 35.6, 44.2, 52.7, 61.6, 70.2, 78.8, 87.7, 96.3, 105.1, 113.7])
frequency = 1000


# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(x, y)

# Calculate predicted values
y_predicted = slope * x + intercept

# Print slope and intercept
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"Speed of sound: {slope*0.01*frequency:.6f}")
lol = 346.080000+346.214286+347.153333+ 347.714685+348.571429+346.636364+348.000000  
klok = lol / 7
print(f"average {klok:.6f}")

av = 347.195728

temp = (346.080000 - av)**2 + (346.214286 - av)**2 + (347.153333 - av)**2 + (347.714685 - av)**2 + (348.571429 - av)**2 + (346.636364 - av)**2 + (348.000000 - av)**2

s = temp / 6

print(f"standard s^2 deviation {s:.6f}")
print(f"standard deviation {s**0.5:.6f}")


# Calculate standard error of the estimate
print(f"std_error {std_err}")




# Linear regression equation
equation = f"y = {slope:.6f}x + {intercept:.6f}"
print(f"Linear Regression Equation: {equation}")

# Calculate average and standard deviation of y values
average_y = np.mean(y)
std_dev_y = np.std(y)

print(f"Average of y values: {average_y:.6f}")
print(f"Standard Deviation of y values: {std_dev_y:.6f}")

# Plot the data and regression line
plt.scatter(x, y, label='Data')
plt.plot(x, y_predicted, color='red', label='Linear Regression')
plt.xlabel('p = ∆φ/2π')
plt.ylabel(f'l {frequency}Hz [cm]')
plt.title(f'Linear Regression (l on p) {frequency} Hz [cm]')
plt.legend()

# Annotate the equation on the plot
plt.annotate(equation, xy=(0.5, 80), fontsize=10, color='blue')

plt.show()
