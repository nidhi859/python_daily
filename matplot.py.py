#!/usr/bin/env python
# coding: utf-8

# In[3]:


from matplotlib import pylab
import numpy as np
x = np.linspace(0,10,26)
y = x*x+2
pylab.plot(x,y,'r')


# In[22]:


# subgraphs
pylab.subplot(1,2,1)#(rows, columns, indexes)
pylab.plot(x,y,'r--')
pylab.subplot(1,2,1)
pylab.plot(y,x,'g')
pylab.subplot(2,2,2)
pylab.plot(y,x,'b--')
pylab.subplot(2,2,2)
pylab.plot(x,y,'y')


# # operator description
# fig.add_axes()=Initialize subplot a = fig_add_subplot(222)
# fig.b = plt.subplots(rows = 3, nodes = 2) = adds subplot
# ax = plt.subplots(2.2) = creates subplot

# In[23]:


from matplotlib import pyplot as plt


# In[32]:


fig = plt.figure()
axis = fig.add_axes([0.5, 0.1, 0.8, 0.8]) #control the (left,right,width,height)of the canvas (from 0 to 1)
axis.plot(x,y,'r')


# In[34]:


# gain we can draw subgraph
fig, axes = plt.subplots(nrows = 1, ncols = 2) # subgraph is of 1 row and 2 columns
for ax in axes:
    ax.plot(x,y,'r')


# In[37]:


# we can also draw a picture or graph inside another graph
fig = plt.figure()
axis1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axis2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
axis1.plot(x,y,'r')
axis2.plot(y,x,'b')


# In[108]:


fig = plt.figure(figsize =(10,5), dpi = 80) #fisize resize the size of canvas..like here..10*5
fig.add_subplot()
plt.plot(x,y,'r')


# In[50]:


ax.legend(["label1", "label2"])
fig ,axes = plt.subplots()
axes.set_title("This is my first title")
axes.set_xlabel("x-axis")
axes.set_ylabel("y-axis")
axes.plot(x,x**2,'r')
axes.plot(x,x**3,'y')
axes.legend(["y = x**2", "y = x**3"], loc = 2)


# In[73]:


# also you can set other properties such as line color, traparency, and more
fig,axes = plt.subplots(dpi=150)
axes.plot(x,x+1,color = 'black', alpha = .8,linewidth = 2,linestyle = "-")
axes.plot(x,x+2,color = '#1160de', lw = 3, linestyle = ":")
axes.plot(x,x+3,color = '#15cc55', alpha = 1, lw = 1, linestyle = "-.")

line, = axes.plot(x, x+4, color="blue",lw = 1.50)
line.set_dashes([5,10,15,10])
line, = axes.plot(x, x+5, color="blue",lw = 1.50)
line.set_dashes([5,10,15,10])
line, = axes.plot(x, x+6, color="blue",lw = 1.50)
line.set_dashes([5,10,15,10])


# In[76]:


fig,axes = plt.subplots(dpi=150)
axes.plot(x,x+1,color = 'black', lw = 2,linestyle = "-")
axes.plot(x,x+2,color = '#1160de', lw = 2, linestyle = ":")
axes.plot(x,x+3,color = '#15cc55', lw = 2, linestyle = "-.")

line, = axes.plot(x, x+4, color="blue",lw = 1.50)
line.set_dashes([5,10,15,10])
line, = axes.plot(x, x+5, color="blue",lw = 1.50)
line.set_dashes([5,10,15,5])
line, = axes.plot(x, x+6, color="blue",lw = 1.50)
line.set_dashes([5,10,4,10])


# In[94]:


fig,axes = plt.subplots(dpi=100)
axes.plot(x,x+1,color = 'black', lw = 2, marker ="o")
axes.plot(x,x+2,color = '#1160de', lw = 2, marker = "1")
axes.plot(x,x+3,color = '#15cc55', lw = 2, marker = "s")
axes.plot(x,x+4,color = '#15cc55', lw = 2, marker = "+")
axes.plot(x,x+5,color = 'blue', lw = 2, marker = "o", markersize = 2)
axes.plot(x,x+6,color = 'blue', lw = 2, marker = "o", markerfacecolor = 'red')
axes.plot(x,x+7,color = 'yellow', lw = 2, marker = "o", markersize = 5, markerfacecolor = 'green')


# In[104]:


# set the canvas grid and axis range
fig,ax = plt.subplots(1, 2, figsize = (10,5))

ax[0].plot(x, x**2, x, x**3, lw=2)
ax[0].grid(True)

ax[1].plot(x, x**2, x, x**3, lw=2)
ax[1].set_ylim([0,60])
ax[1].set_xlim([2,5])
ax[1].grid(True)


# # Other 2D graphics

# In[113]:


n = np.array([0,1,2,3,4,5])
fig,ax = plt.subplots(1, 4, figsize = (10,5))
ax[0].set_title("Scatter")
# Scatter plots are used to observe relationship between variables and uses dots to represent the relationship between them. 
# matplotlib.pyplot.scatter(x_axis_data, y_axis_data, s=None, c=None, marker=None, cmap=None, vmin=None, vmax=None, alpha=None, linewidths=None, edgecolors=None) 
ax[0].scatter(x, x+0.25*np.random.randn(len(x))) 

ax[1].set_title("Step")
ax[1].step(n,n**2,lw=2)

ax[2].set_title("Bar")
ax[2].bar(n,n**2,align="center",width=0.5,alpha=0.5)

ax[3].set_title("Fill_between")
ax[3].fill_between(x, x**2,x**3, color="red",alpha=0.5)


# In[120]:


# Drawa radar chart
fig = plt.figure(figsize = (6,6))
ax = fig.add_axes([0.0, 0.0, 0.6, 0.6], polar = True)


# In[124]:


fig = plt.figure(figsize = (6,6))
ax = fig.add_axes([0.0, 0.0, 0.6, 0.6], polar = True)

t = np.linspace(0, 2*np.pi, 100)
ax.plot(t,t,color="blue",lw =3)


# In[126]:


# Draw a histogram
n = np.random.randn(1000000)
fig,axes = plt.subplots(1,2,figsize = (12,4))
axes[0].set_title("Default histogram")
axes[0].hist(n)

axes[1].set_title("cumulative detailed histogram")
axes[1].hist(n, cumulative= True, bins = 10)


# In[127]:


# Draw Contour Image

import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-3.0, 3.0, delta)
x,y = np.meshgrid(x,y)
z1 = np.exp(-x**2 - y**2)
z2 = np.exp(-(x-1)**2 - (y-1)**2)
z = (z1-z2)*2


# In[128]:


fig,ax = plt.subplots()
cs = ax.contour(x,y,z)
ax.clabel(cs, inline = 1, fontsize = 10)


# In[130]:


# Draw 3D surface image
from mpl_toolkits.mplot3d.axes3d import Axes3D
fig = plt.figure(figsize = (14,6))

# specify the 3D graphics to draw with projection = '3d'
ax = fig.add_subplot(1,2,1,projection = "3d")
ax.plot_surface(x,y,z,rstride=4, cstride=4, linewidth =0)


# In[131]:


# Heat map....color map


# # Practice example
# # Writ a python programming to create a pie chart of the popularity of programming languages
# 

# In[137]:


import matplotlib.pyplot as plt
# data of plot
languages = ['python', 'java', 'c++', 'javascript', 'php', 'c#']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ["#1234de" , "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]


# In[138]:


#explode 1st slice
explode = (0.1, 0, 0, 0, 0, 0)
plt.pie(popularity, explode = explode, labels = languages, colors = colors,
autopct = '%1.1f%%',shadow =True, startangle = 140)

