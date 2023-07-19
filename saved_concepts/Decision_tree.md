# Decision Tree

A decision tree is a simple yet powerful machine learning algorithm used for
classification and regression tasks. It is a flowchart-like structure where
each internal node represents a feature or attribute, each branch represents a
decision rule, and each leaf node represents the outcome or the class label.

## How does it work?

1. The decision tree algorithm starts with the entire dataset at the root node.
2. It then selects the best feature to split the data based on certain criteria,
   such as information gain or Gini impurity.
3. The dataset is divided into subsets based on the values of the selected
   feature.
4. The process is repeated recursively on each subset until a stopping
   criterion is met, such as reaching a maximum depth or no further improvement
   in the class purity.

## Example:

Let's say we want to build a decision tree to predict whether a person will
play tennis based on weather conditions. We have the following dataset:

| Outlook   | Temperature | Humidity | Windy | Play Tennis |
|-----------|-------------|----------|-------|-------------|
| Sunny     | Hot         | High     | False | No          |
| Sunny     | Hot         | High     | True  | No          |
| Overcast  | Hot         | High     | False | Yes         |
| Rainy     | Mild        | High     | False | Yes         |
| Rainy     | Cool        | Normal   | False | Yes         |
| Rainy     | Cool        | Normal   | True  | No          |
| Overcast  | Cool        | Normal   | True  | Yes         |
| Sunny     | Mild        | High     | False | No          |
| Sunny     | Cool        | Normal   | False | Yes         |
| Rainy     | Mild        | Normal   | False | Yes         |
| Sunny     | Mild        | Normal   | True  | Yes         |
| Overcast  | Mild        | High     | True  | Yes         |
| Overcast  | Hot         | Normal   | False | Yes         |
| Rainy     | Mild        | High     | True  | No          |

The decision tree algorithm will analyze the dataset and create a tree-like
structure. For example, it might split the data based on the "Outlook" feature
first, then further split based on other features like "Temperature" and
"Humidity". The leaf nodes will represent the predicted class label, either
"Yes" or "No" for playing tennis.

## Follow-up questions:

1. What criteria are used to select the best feature for splitting?
   - The criteria can be information gain, Gini impurity, or other measures of
     impurity reduction. These measures quantify how well a feature separates
     the data into different classes.
2. How does the algorithm handle missing values in the dataset?
   - There are different approaches to handle missing values, such as ignoring
     the instance, using the most common value, or using statistical methods to
     estimate the missing value.
3. Can decision trees handle continuous or numerical features?
   - Yes, decision trees can handle continuous features by selecting a split
     point based on a threshold value. For example, "Temperature > 25°C" or
     "Humidity <= 70%".

## Etymology and History:

The concept of decision trees dates back to the 1960s. The term "decision tree"
was coined by Ross Quinlan in 1986. Since then, decision trees have become a
popular and widely used machine learning algorithm due to their simplicity and
interpretability.

## Summary:

In simple terms, a decision tree is a flowchart-like structure used for
classification and regression tasks. It helps make decisions by splitting the
data based on features and creating a tree-like structure. Each internal node
represents a feature, each branch represents a decision rule, and each leaf
node represents the outcome or class label.

## See also:

- [Random Forest](?concept=random+forest&specialist_role=Data+analyst&target_audience=Software+developer)
- [Gradient Boosting](?concept=gradient+boosting&specialist_role=Data+analyst&target_audience=Software+developer)
- [Support Vector Machines](?concept=support+vector+machines&specialist_role=Data+analyst&target_audience=Software+developer)