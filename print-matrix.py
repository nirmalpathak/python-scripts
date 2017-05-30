#!/usr/bin/env python
#############################################################
# Date:     2017/04/28
# Author:   Nirmal Pathak
# Web:      
#
# Program:
#   Script to create NxN matrix of two values 'on' & 'off'.
############################################################

import itertools

def switches(n):
        lst = list(itertools.product(['on', 'off'], repeat=n))
        for i in range(len(lst)):
                print lst[i]

switches(3)
