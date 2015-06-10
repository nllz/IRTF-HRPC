# IRTF-HRPC
This is the repository for the Internet Research Taskforce (IRTF) Human Rights Protocol Consideration (hrpc) Research Group.

We're currently experimenting with how we're managing version control of the documents produced by and for the proposed research group. We're currently using the mailinglist [0] etherpads [1] and ethercalc [2] and this repository. We hope to have a trac installation on the IETF site soon. 

[0] https://www.irtf.org/mailman/listinfo/hrpc

[1] https://hrpc.etherpad.mozilla.org/

[2] https://www.ethercalc.org/tdeh4wx2zo


Building drafts for HRPC
========================

Install dependencies:

      # apt install kramdown-rfc2629 xml2rfc

Draft editing workflow:

      $EDITOR draft-glossary.md
      make
