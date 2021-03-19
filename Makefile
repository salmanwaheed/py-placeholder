# https://devhints.io/makefile

clean:
	find . -type d -name '*pycache*' -exec rm -rf '{}' +
	find . -type f -name '*.pyc*' -exec rm -rf '{}' +

