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


from unittest import TestCase

from lib.meos import MEoS
from lib import unidades


class Ar(MEoS):
    """Multiparamter equation of state for argon"""
    name = "argon"
    CASNumber = "7440-37-1"
    formula = "Ar"
    synonym = "R-740"
    rhoc = unidades.Density(535.6)
    Tc = unidades.Temperature(150.687)
    Pc = unidades.Pressure(4863, "kPa")
    M = 39.948  # g/mol
    Tt = unidades.Temperature(83.8058)
    Tb = unidades.Temperature(87.302)
    f_acent = -0.00219
    momentoDipolar = unidades.DipoleMoment(0.0, "Debye")
    id = 98
    _Tr = unidades.Temperature(147.707801)
    _rhor = unidades.Density(540.014968)
    _w = 0.000305675

    Fi1 = {"ao_log": [1, 1.5],
           "pow": [0, 1],
           "ao_pow": [8.31666243, -4.94651164],
           "ao_exp": [], "titao": []}

    CP1 = {"ao": 2.5,
           "an": [], "pow": [], "ao_exp": [], "exp": [],
           "ao_hyp": [], "hyp": []}

    Fi2 = {"ao_log": [1, 1.5],
           "pow": [0, 1],
           "ao_pow": [8.3166315, -4.9465026],
           "ao_exp": [], "titao": [],
           "ao_hyp": [], "hyp": []}

    helmholtz1 = {
        "__type__": "Helmholtz",
        "__name__": "FEQ Helmholtz equation of state for argon of Tegeler et "
                    "al. (1999).",
        "__doi__": {"autor": "Tegeler, Ch., Span, R., Wagner, W.",
                    "title": "A New Equation of State for Argon Covering the "
                             "Fluid Region for Temperatures From the Melting "
                             "Line to 700 K at Pressures up to 1000 MPa",
                    "ref": "J. Phys. Chem. Ref. Data 28, 779 (1999)",
                    "doi": "10.1063/1.556037"},

        "R": 8.31451,
        "cp": Fi1,
        "ref": "OTO",

        "Tmin": Tt, "Tmax": 2000., "Pmax": 1000000.0, "rhomax": 50.65,
        "Pmin": 68.891, "rhomin": 35.465,

        "nr1": [0.887223049900e-1, 0.705148051673, -0.168201156541e1,
                -0.149090144315, -0.120248046009, -0.121649787986,
                0.400359336268, -0.271360626991, 0.242119245796,
                0.578895831856e-2, -0.410973356153e-1, 0.247107615416e-1],
        "d1": [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4],
        "t1": [0., 0.25, 1., 2.75, 4.0, 0., 0.25, 0.75, 2.75, 0.0, 2.0, 0.75],

        "nr2": [-0.321813917507, 0.332300176958, 0.310199862873e-1,
                -0.307770860024e-1, 0.938911374196e-1, -0.906432106820e-1,
                -0.457783492767e-3, -0.826597290252e-4, 0.130134156031e-3,
                -0.113978400020e-1, -0.244551699605e-1, -0.643240671760e-1,
                0.588894710937e-1, -0.649335521130e-3, -0.138898621584e-1,
                0.404898392969, -0.386125195947, -0.188171423322,
                0.159776475965, 0.539855185139e-1, -0.289534179580e-1,
                -0.130254133814e-1, 0.289486967758e-2, -0.226471343048e-2,
                0.176164561964e-2],
        "c2": [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3,
               3, 3, 4, 4],
        "d2": [1, 1, 3, 4, 4, 5, 7, 10, 10, 2, 2, 4, 4, 8, 3, 5, 5, 6, 6, 7, 7,
               8, 9, 5, 6],
        "t2": [3., 3.5, 1., 2., 4., 3., 0., 0.5, 1., 1., 7., 5., 6., 6., 10.,
               13., 14., 11., 14., 8., 14., 6., 7., 24., 22.],
        "gamma2": [1]*25,

        "nr3": [0.585524544828e-2, -0.6925190827, 0.153154900305e1,
                -0.273804474498e-2],
        "d3": [2, 1, 2, 3],
        "t3": [3, 1, 0, 0],
        "alfa3": [20]*4,
        "beta3": [250, 375, 300, 225],
        "gamma3": [1.11, 1.14, 1.17, 1.11],
        "epsilon3": [1, 1, 1, 1],
        "nr4": []}

    GERG = {
        "__type__": "Helmholtz",
        "__name__": "Helmholtz equation of state for argon of Kunz and Wagner (2004).",
        "__doi__": {"autor": "Kunz, O., Wagner, W.",
                    "title": "The GERG-2008 Wide-Range Equation of State for Natural Gases and Other Mixtures: An Expansion of GERG-2004",
                    "ref": "J. Chem. Eng. Data, 2012, 57 (11), pp 3032–3091",
                    "doi":  "10.1021/je300655b"},
        "R": 8.314472,
        "cp": Fi2,
        "ref": "OTO",

        "Tmin": Tt, "Tmax": 700., "Pmax": 1000000.0, "rhomax": 50.65,
        "Pmin": 68.891, "rhomin": 35.465,

        "nr1": [0.85095714803969, -0.24003222943480e1, 0.54127841476466,
                0.16919770692538e-1, 0.68825965019035e-1, 0.21428032815338e-3],
        "d1": [1, 1, 1, 2, 3, 7],
        "t1": [0.25, 1.125, 1.5, 1.375, 0.25, 0.875],

        "nr2": [0.17429895321992, -0.033654495604194, -0.13526799857691,
                -0.016387350791552, -0.024987666851475, 0.0088769204815709],
        "c2": [1, 1, 2, 2, 3, 3],
        "d2": [2, 5, 1, 4, 3, 4],
        "t2": [0.625, 1.75, 3.625, 3.625, 14.5, 12],
        "gamma2": [1]*6,

        "nr3": [],
        "nr4": []}

    helmholtz3 = {
        "__type__": "Helmholtz",
        "__name__": "Helmholtz equation of state for argon of Stewart and "
                    "Jacobsen (1989).",
        "__doi__": {"autor": "Stewart, R.B. and Jacobsen, R.T.",
                    "title": "Thermodynamic Properties of Argon from the "
                             "Triple Point to 1200 K at Pressures to 1000 MPa",
                    "ref": "J. Phys. Chem. Ref. Data, 18(2):639-798, 1989",
                    "doi": "10.1063/1.555829"},

        "R": 8.31434,
        "cp": CP1,
        "ref": {"Tref": 298.15, "Pref": 101.325, "ho": 6197, "so": 154.732},
        "Tc": 150.6633, "Pc": 4860, "rhoc": 13.29, "Tt": 83.804,

        "Tmin": 83.804, "Tmax": 1200., "Pmax": 1000000.0, "rhomax": 45.814,
        "Pmin": 68.961, "rhomin": 35.475,

        "nr1": [0.7918675715, -1.633346151, -0.439530293, 0.1033899999,
                0.2061801664, -0.2888681776, 0.439801055, -0.08429550391,
                -0.2155658654, 0.4786509099, -0.3525884593, 0.03015073692,
                0.02987679059, -0.01522568583, 0.0007435785786],
        "d1": [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 6],
        "t1": [0.25, 1, 3, 4, 0.25, 1, 2.5, 3.5, 0.75, 1, 1.5, 2.5, 1, 2, 2],

        "nr2": [0.07099541624, -0.02904237185, -0.06223078525, 0.0001410895187,
                -0.001481241783, 0.03023342784, -0.06126784685, 0.0270996709,
                0.09411034405, -0.007291645114, -0.001586314976,
                0.0009510948813, 0.0007786181844],
        "c2": [3, 3, 2, 4, 6, 3, 3, 3, 2, 2, 4, 2, 2],
        "d2": [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 8, 8],
        "t2": [5, 7, 5, 22, 16, 10, 14, 16, 4, 8, 10, 5, 6],
        "gamma2": [1]*13,

        "nr3": [],
        "nr4": []}

    helmholtz4 = {
        "__type__": "Helmholtz",
        "__name__": "short Helmholtz equation of state for argon of Span and Wagner (2003).",
        "__doi__": {"autor": "Span, R., Wagner, W.",
                    "title": "Equations of state for technical applications. II. Results for nonpolar fluids.",
                    "ref": "Int. J. Thermophys. 24 (2003), 41 – 109.",
                    "doi": "10.1023/A:1022310214958"},
        "__test__": """
            >>> st=Ar(T=700, rho=200, eq=4)
            >>> print "%0.4f %0.3f %0.4f" % (st.cp0.kJkgK, st.P.MPa, st.cp.kJkgK)
            0.5203 31.922 0.5630
            >>> st2=Ar(T=750, rho=100, eq=4)
            >>> print "%0.2f %0.5f" % (st2.h.kJkg-st.h.kJkg, st2.s.kJkgK-st.s.kJkgK)
            25.97 0.18479
            """, # Table III, Pag 46

        "R": 8.31451,
        "cp": Fi1,
        "ref": "OTO",

        "Tmin": Tt, "Tmax": 750., "Pmax": 100000.0, "rhomax": 50.65,
        "Pmin": 69.026, "rhomin": 35.498,

        "nr1": [0.85095715, -0.24003223e1, 0.54127841, 0.16919771e-1,
                0.68825965e-1, 0.21428033e-3],
        "d1": [1, 1, 1, 2, 3, 7],
        "t1": [0.25, 1.125, 1.5, 1.375, 0.25, 0.875],

        "nr2": [0.17429895, -0.33654496e-1, -0.135268, -0.16387351e-1,
                -0.24987667e-1, 0.88769205e-2],
        "c2": [1, 1, 2, 2, 3, 3],
        "d2": [2, 5, 1, 4, 3, 4],
        "t2": [0.625, 1.75, 3.625, 3.625, 14.5, 12],
        "gamma2": [1]*6,

        "nr3": [],
        "nr4": []}

    MBWR = {
        "__type__": "MBWR",
        "__name__": "BWR  MBWR equation of state for argon of Younglove (1982).",
        "__doi__": {"autor": "Younglove, B.A.",
                    "title": "Thermophysical Properties of Fluids. I. Argon, Ethylene, Parahydrogen, Nitrogen, Nitrogen Trifluoride, and Oxygen",
                    "ref": "J. Phys. Chem. Ref. Data, Vol. 11, Suppl. 1, pp. 1-11, 1982.",
                    "doi": ""},

        "R": 8.31434,
        "cp": CP1,
        "ref": {"Tref": 298.15, "Pref": 101.325, "ho": 6197, "so": 154.732},

        "Tmin": 83.80, "Tmax": 400., "Pmax": 101000.0, "rhomax": 50.65,
        "Pmin": 68.906, "rhomin": 35.4,

        "b": [None, -0.6569731294e-3, 0.1822957801, -0.3649470141e1,
              0.1232012107e3, -0.8613578274e4, 0.7978579691e-4, -0.2911489110e-1,
              0.7581821758e1, 0.8780488169e4, 0.1423145989e-6, 0.1674146131e-2,
              -0.3200447909, 0.2561766372e-4, -0.5475934941e-3, -0.4505032058,
              0.2013254653e-4, -0.1678941273e-6, 0.4207329271e-3, -0.5444212996e-5,
              -0.8004855011e4, -0.1319304201e6, -0.4954923930e2, 0.8092132177e5,
              -0.9870104061e-1, 0.2020441562e1, -0.1637417205e-3, -0.7038944136,
              -0.1154324539e-6, 0.1555990117e-4, -0.1492178536e-9,
              -0.1001356071e-7, 0.2933963216e-6]}

    eq = helmholtz1, MBWR, GERG, helmholtz3, helmholtz4
    _PR = -0.0034

    _dielectric = {
        "eq": 3, "Tref": 273.16, "rhoref": 1000.,
        "a0": [],  "expt0": [], "expd0": [],
        "a1": [4.1414], "expt1": [0], "expd1": [1],
        "a2": [1.597, 0.262, -117.9], "expt2": [0, 1, 0], "expd2": [2, 2, 3.1]}
    _melting = {
        "eq": 1, "Tref": Tt, "Pref": 68.891,
        "Tmin": 83.8058, "Tmax": 700.0,
        "a1": [1, -7476.26651, 9959.06125, 7476.26651, -9959.06125],
        "exp1": [0, 1.05, 1.275, 0, 0],
        "a2": [], "exp2": [], "a3": [], "exp3": []}
    _sublimation = {
        "eq": 3, "Tref": Tt, "Pref": 68.891,
        "Tmin": 83.8058, "Tmax": 83.8058,
        "a1": [], "exp1": [],
        "a2": [-11.1307], "exp2": [1],
        "a3": [], "exp3": []}
    _surface = {"sigma": [0.037], "exp": [1.25]}
    _vapor_Pressure = {
        "eq": 5,
        "ao": [-5.9409785, 1.3553888, -0.4649761, -1.5399043],
        "exp": [1., 1.5, 2., 4.5]}
    _liquid_Density = {
        "eq": 3,
        "ao": [1.5004264, -0.3138129, 0.086461622, -0.041477525],
        "exp": [0.334, 2./3, 7./3, 4]}
    _vapor_Density = {
        "eq": 5,
        "ao": [-0.29182e1, 0.97930e-1, -0.13721e1, -0.22898e1],
        "exp": [0.72, 1.25, 0.32, 4.34]}

    visco0 = {"eq": 1, "omega": 1,
              "__name__": "Lemmon (2004)",
               "__doi__": {"autor": "Lemmon, E.W. and Jacobsen, R.T.",
                            "title": "Viscosity and Thermal Conductivity Equations for Nitrogen, Oxygen, Argon, and Air",
                            "ref": "Int. J. Thermophys., 25:21-69, 2004.",
                            "doi": "10.1023/B:IJOT.0000022327.04529.f3"},
               "__test__": """
                    >>> st=Ar(T=100, rhom=0)
                    >>> print "%0.5f" % st.mu.muPas
                    8.18940
                    >>> st=Ar(T=300, rhom=0)
                    >>> print "%0.4f" % st.mu.muPas
                    22.7241
                    >>> st=Ar(T=100, rhom=33)
                    >>> print "%0.3f" % st.mu.muPas
                    184.232
                    >>> st=Ar(T=200, rhom=10)
                    >>> print "%0.4f" % st.mu.muPas
                    25.5662
                    >>> st=Ar(T=300, rhom=5)
                    >>> print "%0.4f" % st.mu.muPas
                    26.3706
                    >>> st=Ar(T=150.69, rhom=13.4)
                    >>> print "%0.4f" % st.mu.muPas
                    27.6101
                    """, # Table V, Pag 28

              "ek": 143.2, "sigma": 0.335,
              "n_poly": [12.19, 13.99, 0.005027, -18.93, -6.698, -3.827],
              "t_poly": [0.42, 0.0, 0.95, 0.5, 0.9, 0.8],
              "d_poly": [1, 2, 10, 5, 1, 2],
              "g_poly": [0, 0, 0, 1, 1, 1],
              "c_poly": [0, 0, 0, 2, 4, 4]}

    visco1 = {"eq": 3,
              "__name__": "Younglove (1986)",
              "__doi__": {"autor": "Younglove, B.A. and Hanley, H.J.M.",
                           "title": "The Viscosity and Thermal Conductivity Coefficients of Gaseous and Liquid Argon",
                           "ref": "J. Phys. Chem. Ref. Data 15, 1323 (1986)",
                           "doi": "10.1063/1.555765"},
              "__test__": """
                   >>> st=Ar(T=86, P=1e5, visco=1)
                   >>> print "%0.1f" % st.mu.muPas
                   270.0
                   """, # Table V, Pag 28

              "Tref": 1, "muref": 1.0,
              "n_poly": [-0.8973188257e5, 0.8259113473e5, -0.2766475915e5,
                         0.3068539784e4, 0.4553103615e3, -0.1793443839e3,
                         0.2272225106e2, -0.1350672796e1, 0.3183693230e-1],
              "t_poly": [-1., -2./3, -1./3, 0, 1./3, 2./3, 1., 4./3, 5./3],
              "n_num": [0.5927733783, -0.4251221169e2, -0.2698477165e-1,
                        0.3727762288e2, -0.3958508720e4, 0.3636730841e-2,
                        -0.2633471347e1, 0.2936563322e3, -0.3811869019e-4,
                        0.4451947464e-1, -0.5385874487e1, 1, -0.1115054926e-1,
                        -0.1328893444e1],
              "t_num": [0, -1, 0, -1, -2, 0, -1, -2, 0, -1, -2, 0, 0, -1],
              "d_num": [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 0, 1, 1],
              "n_den": [1.0, -0.1115054926e-1, -0.1328893444e1],
              "t_den": [0, 0, -1],
              "d_den": [0, 1, 1]}

    visco2 = {"eq": 2, "omega": 2,
              "collision": [25.7830291943396, -234.320222858983, 814.636688705024,
                            -1452.04353466585, 1467.17535558104, -870.164951237067,
                            313.024934147423, -61.2072628957372, 5.07700488990665],
              "__name__": "Younglove (1982)",
              "__doi__": {"autor": "Younglove, B.A.",
                          "title": "Thermophysical Properties of Fluids. I. Argon, Ethylene, Parahydrogen, Nitrogen, Nitrogen Trifluoride, and Oxygen",
                          "ref": "J. Phys. Chem. Ref. Data, Vol. 11, Suppl. 1, pp. 1-11, 1982.",
                          "doi": ""},

              "ek": 152.8, "sigma": 0.3297,
              "n_chapman": 0.16871158559818,
              "t_chapman": 0,
              "F": [5.85384107393e-3, -3.09546765250e-3, 1.4, 152.8],
              "E": [-12.313579086, 40.136071933, 11.6160872385243,
                    -413.04094973717, 4.13624595833e-2, 7.96883967907912,
                    234.196850483958],
              "rhoc": 13.4424752177831}

    _viscosity = visco0, visco1, visco2

    thermo0 = {"eq": 1,
               "__name__": "Lemmon (2004)",
               "__doi__": {"autor": "Lemmon, E.W. and Jacobsen, R.T.",
                            "title": "Viscosity and Thermal Conductivity Equations for Nitrogen, Oxygen, Argon, and Air",
                            "ref": "Int. J. Thermophys., 25:21-69, 2004.",
                            "doi": "10.1023/B:IJOT.0000022327.04529.f3"},
               "__test__": """
                    >>> st=Ar(T=100, rhom=0)
                    >>> print "%0.5f" % st.k.mWmK
                    6.36587
                    >>> st=Ar(T=300, rhom=0)
                    >>> print "%0.4f" % st.k.mWmK
                    17.8042
                    >>> st=Ar(T=100, rhom=33)
                    >>> print "%0.3f" % st.k.mWmK
                    111.266
                    >>> st=Ar(T=200, rhom=10)
                    >>> print "%0.4f" % st.k.mWmK
                    26.1377
                    >>> st=Ar(T=300, rhom=5)
                    >>> print "%0.4f" % st.k.mWmK
                    23.2302
                    >>> st=Ar(T=150.69, rhom=13.4)
                    >>> print "%0.4f" % st.k.mWmK
                    856.793
                    """, # Table V, Pag 28

               "Tref": 150.687, "kref": 1e-3,
               "no": [0.8158, -0.432],
               "co": [-97, -0.77],

               "Trefb": 150.687, "rhorefb": 13.40742965, "krefb": 1e-3,
               "nb": [13.73, 10.07, 0.7375, -33.96, 20.47, -2.274, -3.973],
               "tb": [0.0, 0.0, 0.0, 0.8, 1.2, 0.8, 0.5],
               "db": [1, 2, 4, 5, 6, 9, 1],
               "cb": [0, 0, 0, 2, 2, 2, 4],

               "critical": 3,
               "gnu": 0.63, "gamma": 1.2415, "R0": 1.01,
               "Xio": 0.13e-9, "gam0": 0.55e-1, "qd": 0.32e-9, "Tcref": 301.374}

    thermo1 = {"eq": 3,
               "__name__": "Younglove (1982)",
               "__doi__": {"autor": "Younglove, B.A.",
                           "title": "Thermophysical Properties of Fluids. I. Argon, Ethylene, Parahydrogen, Nitrogen, Nitrogen Trifluoride, and Oxygen",
                           "ref": "J. Phys. Chem. Ref. Data, Vol. 11, Suppl. 1, pp. 1-11, 1982.",
                           "doi": ""},

               "ek": 152.8, "sigma": 0.3297,
               "Nchapman": 0.16871158559818,
               "tchapman": 0,
               "b": [2.64712871543e-2, -.216629583011974, 0.709700888884514,
                     -1.21908891344223, 1.20168985706305, -.700084760049098,
                     0.24816605762696, -4.79479287295e-2, 3.93679190444e-3],
               "F": [9.64428741429e-4, 3.02391316601e-4, 1, 152.8],
               "E": [-33.327027332, -355.59415848, 22.2441164817987,
                     1663.62775376509, 0, 0, 0],
               "rhoc": 25.0325423049965,
               "ff": 1.7124,
               "rm": 0.00000003669}

    thermo2 = {"eq": 1,
               "__name__": "Perkins (1991)",
               "__doi__": {"autor": "Perkins, R.A., Friend, D.G., Roder, H.M., and Nieto de Castro, C.A.",
                           "title": "Thermal Conductivity Surface of Argon:  A Fresh Analysis",
                           "ref": "Int. J. Thermophys., 12(6):965-984, 1991.",
                           "doi": "10.1007/BF00503513"},

               "Tref": 1.0, "kref": 1e-3,
               "no": [.1225067272e5, -.9096222831e4, .2744958263e4,
                      -.4170419051e3, .2527591169e2, .1604421067e1,
                      -.2618841031, .1381696924e-1, -.2463115922e-3],
               "co": [-1, -2./3, -1./3, 0, 1./3, 2./3, 1., 4./3, 5./3],

               "Trefb": 1., "rhorefb": 1., "krefb": 1.,
               "nb": [0.757894e-3, 0.612624e-4, -0.205353e-5,  0.745621e-7],
               "tb": [0, 0, 0, 0],
               "db": [1, 2, 3, 4],
               "cb": [0, 0, 0, 0],

               "critical": 4,
               "Tcref": 150.86, "Pcref": 4905.8, "rhocref": 13.41, "kcref": 1e-3,
               "gamma": 1.02,
               "expo": 0.46807, "alfa": 39.8, "beta": 5.45, "Xio": 6.0795e-1}

    _thermal = thermo0, thermo1, thermo2


class Test(TestCase):

    def test_Tegeler(self):
        # Selected point from Table 33, Pag 828, saturation states
        st = Ar(T=83.8058, x=0.5)
        self.assertEqual(round(st.P.MPa, 6), 0.068891)
        self.assertEqual(round(st.Liquido.rho, 2), 1416.77)
        self.assertEqual(round(st.Liquido.h.kJkg, 2), -276.56)
        self.assertEqual(round(st.Liquido.s.kJkgK, 4), -2.5440)
        self.assertEqual(round(st.Liquido.cv.kJkgK, 5), 0.54960)
        self.assertEqual(round(st.Liquido.cp.kJkgK, 4), 1.1157)
        self.assertEqual(round(st.Liquido.w, 2), 862.43)
        self.assertEqual(round(st.Gas.rho, 4), 4.0546)
        self.assertEqual(round(st.Gas.h.kJkg, 2), -112.85)
        self.assertEqual(round(st.Gas.s.kJkgK, 5), -0.59044)
        self.assertEqual(round(st.Gas.cv.kJkgK, 5), 0.32471)
        self.assertEqual(round(st.Gas.cp.kJkgK, 5), 0.55503)
        self.assertEqual(round(st.Gas.w, 2), 168.12)

        st = Ar(T=90, x=0.5)
        self.assertEqual(round(st.P.MPa, 5), 0.13351)
        self.assertEqual(round(st.Liquido.rho, 2), 1378.63)
        self.assertEqual(round(st.Liquido.h.kJkg, 2), -269.61)
        self.assertEqual(round(st.Liquido.s.kJkgK, 4), -2.4645)
        self.assertEqual(round(st.Liquido.cv.kJkgK, 5), 0.52677)
        self.assertEqual(round(st.Liquido.cp.kJkgK, 4), 1.1212)
        self.assertEqual(round(st.Liquido.w, 2), 819.45)
        self.assertEqual(round(st.Gas.rho, 4), 7.4362)
        self.assertEqual(round(st.Gas.h.kJkg, 2), -110.55)
        self.assertEqual(round(st.Gas.s.kJkgK, 5), -0.69718)
        self.assertEqual(round(st.Gas.cv.kJkgK, 5), 0.33094)
        self.assertEqual(round(st.Gas.cp.kJkgK, 5), 0.57569)
        self.assertEqual(round(st.Gas.w, 2), 172.83)

        st = Ar(T=120, x=0.5)
        self.assertEqual(round(st.P.MPa, 3), 1.2130)
        self.assertEqual(round(st.Liquido.rho, 2), 1162.82)
        self.assertEqual(round(st.Liquido.h.kJkg, 2), -233.48)
        self.assertEqual(round(st.Liquido.s.kJkgK, 4), -2.1274)
        self.assertEqual(round(st.Liquido.cv.kJkgK, 5), 0.45763)
        self.assertEqual(round(st.Liquido.cp.kJkgK, 4), 1.3324)
        self.assertEqual(round(st.Liquido.w, 2), 584.19)
        self.assertEqual(round(st.Gas.rho, 3), 60.144)
        self.assertEqual(round(st.Gas.h.kJkg, 2), -106.71)
        self.assertEqual(round(st.Gas.s.kJkgK, 4), -1.0710)
        self.assertEqual(round(st.Gas.cv.kJkgK, 5), 0.38934)
        self.assertEqual(round(st.Gas.cp.kJkgK, 5), 0.86265)
        self.assertEqual(round(st.Gas.w, 2), 185.09)

        st = Ar(T=150, x=0.5)
        self.assertEqual(round(st.P.MPa, 4), 4.7346)
        self.assertEqual(round(st.Liquido.rho, 2), 680.43)
        self.assertEqual(round(st.Liquido.h.kJkg, 2), -173.01)
        self.assertEqual(round(st.Liquido.s.kJkgK, 4), -1.7145)
        self.assertEqual(round(st.Liquido.cv.kJkgK, 5), 0.70603)
        self.assertEqual(round(st.Liquido.cp.kJkgK, 3), 23.582)
        self.assertEqual(round(st.Liquido.w, 2), 174.74)
        self.assertEqual(round(st.Gas.rho, 2), 394.50)
        self.assertEqual(round(st.Gas.h.kJkg, 2), -143.60)
        self.assertEqual(round(st.Gas.s.kJkgK, 4), -1.5185)
        self.assertEqual(round(st.Gas.cv.kJkgK, 5), 0.82182)
        self.assertEqual(round(st.Gas.cp.kJkgK, 3), 35.468)
        self.assertEqual(round(st.Gas.w, 2), 157.01)

        # Selected points from Table 34, Pag 830, Single phase points

        st = Ar(T=83.814, P=1e5)
        self.assertEqual(round(st.rho, 2), 1416.80)
        self.assertEqual(round(st.u.kJkg, 2), -276.61)
        self.assertEqual(round(st.h.kJkg, 2), -276.54)
        self.assertEqual(round(st.s.kJkgK, 4), -2.5440)
        self.assertEqual(round(st.cv.kJkgK, 5), 0.54961)
        self.assertEqual(round(st.cp.kJkgK, 4), 1.1156)
        self.assertEqual(round(st.w, 2), 862.52)

        st = Ar(T=700, P=1e5)
        self.assertEqual(round(st.rho, 5), 0.68619)
        self.assertEqual(round(st.u.kJkg, 3), 63.355)
        self.assertEqual(round(st.h.kJkg, 2), 209.09)
        self.assertEqual(round(st.s.kJkgK, 5), 0.44677)
        self.assertEqual(round(st.cv.kJkgK, 5), 0.31223)
        self.assertEqual(round(st.cp.kJkgK, 4), 0.5205)
        self.assertEqual(round(st.w, 2), 492.95)

        st = Ar(T=150, P=5e5)
        self.assertEqual(round(st.rho, 3), 16.605)
        self.assertEqual(round(st.u.kJkg, 2), -110.45)
        self.assertEqual(round(st.h.kJkg, 3), -80.334)
        self.assertEqual(round(st.s.kJkgK, 5), -0.70404)
        self.assertEqual(round(st.cv.kJkgK, 5), 0.32098)
        self.assertEqual(round(st.cp.kJkgK, 5), 0.55987)
        self.assertEqual(round(st.w, 2), 224.97)

        st = Ar(T=170, P=1e6)
        self.assertEqual(round(st.rho, 3), 29.723)
        self.assertEqual(round(st.u.kJkg, 2), -105.62)
        self.assertEqual(round(st.h.kJkg, 3), -71.972)
        self.assertEqual(round(st.s.kJkgK, 5), -0.78987)
        self.assertEqual(round(st.cv.kJkgK, 5), 0.32356)
        self.assertEqual(round(st.cp.kJkgK, 5), 0.57801)
        self.assertEqual(round(st.w, 2), 238.88)

        st = Ar(T=125, P=2e6)
        self.assertEqual(round(st.rho, 2), 1122.34)
        self.assertEqual(round(st.u.kJkg, 2), -228.45)
        self.assertEqual(round(st.h.kJkg, 2), -226.66)
        self.assertEqual(round(st.s.kJkgK, 4), -2.0773)
        self.assertEqual(round(st.cv.kJkgK, 5), 0.45179)
        self.assertEqual(round(st.cp.kJkgK, 4), 1.4048)
        self.assertEqual(round(st.w, 2), 544.65)

        st = Ar(T=135, P=3e6)
        self.assertEqual(round(st.rho, 2), 1020.52)
        self.assertEqual(round(st.u.kJkg, 2), -214.63)
        self.assertEqual(round(st.h.kJkg, 2), -211.69)
        self.assertEqual(round(st.s.kJkgK, 4), -1.9694)
        self.assertEqual(round(st.cv.kJkgK, 5), 0.44845)
        self.assertEqual(round(st.cp.kJkgK, 4), 1.7159)
        self.assertEqual(round(st.w, 2), 445.83)

        st = Ar(T=150, P=4e6)
        self.assertEqual(round(st.rho, 2), 209.45)
        self.assertEqual(round(st.u.kJkg, 2), -134.47)
        self.assertEqual(round(st.h.kJkg, 2), -115.38)
        self.assertEqual(round(st.s.kJkgK, 4), -1.3116)
        self.assertEqual(round(st.cv.kJkgK, 5), 0.46106)
        self.assertEqual(round(st.cp.kJkgK, 4), 1.8982)
        self.assertEqual(round(st.w, 2), 193.39)

        st = Ar(T=675, P=5e6)
        self.assertEqual(round(st.rho, 3), 35.123)
        self.assertEqual(round(st.u.kJkg, 3), 53.149)
        self.assertEqual(round(st.h.kJkg, 2), 195.50)
        self.assertEqual(round(st.s.kJkgK, 5), -0.38989)
        self.assertEqual(round(st.cv.kJkgK, 5), 0.31374)
        self.assertEqual(round(st.cp.kJkgK, 5), 0.52898)
        self.assertEqual(round(st.w, 2), 493.26)

        st = Ar(T=400, P=1e7)
        self.assertEqual(round(st.rho, 2), 119.43)
        self.assertEqual(round(st.u.kJkg, 3), -40.267)
        self.assertEqual(round(st.h.kJkg, 3), 43.464)
        self.assertEqual(round(st.s.kJkgK, 5), -0.82699)
        self.assertEqual(round(st.cv.kJkgK, 5), 0.32049)
        self.assertEqual(round(st.cp.kJkgK, 5), 0.57843)
        self.assertEqual(round(st.w, 2), 391.51)

        st = Ar(T=110, P=1e8)
        self.assertEqual(round(st.rho, 2), 1494.28)
        self.assertEqual(round(st.u.kJkg, 2), -268.41)
        self.assertEqual(round(st.h.kJkg, 2), -201.49)
        self.assertEqual(round(st.s.kJkgK, 4), -2.4764)
        self.assertEqual(round(st.cv.kJkgK, 5), 0.56101)
        self.assertEqual(round(st.cp.kJkgK, 5), 0.94752)
        self.assertEqual(round(st.w, 1), 1074.3)

        st = Ar(T=330, P=1e9)
        self.assertEqual(round(st.rho, 2), 1764.39)
        self.assertEqual(round(st.u.kJkg, 2), -144.17)
        self.assertEqual(round(st.h.kJkg, 2), 422.60)
        self.assertEqual(round(st.s.kJkgK, 4), -2.0896)
        self.assertEqual(round(st.cv.kJkgK, 5), 0.55397)
        self.assertEqual(round(st.cp.kJkgK, 5), 0.75591)
        self.assertEqual(round(st.w, 1), 1851.9)

    def test_Jacobsen(self):

        # Saturation pressures from Table 12, pag. 675
        st = Ar(T=84, x=0.5, eq=3)
        self.assertEqual(round(st.P.MPa, 4), 0.0705)
        st = Ar(T=90, x=0.5, eq=3)
        self.assertEqual(round(st.P.MPa, 4), 0.1336)
        st = Ar(T=95, x=0.5, eq=3)
        self.assertEqual(round(st.P.MPa, 4), 0.2132)
        st = Ar(T=100, x=0.5, eq=3)
        self.assertEqual(round(st.P.MPa, 4), 0.3240)
        st = Ar(T=105, x=0.5, eq=3)
        self.assertEqual(round(st.P.MPa, 5), 0.47258)
        st = Ar(T=110, x=0.5, eq=3)
        self.assertEqual(round(st.P.MPa, 5), 0.66574)
        st = Ar(T=115, x=0.5, eq=3)
        self.assertEqual(round(st.P.MPa, 5), 0.91046)
        st = Ar(T=120, x=0.5, eq=3)
        self.assertEqual(round(st.P.MPa, 5), 1.21391)
        st = Ar(T=125, x=0.5, eq=3)
        self.assertEqual(round(st.P.MPa, 4), 1.5835)
        st = Ar(T=130, x=0.5, eq=3)
        self.assertEqual(round(st.P.MPa, 5), 2.02700)
        st = Ar(T=135, x=0.5, eq=3)
        self.assertEqual(round(st.P.MPa, 5), 2.55295)
        st = Ar(T=140, x=0.5, eq=3)
        self.assertEqual(round(st.P.MPa, 5), 3.17100)
        st = Ar(T=145, x=0.5, eq=3)
        self.assertEqual(round(st.P.MPa, 5), 3.89294)
        st = Ar(T=150, x=0.5, eq=3)
        self.assertEqual(round(st.P.MPa, 5), 4.73599)

        # Selected point from Table 14, Pag 679, saturation states
        st = Ar(T=83.804, x=0.5, eq=3)
        self.assertEqual(round(st.P.MPa, 5), 0.06896)
        self.assertEqual(round(st.Liquido.rhoM, 3), 35.475)
        self.assertEqual(round(st.Liquido.hM.kJkmol, 1), -4835.9)
        self.assertEqual(round(st.Liquido.sM.kJkmolK, 2), 53.29)
        self.assertEqual(round(st.Liquido.cvM.kJkmolK, 2), 21.34)
        self.assertEqual(round(st.Liquido.cpM.kJkmolK, 2), 42.61)
        self.assertEqual(round(st.Liquido.w, 0), 853)
        self.assertEqual(round(st.Gas.rhoM, 5), 0.10154)
        self.assertEqual(round(st.Gas.hM.kJkmol, 1), 1701.4)
        self.assertEqual(round(st.Gas.sM.kJkmolK, 1), 131.3)
        self.assertEqual(round(st.Gas.w, 0), 209)

        st = Ar(T=90, x=0.5, eq=3)
        self.assertEqual(round(st.P.MPa, 5), 0.13361)
        self.assertEqual(round(st.Liquido.rhoM, 3), 34.538)
        self.assertEqual(round(st.Liquido.hM.kJkmol, 1), -4568.1)
        self.assertEqual(round(st.Liquido.sM.kJkmolK, 2), 56.35)
        self.assertEqual(round(st.Liquido.cvM.kJkmolK, 2), 20.59)
        self.assertEqual(round(st.Liquido.cpM.kJkmolK, 2), 43.49)
        self.assertEqual(round(st.Liquido.w, 0), 812)
        self.assertEqual(round(st.Gas.rhoM, 5), 0.18649)
        self.assertEqual(round(st.Gas.hM.kJkmol, 1), 1777.5)
        self.assertEqual(round(st.Gas.sM.kJkmolK, 2), 126.86)
        self.assertEqual(round(st.Gas.w, 0), 186)

        st = Ar(T=120, x=0.5, eq=3)
        self.assertEqual(round(st.P.MPa, 4), 1.2139)
        self.assertEqual(round(st.Liquido.rhoM, 3), 29.123)
        self.assertEqual(round(st.Liquido.hM.kJkmol, 1), -3138.4)
        self.assertEqual(round(st.Liquido.sM.kJkmolK, 2), 69.68)
        self.assertEqual(round(st.Liquido.cvM.kJkmolK, 2), 18.16)
        self.assertEqual(round(st.Liquido.cpM.kJkmolK, 2), 53.27)
        self.assertEqual(round(st.Liquido.w, 0), 587)
        self.assertEqual(round(st.Gas.rhoM, 4), 1.5089)
        self.assertEqual(round(st.Gas.hM.kJkmol, 1), 1917.7)
        self.assertEqual(round(st.Gas.sM.kJkmolK, 2), 111.81)
        self.assertEqual(round(st.Gas.cvM.kJkmolK, 2), 16.75)
        self.assertEqual(round(st.Gas.cpM.kJkmolK, 2), 36.15)
        self.assertEqual(round(st.Gas.w, 0), 182)

        st = Ar(T=149, x=0.5, eq=3)
        self.assertEqual(round(st.P.MPa, 4), 4.5560)
        self.assertEqual(round(st.Liquido.rhoM, 3), 18.235)
        self.assertEqual(round(st.Liquido.hM.kJkmol, 1), -911.4)
        self.assertEqual(round(st.Liquido.sM.kJkmolK, 2), 84.99)
        self.assertEqual(round(st.Liquido.cvM.kJkmolK, 2), 22.45)
        self.assertEqual(round(st.Liquido.cpM.kJkmolK, 2), 366.38)
        self.assertEqual(round(st.Liquido.w, 0), 218)
        self.assertEqual(round(st.Gas.rhoM, 3), 8.564)
        self.assertEqual(round(st.Gas.hM.kJkmol, 1), 718.6)
        self.assertEqual(round(st.Gas.sM.kJkmolK, 2), 95.93)
        self.assertEqual(round(st.Gas.cvM.kJkmolK, 2), 24.79)
        self.assertEqual(round(st.Gas.cpM.kJkmolK, 1), 472.2)
        self.assertEqual(round(st.Gas.w, 0), 173)

        # Table 15, Pag 684, Single phase points
        st = Ar(T=84, P=8e4, eq=3)
        self.assertEqual(round(st.rhoM, 3), 35.447)
        self.assertEqual(round(st.uM.kJkmol, 1), -4829.6)
        self.assertEqual(round(st.hM.kJkmol, 1), -4827.3)
        self.assertEqual(round(st.sM.kJkmolK, 2), 53.39)
        self.assertEqual(round(st.cvM.kJkmolK, 2), 21.31)
        self.assertEqual(round(st.cpM.kJkmolK, 2), 42.64)
        self.assertEqual(round(st.w, 0), 852)

        st = Ar(T=1200, P=8e4, eq=3)
        self.assertEqual(round(st.rhoM, 5), 0.00802)
        self.assertEqual(round(st.uM.kJkmol, 0), 14965)
        self.assertEqual(round(st.hM.kJkmol, 0), 24944)
        self.assertEqual(round(st.sM.kJkmolK, 2), 185.64)
        self.assertEqual(round(st.cvM.kJkmolK, 2), 12.47)
        self.assertEqual(round(st.cpM.kJkmolK, 2), 20.79)
        self.assertEqual(round(st.w, 0), 645)

        st = Ar(T=84, P=1e5, eq=3)
        self.assertEqual(round(st.rhoM, 3), 35.448)
        self.assertEqual(round(st.uM.kJkmol, 1), -4829.8)
        self.assertEqual(round(st.hM.kJkmol, 1), -4827.0)
        self.assertEqual(round(st.sM.kJkmolK, 2), 53.39)
        self.assertEqual(round(st.cvM.kJkmolK, 2), 21.31)
        self.assertEqual(round(st.cpM.kJkmolK, 2), 42.63)
        self.assertEqual(round(st.w, 0), 852)

        st = Ar(T=150, P=1.5e5, eq=3)
        self.assertEqual(round(st.rhoM, 5), 0.12154)
        self.assertEqual(round(st.uM.kJkmol, 1), 1845.3)
        self.assertEqual(round(st.hM.kJkmol, 1), 3079.4)
        self.assertEqual(round(st.sM.kJkmolK, 2), 137.02)
        self.assertEqual(round(st.cvM.kJkmolK, 2), 12.58)
        self.assertEqual(round(st.cpM.kJkmolK, 2), 21.23)
        self.assertEqual(round(st.w, 0), 227)

        st = Ar(T=1200, P=2e5, eq=3)
        self.assertEqual(round(st.rhoM, 5), 0.02004)
        self.assertEqual(round(st.uM.kJkmol, 0), 14964)
        self.assertEqual(round(st.hM.kJkmol, 0), 24945)
        self.assertEqual(round(st.sM.kJkmolK, 2), 178.02)
        self.assertEqual(round(st.cvM.kJkmolK, 2), 12.47)
        self.assertEqual(round(st.cpM.kJkmolK, 2), 20.79)
        self.assertEqual(round(st.w, 0), 645)

        st = Ar(T=100, P=5e5, eq=3)
        self.assertEqual(round(st.rhoM, 3), 32.937)
        self.assertEqual(round(st.uM.kJkmol, 1), -4133.5)
        self.assertEqual(round(st.hM.kJkmol, 1), -4118.3)
        self.assertEqual(round(st.sM.kJkmolK, 2), 60.98)
        self.assertEqual(round(st.cvM.kJkmolK, 2), 19.56)
        self.assertEqual(round(st.cpM.kJkmolK, 2), 45.42)
        self.assertEqual(round(st.w, 0), 744)

        st = Ar(T=116, P=1e6, eq=3)
        self.assertEqual(round(st.rhoM, 3), 29.967)
        self.assertEqual(round(st.uM.kJkmol, 1), -3380.9)
        self.assertEqual(round(st.hM.kJkmol, 1), -3347.5)
        self.assertEqual(round(st.sM.kJkmolK, 2), 67.97)
        self.assertEqual(round(st.cvM.kJkmolK, 2), 18.37)
        self.assertEqual(round(st.cpM.kJkmolK, 2), 50.98)
        self.assertEqual(round(st.w, 0), 621)

        st = Ar(T=130, P=2e6, eq=3)
        self.assertEqual(round(st.rhoM, 4), 2.5433)
        self.assertEqual(round(st.uM.kJkmol, 1), 1030.3)
        self.assertEqual(round(st.hM.kJkmol, 1), 1816.7)
        self.assertEqual(round(st.sM.kJkmolK, 2), 107.82)
        self.assertEqual(round(st.cvM.kJkmolK, 2), 17.89)
        self.assertEqual(round(st.cpM.kJkmolK, 2), 47.16)
        self.assertEqual(round(st.w, 0), 183)

        st = Ar(T=150, P=5e6, eq=3)
        self.assertEqual(round(st.rhoM, 3), 18.975)
        self.assertEqual(round(st.uM.kJkmol, 1), -1229.6)
        self.assertEqual(round(st.hM.kJkmol, 2), -966.09)
        self.assertEqual(round(st.sM.kJkmolK, 2), 84.46)
        self.assertEqual(round(st.cvM.kJkmolK, 2), 21.06)
        self.assertEqual(round(st.cpM.kJkmolK, 1), 209.4)
        self.assertEqual(round(st.w, 0), 245)

        st = Ar(T=100, P=1e7, eq=3)
        self.assertEqual(round(st.rhoM, 3), 33.825)
        self.assertEqual(round(st.uM.kJkmol, 1), -4265.2)
        self.assertEqual(round(st.hM.kJkmol, 1), -3969.5)
        self.assertEqual(round(st.sM.kJkmolK, 2), 59.62)
        self.assertEqual(round(st.cvM.kJkmolK, 2), 19.92)
        self.assertEqual(round(st.cpM.kJkmolK, 2), 42.91)
        self.assertEqual(round(st.w, 0), 802)

        st = Ar(T=310, P=5e7, eq=3)
        self.assertEqual(round(st.rhoM, 3), 16.752)
        self.assertEqual(round(st.uM.kJkmol, 1), 1583.6)
        self.assertEqual(round(st.hM.kJkmol, 1), 4568.4)
        self.assertEqual(round(st.sM.kJkmolK, 2), 98.28)
        self.assertEqual(round(st.cvM.kJkmolK, 2), 14.54)
        self.assertEqual(round(st.cpM.kJkmolK, 2), 32.29)
        self.assertEqual(round(st.w, 0), 519)

        st = Ar(T=106.75, P=1e8, eq=3)
        self.assertEqual(round(st.rhoM, 3), 37.796)
        self.assertEqual(round(st.uM.kJkmol, 1), -4623.9)
        self.assertEqual(round(st.hM.kJkmol, 1), -1978.1)
        self.assertEqual(round(st.sM.kJkmolK, 2), 54.71)
        self.assertEqual(round(st.cvM.kJkmolK, 2), 22.11)
        self.assertEqual(round(st.cpM.kJkmolK, 2), 36.10)
        self.assertEqual(round(st.w, 0), 1064)

        st = Ar(T=850, P=5e8, eq=3)
        self.assertEqual(round(st.rhoM, 3), 27.468)
        self.assertEqual(round(st.uM.kJkmol, 1), 8752.3)
        self.assertEqual(round(st.hM.kJkmol, 0), 26956)
        self.assertEqual(round(st.sM.kJkmolK, 2), 103.80)
        self.assertEqual(round(st.cvM.kJkmolK, 2), 15.18)
        self.assertEqual(round(st.cpM.kJkmolK, 2), 24.23)
        self.assertEqual(round(st.w, 0), 1304)

        st = Ar(T=253.52, P=1e9, eq=3)
        self.assertEqual(round(st.rhoM, 3), 45.826)
        self.assertEqual(round(st.uM.kJkmol, 1), -1222.0)
        self.assertEqual(round(st.hM.kJkmol, 0), 20600)
        self.assertEqual(round(st.sM.kJkmolK, 2), 62.61)
        self.assertEqual(round(st.cvM.kJkmolK, 2), 25.18)
        self.assertEqual(round(st.cpM.kJkmolK, 2), 33.75)
        self.assertEqual(round(st.w, 0), 1937)

        st = Ar(T=1200, P=1e9, eq=3)
        self.assertEqual(round(st.rhoM, 3), 32.059)
        self.assertEqual(round(st.uM.kJkmol, 0), 14382)
        self.assertEqual(round(st.hM.kJkmol, 0), 45575)
        self.assertEqual(round(st.sM.kJkmolK, 2), 105.67)
        self.assertEqual(round(st.cvM.kJkmolK, 2), 15.44)
        self.assertEqual(round(st.cpM.kJkmolK, 2), 23.57)
        self.assertEqual(round(st.w, 0), 1715)
