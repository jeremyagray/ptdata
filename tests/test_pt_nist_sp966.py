# ******************************************************************************
#
# ptdata, periodic table data sets
#
# Copyright 2024 Jeremy A Gray <gray@flyquackswim.com>.
#
# All rights reserved.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# ******************************************************************************

"""NIST SP966 periodic table data tests."""

import ptdata


def test_all_symbol_data():
    """Should produce all hydrogen data."""
    assert ptdata.pt["H"]["symbol"] == "H"
    assert ptdata.pt["H"]["number"] == "1"
    assert ptdata.pt["H"]["name"] == "Hydrogen"
    assert ptdata.pt["H"]["ec"] == "1s1"
    assert ptdata.pt["H"]["ec_aufbau"] == "1s1"
    assert ptdata.pt["H"]["period"] == "1"
    assert ptdata.pt["H"]["mass_str"] == "1.008"
    assert ptdata.pt["H"]["mass"] == 1.008
    assert ptdata.pt["H"]["mass_approx"] is False
    assert ptdata.pt["H"]["mass_unit"] == "g mol^-1"
    assert ptdata.pt["H"]["ionization"] == 13.5984
    assert ptdata.pt["H"]["ionization_str"] == "13.5984"
    assert ptdata.pt["H"]["ionization_unit"] == "eV"


def test_all_keys():
    """Should produce hydrogen data from all keys."""
    assert ptdata.pt["h"] == ptdata.pt["H"]
    assert ptdata.pt["Hydrogen"] == ptdata.pt["H"]
    assert ptdata.pt["hydrogen"] == ptdata.pt["H"]
    assert ptdata.pt["1"] == ptdata.pt["H"]
    assert ptdata.pt[1] == ptdata.pt["H"]


def test_approximate_mass():
    """Should produce approximate masses."""
    assert ptdata.pt["Tc"]["mass"] == 97
    assert ptdata.pt["Tc"]["mass_approx"] is True


def test_missing_ionization():
    """Should indicate missing ionization energy."""
    assert ptdata.pt["Og"]["ionization"] is None
    assert ptdata.pt["Og"]["ionization_str"] is None
