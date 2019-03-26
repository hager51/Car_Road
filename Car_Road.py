from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
import numpy as np
from math import  *

    
def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, .1, 100)
    gluLookAt(8,9,10, 0,0,0, 0,1,0)
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)

angle = 0
x = 0
forward = 0
def display():
    global angle
    global x
    global forward
    
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClearColor(0,.8,0,1)

    glBegin(GL_POLYGON)  #sky 
    glColor(0,.6,.9,1)
    glVertex(10, 6, -.5)
    glVertex(-18, 6, -.5)
    glVertex(-18, 10, -.5)
    glVertex(10, 10, -.5)
    glEnd()

    glBegin(GL_POLYGON)  #Road
    glColor(.4,.4,.4,1)
    glVertex(11, -11, -.5)
    glVertex(-30, -11, -.5)
    glVertex(-30, 3.5, -.5)
    glVertex(11, 3.5, -.5)
    glEnd()

    glLoadIdentity()
    glColor(1,1,1,1)
    glTranslate(5, 1 , 1)
    glScale(4, 0, 1)
    glutSolidCube(1)

    glLoadIdentity()
    glColor(1,1,1,1)
    glTranslate(-1, 1 , 1)
    glScale(4, 0, 1)
    glutSolidCube(1)

    glLoadIdentity()
    glColor(1,1,1,1)
    glTranslate(-7, 1 , 1)
    glScale(4, 0, 1)
    glutSolidCube(1)

    glLoadIdentity()
    glColor(1,1,1,1)
    glTranslate(-13, 1 , 1)
    glScale(4, 0, 1)
    glutSolidCube(1)

    glLoadIdentity()
    glColor(0,0,0,1)
    glTranslate(6, -10.5 , 0)
    glScale(3, 1, 1)
    glutSolidCube(1)

    glLoadIdentity()
    glColor(1,1,1,1)
    glTranslate(3, -10.5 , 0)
    glScale(3, 1, 1)
    glutSolidCube(1)

    glLoadIdentity()
    glColor(0,0,0,1)
    glTranslate(0, -10.5 , 0)
    glScale(3, 1, 1)
    glutSolidCube(1)

    glLoadIdentity()
    glColor(1,1,1,1)
    glTranslate(-3, -10.5 , 0)
    glScale(3, 1, 1)
    glutSolidCube(1)

    glLoadIdentity()
    glColor(0,0,0,1)
    glTranslate(-6, -10.5 , 0)
    glScale(3, 1, 1)
    glutSolidCube(1)

    glLoadIdentity()
    glColor(1,1,1,1)
    glTranslate(-9, -10.5 , 0)
    glScale(3, 1, 1)
    glutSolidCube(1)

    glLoadIdentity()
    glColor(0,0,0,1)
    glTranslate(-12, -10.5 , 0)
    glScale(3, 1, 1)
    glutSolidCube(1)

    glLoadIdentity()
    glColor(1,1,1,1)
    glTranslate(-15, -10.5 , 0)
    glScale(3, 1, 1)
    glutSolidCube(1)

    glLoadIdentity()
    glColor(0,0,0,1)
    glTranslate(-18, -10.5 , 0)
    glScale(3, 1, 1)
    glutSolidCube(1)

    glLoadIdentity()
    glColor(1,1,1,1)
    glTranslate(-21, -10.5 , 0)
    glScale(3, 1, 1)
    glutSolidCube(1)

    glLoadIdentity()
    glColor(0,0,0,1)
    glTranslate(-24, -10.5 , 0)
    glScale(3, 1, 1)
    glutSolidCube(1)

    glLoadIdentity()
    glColor(.8,.4,0,1)
    glTranslate(1, -13 , 0)
    glScale(.5, 7, .5)
    glutSolidCube(1)

    glLoadIdentity()
    glColor(.4,.6,0,1)
    glTranslate(.2,-10,-1)
    glutWireSphere(2, 100, 100)

    glLoadIdentity()
    glColor(.8,.4,0,1)
    glTranslate(-7, -13 , 0)
    glScale(.5, 7, .5)
    glutSolidCube(1)

    glLoadIdentity()
    glColor(.4,.6,0,1)
    glTranslate(-8,-10,-.8)
    glutWireSphere(2, 100, 100)

    glLoadIdentity()
    glColor(.8,.4,0,1)
    glTranslate(-17, -13 , 0)
    glScale(.5, 7, .5)
    glutSolidCube(1)

    glLoadIdentity()
    glColor(.4,.6,0,1)
    glTranslate(-18,-10,-.6)
    glutWireSphere(2, 100, 100)

    glLoadIdentity()
    glColor(.8,.4,0,1)
    glTranslate(1, 4.8 , 0)
    glScale(.4, 3.5, .4)
    glutSolidCube(.5)

    glLoadIdentity()
    glColor(.4,.6,0,1)
    glTranslate(1,6,0)
    glutWireSphere(.8, 100, 100)

    glLoadIdentity()
    glColor(.8,.4,0,1)
    glTranslate(5, 4.8 , 0)
    glScale(.4, 3.5, .4)
    glutSolidCube(.5)

    glLoadIdentity()
    glColor(.4,.6,0,1)
    glTranslate(5,6,0)
    glutWireSphere(.8, 100, 100)

    glLoadIdentity()
    glColor(.8,.4,0,1)
    glTranslate(-5, 4.8 , 0)
    glScale(.4, 3.5, .4)
    glutSolidCube(.5)

    glLoadIdentity()
    glColor(.4,.6,0,1)
    glTranslate(-5,6,0)
    glutWireSphere(.8, 100, 100)

    glLoadIdentity()
    glColor(.8,.4,0,1)
    glTranslate(-11, 4.8 , 0)
    glScale(.4, 3.5, .4)
    glutSolidCube(.5)

    glLoadIdentity()
    glColor(.4,.6,0,1)
    glTranslate(-11,6,0)
    glutWireSphere(.8, 100, 100)

    glLoadIdentity()
    glColor(0,0,0,1)
    glTranslate(-15, 4 , 0)
    glScale(1, .2, .2)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1,1,1,1)
    glTranslate(-13, 4 , 0)
    glScale(1, .2, .2)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0,0,0,1)
    glTranslate(-11, 4 , 0)
    glScale(1, .2, .2)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1,1,1,1)
    glTranslate(-9, 4 , 0)
    glScale(1, .2, .2)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0,0,0,1)
    glTranslate(-7, 4 , 0)
    glScale(1, .2, .2)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1,1,1,1)
    glTranslate(-5, 4 , 0)
    glScale(1, .2, .2)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0,0,0,1)
    glTranslate(-3, 4 , 0)
    glScale(1, .2, .2)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1,1,1,1)
    glTranslate(-1, 4 , 0)
    glScale(1, .2, .2)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0,0,0,1)
    glTranslate(1, 4 , 0)
    glScale(1, .2, .2)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1,1,1,1)
    glTranslate(3, 4 , 0)
    glScale(1, .2, .2)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0,0,0,1)
    glTranslate(5, 4 , 0)
    glScale(1, .2, .2)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1,1,1,1)
    glTranslate(7, 4 , 0)
    glScale(1, .2, .2)
    glutSolidCube(2)

    
    glColor(0,0,0,1)
    
    glLoadIdentity()
    glTranslate(2.5+x, -2.5*.25 , 2.5*.5)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(.2, .5, 12, 8)

    glLoadIdentity()
    glTranslate(2.5+x, -2.5*.25 , -2.5*.5)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(.2, .5, 12, 8)

    glLoadIdentity()
    glTranslate(-2.5+x, -2.5*.25 , 2.5*.5)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(.2, .5, 12, 8)

    glLoadIdentity()
    glTranslate(-2.5+x, -2.5*.25 , -2.5*.5)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(.2, .5, 12, 8)
    
    glColor(1,0,0,1)
    
    glLoadIdentity()
    glTranslate(x, 0, 0)
    glScale(1, .25, .5)
    glutSolidCube(5)

    glLoadIdentity()
    glTranslate(x, 1.25 , 0)
    glScale(.5, .25, .5)
    glutSolidCube(5)

    if forward:
         angle -= 0.1
         x += .01
         if x>5:
             forward = False
        
    else:
         angle += 0.1
         x -= .01
         if x<-5:
             forward = True

    
    glutSwapBuffers()
    glFlush()
    
def main():
    
    glutInit("")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    window = glutCreateWindow(b"Car_Road")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    myInit()
    glutMainLoop()                                  

main()
