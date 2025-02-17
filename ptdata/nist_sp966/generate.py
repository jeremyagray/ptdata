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

"""Generate NIST SP966 JSON file."""

import csv
import json
import re

shells = {
    1: ("1s",),
    2: (
        "2s",
        "2p",
    ),
    3: (
        "3s",
        "3p",
    ),
    4: (
        "4s",
        "3d",
        "4p",
    ),
    5: (
        "5s",
        "4d",
        "5p",
    ),
    6: (
        "6s",
        "4f",
        "5d",
        "6p",
    ),
    7: (
        "7s",
        "5f",
        "6d",
        "7p",
    ),
}


def _load_nist_sp966():
    """Load the NIST SP966 periodic table data."""
    files = [
        "names.csv",
        "symbols.csv",
        "ec.csv",
        "ec_aufbau.csv",
        "ionization.csv",
        "mass.csv",
    ]

    data = {}

    # Load data.
    for file in files:
        with open(file, "r") as f:

            data[file.removesuffix(".csv")] = []

            # Detect CSV dialect and reset file object.
            sniffer = csv.Sniffer()
            dialect = sniffer.sniff(f.readline())
            f.seek(0)

            # Read CSV file and process data.
            reader = csv.reader(f, dialect)
            next(reader)

            for row in reader:
                data[file.removesuffix(".csv")].append(row[1])

    pt = {}

    for num, symbol in enumerate(data["symbols"], 1):
        pt[symbol] = {
            "symbol": str(symbol),
            "number": str(num),
            "name": str(data["names"][num - 1]),
            "ec": str(data["ec"][num - 1]),
            "ec_aufbau": str(data["ec_aufbau"][num - 1]),
        }

        mass = re.match(r"\[([0-9]+)\]", data["mass"][num - 1])

        if mass:
            pt[symbol]["mass_str"] = str(mass.groups()[0])
            pt[symbol]["mass"] = int(mass.groups()[0])
            pt[symbol]["mass_approx"] = True
        else:
            pt[symbol]["mass_str"] = str(data["mass"][num - 1])
            pt[symbol]["mass"] = float(data["mass"][num - 1])
            pt[symbol]["mass_approx"] = False

        pt[symbol]["mass_unit"] = "g mol^-1"

        ionization = data["ionization"][num - 1]

        if ionization == "NaN":
            pt[symbol]["ionization"] = None
            pt[symbol]["ionization_str"] = None
        else:
            pt[symbol]["ionization"] = float(ionization)
            pt[symbol]["ionization_str"] = ionization

        pt[symbol]["ionization_unit"] = "eV"

    return pt


def _generate_pt_json(pt):
    """Generate the JSON PT data."""
    with open("nist_sp966.json", "w") as f:
        json.dump(pt, f, indent=2)


if __name__ == "__main__":
    pt = _load_nist_sp966()
    _generate_pt_json(pt)
