from display import *
from draw import *
from parser import *
from matrix import *
from sys import argv

import math

screen = new_screen()
zbuffer = new_zbuffer()
color = [ 0, 0, 0 ]
edges = []
polygons = []
transform = new_matrix()
parse_file( 'scanline_test', edges, polygons, transform, screen, zbuffer, color )
'''
if len(argv) != 2:
    parse_file( 'script', edges, polygons, transform, screen, zbuffer, color )
else:
    parse_file( argv[1], edges, polygons, transform, screen, zbuffer, color )'''
