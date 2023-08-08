**Pearson correlation** is a statistical measure that quantifies the strength and direction of the linear relationship between two variables. It tells us how closely the data points of two variables align on a straight line.

A software developer might ask:
1. How is Pearson correlation calculated?
2. What does the correlation coefficient value mean?
3. Can you provide an example?

1. Pearson correlation is calculated by dividing the covariance of the two variables by the product of their standard deviations. It can be expressed using the following formula:

   ![Pearson correlation formula](https://latex.codecogs.com/png.latex?%5Crho%20%3D%20%5Cfrac%7B%5Ctext%7BCov%7D%28X%2CY%29%7D%7B%5Csigma_X%5Csigma_Y%7D)

   Here, Cov(X,Y) represents the covariance between X and Y, while σX and σY represent the standard deviations of X and Y, respectively.

2. The correlation coefficient value ranges from -1 to 1. 
   - A value of 1 indicates a perfect positive linear relationship, meaning that as one variable increases, the other variable also increases proportionally.
   - A value of -1 indicates a perfect negative linear relationship, meaning that as one variable increases, the other variable decreases proportionally.
   - A value of 0 indicates no linear relationship between the variables.

3. Let's consider an example where we want to measure the correlation between the number of hours studied and the exam scores of a group of students. The correlation coefficient is found to be 0.8, indicating a strong positive linear relationship. This means that as the number of hours studied increases, the exam scores also tend to increase.

**Etymology and History:**
The Pearson correlation coefficient is named after Karl Pearson, a British mathematician and biostatistician who developed the concept in the late 19th century. Pearson's work in statistics significantly contributed to the field, and his correlation coefficient became widely used for measuring linear relationships between variables.

**Summary:**
Pearson correlation is a statistical measure that quantifies the strength and direction of the linear relationship between two variables. It ranges from -1 to 1, where 1 indicates a perfect positive linear relationship, -1 indicates a perfect negative linear relationship, and 0 indicates no linear relationship.

**See also:**
- [Covariance](?concept=covariance&specialist_role=ML+Engineer&target_audience=Software+developer): Measures the relationship between two variables.
- [Spearman correlation](?concept=spearman+correlation&specialist_role=ML+Engineer&target_audience=Software+developer): Measures the strength and direction of monotonic relationships between variables.