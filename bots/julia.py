import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random, os
from datetime import datetime
from PIL import Image

def Julia(f, zmin, zmax, m, n, tmax=256):
    xs = np.linspace(zmin.real, zmax.real, n)
    ys = np.linspace(zmin.imag, zmax.imag, m)
    X, Y = np.meshgrid(xs, ys)
    Z = X+1j*Y
    J = np.ones(Z.shape) *tmax
    for t in range(tmax):
        mask = np.abs(Z) <= 2.
        Z[ mask] = f(Z[mask])
        J[~mask] -= 1
    return J

def save_julia(cx, cy):
    colormaps = [cm.gist_ncar, cm.rainbow, cm.gist_rainbow, cm.terrain, cm.gnuplot2, cm.spring, cm.cool]
    col_len = len(colormaps)
    map_num = random.randint(0,len(colormaps)-1)
    def f1(z, c = float(cx)+float(cy)*1j):
        return z**2+c
    # compute array J of escape times
    zmin = -1.3 - 1j *1.3
    zmax = 1.3 + 1j *1.3
    J = Julia(f1, zmin, zmax, m=1024, n=1024)
    # save array J as a PNG color image
    name = "first_fractal.png"
    plt.imsave(name, J, cmap=colormaps[map_num], origin="lower")
    julia_image = Image.open(name)
    name_compressed = "fractal.png"
    size = 1000,1000
    final_img = julia_image.resize(size, Image.ANTIALIAS)
    final_img.save(name_compressed)
    os.remove(name)
    return name_compressed
