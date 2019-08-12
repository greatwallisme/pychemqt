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


import os

from scipy.constants import R

from lib.bip import Kij, Mixing_Rule
from lib.EoS.cubic import Cubic


class vdW(Cubic):
    r"""Equation of state of van der Waals (1873)
    This equation is not accuracy and is implemented only by its historic
    relevance, so this is the first cubic equation of state.

    .. math::
        \begin{array}[t]{l}
        P = \frac{RT}{V-b}-\frac{a}{V^2}\\
        a = 0.421875\frac{R^2T_c^2}{P_c}\\
        b = 0.125\frac{RT_c}{P_c}\\
        \end{array}

    Examples
    --------
    Example 4.3 from 1_, Propane saturated at 300K

    >>> from lib.mezcla import Mezcla
    >>> mix = Mezcla(5, ids=[4], caudalMolar=1, fraccionMolar=[1])
    >>> eq = vdW(300, 9.9742e5, mix)
    >>> '%0.0f %0.1f' % (eq.Vg.ccmol, eq.Vl.ccmol)
    '2177 145.4'
    >>> eq = vdW(300, 42.477e5, mix)
    >>> '%0.1f' % (eq.Vl.ccmol)
    '135.5'
    """

    __title__ = "van der Waals (1890)"
    __status__ = "vdW"
    __doi__ = {
        "autor": "van der Waals, J.D.",
        "title": "Over de Continuiteit van den Gas- En Vloestoftoestand",
        "ref": "Dissertation, Leiden University, Leiden, Niederlande, 1873",
        "doi": ""},

    def __init__(self, T, P, mezcla):

        x = mezcla.fraccion

        ai = []
        bi = []
        for cmp in mezcla.componente:
            a, b = self.__lib(cmp)
            ai.append(a)
            bi.append(b)

        self.kij = Kij(mezcla.ids)
        am, bm = Mixing_Rule(x, [ai, bi], self.kij)

        self.ai = ai
        self.bi = bi
        self.b = bm
        self.tita = am
        self.delta = 0
        self.epsilon = 0


        super(vdW, self).__init__(T, P, mezcla)

    def __lib(self, cmp):
        a = 0.421875*R**2*cmp.Tc**2/cmp.Pc
        b = 0.125*R*cmp.Tc/cmp.Pc
        return a, b

    # From Tarek
    # Zv in reference has a typo, the expressed polynomial has other high root
    # >>> from lib.corriente import Mezcla
    # >>> mix = Mezcla(1, ids=[4], caudalUnitarioMasico=[1.])
    # >>> T = unidades.Temperature(100, "F")
    # >>> P = unidades.Pressure(185, "psi")
    # >>> eq = vdW(T, P, mix)
    # >>> '%0.5f %0.5f' % (eq.Zl, eq.Zv)
    # '0.07533 0.84348'

if __name__ == "__main__":
    from lib.mezcla import Mezcla
    mix = Mezcla(5, ids=[4], caudalMolar=1, fraccionMolar=[1])
    eq = vdW(300, 9.9742e5, mix)
    print('%0.0f %0.1f' % (eq.Vg.ccmol, eq.Vl.ccmol))
    eq = vdW(300, 42.477e5, mix)
    print('%0.1f' % (eq.Vl.ccmol))
