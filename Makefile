DRAFTS = glossary
OUTPUTS = $(foreach draft,$(DRAFTS),draft-${draft}.html draft-${draft}.xml draft-${draft}.txt)

all: $(OUTPUTS)

clean:
	rm -f $(OUTPUTS)

draft-%.html: draft-%.xml
	xml2rfc $< --html

draft-%.xml: draft-%.md
	kramdown-rfc2629 $< >$@

draft-%.txt: draft-%.xml
	xml2rfc $< --text

.PHONY: all clean
