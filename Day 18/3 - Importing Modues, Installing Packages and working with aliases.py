# 1. Simple Import:
import turtle

# 2. Importing specific package:
from turtle import Turtle
from turtle import *
# * means that we want to include everything from the module turtle

"""
Note:
This gets confusing sometimes as we don;t know which function is cminf from where. For example:
from random import *
choice()
"""

# 3. Aliasing Modules:
import numpy as np
# np.arange()
import matplotlib.pyplot as plt

# 4. Downloading Modules:
# Modules not inncluded in the python standard library need to be installed. For example:
# pip install heroes

import heroes
print(heroes.gen())