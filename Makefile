# NOTE: the first target of a makefile executed when ``make`` is
# executed without arguments.
# It was deliberately named "default" here but could be any name.
# Also feel free to modify it to execute a custom command.
#
#
default: dependencies tests docs

dependencies:
	pip install -q -U pip --no-cache-dir
	pip install -q -r development.txt

develop:
	python setup.py develop

tests: unit functional

unit:
	nosetests tests/unit --cover-erase # let's clear the test coverage report during unit tests only

functional:
	nosetests tests/functional

docs:
	cd docs && make html

release:
	@rm -rf dist/*
	@./.release
	@make pypi

pypi:
	@python setup.py build sdist
	@twine upload dist/*.tar.gz

clean:
	@find . -type f -name '*.pyc' -exec rm -fv {} \;
	@rm -rfv docs/build dist *egg-info*

# tells "make" that the target "make docs" is phony, meaning that make
# should ignore the existence of a file or folder named "docs" and
# simply execute commands described in the target
.PHONY: docs
