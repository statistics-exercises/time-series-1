# The exponential random variable

The programming exercises in this exercise will focus on generating the new types of random variable that you have learned about in the lectures and videos this week.  In addition, there will be some revision of the techniques and algorithms that you have learned about in previous weeks.

As discussed in the video you can generate an exponential random variable by first generating a uniform random variable in the usual way.  This random variable is inserted into the inverse function for the cumulative probability distribution for the exponential random variable.  The random variable that emerges from this inverse function is then a sample from an exponential random variable.  

Your task in this exercise is to write a function called `exponential` that takes in a parameter `lam`.  This function should return an exponential random variable generated from a distribution with parameter `lam`.  Please note that you can calculate the natural logarithm of a variable, `x`, by using the command:

````
logx = np.log(x)
````

as you will need this in your function to calculate the random variable. 
