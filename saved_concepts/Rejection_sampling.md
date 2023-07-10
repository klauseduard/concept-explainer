# Rejection Sampling

Rejection sampling is a technique used in statistics and machine learning to
generate samples from a probability distribution. It is a simple and intuitive
method that can be understood without much technical background.

## How does it work?

1. Define a "proposal distribution" that is easy to sample from.
2. Generate samples from the proposal distribution.
3. Evaluate the probability density function (PDF) of the target distribution
   for each sample.
4. Accept or reject each sample based on a comparison between the PDF of the
   target distribution and a uniform random number.
5. Repeat steps 2-4 until the desired number of samples is obtained.

## Example

Let's say we want to generate samples from a normal distribution with mean 0 and
standard deviation 1. We can use rejection sampling to achieve this.

1. We choose a proposal distribution, such as a uniform distribution between -5
   and 5, which is easy to sample from.
2. We generate a sample from the proposal distribution, let's say -2.5.
3. We evaluate the PDF of the target distribution (normal distribution) for the
   sample -2.5.
4. We compare the PDF value with a randomly generated number between 0 and 1.
   If the PDF value is greater than the random number, we accept the sample;
   otherwise, we reject it.
5. We repeat steps 2-4 until we obtain the desired number of accepted samples.

## Follow-up Questions

**Q1: Why do we need to use a proposal distribution?**

A1: The proposal distribution is used as an approximation to the target
distribution. It should be chosen such that it is easy to sample from and
covers the entire support of the target distribution. Rejection sampling relies
on the fact that the proposal distribution is easier to sample from than the
target distribution.

**Q2: How do we choose the proposal distribution?**

A2: The choice of the proposal distribution depends on the characteristics of
the target distribution. It should be similar to the target distribution in
shape and cover the same range of values. The proposal distribution should also
be easy to sample from, such as a uniform or Gaussian distribution.

**Q3: How do we determine the number of samples to generate?**

A3: The number of samples to generate depends on the desired accuracy and the
efficiency of the rejection sampling algorithm. It is typically determined
through experimentation and can be adjusted based on the trade-off between
accuracy and computational resources.

## Summary

Rejection sampling is a technique used to generate samples from a probability
distribution. It involves using a proposal distribution to generate samples and
accepting or rejecting them based on a comparison with the target distribution's
probability density function. It is a simple and intuitive method that can be
used when sampling directly from the target distribution is difficult.

## See also

- [Importance Sampling](?concept=importance+sampling&specialist_role=Machine+learning+specialist&target_audience=Manager+without+much+technical+background):
  Another sampling technique used in statistics and machine learning.
- [Markov Chain Monte Carlo (MCMC)](?concept=markov+chain+monte+carlo+mcmc&specialist_role=Machine+learning+specialist&target_audience=Manager+without+much+technical+background):
  A more advanced sampling method that can be used when direct sampling is not
  feasible.