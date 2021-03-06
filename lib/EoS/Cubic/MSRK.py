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


from lib.EoS.Cubic.SRK import SRK


# TODO: Find source of data and remove support in database
dat = {
    1: (0.256300, -0.074200),
    2: (0.463100, 0.069800),
    3: (0.555800, 0.120800),
    4: (0.603800, 0.156300),
    5: (0.625100, 0.181800),
    6: (0.660100, 0.178900),
    7: (0.686000, 0.196000),
    8: (0.709400, 0.210300),
    9: (0.588700, 0.221700),
    10: (0.744600, 0.247600),
    11: (0.784100, 0.282800),
    12: (0.825300, 0.316400),
    13: (0.867500, 0.347200),
    14: (0.890500, 0.386300),
    15: (0.946700, 0.409100),
    16: (0.960400, 0.447900),
    17: (1.021200, 0.468600),
    18: (1.080400, 0.483000),
    19: (1.110400, 0.513200),
    20: (1.127400, 0.550600),
    21: (1.141400, 0.572800),
    22: (0.520200, 0.130000),
    23: (0.588300, 0.156700),
    24: (0.634100, 0.184900),
    25: (0.638300, 0.196600),
    26: (0.714100, 0.161400),
    27: (0.643500, 0.183300),
    29: (0.693000, 0.201100),
    30: (0.667900, 0.225400),
    31: (0.673800, 0.218600),
    32: (0.647800, 0.230800),
    33: (0.709900, 0.178200),
    34: (0.650100, 0.236800),
    35: (0.731800, 0.235900),
    36: (0.633300, 0.190600),
    37: (0.661100, 0.216800),
    38: (0.605600, 0.228200),
    39: (0.662000, 0.222400),
    40: (0.604300, 0.228500),
    41: (0.711700, 0.224200),
    42: (0.773700, 0.241500),
    43: (0.801100, 0.242100),
    44: (0.794100, 0.240000),
    45: (0.745800, 0.251200),
    46: (0.446800, 0.109300),
    47: (0.487100, 0.071700),
    49: (0.580900, 0.272700),
    50: (0.459400, 0.179000),
    51: (0.635800, 0.261400),
    52: (0.721200, 0.236300),
    53: (0.724500, 0.226900),
    54: (0.664500, 0.215800),
    55: (0.692300, 0.216200),
    59: (0.711600, 0.233100),
    60: (0.579100, 0.296000),
    62: (0.949900, 0.163300),
    63: (0.783800, 0.160400),
    65: (0.655300, 0.167200),
    66: (0.624500, 0.219200),
    67: (0.187700, 0.346800),
    68: (0.643500, 0.183300),
    70: (0.792100, 0.271200),
    71: (0.740200, 0.284000),
    72: (0.744200, 0.308700),
    73: (0.669600, 0.349100),
    74: (0.764200, 0.300400),
    75: (0.856900, 0.254200),
    76: (0.868200, 0.260200),
    77: (0.898700, 0.266300),
    78: (0.846000, 0.295200),
    79: (0.771000, 0.267500),
    80: (0.766700, 0.261900),
    81: (0.814900, 0.298700),
    82: (0.747700, 0.249800),
    84: (0.563000, 0.297300),
    85: (0.571300, 0.290200),
    86: (0.627100, 0.259000),
    87: (0.616300, 0.259500),
    88: (0.583000, 0.285200),
    89: (0.604100, 0.274800),
    90: (1.099200, 0.629000),
    91: (1.014100, 0.721300),
    92: (1.068200, 0.793100),
    93: (0.753100, 0.201200),
    94: (0.723700, 0.220800),
    95: (0.734000, 0.214100),
    96: (0.800400, 0.186300),
    97: (0.717100, 0.221100),
    100: (0.609200, 0.202600),
    102: (0.621100, 0.091000),
    104: (0.628800, 0.112400),
    105: (0.459700, 0.154300),
    110: (0.058700, 0.497100),
    112: (0.681600, 0.188300),
    113: (1.349800, -0.040600),
    115: (0.620500, 0.150300),
    116: (0.372900, 0.235700),
    117: (1.301300, 0.200500),
    118: (0.713100, 0.260200),
    119: (0.625200, 0.249800),
    121: (0.876700, 0.144400),
    122: (0.485900, 0.201200),
    126: (0.740400, 0.177900),
    129: (0.673900, 0.171600),
    131: (0.728000, 0.211900),
    132: (0.651800, 0.174300),
    133: (0.672000, 0.172700),
    134: (1.154500, 0.404700),
    136: (0.618000, 0.194700),
    137: (0.608600, 0.198400),
    138: (0.702200, 0.269300),
    140: (0.795100, 0.220500),
    141: (0.617200, 0.308300),
    142: (0.741700, 0.277700),
    145: (0.643400, 0.785400),
    146: (0.691700, 0.695800),
    147: (0.643700, 0.190900),
    151: (0.389800, 0.292800),
    153: (0.779300, 0.250700),
    155: (0.762300, 0.314200),
    156: (0.728300, 0.317400),
    157: (0.627800, 0.338000),
    159: (0.345300, 0.898900),
    160: (0.415100, 0.850600),
    161: (0.237400, 1.003500),
    162: (0.747300, 0.227900),
    165: (0.756400, 0.295000),
    166: (0.767200, 0.345700),
    171: (0.690600, 0.219600),
    172: (0.671700, 0.231800),
    174: (0.837200, 0.356600),
    177: (0.827600, 0.357000),
    179: (0.650500, 0.300200),
    184: (0.518900, 0.354800),
    185: (0.756600, 0.242700),
    190: (0.837400, 0.260300),
    191: (1.016300, 0.220000),
    194: (0.827400, 0.276200),
    200: (0.968500, 0.228400),
    215: (0.701200, 0.205600),
    216: (0.560500, 0.215600),
    217: (0.630200, 0.183800),
    218: (0.671500, 0.149600),
    219: (0.536800, 0.138700),
    220: (0.665000, 0.201300),
    222: (0.718300, 0.150100),
    224: (0.310400, 0.250100),
    225: (0.644100, 0.172300),
    226: (0.993800, 0.129600),
    227: (0.591200, 0.164300),
    229: (0.742700, 0.199500),
    231: (0.611400, 0.277200),
    243: (0.724900, 0.204100),
    245: (0.590600, 0.276400),
    247: (0.784700, 0.197400),
    249: (0.582700, 0.350900),
    269: (0.563800, 0.259900),
    270: (0.534200, 0.369800),
    290: (0.760300, 0.227200),
    294: (0.542500, 0.387700),
    299: (0.404800, 0.331300),
    304: (0.784500, 0.279600),
    309: (0.772400, 0.343900),
    318: (0.830900, 0.230700),
    321: (1.182200, 0.249900),
    322: (0.751300, 0.188300),
    329: (0.829900, 0.288900),
    337: (0.726600, 0.297300),
    346: (0.726000, 0.454000),
    347: (0.939100, 0.371700),
    369: (0.748600, 0.309100),
    370: (0.758200, 0.311800),
    371: (0.834300, 0.233400),
    372: (0.671500, 0.274400),
    373: (0.738100, 0.266600),
    374: (0.740800, 0.270100),
    375: (0.719300, 0.266000),
    377: (0.886600, 0.246900),
    378: (0.835400, 0.270900),
    379: (0.746500, 0.301200),
    380: (0.881700, 0.261600),
    381: (0.872500, 0.261300),
    382: (0.835300, 0.277700),
    398: (0.889000, 0.371400),
    401: (0.905100, 0.414400),
    406: (0.981500, 0.302100),
    407: (0.963400, 0.442800),
    410: (0.949500, 0.498000),
    432: (0.722300, 0.246500),
    433: (0.742100, 0.244700),
    434: (0.733700, 0.258500),
    435: (0.722800, 0.221400),
    436: (0.740500, 0.263500),
    437: (0.695400, 0.218200),
    460: (0.726600, 0.297300),
    541: (0.731300, 0.253500),
    552: (0.797500, 0.209600),
    553: (0.743500, 0.239200),
    554: (0.770400, 0.224300),
    577: (0.631700, 0.256300),
    583: (0.628500, 0.277500),
    590: (0.799200, 0.299500),
    591: (0.799900, 0.300200),
    592: (0.759400, 0.285600),
    593: (0.783500, 0.279800),
    594: (0.768800, 0.285800),
    595: (0.784700, 0.291100),
    596: (0.763200, 0.261100),
    597: (0.776100, 0.274800),
    598: (0.790900, 0.293400),
    599: (0.747700, 0.233000),
    600: (0.761000, 0.255800),
    601: (0.765400, 0.271300),
    602: (0.766500, 0.237300),
    603: (0.551500, 0.313900),
    611: (0.829000, 0.344600),
    630: (0.707600, 0.429200),
    643: (0.769900, 0.185300),
    693: (0.662300, 0.391800),
    743: (0.745100, 0.264900)}


class MSRK(SRK):
    r"""Modified SRK two parameters cubic equation of state as explain in [1]_

    .. math::
        \begin{array}[t]{l}
        P = \frac{RT}{V-b}-\frac{a}{V\left(V+b\right)}\\
        a = 0.42747\frac{R^2T_c^2}{P_c}\alpha\\
        b = 0.08664\frac{RT_c}{P_c}\\
        \alpha = 1 + m\left(1-Tr\right) + n\left(\frac{1}{T_R}-1\right)\\
        \end{array}

    m and n are compound specific parameters saved in database

    Examples
    --------
    Example 4.3 from [2]_, Propane saturated at 300K

    >>> from lib.mezcla import Mezcla
    >>> mix = Mezcla(5, ids=[4], caudalMolar=1, fraccionMolar=[1])
    >>> eq = MSRK(300, 9.9742e5, mix)
    >>> '%0.0f %0.1f' % (eq.Vg.ccmol, eq.Vl.ccmol)
    '2063 98.2'
    >>> eq = MSRK(300, 42.477e5, mix)
    >>> '%0.1f' % (eq.Vl.ccmol)
    '94.9'
    """
    __title__ = "M-SRK (1984)"
    __status__ = "MSRK"
    __doi__ = (
      {
        "autor": "Soave, G.",
        "title": "Improvement of the van der Waals Equation of State",
        "ref": "Chem. Eng. Sci. 39(2) (1984) 357-369",
        "doi": "10.1016/0009-2509(84)80034-2"},
      {
         "autor": "Poling, B.E, Prausnitz, J.M, O'Connell, J.P",
         "title": "The Properties of Gases and Liquids 5th Edition",
         "ref": "McGraw-Hill, New York, 2001",
         "doi": ""})

    def _alfa(self, cmp, T):
        """Special alpha function for this modified version, if the compound
        specified parameters are not available in database use the standard
        SRK alpha expresion"""
        if cmp.id in dat:
            m, n = dat[cmp.id]
            alfa = 1 + m*(1-T/cmp.Tc) + n*(cmp.Tc/T-1)                  # Eq 7
        else:
            alfa = SRK._alfa(self, cmp, T)
        return alfa


if __name__ == "__main__":
    from lib.mezcla import Mezcla
    mix = Mezcla(5, ids=[4], caudalMolar=1, fraccionMolar=[1])
    eq = MSRK(300, 9.9742e5, mix)
    print('%0.0f %0.1f' % (eq.Vg.ccmol, eq.Vl.ccmol))
    eq = MSRK(300, 42.477e5, mix)
    print('%0.1f' % (eq.Vl.ccmol))
