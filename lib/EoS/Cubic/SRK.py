#!/usr/bin/python3
# -*- coding: utf-8 -*-

r"""Pychemqt, Chemical Engineering Process simulator
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
along with this program.  If not, see <http://www.gnu.org/licenses/>."""


from scipy.constants import R

from lib.EoS.cubic import Cubic


class SRK(Cubic):
    r"""Equation of state of Soave-Redlich-Kwong (1972)

    .. math::
        \begin{array}[t]{l}
        P = \frac{RT}{V-b}-\frac{a}{V\left(V+b\right)}\\
        a = 0.42747\frac{R^2T_c^2}{P_c}\alpha\\
        b = 0.08664\frac{RT_c}{P_c}\\
        \alpha^{0.5} = 1 + m\left(1-Tr^{0.5}\right)\\
        m = 0.48 + 1.574\omega - 0.176\omega^2\\
        \end{array}

    Examples
    --------
    Example 4.3 from [2]_, Propane saturated at 300K

    >>> from lib.mezcla import Mezcla
    >>> mix = Mezcla(5, ids=[4], caudalMolar=1, fraccionMolar=[1])
    >>> eq = SRK(300, 9.9742e5, mix)
    >>> '%0.0f %0.1f' % (eq.Vg.ccmol, eq.Vl.ccmol)
    '2065 98.4'
    >>> eq = SRK(300, 42.477e5, mix)
    >>> '%0.1f' % (eq.Vl.ccmol)
    '95.1'
    """

    __title__ = "Soave-Redlich-Kwong (1972)"
    __status__ = "SRK72"
    __doi__ = (
      {
        "autor": "Soave, G.",
        "title": "Equilibrium Constants from a modified Redlich-Kwong "
                 "Equation of State",
        "ref": "Chem. Eng. Sci. 27 (1972) 1197-1203",
        "doi": "10.1016/0009-2509(72)80096-4"},
      {
         "autor": "Poling, B.E, Prausnitz, J.M, O'Connell, J.P",
         "title": "The Properties of Gases and Liquids 5th Edition",
         "ref": "McGraw-Hill, New York, 2001",
         "doi": ""})

    def __init__(self, T, P, mezcla):
        self.T = T
        self.P = P
        self.mezcla = mezcla

        ai = []
        bi = []
        for cmp in mezcla.componente:
            a, b = self._lib(cmp, T)
            ai.append(a)
            bi.append(b)

        am, bm = self._mixture("SRK", mezcla.ids, [ai, bi])

        self.ai = ai
        self.bi = bi
        self.b = bm
        self.tita = am
        self.delta = bm
        self.epsilon = 0

        super(SRK, self).__init__(T, P, mezcla)

    def _lib(self, cmp, T):
        ao = 0.42747*R**2*cmp.Tc**2/cmp.Pc                              # Eq 5
        b = 0.08664*R*cmp.Tc/cmp.Pc                                     # Eq 6
        alfa = self._alfa(cmp, T)
        return ao*alfa, b

    def _alfa(self, cmp, T):
        m = 0.48 + 1.574*cmp.f_acent - 0.176*cmp.f_acent**2             # Eq 15
        return (1+m*(1-(T/cmp.Tc)**0.5))**2                             # Eq 13
