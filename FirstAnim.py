import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np
t0=0 # [hrs]
t_end = 2
dt=0.005
#

# create array for time
t=np.arange(t0,t_end+dt,dt)

#create an x array
x = 800*t # [km]
# create a y array
altitude=2
y=np.ones(len(t))*altitude
#print(len(t))


######## ANIMATION ##################

frame_amount=len(t)

def update_plot(num):
    plane_trajectory.set_data(x[0:num],y[0:num])
    plane_trajectory2.set_data(x[0:num],y[0:num])

    return plane_trajectory,plane_trajectory2,

fig=plt.figure(figsize=(16,9),dpi=120,facecolor=(0.8,0.8,0.8)) 
# defines a figure with properties: figsize(size), dpi=resolution, facecolor=color(R,B,G)
#fig2=plt.figure(figsize=(4,9),dpi=120,facecolor=(0,0,0))
gs=gridspec.GridSpec(2,2) # creates an object gs
gs2=gridspec.GridSpec(3,3)

# Subplot 1
ax0=fig.add_subplot(gs[1,1],facecolor=(0.9,0.9,0.9))
plane_trajectory,=ax0.plot([],[],'g',linewidth=2) # comma after plane_trajectory gets ride of brackets(from array)
plt.xlim(x[0],x[-1]) # defines x axis limits on plot
plt.ylim(0,y[0]+1) # defines y axis limits on plot

# Subplot 2
ax2=fig.add_subplot(gs2[0,2], facecolor=(0.9,0.9,0.9))
plane_trajectory2,=ax0.plot([],[],'r',linewidth=5)
plt.xlim(x[0],x[-1]) # defines x axis limits on plot 2
plt.ylim(0,y[0]+1) # defines y axis limits on plot 2

plane_ani=animation.FuncAnimation(fig,update_plot,frames=frame_amount,interval=20,repeat=True,blit=True)
# statement above description
 
plt.show() # shows plot 