# ******************************************************************************
#
# ptdata, periodic table data sets
#
# Copyright 2024-2025 Jeremy A Gray <gray@flyquackswim.com>.
#
# All rights reserved.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# ******************************************************************************

"""Periodic table data."""

import json
from pathlib import Path

GROUP_ONE = (
    1,
    3,
    11,
    19,
    37,
    55,
    87,
)
GROUP_TWO = (
    4,
    12,
    20,
    38,
    56,
    88,
)
GROUP_THREE = (
    21,
    39,
)
GROUP_FOUR = (
    22,
    40,
    72,
    104,
)
GROUP_FIVE = (
    23,
    41,
    73,
    105,
)
GROUP_SIX = (
    24,
    42,
    74,
    106,
)
GROUP_SEVEN = (
    25,
    43,
    75,
    107,
)
GROUP_EIGHT = (
    26,
    44,
    76,
    108,
)
GROUP_NINE = (
    27,
    45,
    77,
    109,
)
GROUP_TEN = (
    28,
    46,
    78,
    110,
)
GROUP_ELEVEN = (
    29,
    47,
    79,
    111,
)
GROUP_TWELVE = (
    30,
    48,
    80,
    112,
)
GROUP_THIRTEEN = (
    5,
    13,
    31,
    49,
    81,
    113,
)
GROUP_FOURTEEN = (
    6,
    14,
    32,
    50,
    82,
    114,
)
GROUP_FIFTEEN = (
    7,
    15,
    33,
    51,
    83,
    115,
)
GROUP_SIXTEEN = (
    8,
    16,
    34,
    52,
    84,
    116,
)
GROUP_SEVENTEEN = (
    9,
    17,
    35,
    53,
    85,
    117,
)
GROUP_EIGHTEEN = (
    2,
    10,
    18,
    36,
    54,
    86,
    118,
)


def _load_dataset(fn=Path(__file__).resolve().parent / "nist_sp966.json"):
    """Load a dataset."""
    ds = {}
    with open(fn, "r") as f:
        ds = json.load(f)

    return ds


def _assign_groups(pt):
    """Assign elements to their correct groups."""
    for k, ele in pt.items():
        if int(ele["number"]) in GROUP_ONE:
            ele["group"] = 1
        elif int(ele["number"]) in GROUP_TWO:
            ele["group"] = 2
        elif int(ele["number"]) in GROUP_THREE:
            ele["group"] = 3
        elif int(ele["number"]) in GROUP_FOUR:
            ele["group"] = 4
        elif int(ele["number"]) in GROUP_FIVE:
            ele["group"] = 5
        elif int(ele["number"]) in GROUP_SIX:
            ele["group"] = 6
        elif int(ele["number"]) in GROUP_SEVEN:
            ele["group"] = 7
        elif int(ele["number"]) in GROUP_EIGHT:
            ele["group"] = 8
        elif int(ele["number"]) in GROUP_NINE:
            ele["group"] = 9
        elif int(ele["number"]) in GROUP_TEN:
            ele["group"] = 10
        elif int(ele["number"]) in GROUP_ELEVEN:
            ele["group"] = 11
        elif int(ele["number"]) in GROUP_TWELVE:
            ele["group"] = 12
        elif int(ele["number"]) in GROUP_THIRTEEN:
            ele["group"] = 13
        elif int(ele["number"]) in GROUP_FOURTEEN:
            ele["group"] = 14
        elif int(ele["number"]) in GROUP_FIFTEEN:
            ele["group"] = 15
        elif int(ele["number"]) in GROUP_SIXTEEN:
            ele["group"] = 16
        elif int(ele["number"]) in GROUP_SEVENTEEN:
            ele["group"] = 17
        elif int(ele["number"]) in GROUP_EIGHTEEN:
            ele["group"] = 18

    return pt


def _assign_periods(pt):
    """Assign elements to their correct periods."""
    for k, ele in pt.items():
        if int(ele["number"]) <= 2:
            ele["period"] = 1
        elif int(ele["number"]) <= 10:
            ele["period"] = 2
        elif int(ele["number"]) <= 18:
            ele["period"] = 3
        elif int(ele["number"]) <= 36:
            ele["period"] = 4
        elif int(ele["number"]) <= 54:
            ele["period"] = 5
        elif int(ele["number"]) <= 86:
            ele["period"] = 6
        elif int(ele["number"]) <= 118:
            ele["period"] = 7
        else:
            raise ValueError("Discovered a new element, have we?")

    return pt


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


pt = _create_references(_assign_groups(_assign_periods(_load_dataset())))
