#!/usr/bin/env python
# coding=utf-8
import math 
from OpenGL.GL import * 
from OpenGL.arrays import vbo 
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np 

class common(object):
    bCreate= False 

class shere(object):
    def __init__(self, rigns, segments, radius ):
        self.rigns = rigns
        self.segments = segments 
        self.radius = radius 
    def createVAO(self):
        vdata = [] 
        vindex = [] 
        for y in range(self.rigns):
            phi = (y/(self.rigns -1)) * np.pi 
            for x in range(self.segments):
                theta = (x/(self.segments -1)) * 2 *np.pi 

