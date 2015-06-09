draft-glossary.html: draft-glossary.xml
	xml2rfc $< --html

draft-glossary.xml: draft-glossary.md
	kramdown-rfc2629 $< >$@

draft-glossary.txt: draft-glossary.xml
	xml2rfc $< --text
