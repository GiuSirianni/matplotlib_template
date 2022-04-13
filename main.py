# imports
import matplotlib.pyplot as plt
import numpy as np


# set the style
plt.style.use('clean_gs.mplstyle')

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

plt.plot(x, y1,                         label=r'$\sin(x)$')
plt.plot(x, y3,         linewidth=2,    label=r'$\sin(x)^2$')
plt.plot(x, y2,                         label=r'$\cos(x)$')
plt.plot(x, y4,         linewidth=2,    label=r'$\cos(x)^2$')
plt.plot(x, y5, "--",                   label=r'$\tanh(x)$')
plt.plot(x, y6, ":",    linewidth=1,    label=r'$\sinh(x)^2$')

# label the axis
plt.xlabel('x [m]')
plt.ylabel('y [-]')

# position the legend over the plot
plt.legend(bbox_to_anchor=(0.05, 1.22), loc="upper left", ncol=3, frameon=False)

# show and save the figure (can be .png, .svg, .pdf, etc)
plt.show()
plt.savefig('fig1.png', bbox_inches='tight')
plt.close()
