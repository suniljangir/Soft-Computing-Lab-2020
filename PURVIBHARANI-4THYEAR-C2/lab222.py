#!/usr/bin/env python
# coding: utf-8
Aim: Demonstrate the use of Matplotlib library
# In[1]:


import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


plt.plot([2,3,4,5],alpha=.5) #plot() method to create a plot of points on the graph.
#We can use the alpha channel to soften the colors.
plt.xlabel('Actual birth weight') #set label for x-axis.
plt.ylabel('Estimated birth weight') #set label for y-axis.
plt.show() #To display the plot


# In[3]:


plt.plot([2,3,4,5],[3,8,10,12],'gs')
#This takes the first list for x-axis and the second for the y-axis. 
#A third argument will let you choose the color and the line type of the plot. The default format string gives us a solid blue line('b-'').
plt.xlabel('Actual birth weight')
plt.ylabel('Estimated birth weight')
plt.show()


# In[4]:


plt.plot([1,2,3],[2,4,9],color='orange',ls=':',marker='.',markerfacecolor='blue',markersize=13.0)
#To select what symbol you want to display at breakpoints and bends -'marker'.
#To set the color of the plot -'color'.
#To choose the style of line you want for your plot -'linestyle' or 'ls'.
plt.show()

1) Pie chart
-A Pie Chart can only display one series of data.
-Pie charts show the size of items (called wedge) in one data series, proportional to the sum of the items.
-The data points in a pie chart are shown as a percentage of the whole pie.
# In[5]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
langs = ['Hindi', 'Spanish', 'English', 'German', 'French']
students = [23,17,35,29,12]
ax.pie(students, labels = langs,autopct='%1.2f%%')
ax.set_title('Pie chart')
plt.show()

2) Scatter plot
-Scatter plots are used to plot data points on horizontal and vertical axis in the attempt to show how much one variable is affected by another.
-Each row in the data table is represented by a marker the position depends on its values in the columns set on the X and Y axes.
# In[6]:


girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
boys_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.scatter(grades_range, girls_grades, color='y')
ax.scatter(grades_range, boys_grades, color='g')
ax.set_xlabel('Grades Range')
ax.set_ylabel('Grades Scored')
ax.set_title('Scatter plot')
plt.show()

3) Barplot
-A bar graph shows comparisons among discrete categories.
-One axis of the chart shows the specific categories being compared, and the other axis represents a measured value.
# In[7]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['India', 'Australia', 'USA', 'France', 'Germany']
emps = [23,17,35,29,12]
ax.bar(langs,emps)
ax.set_title('Bar plot')
plt.show()

4) Histogram
-A histogram is an accurate representation of the distribution of numerical data.
-It is an estimate of the probability distribution of a continuous variable. It is a kind of bar graph.
# In[8]:


fig,ax = plt.subplots(1,1)
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
ax.hist(a, bins = [0,25,50,75,100],color='orange',alpha=0.3)
ax.set_title("Histogram")
ax.set_xticks([0,25,50,75,100])
ax.set_xlabel('marks')
ax.set_ylabel('no. of students')
plt.show()

5) Contour plot
-Contour plots (sometimes called Level Plots) are a way to show a three-dimensional surface on a two-dimensional plane.
-It graphs two predictor variables X,Y on the y-axis and a response variable Z as contours.
-These contours are sometimes called the z-slices or the iso-response values.
-A contour plot is appropriate if you want to see how alue Z changes as a function of two inputs X and Y, such that Z = f(X,Y).
# In[9]:


xlist = np.linspace(-3.0, 3.0, 100)
ylist = np.linspace(-3.0, 3.0, 100)
X, Y = np.meshgrid(xlist, ylist)
Z = np.sqrt(X**2 + Y**2)
fig,ax=plt.subplots(1,1)
cp = ax.contourf(X, Y, Z)
fig.colorbar(cp) # Add a colorbar to a plot
ax.set_title('Filled Contours Plot')
ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')
plt.show()

6) Boxplot
-A box plot which is also known as a whisker plot displays a summary of a set of data containing the minimum, first quartile, median, third quartile, and maximum.
-In a box plot, we draw a box from the first quartile to the third quartile.
-A vertical line goes through the box at the median.
-The whiskers go from each quartile to the minimum or maximum.
# In[10]:


np.random.seed(10)   
data_1 = np.random.normal(100, 10, 200) 
data_2 = np.random.normal(90, 20, 200) 
data_3 = np.random.normal(80, 30, 200) 
data_4 = np.random.normal(70, 40, 200) 
data = [data_1, data_2, data_3, data_4]   
fig = plt.figure(figsize =(8, 4)) 
ax = fig.add_axes([0, 0, 1, 1]) 
bp = ax.boxplot(data) 
ax.set_title('Boxplot')
plt.show()


# In[ ]:




