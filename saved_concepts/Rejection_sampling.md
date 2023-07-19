## Rejection Sampling

Rejection sampling is a simple and intuitive method used in statistics and
machine learning to generate samples from a probability distribution. It is
often used when it is difficult to directly sample from a target distribution,
but we can easily sample from a different distribution that is easier to work
with.

In rejection sampling, we generate samples from a proposal distribution, which
is a distribution that we can sample from easily. We then evaluate the
probability density function (PDF) of the target distribution at each sample
point. If the sample point lies below the PDF curve of the target distribution,
we accept the sample. Otherwise, we reject it and generate a new sample.

The idea behind rejection sampling is that even though the samples are drawn
from a different distribution, by accepting only those samples that lie under
the target distribution, we can approximate the target distribution.

### Example:

Let's say we want to estimate the average height of people in a city, but we
don't have access to the entire population. We can use rejection sampling to
estimate this average height.

1. We randomly sample a group of people from a different city, for which we
   know the height distribution.
2. We calculate the average height of this sample group.
3. We compare the average height of the sample group with the average height of
   the people in the city we are interested in.
4. If the average height of the sample group is close to the average height of
   the city population, we accept the sample. Otherwise, we reject it and
   sample a new group.
5. We repeat steps 1-4 until we have enough accepted samples.
6. Finally, we calculate the average height of all the accepted samples, which
   gives us an estimate of the average height of the city population.

### Follow-up Questions:

**Q1: How do we choose the proposal distribution?**

A1: Choosing the proposal distribution is crucial for the success of rejection
sampling. Ideally, the proposal distribution should be similar to the target
distribution, but easier to sample from. The choice of the proposal
distribution depends on the problem at hand and requires some domain knowledge
or experimentation.

**Q2: Can rejection sampling be used for any type of probability distribution?**

A2: Rejection sampling can be used for any probability distribution, but its
effectiveness depends on the shape of the target distribution and the choice of
the proposal distribution. If the target distribution has a complex shape or
has heavy tails, rejection sampling may not be the most efficient method.

### Etymology and History:

The term "rejection sampling" was coined by statistician John von Neumann in
the 1950s. The method itself, however, has been used in various forms for much
longer. It is based on the idea of generating samples from a proposal
distribution and accepting or rejecting them based on their likelihood under
the target distribution.

### Summary:

Rejection sampling is a technique used to generate samples from a probability
distribution when direct sampling is difficult. It involves sampling from a
proposal distribution and accepting or rejecting the samples based on their
likelihood under the target distribution. While simple, rejection sampling
requires careful choice of the proposal distribution and may not be efficient
for complex target distributions.

### See also:

- [Importance Sampling](?concept=importance+sampling&specialist_role=Machine+learning+specialist&target_audience=Manager+without+much+technical+background)
- [Markov Chain Monte Carlo](?concept=markov+chain+monte+carlo&specialist_role=Machine+learning+specialist&target_audience=Manager+without+much+technical+background)