# Plotting at negative values

The last exercise was very similar to the first exercise, so you hopefully found it straightforward.  The most crucial difference was the change in the mathematical nomenclature from the symbols that we use for sequences to the symbols that use for functions.  We have different mathematical nomenclature for sequences and functions because these are different objects.  The critical difference is that we can evaluate the 3rd term in a sequence, but we cannot evaluate the 4.5th or -6th term.   The value of many functions can, by contrast, be evaluated for any real number.  We can work out a y value of our function (0.1x) for x values of 4.5 or -6.  Given this fact we might choose to not draw the points in our graph of the function:

![](https://render.githubusercontent.com/render/math?math=y=0.1x)

only for positive integer values of x.  We might also want to draw points for negative values of x or non-integer values of x.  We might also like to draw a line that connects the points in our graph rather than discrete points to indicate that our function is continuous.

To complete this exercise, you must draw a graph of ![](https://render.githubusercontent.com/render/math?math=y=0.1x) with points plotted at integer x values that run from -50 up to and including +50.  I would like you to draw a line connecting the points.  To draw a line rather than points using matplotlib, you would use the commands:

````
plt.plot( xvalues, yalues, "k-" )
plt.savefig( "mygraph.png" )
````

_The difference here is that you write "k-" rather than "ko" in the plot command.  Using k- here tells matplotlib that you would like to draw a line while ko tells matplotlib that you would like to draw big dots._

