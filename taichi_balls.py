# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 15:11:11 2021

@author: fayya
"""


import taichi as ti
ti.init()

N = 100
dt = 1e-4
m = 1
g = 9.8
x = ti.Vector.field(2, float, N, needs_grad=True)  # position of particles
v = ti.Vector.field(2, float, N)  # velocity of particles
U = ti.field(float, (), needs_grad=True)  # potential energy


@ti.kernel
def compute_U():
    for i in ti.ndrange(N):
        r = x[i]
        # r.norm(1e-3) is equivalent to ti.sqrt(r.norm()**2 + 1e-3)
        # This is to prevent 1/0 error which can cause wrong derivative
        U[None] += m*g*x[i][1]  # U += -1 / |r|


@ti.kernel
def advance():
    for i in x:
        v[i] += dt * -x.grad[i]  # dv/dt = -dU/dx
    for i in x:
        x[i] += dt * v[i]  # dx/dt = v
        if x[i][1]<0:
            x[i][1]=0
            v[i][0]=0
            v[i][1]=0


def substep():
    with ti.Tape(U):
        # every kernel invocation within this indent scope
        # will also be accounted into the partial derivate of U
        # with corresponding input variables like x.
        compute_U()  # will also computes dU/dx and save in x.grad
    advance()


@ti.kernel
def init():
    for i in x:
        x[i] = [0*ti.random(), 0]
    for i in v:
       v[i] = [2*ti.random(), 5*ti.random()]


init()
gui = ti.GUI('Autodiff gravity',512)
while gui.running:
    for i in range(50):
        substep()
    
    
    gui.circles(x.to_numpy(), radius=3)
    gui.show()
    print('U = ', U[None])
    if(U[None]<=0):
        break        