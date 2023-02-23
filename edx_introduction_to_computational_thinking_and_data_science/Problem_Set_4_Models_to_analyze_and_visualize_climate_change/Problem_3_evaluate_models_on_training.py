"""
We have learned how to obtain a numerical metric for evaluation. Visualizing our data samples along with fitting curves
can also help us figure out the goodness of obtained models. In this problem, we will integrate the numerical metrics
and visualization for a comprehensive evaluation.

Implement function evaluate_models_on_training. This function takes as input your data samples (x and y) and the list of
models (which are lists of coefficients obtained from generate_models) that you want to apply to your data.

This function should generate a figure for each model. In this figure, you are to plot your data along with your best
fit curve, and report on the goodness of the fit with the R^2 value. When you are writing this function try to make your
graph match the following format:

- Plot the data points as individual blue dots
- Plot your model as a red solid line
- Include a title and label your axes

Your title should include the value of your model and the R^2 degree of this model.
Your title could be longer than your graph. To fix that you can add "\n", which adds a newline to your string,
in your title when you concatenate several pieces of information (e.g., title = string_a + "\n" + string_b ).
"""
import pylab
from Problem_1_Curve_Fitting import Climate, INTERVAL_1, INTERVAL_2, generate_models
from Problem_2_R_2 import r_squared


def evaluate_models_on_training(x, y, models):
    """
    For each regression model, compute the R-square for this model with the
    standard error over slope of a linear regression line (only if the model is
    linear), and plot the data along with the best fit curve.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        R-square of your model evaluated on the given data points
    Args:
        x: a list of length N, representing the x-coords of N sample points
        y: a list of length N, representing the y-coords of N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a numpy array storing the coefficients of
            a polynomial.
    Returns:
        None
    """
    degrees = [1, 2, 4, 32]
    pylab.plot(x, y, 'o', label='Data')
    for i in range(len(models)):
        estYVals = pylab.polyval(models[i], x)
        error = r_squared(y, estYVals)
        pylab.plot(x, estYVals,
                   label='Fit of degree ' \
                         + str(degrees[i]) \
                         + ', R2 = ' + str(round(error, 3)))
    pylab.legend(loc='best')
    pylab.title('Evaluate models on training')
    pylab.show()


### Begining of program
raw_data = Climate('data_files/data.csv')

"""
y = []
x = INTERVAL_1
for year in INTERVAL_1:
    y.append(raw_data.get_daily_temp('BOSTON', 1, 10, year))
models = generate_models(x, y, [1, 2, 4, 32])
evaluate_models_on_training(x, y, models)
"""