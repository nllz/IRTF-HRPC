---
title: Human Rights Protocol Considerations Methodology
abbrev: hrpcm
docname: draft-dkg-hrpc-methodology
category: info

ipr: trust200902
area: General
workgroup: Human Rights Protocol Considerations Research Group
keyword: Internet-Draft

stand_alone: yes
pi:
  rfcedstyle: yes
  toc: yes
  tocindent: yes
  sortrefs: yes
  symrefs: yes
  strict: yes
  comments: yes
  inline: yes
  text-list-symbols: -o*+
author:
 -
       ins: J. Varron Ferraz
       name: Joana Varron Ferraz
       organization: Coding Rights
       email: joana@varonferraz.com
 -
       ins: C.J.N. Cath
       name: Corinne Cath
       organization: Oxford Internet Institute
       email: corinne.cath@oii.ox.ac.uk


normative:

informative:

   RFC1958:
   RFC1984:
   RFC2026:
   RFC2639:
   RFC2919:
   RFC3365:
   RFC5890:
   RFC5891:
   RFC5892:
   RFC5893:
   RFC6162:
   RFC6783:
   RFC6973:
   RFC7230:
   RFC7231:
   RFC7232:
   RFC7234:
   RFC7235:
   RFC7236:
   RFC7237:
   RFC7258:


   UDHR:
     title: The Universal Declaration of Human Rights
     date: 1948
     author:
        org: United Nations General Assembly
     target:  http://www.un.org/en/documents/udhr/

   HRPC-GLOSSARY:
     title: Human Rights Protocol Considerations Glossary
     date: 2015
     author:
        - ins: N. ten Oever
        - ins: A. Doria
        - ins: D. K. Gillmor



--- abstract

This document presents the methodology used to map between
concepts common in human rights discussions and engineering
discussions.  It is intended to facilitate work by the proposed Human
Rights Protocol Considerations research group, as well as other
authors within the IETF.


Decisive and human rights enabling characteristics of the Internet might be degraded if they're not properly defined, described and protected.  Not protecting these characteristics could result in (partial) loss of functionality and connectivity.

As stated in {{RFC1958}}, the Internet aims to be the global network of networks that provides unfettered connectivity to all users at all times and for any content. Open, secure and reliable connectivity is essential for rights such as freedom of expression and freedom of
association. Since the Internet's objective of connectivity makes it an enabler of human rights, its architectural design converges with the human rights framework.

Concerns for freedom of expression and association were a strong part of the world-view of the community involved in developing the first Internet protocols. The Internet was designed with freedom and openness of communications as core values. But as the scale and the
industrialization of the Internet has grown greatly, the influence of such world-views started to compete with other values.

While work has been done on privacy issues that should be considered when creating an Internet protocol, this ID is willing to frame a methodology to enable expose the relations between human rights and protocols and to provide guidelines to inform future protocol development and decision making where protocols impact the effective exercise of the rights to freedom of expression or association.

 Discussion on this draft at: hrpc@irtf.org


--- middle

Introduction
============

In a manner similar to the work done for {{RFC6973}} on Privacy Consideration Guidelines, the premise of this research is that some standards and protocols can solidify, enable or threaten human rights.

As stated in {{RFC1958}}, the Internet aims to be the global network of networks that provides unfettered connectivity to all users at all times and for any content.  Open, secure and reliable connectivity is essential for human rights such as freedom of expression and freedom of association, as defined in the Universal Declaration of Human Rights {{UDHR}}.  Therefore, considering connectivity as the ultimate objective of the Internet, this makes a clear case that the Internet is not only an enabler of human rights, but that human rights lie at the basis of, and are ingrained in, the architecture of the network.

An essential part of maintaining the Internet as a tool for communication and connectivity is security.  Indeed, "development of security mechanisms is seen as a key factor in the future growth of the Internet as a motor for international commerce and communication" {{RFC1984}} and according to the Danvers Doctrine {{RFC3365}}, there is an overwhelming consensus in the IETF that the best security should be used and standardized.

In {{RFC1984}}, the Internet Architecture Board (IAB) and the Internet Engineering Steering Group (IESG), the bodies which oversee architecture and standards for the Internet, expressed: "concern by the need for increased protection of international commercial transactions on the Internet, and by the need to offer all Internet users an adequate degree of privacy."  Indeed, the IETF has been doing a significant job in this area {{RFC6973}} {{RFC7258}}, considering privacy concerns as a subset of security concerns.

Besides privacy, it should be possible to highlight other aspects of connectivity embedded in standards and protocols that can have human rights considerations, such as freedom of expression and the right to association and assembly online.

 This ID is working to develop a methodology that enables us to extract these considerations.

To move this debate further, information has been compiled at the https://trac.tools.ietf.org/ (FIXME: figure out what is our trac) and discussions are happening through the list hrpc@irtf.org


Research Topic
==============

The growing impact of the Internet on the lives of individuals makes Internet standards and protocols increasingly important to society. The IETF itself, in {{RFC2026}}, specifically states that the ‘interests of the Internet community need to be protected’.

There are various examples of protocols and standards having a direct impact on society, and by extension the human rights of end-users. Privacy is but one example, but other rights, such as the right to freedom of expression and association can also be considered.

According to the Universal Declaration of Human Rights:
Freedom of Expression - Article 19
Everyone has the right to freedom of opinion and expression; this right includes freedom to hold opinions without interference and  to seek, receive and impart information and ideas through any  media and regardless of frontiers.

Freedom of Association - Article 20
Everyone has the right to freedom of peaceful assembly and association.

Protocol and Standard Examples related to FoE and FoA
-----------------------------------------------------

Below just several examples of the potential link between protocols, standards and FoA and FoE will be presented.


HTTP
Websites made it extremely easy for individuals to publish their ideas, opinions and thoughts.  Never before has the world seen an infrastructure that made it this easy to share information and ideas with such a large group of other people.  The HTTP architecture and standards, including {{RFC7230}}, {{RFC7231}}, {{RFC7232}}, {{RFC7234}}, {{RFC7235}}, {{RFC7236}}, and {{RFC7237}}, are essential for the publishing of information.  The HTTP protocol, therefore, forms an crucial enabler for freedom of expression, but also for the right to freely participate in the culture life of the community (Article 27) {{UDHR}}, to enjoy the arts and to share in scientific advancement and its benefits.


Real time communications through XMPP and WebRTC
Collaborations and cooperation via the Internet have take a large step forward with the progress of chat and other other real time communications protocols.  The work on XMPP {{RFC6162}} has enabled new methods of global interactions, cooperation and human right advocacy.  The WebRTC work being done to standardize the API and protocol elements to support real-time communications for browsers, mobile applications and IoT by the World Wide Consortium (W3C) and the IETF is another artifact enabling human rights globally on the Internet.

Mailing lists
Collaboration  and cooperation have been part of the Internet since its early  beginning, one of the instruments of facilitating working together in  groups are mailing lists (as described in {{RFC2639}}, {{RFC2919}}, and {{RFC6783}}.  Mailing lists are critical  instruments and enablers for group communication and organization, and  therefore form early artifacts of the (standardized) ability of Internet standards to enable the right to freedom of assembly and association.


IDNs
English has been the lingua franca of the Internet, but for many Internet user English is not their first language.  To have a true global Internet, one that serves the whole world, it would need to reflect the languages of these different communities.  The Internationalized Domain Names IDNA2008 ({{RFC5890}}, {{RFC5891}}, {{RFC5892}}, and {{RFC5893}}), describes standards for the use of a broad range of strings and characters (some also written from right to left).  This enables users who use other characters than the standard LDH ascii typeset to have their own URLs.  This shows the ambition of the Internet community to reflect the diversity of users and to be in line with Article 2 of the Universal Declaration of Human Rights which clearly stipulates that "everyone is entitles to all rights and freedoms `[...]`, without distinction of any kind, such as `[...]` language `[...]`." {{UDHR}}

Current research questions
--------------------------

What are the relationships between protocols and human rights, especially freedom of expression and assembly?

How to talk about human rights in an engineering context?

Can we translate human rights terminology into Internet architecture technical terms?


Methodology
===========

Mapping the relation between human rights and protocols and architectures is a new research challenge, which requires a good amount of cross organizational cooperation to develop a consistent  methodology.  While the authors of this first draft are involved in  both human rights advocacy and research on Internet technologies - we believe that bringing this work into the IRTF facilitates and  improves this work by bringing human rights experts together with the  community of researchers and developers of Internet standards and technologies.

In order to map the potential relation between human rights and protocols, the IRTF research group gathered the data informing this research from three specific venues:

a. Discourse analysis of RFCs
To start addressing the issue, a mapping exercise analyzing Internet architecture and protocols features, vis-a-vis possible impact on human rights is being undertaken. Therefore, research on the language used in current and historic RFCs and mailing list discussions is underway to expose core architectural principles, language and deliberations on human rights of those affected by the network.

b. Elite-Interviews with IETF participants at Dallas meeting March 2015
Interviews with the current and past members of the Internet Architecture Board (IAB), current and past members of the Internet Engineering Steering Group(IESG) and chairs of selected working groups and RFC authors. To get an insider understanding of how they view the relationship (if any) between human rights and protocols to play out in their work.

c. Participant observation in Working Groups
By participating in various working groups information was gathered about the IETFs day-to-day work. From which which general themes and use-cases about human rights and protocols were extracted.


All this data was then processed using the following three consecutive strategies:

Translating Human Rights Concept into Technical Definitions
-----------------------------------------------------------

Step 1.1 - Mapping protocols and standards related to FoE and FoA
Action: Mapping of protocols and standards that potentially enable the internet as a tool for freedom of expression
Expected Outcome: list of RFCs that describe standards and protocols that are potentially more closely related to FoE and FoA.

Step 1.2 - Extracting concepts from mapped RFCs
Activity: Read the selected RFCs to highlight central design and technical concepts which impact human rights.
Expected Outcome 1:  a list of  technical terms that combined create the enabling environment for human rights, such a freedom of expression and freedom of association.
Expected Outcome 2: Translating human rights to technical terms.

Step 1.3 - Building a common glossary
In the analysis of existing RFCs central design and technical concepts shall be found which impact human rights.
Expected Outcome:  list of concepts and definitions of technical concepts

Mapping cases of protocols being exploited
------------------------------------------

Activity: Map cases in which users rights have been exploited, violated or compromised, analyze which protocols or vulnerabilities in protocols are key to this.

Expected Outcome: list of protocols that have been exploited to expose users to rights violation.
Violations in this case being defined as:
- Unlawful monitoring
- Deterioration of connectivity (to the network or specific services)
- Non-transparent

Applying technical definitions to the mapped cases of protocol exploitation
---------------------------------------------------------------------------

Activity: Understand technical rational for the use of particular protocols that undermine human rights. Investigate alternative technical options from within list of technical design principle (see {{HRPC-GLOSSARY}}) that have been found to strengthen our technical definition of FoE and FoA, and hence human rights and connectivity of the network, .

Expected Outcome:
Identifying best (and worst) practices. Develop procedures to systematically evaluate protocols for potential human rights impact.



Preliminary Findings
====================

Translating Human Rights Concept into Technical Definitions
Step 1.1 - Mapping protocols and standards related to FoE and FoA
Current Status: A raw list of RFCs that describe standards and protocols that are potentially related to FoE and FoA.
https://github.com/nllz/IRTF-HRPC/blob/master/RFC%20overview.ods

Step 1.2 - Extracting concepts from mapped RFCs
Current Status: Expected Outcome 1:  a list of  technical terms that combined create the enabling environment for human rights, such a freedom of expression and freedom of association.

      Architectural principles                    Enabling features
        and characteristics                        for user rights

                       /------------------------------------------------\
                       |                                                |
     +=================|=============================+                  |
     =                 |                             =                  |
     =                 |           End to end        =                  |
     =                 |          Reliability        =                  |
     =                 |           Resilience        =  Access as       |
     =                 |        Interoperability     =   Human Right    |
     =    Good enough  |          Transparency       =                  |
     =     principle   |       Data minimization     =                  |
     =                 |  Permissionless innovation  =                  |
     =                 |     Graceful degradation    =                  |
     =                 |          Connectivity       =                  |
     =                 |                             =                  |
     =                 \------------------------------------------------/
     =                                               =
     +===============================================+

Current status: Expected Outcome 2: Translating human rights to technical terms. This analysis points to translating the concept of freedom of expression as follows:

                             +--
                             |  content agnosticism
     freedom of expression = |  connectivity
                             |  privacy
                             |  security
                             +--

Step 1.3 - Build a common glossary
Current status: a first list of concepts, which definitions should be improved and further aligned with existing RFCs, is being publish as ID: []



Protecting human rights - in paticular FoA and FoE- can be seen as a form of security.       Security is about the ability to robustly deal with attacks that  undermine the fundamental functioning of the network. One of the central  aims of the network is to enable connectivity.  Assuring  that FoA and  FoE are protected strengthens connectivity,  increases  trust   in  the  network, and hence provides an additional type of security to the network.


Future research questions
=========================

All of the steps taken above raise the following question that need to be in addressed after the research outlined above has been completed:

How can the rights enabling environment be safeguarded in (future) protocol development?

How  can (nontransparent) human rights violations be minimized in (future)  protocol development?

Can we propose guidelines to protect the Internet  as a human-rights-enabling environment in future protocol development,  specially in relation to freedom of expression and freedom of  association, in a manner similar to the work done for Privacy  Considerations in {{RFC6973}}?

Assuming that the research produces useful results, the objective  will evolve into the creation of a set of recommended considerations for the protection of applicable human rights.



