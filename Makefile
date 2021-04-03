# -*- Makefile -*-

codestyle:
	- flake8 . 2>&1 | sed "s,.*,$/`echo "\033[33m"`&$/`echo "\033[0m"`,"

check_imports:
	- isort -c . 2>&1 | sed "s/ERROR:/$/`echo "\033[31mERROR:\033[0m"`/g"

fix_imports:
	isort .

test:
	python manage.py test 2>&1 | sed -e "s/FAILED/$/`echo "\033[31mFAILED\033[0m"`/g"

coverage:
	./run_coverage.sh

precommit:
	make check_imports
	make codestyle
	make test
