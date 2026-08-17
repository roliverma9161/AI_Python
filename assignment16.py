#Q.1
Q.1 What is Matplotlib?
a) A programming language
b) A data visualization library
c) A database management system
d) An operating system
Ans:b 
Q.2 What is the purpose of Matplotlib’s pyplot module?
a) To create data visualizations
b) To manage data storage
c) To manipulate data frames
d) To install third-party packages
Ans:a
Q.3 Which of the following is not a type of Matplotlib plot?
a) Line plot
b) Scatter plot
c) Pie chart
d) Bar chart
Ans:c
Q.4 How can you add a title to a Matplotlib plot?
a) By using the title() function
b) By using the label() function
c) By using the text() function
d) By using the legend() function
Ans:a
Q.5 What is the purpose of the xlabel() and ylabel() functions in Matplotlib?
a) To add a legend to a plot
b) To add a title to a plot
c) To label the x and y axes of a plot
d) To change the color of a plot
Ans:c
6.How can you save a Matplotlib plot as an image file?
a) By using the save() function
b) By using the export() function
c) By using the savefig() function
d) By using the exportfig() function
Ans:c
Q. 7  What is the default color for Matplotlib plots?
a) Red
b) Blue
c) Green
d) Black
Ans:b
Q.8 How can you change the color of a Matplotlib plot?
a) By using the color() function
b) By using the hue() function
c) By using the palette() function
d) By specifying the color parameter in the plot() function
Ans:d
Q.9 What is the purpose of the legend() function in Matplotlib?
a) To label the x and y axes of a plot
b) To add a title to a plot
c) To add annotations to a plot
d) To label different lines or markers on a plot
Ans:d
Q.10 What is the purpose of the subplot() function in Matplotlib?
a) To create multiple plots in the same figure
b) To adjust the size of a plot
c) To change the color of a plot
d) To add annotations to a plo
Ans:a

#Q.2 Write a Python program to draw a line with suitable label in the
#x axis, y axis  and a title.
import matplotlib.pyplot as plt
X = range(1, 50)
Y = [value * 3 for value in X]
print("Values of X:")
print(*range(1,50)) 
print("Values of Y (thrice of X):")
print(Y)
# Plot lines and/or markers to the Axes.
plt.plot(X,Y)
# Set the x axis label of the current axis.
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title 
plt.title('Draw a line.')
# Display the figure.
plt.show()

#Q.3 Write a Python programming to display a bar chart of the
#popularity of programming Languages.
#Sample data:
#Programming languages: Java, Python, PHP, JavaScript, C#, C++
#Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i,for i,j  in enumerate(x)]
plt.bar(x_pos, popularity, color='blue')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.xticks(x_pos, x)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
#Q.4Write a Python programming to create a pie chart with a title of
#the popularity of programming Languages.
#Sample data:
#Programming languages: Java, Python, PHP, JavaScript, C#, C++
#Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

import matplotlib.pyplot as plt
# Plot data
languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
#colors = ['red', 'gold', 'yellowgreen', 'blue', 'lightcoral', 'lightskyblue']
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
# explode 1st slice
explode = (0.1, 0, 0, 0, 0, 0)  
# Plot
plt.pie(popuratity, explode=explode, labels=languages, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago", bbox={'facecolor':'0.8', 'pad':5})
plt.show()

#Q.5 Write a Python program to draw a scatter plot with empty circles taking a
#   random distribution in X and Y and plotted against each other
 
import matplotlib.pyplot as plt 
import numpy as np 
x = np.random.randn(50) 
y = np.random.randn(50)
plt.scatter(x, y, s=70, facecolors='none', edgecolors='g')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()








plt.show()
