#exercicio 4 - FINAL 

import numpy as np
import matplotlib.pyplot as plt
import os, sys
import matplotlib
matplotlib.rc('font', size=18)
matplotlib.rc('font', family='Arial')
N = 51 
dt = 5.e-4 
L = float(1) 
nsteps = 620 
dx = L/(N-1) 
nplot = 20 
r = dt/dx**2 
A = np.zeros((N,N))
B = np.zeros((N,N))
for i in range(N):
    if i==0:
        A[i,:] = [1+0.5*r if j==0 else -0.5*r if j==1 else 0 for j in range(N)]
        B[i,:] = [1-0.5*r if j==0 else 0.5*r if j==1 else 0 for j in range(N)]
    elif i==N-1:
        A[i,:] = [1+0.5*r if j==N-1 else -0.5*r if j==N-2 else 0 for j in range(N)]
        B[i,:] = [1-0.5*r if j==N-1 else 0.5*r if j==N-2 else 0 for j in range(N)]
    else:
        A[i,:] = [-0.5*r if j==i-1 or j==i+1 else 1+1.*r if j==i else 0 for j in range(N)]
        B[i,:] = [0.5*r if j==i-1 or j==i+1 else 1-1.0*r if j==i else 0 for j in range(N)]
x = np.linspace(0,1,N)
u = np.asarray([2*xx if xx<=0.5 else 2*(1-xx) for xx in x])
bb = B.dot(u[:]) 
fig = plt.figure()
plt.plot(x,u,linewidth=2)
filename = 'foo000.jpg';
fig.set_tight_layout(True);
plt.xlabel("x")
plt.ylabel("u")
plt.title("t = 0")
plt.savefig(filename)
plt.clf()
c = 0
for j in range(nsteps):
    u[:] = np.linalg.solve(A,bb)
    print(j)
    bb = B.dot(u[:]) 
    if(j%nplot==0): 
        plt.plot(x,u,linewidth=2)
        filename = 'foo' + str(c+1).zfill(3) + '.jpg';
        plt.xlabel("x")
        plt.ylabel("u")
        plt.ylim([0,1])
        plt.title("t = %2.2f"%(dt*(j+1)))
        plt.savefig(filename)
        plt.clf()
        c += 1

os.system("ffmpeg -r 5 -y -i 'foo%03d.jpg' d4.m4v")
os.system("rm -f *.jpg")
