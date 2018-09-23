#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Generate the MEoS-*.rst files with list of references

import os

import lib


# Generate index file
txt = "lib.mEoS"
txt += os.linesep + "========" + os.linesep + os.linesep
txt += "The list of available fluid with high quality multiparameter equations"
txt += " is automatically updated here:" + os.linesep + os.linesep
txt += ".. toctree::" + os.linesep + os.linesep
for mod in lib.mEoS.__all__:
    txt += "    lib.mEoS.%s" % mod.__name__
    txt += os.linesep

with open("docs/lib.mEoS.rst", "w") as file:
    file.write(txt)


# Generate the individual compounds files
for mod in lib.mEoS.__all__:
    txt = "lib.mEoS.%s" % mod.__name__
    txt += os.linesep + "="*len(txt) + os.linesep + os.linesep

    # Section for fluid info
    txt += "Fluid info" + os.linesep
    txt += "----------" + os.linesep + os.linesep
    txt += "* CAS Number: " + mod.CASNumber + os.linesep
    txt += "* Formula: " + mod.formula + os.linesep
    if mod.synonym:
        txt += "* Synonym: " + mod.synonym + os.linesep

    txt += "* Molecular weigth: %s g/mol" % mod.M + os.linesep
    txt += "* Tc: " + mod.Tc.str + os.linesep
    txt += "* Pc: " + mod.Pc.str + os.linesep
    txt += "* ρc: " + mod.rhoc.str + os.linesep
    txt += "* Tt: " + mod.Tt.str + os.linesep
    txt += "* Tb: " + mod.Tb.str + os.linesep
    txt += "* Acentric factor: %s" % mod.f_acent + os.linesep

    txt += "Equation of state" + os.linesep
    txt += "-----------------" + os.linesep + os.linesep
    for eq in mod.eq:
        rf = eq["__doi__"]
        txt += "* %s; %s. %s" % (rf["autor"], rf["title"], rf["ref"])
        if rf["doi"]:
            txt += ", http://dx.doi.org/%s" % rf["doi"]
        txt += os.linesep
    txt += os.linesep + os.linesep

    if mod._viscosity:
        txt += "Viscosity" + os.linesep
        txt += "---------" + os.linesep + os.linesep
        for eq in mod._viscosity:
            rf = eq["__doi__"]
            txt += "* %s; %s. %s" % (rf["autor"], rf["title"], rf["ref"])
            if rf["doi"]:
                txt += ", http://dx.doi.org/%s" % rf["doi"]
            txt += os.linesep

    if mod._thermal:
        txt += "Thermal Conductivity" + os.linesep
        txt += "--------------------" + os.linesep + os.linesep
        for eq in mod._thermal:
            rf = eq["__doi__"]
            txt += "* %s; %s. %s" % (rf["autor"], rf["title"], rf["ref"])
            if rf["doi"]:
                txt += ", http://dx.doi.org/%s" % rf["doi"]
            txt += os.linesep

    imageFname = "docs/images/%s.png" % mod.__name__
    if os.path.isfile(imageFname):
        txt += os.linesep + "Calculation example" + os.linesep
        txt += "-------------" + os.linesep
        txt += os.linesep + os.linesep
        txt += "Using the default option for equation of state, viscosity and"
        txt += " thermal conductivity we can get this diagram plots:"
        txt += os.linesep + os.linesep
        txt += ".. image:: images/%s.png" % mod.__name__
        txt += os.linesep + os.linesep

    with open("docs/lib.mEoS.%s.rst" % mod.__name__, "w") as file:
        file.write(txt)
