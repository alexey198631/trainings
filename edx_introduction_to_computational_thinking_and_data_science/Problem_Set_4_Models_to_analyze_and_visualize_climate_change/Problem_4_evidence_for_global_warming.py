"""
Let's try another way to get data points and see whether we can find some evidence for global warming.
We surmise, due to global warming, the average temperature should increase over time.
Thus, we are going to plot the results of a linear regression on the average annual temperature of Boston.

In a similar manner to Problem 3, fill in the missing piece to the following code.
The code should generate your data samples. Each sample represents a year from 1961 to 2005 and the average
annual temperature in Boston in that year (again, the provided helper class is helpful).
Fit your data to a linear line with generate_models and plot the regression results with evaluate_models_on_training.
"""
import numpy as np
from Problem_1_Curve_Fitting import INTERVAL_1, INTERVAL_2, generate_models
from Problem_3_evaluate_models_on_training import raw_data, evaluate_models_on_training


x1 = INTERVAL_1
x2 = INTERVAL_2
y = []
for year in INTERVAL_1:
    y.append(np.mean(raw_data.get_yearly_temp('BOSTON', year)))
models = generate_models(x1, y, [1])
evaluate_models_on_training(x1, y, models)