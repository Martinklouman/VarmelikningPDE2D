'''
TMA4121, Matematikk 4 MTTK, NTNU
Martin Andreas Wettergreen Klouman
08.04.2024
'''

'''
Numerisk løsning av partielle differensialligningen, varmeligningen
'''

import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib.animation as anim

#Variabler og lister
Len_x = 1
Len_y = 1
T = 0.05
N_x = 20
N_y = 20
N_t = 1000

dx = Len_x/N_x
dy = Len_x/N_x
dt = T/N_t

alpha = 0.42

#Funksjoner og startbetingelser
x = np.linspace(0, Len_x, N_x)
y = np.linspace(0, Len_y, N_y)
t = np.linspace(0, T, N_t)
u = np.zeros((N_x,N_y,N_t))



#f = lambda x, y: x
#f = lambda x, y: x-0.5
#f = lambda x, y: np.sin(4*np.pi*x)
f = lambda x, y: np.sin(3*np.pi*np.sqrt((x-0.5)**2+(y-0.5)**2))


f_values = np.array([[f(x_value, y_value) for y_value in y] for x_value in x])
u[1:-1,1:-1,0] = f_values[1:-1, 1:-1]

#u[N_x//2,N_y//2] = 1

def u_nxt(u):
    u_nxt = np.zeros((N_x,N_y))
    for i in range(1,N_x-1):
        for j in range(1, N_y-1):
            u_nxt[i,j] = u[i,j] + alpha*dt/(dx**2)*(u[i-1,j]-2*u[i, j]+u[i+1,j]) + alpha*dt/(dy**2)*(u[i,j-1]-2*u[i,j]+u[i,j+1])
    return u_nxt

for i in range(N_t-1):
    u[:,:,i+1] = u_nxt(u[:,:,i])

#Grafisk
T_anim = 2 #Animasjonslengde
framesTot = T_anim*60 #60 frames per second
fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
mX, mY = np.meshgrid(x,y)

def oppdater(frame):
    ax.clear()
    surf = ax.plot_surface(mX,mY, u[:,:,frame], cmap = cm.coolwarm)
    ax.set_title(f'step :  {frame}')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("u")
    ax.set_xlim((0,Len_x))
    ax.set_ylim((0,Len_y))
    ax.set_zlim((-1,1))
    return surf;

        
ani = anim.FuncAnimation(fig,oppdater, frames = np.linspace(0, N_t-1,framesTot).astype(int), interval = 1000/60)
ani.save("Animation2D.gif")
plt.show()