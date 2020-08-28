#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#This file contains a list of the integration functions
#Reimann-left, Reimann-right, midpoint,trap., and simpson


# In[ ]:





# In[34]:


import math
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'notebook')


# In[35]:


def riemann_left(f,x0,xn,n):
    dx = (xn-x0)/float(n)
    area = dx*math.fsum(f(x0 + i*dx) for i in range (0,n))
    return area


# In[36]:


def riemann_right(f,x0,xn,n):
    dx = (xn-x0)/float(n)
    area = dx*math.fsum(f(x0 + i*dx) for i in range (1,n+1))
    return area


# In[37]:


def midpoint(f,x0,xn,n):
    dx = (xn-x0)/float(n)
    area = dx*math.fsum(f(x0 + (i+0.5)*dx) for i in range (0,n))
    return area


# In[91]:


def trap(f,x0,xn,n):
    dx = (xn-x0)/float(n)
    #area = 0.5*dx*math.fsum(2*f(x0 + i*dx) for i in range (1,n))
    #area += 0.5*dx*(f(x0) + f(xn))
    area = dx*math.fsum(0.5*(f(x0 +i*dx) + f(x0 + (i+1)*dx)) for i in range (0,n))
    return area


# In[147]:


def simp(f,x0,xn,n):
    dx = (xn-x0)/float(n)
    s_odd = 0
    s_even = 0
    for i in range (1,n,2):
        s_odd += 4*f(x0 + i*dx) 
    for j in range (2,n-1,2):
        s_even += 2*f(x0 + j*dx) 
    area = (dx/3.0)*(f(x0) + s_even + s_odd + f(xn))
    return area


# In[148]:


#def f(x):
#    return np.e**x

#x0 = 0
#xn = 2
#n = 4
#print(simp(f,x0,xn,n))


# In[93]:


def plot_riemann_left(f, x0, xn, namef="$f(x)$", n=10, figname=None):
    plt.figure()
    xvalues = np.linspace(x0, xn, 1000) #create x-values
    yvalues = [f(x) for x in xvalues] #calculate y values
    plt.plot(xvalues, yvalues, 'r-')  # plots the function as a red line
    # Now plot the rectangles
    dx = (xn - x0) / float(n)
    xi = [x0 + i * dx for i in range(0, n)]
    yi = [f(x) for x in xi]  # left rectangles!
    for x, y in zip(xi, yi):
        plt.plot([x, x, x + dx, x + dx, x], [0, y, y, 0, 0], 'b-')
        #plt.plot([0.25,0.25,1,1],[0,2,2,0])
    # Finally, computing the area
    area = dx * math.fsum(yi)
    plt.title("Riemman left rectangles for {} with {} rectangles. Area is {:.4g}.".format(namef, n, area))
    plt.xlim(x0, xn)
    if figname:
        plt.savefig(figname)  # Default was "riemannleft.png"
    return area


# In[94]:


def plot_riemann_right(f, x0, xn, namef="$f(x)$", n=10, figname=None):
    plt.figure()
    xvalues = np.linspace(x0, xn, 1000) #create x-values
    yvalues = [f(x) for x in xvalues] #calculate y values
    plt.plot(xvalues, yvalues, 'r-')  # plots the function as a red line
    # Now plot the rectangles
    dx = (xn - x0) / float(n)
    xi = [x0 + i * dx for i in range(0, n)]
    yi = [f(x+dx) for x in xi]  # left rectangles!
    for x, y in zip(xi, yi):
        plt.plot([x, x, x + dx, x + dx, x], [0, y, y, 0, 0], 'b-')
        #plt.plot([0.25,0.25,1,1],[0,2,2,0])
    # Finally, computing the area
    area = dx * math.fsum(yi)
    plt.title("Riemman left rectangles for {} with {} rectangles. Area is {:.4g}.".format(namef, n, area))
    plt.xlim(x0, xn)
    if figname:
        plt.savefig(figname)  # Default was "riemannleft.png"
    return area


# In[95]:


def plot_midpoint(f, x0, xn, namef="$f(x)$", n=10, figname=None):
    plt.figure()
    xvalues = np.linspace(x0, xn, 1000) #create x-values
    yvalues = [f(x) for x in xvalues] #calculate y values
    plt.plot(xvalues, yvalues, 'r-')  # plots the function as a red line
    # Now plot the rectangles
    dx = (xn - x0) / float(n)
    xi = [x0 + i * dx for i in range(0, n)]
    yi = [f(x+0.5*dx) for x in xi]  # left rectangles!
    for x, y in zip(xi, yi):
        plt.plot([x, x, x + dx, x + dx, x], [0, y, y, 0, 0], 'b-')
        #plt.plot([0.25,0.25,1,1],[0,2,2,0])
    # Finally, computing the area
    area = dx * math.fsum(yi)
    plt.title("Riemman left rectangles for {} with {} rectangles. Area is {:.4g}.".format(namef, n, area))
    plt.xlim(x0, xn)
    if figname:
        plt.savefig(figname)  # Default was "riemannleft.png"
    return area


# In[145]:


def plot_trap(f, x0, xn, namef="$f(x)$", n=10, figname=None):
    plt.figure()
    xvalues = np.linspace(x0, xn, 1000) #create x-values
    yvalues = [f(x) for x in xvalues] #calculate y values
    plt.plot(xvalues, yvalues, 'r-')  # plots the function as a red line
    # Now plot the rectangles
    dx = (xn - x0) / float(n)
    xi = [x0 + i * dx for i in range(0, n)]
    # Trapezoides !
    for x in xi:
        plt.plot([x, x, x + dx, x + dx, x], [0, f(x), f(x + dx), 0, 0], 'b-')  # trapez
        plt.plot([x, x, x + dx, x + dx, x], [0, 0.5 * (f(x) + f(x + dx)), 0.5 * (f(x) + f(x + dx)), 0, 0], 'g:')  # Equivalent rectangle
    # Finally, computing the area
    area = 0.5 * dx * math.fsum(f(x) + f(x + dx) for x in xi)
    plt.title("Trapezoidal rule for {} with {} trapeziums. Area is {:.4g}.".format(namef, n, area))
    plt.xlim(x0, xn)
    if figname:
        plt.savefig(figname)  # Default was "trapezoides.png"
    return area


# In[ ]:





# In[ ]:





# In[ ]:




