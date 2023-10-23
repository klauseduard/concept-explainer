Lambda calculus is a simple mathematical system that represents computation
using functions. It is like a programming language, but with only one type of
data: functions. In lambda calculus, functions can be defined, combined, and
applied to arguments.

Follow-up question: How do you define a function in lambda calculus?

In lambda calculus, a function is defined using a lambda expression. A lambda
expression has the form: `λx.e`, where `x` is a variable and `e` is an
expression that uses `x`. This expression represents a function that takes an
argument `x` and evaluates the expression `e` using that argument.

Example: The lambda expression `λx.x + 1` defines a function that takes an
argument `x` and returns `x + 1`.

Follow-up question: How do you combine functions in lambda calculus?

Functions can be combined in lambda calculus using function application. If `f`
and `g` are lambda expressions representing functions, then `f g` represents
the application of function `f` to argument `g`. This means that the function
`f` is applied to the argument `g` and the resulting expression is evaluated.

Example: If `f` is the lambda expression `λx.x + 1` and `g` is the lambda
expression `λx.x * 2`, then `f g` represents the application of the function `f`
to the argument `g`. The result would be the lambda expression `λx.(x * 2) + 1`.

Etymology and history:
Lambda calculus was introduced by Alonzo Church in the 1930s as a formal system
for studying the foundations of mathematics and computation. The term "lambda"
comes from the Greek letter λ, which Church used to represent functions in his
notation.

Summary:
Lambda calculus is a mathematical system that represents computation using
functions. Functions are defined using lambda expressions, and they can be
combined and applied to arguments. Lambda calculus is a fundamental concept in
computer science and forms the basis for functional programming languages.

See also:
- [Functional programming](?concept=functional+programming&specialist_role=Computer+scientist&target_audience=Software+developer):
  A programming paradigm that is based on lambda calculus and emphasizes the
  use of functions as the primary building blocks of programs.
- [Higher-order functions](?concept=higher-order+functions&specialist_role=Computer+scientist&target_audience=Software+developer):
  Functions that can take other functions as arguments or return functions as
  results. Lambda calculus provides a foundation for understanding and working
  with higher-order functions.