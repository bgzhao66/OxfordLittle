SHELL:=/bin/bash

all:
	# Generate HTML files from Markdown files
	for i in {a..z}; do \
		node ../../examples/scripts/md2html.js ../$$i.md; \
	done
	mv ../*.html .

.PHONY:
clean:
	rm -f *.html

.PHONY:
prepare:
	xargs -n 1 npm install --prefix ../scripts < ../scripts/dependencies.txt
