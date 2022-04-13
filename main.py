# imports
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import Divider, Size


# set the style
plt.style.use('clean_gs.mplstyle')

# arrays with sizes of [padding, axis] for all plots 
# (axis are 3x2) (figure is 4x3) sizes are in inch.
# must be set depending on how they will be placed in the document to avoid discrepancies
h = [Size.Fixed(0.7), Size.Fixed(3.0)]
v = [Size.Fixed(0.5), Size.Fixed(2.0)]


# 
# 
# 
### FIRST PLOT (fig1)
# data
x           = np.linspace(-1.0, 1.0, 1000)
y1          = np.sin(x)
y2          = np.cos(x)
y3          = np.sin(x) * np.sin(x)
y4          = np.cos(x) * np.cos(x)
y5          = np.tanh(x)
y6          = np.sinh(x)

# create figure and plot
fig1 = plt.figure(1)
divider = Divider(fig1, (0, 0, 1, 1), h, v, aspect=False)
ax = fig1.add_axes(divider.get_position(),
axes_locator=divider.new_locator(nx=1, ny=1))

plt.plot(x, y1,                         label=r'$\sin(x)$')
plt.plot(x, y3,         linewidth=2,    label=r'$\sin(x)^2$')
plt.plot(x, y2,                         label=r'$\cos(x)$')
plt.plot(x, y4,         linewidth=2,    label=r'$\cos(x)^2$')
plt.plot(x, y5, "--",                   label=r'$\tanh(x)$')
plt.plot(x, y6, ":",    linewidth=1,    label=r'$\sinh(x)^2$')

# label the axis
plt.xlabel('x [-]')
plt.ylabel('y [-]')

# position the legend over the plot
plt.legend(bbox_to_anchor=(0.5, 1.0), loc="lower center", ncol=3, frameon=False)

# show and save the figure (can be .png, .svg, .pdf, etc)
plt.show()
plt.savefig('fig/fig1.png')#, bbox_inches='tight'
plt.close()


# 
# 
# 
### SECOND PLOT (fig2)
# Fixing random state for reproducibility
np.random.seed(19680801)

dt = 0.005
t = np.arange(0, 1, dt)
nse1 = np.random.randn(len(t))                 # white noise 1
nse2 = np.random.randn(len(t))                 # white noise 2

# Two signals with a coherent part at 10Hz and a random part
s1 = np.sin(2 * np.pi * 10 * t) + nse1
s2 = np.sin(2 * np.pi * 10 * t) + nse2

# create figure and plot
fig1 = plt.figure(2)
divider = Divider(fig1, (0, 0, 1, 1), h, v, aspect=False)
ax = fig1.add_axes(divider.get_position(),
axes_locator=divider.new_locator(nx=1, ny=1))

plt.plot(t, s1, color="c", label="Random white noise 1")
plt.plot(t, s2, color="m", label="Random white noise 2")

# label the axis
plt.xlabel('time [s]')
plt.ylabel('amplitude [-]')

plt.xlim([0, 1.0])

# position the legend over the plot
plt.legend(bbox_to_anchor=(0.5, 1.0), loc="lower center", ncol=2, frameon=False)

# show and save the figure (can be .png, .svg, .pdf, etc)
plt.show()
plt.savefig('fig/fig2.png')#, bbox_inches='tight'
plt.close()


# 
# 
# 
### THIRD PLOT (fig3)
# create figure and plot
fig1 = plt.figure(3)
divider = Divider(fig1, (0, 0, 1, 1), h, v, aspect=False)
ax = fig1.add_axes(divider.get_position(),
axes_locator=divider.new_locator(nx=1, ny=1))


np.random.seed(0)

dt = 0.01  # sampling interval
Fs = 1 / dt  # sampling frequency
t = np.arange(0, 10, dt)

# generate noise:
nse = np.random.randn(len(t))
r = np.exp(-t / 0.05)
cnse = np.convolve(nse, r) * dt
cnse = cnse[:len(t)]

s1 = 0.1 * np.sin(4 * np.pi * t) + cnse  # the signal
s2 = 0.1 * np.cos(4 * np.pi * t) + cnse  # the signal
s1_c = 0.1 * np.sin(4 * np.pi * t)   # the signal
s2_c = 0.1 * np.cos(4 * np.pi * t)   # the signal

# plot time signal:
plt.plot(t, s1_c,":",   color="red",    linewidth=0.5,  label="Clean sine signal")
plt.plot(t, s1,         color="red",                    label="Noisy sine signal")
plt.plot(t, s2_c,":",   color="blue",   linewidth=0.5,  label="Clean cosine signal")
plt.plot(t, s2,         color="blue",                   label="Noisy cosine signal")
plt.xlabel("time [s]")
plt.ylabel("amplitude [-]")

plt.xlim([0, 2.0])


# position the legend over the plot
plt.legend(bbox_to_anchor=(0.5, 1.0), loc="lower center", ncol=2, frameon=False)

# show and save the figure (can be .png, .svg, .pdf, etc)
plt.show()
plt.savefig('fig/fig3.png')#, bbox_inches='tight'
plt.close()
