Underfitting is a concept in machine learning where a model is too simple to
capture the underlying patterns in the data. It occurs when the model is not
able to learn the relationships between the input features and the target
variable effectively.

**Follow-up question 1:** How does underfitting happen?

Underfitting can happen when the model is not complex enough to represent the
data accurately. It may occur if the model has too few parameters or if it
uses a simple algorithm that cannot capture the complexity of the data.

**Example:** Let's say we have a dataset of housing prices with features like
the number of bedrooms, square footage, and location. If we use a linear
regression model with only one parameter (e.g., number of bedrooms) to predict
the prices, the model may underfit the data because it cannot capture the
influence of other important features like square footage and location.

**Follow-up question 2:** What are the consequences of underfitting?

When a model underfits the data, it fails to capture the underlying patterns
and relationships. As a result, the model's predictions are likely to be
inaccurate and have high errors. Underfitting can lead to poor performance on
both the training and test data, as the model is not able to generalize well.

**Example:** In the housing price prediction example, an underfit model might
predict the same price for all houses, regardless of their features. This
would result in inaccurate predictions and make the model practically useless.

**Etymology and History:**

The term "underfitting" is derived from the concept of fitting a model to the
data. In machine learning, the goal is to find a model that fits the data well,
meaning it captures the underlying patterns and relationships. Underfitting
refers to a situation where the model is too simple or lacks complexity to fit
the data accurately.

The concept of underfitting has been around since the early days of machine
learning. It is closely related to the bias-variance tradeoff, which is a
fundamental concept in the field. Underfitting represents the high bias end of
the tradeoff, where the model is too simplistic and fails to capture the
complexity of the data.

**Summary:**

Underfitting occurs when a model is too simple to capture the underlying
patterns in the data. It happens when the model lacks complexity or has too few
parameters to represent the relationships between the input features and the
target variable. Underfitting leads to inaccurate predictions and poor
performance on both training and test data.

**See also:**

- [Overfitting](?concept=overfitting&specialist_role=ML+Engineer&target_audience=Software+developer):
  The opposite of underfitting, where a model is too complex and fits the
  training data too closely, leading to poor generalization.
- [Bias-Variance Tradeoff](?concept=bias-variance+tradeoff&specialist_role=ML+Engineer&target_audience=Software+developer):
  The tradeoff between the model's ability to fit the training data and its
  ability to generalize to new, unseen data.