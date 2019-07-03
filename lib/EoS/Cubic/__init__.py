#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''Pychemqt, Chemical Engineering Process simulator
Copyright (C) 2009-2017, Juan José Gómez Romera <jjgomera@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.'''


from lib.EoS.Cubic.PR import PR
from lib.EoS.Cubic.vdW import vdW 

_all= [vdW, PR]
# _all= [vdW, RK, Wilson, Fuller, SRK, SRK_API, MSRK, SRK_Graboski, PR, PRSV, PR_Gasem, PR_Melhem, PR_Almeida]


# Add references from equation hardcoded in __doi__ property
__doi__ = {}
for obj in _all:
    if obj.__doi__:
        __doi__[obj.__name__] = obj.__doi__
