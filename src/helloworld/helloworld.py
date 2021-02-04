#! /usr/bin/env python
'''
Created on Jan 15, 2020
@author: welling
'''

from __future__ import print_function
import six

# I added this change while creating the for_group2 branch

def main():
    print("""
    Hello World, from...
    Joel S. Welling
    Isabelle Augensen
<<<<<<< HEAD
    Emeline Fromont
=======
    Nico Ortiz de Zárate
>>>>>>> 4ba4265f54740d8a43b5636ce94a16c9b291d6d4
    """)

if __name__ == "__main__":
    main()
