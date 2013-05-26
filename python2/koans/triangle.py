#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
	if a+b > c and abs(a-b) < c:
		pass
	else:
		raise TriangleError
    	
	setlen=len(set([a,b,c]))
	if setlen == 1:
			if a == 0 :
				raise TriangleError
			return 'equilateral'
	elif setlen == 2:
			return 'isosceles'
	elif setlen == 3:
			return 'scalene'
    # DELETE 'PASS' AND WRITE THIS CODE


# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
