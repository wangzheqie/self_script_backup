#!/usr/bin/env python
# coding=utf-8
from OpenGL.GL import * 
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np 
import sys 

def init():
    glClearColor(1.0, 0.0, 1.0, 1.0)
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)

if __name__ == "__main__":
    glutInit(sys.argv)
    glutCreateWindow("Function plotter")

    init()
    glutMainLoop()
