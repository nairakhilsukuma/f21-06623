# -*- coding: utf-8 -*-
"""15_intro_to_linear_algebra_coding.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vGZ62fhjSOdhhp-7PjTqcs55H2u6b-oC

# MCQs
"""

from .MCQs import *

"""# Coding"""

from IPython.display import display, Markdown
from IPython.core.magic import register_cell_magic
from IPython.core.getipython import get_ipython

import numpy as np

"""## Supporting Functions"""

def strip_magic(line, cell):
    lines = cell.split('\n')
    stripped_lines = [line for line in lines if not line.strip().startswith('%')]

    if(len(lines)>len(stripped_lines)):
        print('Warning: The % magic does not work in this cell.')

    return ('\n'.join(stripped_lines))

def create_new_cell(contents):

    shell = get_ipython()
    shell.set_next_input(contents, replace=False)

def within(x, y):
    return np.allclose(x, y)

"""## Q1

Magic
"""

@register_cell_magic
def L15Q1(line, cell):

    # correct answer
    def correct():
        A = np.array([[1, 1,-1], [3, -1, 2], [1, 2, -3]])
        b = np.array([9, 14, 10])
        x = np.linalg.inv(A) @ b
        return x

    globals = dict()
    exec(cell, globals)

    # Now we can check if something was done
    X = globals.get('x', None)

    if X is None:
        print('Looks like you have changed the "x" variable. Use the original template variables.')
        return

    if within(X, correct()):
        print('Correct')
    else:
        print('Incorrect')

"""Question"""

def Code1():

    display(Markdown("""Find the solution to the following set of equations:

$x_1 + x_2 - x_3 = 9$

$3x_1 - x_2 + 2x_3 = 14$

$x_1 + 2x_2 - 3x_3 = 10$"""))

    c = """%%L15Q1
# import the required packages


# use linear algebra to solve


# final answer np.array([x1, x2, x3]):
x =

"""

    create_new_cell(c)

# Code1()

print('Code1() imported')

"""## Q2

Magic
"""

@register_cell_magic
def L15Q2(line, cell):

    # correct answer
    def correct():
        A = np.array([[1, 2, 3], [1, -1, 2], [3, 2, 1]])
        r = np.linalg.matrix_rank(A)
        d = np.linalg.det(A)
        return np.array([r, d])

    globals = dict()
    exec(cell, globals)

    # Now we can check if something was done
    R = globals.get('rank', None)
    D = globals.get('det', None)

    if R is None:
        print('Looks like you have changed the "rank" variable. Use the original template variables.')
        return
    if D is None:
        print('Looks like you have changed the "det" variable. Use the original template variables.')
        return

    if within(np.array([R, D]), correct()):
        print('Correct')
    else:
        print('Incorrect')

"""Question"""

def Code2():

    display(Markdown("""Find the rank and determinant of the matrix in the code cell below."""))

    c = """%%L15Q2
# import the required packages

# given matrix
A = np.array([[1, 2, 3], [1, -1, 2], [3, 2, 1]])

# rank of the matrix
rank =

# determinant of the matrix
det =

"""

    create_new_cell(c)

# Code2()

print('Code2() imported')
