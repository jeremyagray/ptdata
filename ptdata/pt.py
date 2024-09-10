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

"""Periodic table data."""

import json
from pathlib import Path


def _load_dataset(fn=Path(__file__).resolve().parent / "nist_sp966.json"):
    """Load a dataset."""
    ds = {}
    with open(fn, "r") as f:
        ds = json.load(f)

    return ds


def _create_references(pt):
    """Create references in periodic table data.

    Create cross references in the periodic table dictionary by
    capitalized name, lowercase name, lowercase symbol, atomic number
    (as a string), and atomic number in addition to the default
    reference by symbol.

    Parameters
    ----------
    dict: pt
        The periodic table data dictionary using symbols only.

    Returns
    -------
    dict:
        The periodic table data dictionary.
    """
    for (
        k,
        v,
    ) in list(pt.items()):
        pt[v["name"]] = v
        pt[v["name"].lower()] = v
        pt[v["symbol"].lower()] = v
        pt[v["number"]] = v
        pt[int(v["number"])] = v

    return pt


pt = _create_references(_load_dataset())
