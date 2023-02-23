"""
After we create some regression models, we also want to be able to evaluate our models to figure out how well each model
represents our data, and tell good models from poorly fitting ones. One way to evaluate how well the model describes the
data is computing the model's R^2 value. R^2 provides a measure of how well the total variation of samples is explained
by the model.

Implement the function r_squared. This function will take in:

- list, y, that represents the y-coordinates of the original data samples
- estimated, which is a corresponding list of y-coordinates estimated from the regression model

This function should return the computed R^2 value. You can compute R^2 as follows, where  is the estimated y value for
the i-th data point (i.e. predicted by the regression),  is the y value for the ith data point, and
is the mean of the original data samples.
"""


def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    Args:
        y: list with length N, representing the y-coords of N sample points
        estimated: a list of values estimated by the regression model
    Returns:
        a float for the R-squared error term
    """

    numerator = 0
    denominator = 0
    mn = sum(y) / len(y)

    for i in range(len(y)):
        numerator = numerator + ((estimated[i] - y[i]) ** 2)
        denominator = denominator + ((y[i] - mn) ** 2)

    return round(1 - numerator / denominator, 4)