#=========================================================================================================================
# This code divides a sphere into N horizontal bands of equal surface area.  It outputs the values of the dividing angles.
# If you visualize the sphere as Earth (even though Earth isn't a perfect sphere), these angles would correspond to latitudes,
# with 90 = North Pole, 0 = equator, and -90 = South Pole.
#
# Method:
# To divide a sphere into N horizontal bands of equal surface area, we need to use this rule: http://mathworld.wolfram.com/SphericalSegment.html.
# According to that page, the surface area of a band of a sphere is equal to 2*pi*R*h, where R is the radius of the sphere and h is
# the height of the band measured from the center of the sphere (i.e. the Earth's core) toward the top of the sphere (i.e. the North Pole).
# Since 2, pi, and R are constants, the surface area of the horizontal band is proportional to h.  Therefore, if we visualize a line
# between the bottom of the sphere and the top of the sphere, running through the center of the sphere, then cut that line
# into N equal length segments, we should be able to get to our answer.  To calculate the angles, we use a circle (imagining
# that this is the center slice of the sphere), and do trigonometry:
#
# Since we know two angles, we can use arcsin to find the angle of each dividing line.
#   N: number of horizontal bands of equal surface area
#   hypotenuse = R (radius of sphere)
#   h = (2*R) / N
#   opposite = R - (i*h), where i = the number of the dividing line
# Then we can use arcsin(opposite/hypotenuse) to calculate the angle.
# (If this is difficult to visualize, it helps to draw start drawing angles on a circle.)
#
# Author: Michael P. Erb, michael.erb@nau.edu
# Date:   7/18/2019
#=========================================================================================================================

import numpy as np
import math

# A function to print the boundaries between N horizontal bands of equal surface area
def equal_area_sphere_boundaries(N):
    #
    R = 1          # The radius of the sphere is set to 1, for simplicity
    h = (2*R) / N  # Height of each equal-area segment
    #
    print('Divisions between '+str(N)+' horizontal bands of equal surface area (in degrees):')
    hypotenuse = R
    for i in range(1,N):
        opposite = R - (i*h)
        angle_radians = np.arcsin(opposite/hypotenuse)
        angle_degrees = angle_radians*(180/(math.pi))
        print(angle_degrees)

# Usage example: Print the boundaries between 5 horizontal bands of equal surface area
#equal_area_sphere_boundaries(5)

