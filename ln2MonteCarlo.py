#A program to calculate an estimate of ln(2)
#using the Monte Carlo method on the function
#1/(x+1). This works as the area under this function from
#0 to 1 is ln(2), which can be proven by analytical integration

#Impoting modules
import numpy as np
import matplotlib.pyplot as plt
import random as random

#Parameter to control no. of iterations, note, the plot of the randomly
#distributed points gets hard to see for N>20000. Using more iterations
#Should give a more accurate result on avergae, but takes longer to
#Compute
N = 10000

#Initialise lists of iteration no., the result at each iteration,
#and lists for all the x and y pairs. Also create variable to track
#no. of points under the line

iterations = []
values = []
xs = []
ys = []
count = 0

print(f"The number of iterations used is {N}")
for i in range(N):
#Generate a random x-y pair in the unit square, and add to list of pairs
    x = random.random()
    y = random.random()
    xs.append(x)
    ys.append(y)
    cond = 1/(1+x) #Condition to be under the line
    if y <= cond: #Check if y is above or below the line, if yes, increment count
        count += 1
    fraction = count/(i+1) #Gives fraction of points under the line
    values.append(fraction)
    iterations.append(i+1)
    #Prints the first 10 and last 10 outputs to give an idea of values
    if i<10 or (N-i)<11:
        print(f"Iteration no. {i+1} gives a value of {fraction}")

print(f"Using this method, ln(2) = {round(values[N-1],2)} to 2 decimal places")
fig, (ax1, ax2) = plt.subplots(1,2) #Intialise plots for iterations, and individual points
#Plotting the values over the iterations, and also the value of ln(2)
ax1.plot(iterations, values, 'k', label = 'computed ln(2)', linewidth = 0.75)
ax1.plot([0 , iterations [ -1]] , [np.log(2), np.log(2)],
"r", label ="actual ln(2)", linewidth = 1)
#Graph formatting
ax1.set_title("The convergence on ln(2)")
ax1.set(xlabel = 'Iteration', ylabel = 'Value')
ax1.set_ylim([0.55,0.8]) #Setting y limit to interesting range
ax1.grid()
ax1.legend()

#Use s and t to create line of 1/(1+x)
s = np.linspace(0,1,1000)
t = 1/(1+s)
#Overlay the random points with this line, 
ax2.plot(xs, ys, 'ro', label = 'random points', markersize = 0.5)
ax2.plot(s,t, 'b', label = '1/(1+x)')
#Formatting plot
ax2.set(xlabel = 'x', ylabel = 'y')
ax2.set_title("The distribution of random points")
ax2.set_xlim([0,1])
ax2.set_ylim([0,1])
ax2.grid()
ax2.legend(loc = 'upper right')

#Adjust spacing of subplots for clarity
plt.subplots_adjust(wspace=0.25, hspace=0)

#Note to user as figure is clearest in full screen
print("Note, the figure is best viewed in full screen mode")
while True:
    save = input("Would you like to save a pdf of the figure? Enter y/n only: ")
    if save == 'y':
        plt.savefig("ln2Convergence.pdf")
        break
    elif save == 'n':
        break
    else:
        continue
plt.show()
