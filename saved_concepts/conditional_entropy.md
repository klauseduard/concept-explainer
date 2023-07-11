# Conditional Entropy

Conditional entropy is a measure of uncertainty or randomness in a random
variable, given the knowledge of another random variable. In simpler terms, it
tells us how much information is needed, on average, to describe an outcome of
a random variable when we already know the outcome of another related random
variable.

## Example:
Let's say we have a dataset of employees in a company, and we want to analyze
their job satisfaction based on their salary and years of experience. We can
consider job satisfaction as one random variable, and salary and years of
experience as two other random variables.

The conditional entropy of job satisfaction given salary and years of experience
will tell us how much additional information we need to describe the job
satisfaction, given that we already know the salary and years of experience of
an employee.

## Follow-up Questions:

**Q1: How is conditional entropy different from regular entropy?**

A1: Regular entropy measures the average amount of information needed to
describe the outcome of a single random variable. Conditional entropy, on the
other hand, measures the average amount of information needed to describe the
outcome of a random variable, given the knowledge of another related random
variable.

**Q2: How is conditional entropy calculated?**

A2: Conditional entropy is calculated by summing the product of the probability
of each outcome of the first random variable and the entropy of the second
random variable, given that outcome.

**Q3: Can conditional entropy be zero?**

A3: Yes, conditional entropy can be zero. It means that the second random
variable is completely determined by the first random variable. In other words,
knowing the outcome of the first random variable eliminates all uncertainty
about the outcome of the second random variable.

## Summary:

Conditional entropy measures the average amount of additional information
needed to describe the outcome of a random variable, given the knowledge of
another related random variable. It helps us understand the uncertainty or
randomness in a random variable when we already know the outcome of another
related random variable.

## See also:

- [Entropy](?concept=entropy&specialist_role=Information+theorist&target_audience=Manager+without+much+technical+background):
  Explains the concept of entropy, which is the basis for understanding
  conditional entropy.
- [Joint Entropy](?concept=joint+entropy&specialist_role=Information+theorist&target_audience=Manager+without+much+technical+background):
  Describes the entropy of two or more random variables considered together.