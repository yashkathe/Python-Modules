import argparse 
import math

# create a parser
# - container to hold a argument
parser = argparse.ArgumentParser(description="Calculate Volume of A Cylinder")

# add arguments
parser.add_argument('-r', '--radius', type=int, required=True, help='Radius of Cylinder')
parser.add_argument('-H', '--height', type=int, required=True, help='Height of Cylinder')

# parse the args
args = parser.parse_args()

def vol_of_cylinder(radius, height):
    vol = (math.pi) * (radius ** 2) * (height)
    return vol

print(vol_of_cylinder(args.radius, args.height))

# running the program
##################################
# python3 module_argparse.py 4 2 #
##################################

########################################
# python3 module_argparse.py -r 4 -H 2 #
########################################

# captial H for height because -h is by default reserved for help