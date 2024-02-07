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

python-modules = ptdata
python-files =

.PHONY : test-all
test-all:
	pytest --doctest-modules --doctest-glob='*.rst' -vvvv --cov ptdata --cov-report term --cov-report html

.PHONY : build
build : docs
	pip install -q build
	python -m build

.PHONY : clean
clean :
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	cd docs && make clean

.PHONY : dist
dist : clean build

.PHONY : docs
docs :
	cd docs && make html

.PHONY : commit
commit :
	pre-commit run --all-files

.PHONY : lint
lint :
	flake8 --exit-zero $(python-modules) $(python-files)
	isort --check $(python-modules) $(python-files) || exit 0
	black --check $(python-modules) $(python-files)

.PHONY : lint-fix
lint-fix :
	isort $(python-modules) $(python-files)
	black $(python-modules) $(python-files)

.PHONY : test
test :
	pytest --doctest-modules --doctest-glob='*.rst'

.PHONY : upload
upload :
	python3 -m twine upload --verbose dist/*

.PHONY : upload-test
upload-test :
	python3 -m twine upload --verbose --repository testpypi dist/*
