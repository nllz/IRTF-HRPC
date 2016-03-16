---
title: Human Rights Protocol Considerations - Research Report
docname: draft-doria-hrpc-report-01
date: 2016-03-16
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
  ins: A. Doria
  name: Avri Doria
  org: APC
  email: avri@apc.org

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
    target: http://www.un.org/en/documents/udhr/
 
  HRPC-GLOSSARY:
    title: Human Rights Protocol Considerations Glossary
    date: 2015
    author:
      - ins: N. ten Oever
      - ins: A. Doria
      - ins: D. K. Gillmor
    target: https://www.ietf.org/id/draft-dkg-hrpc-glossary-00.txt
 
  HRPC-Method:
    title: Human Rights Protocol Considerations Methodology
    date: 2015
    author:
      - ins: J. Varon
      - ins: C. Cath
    target: https://www.ietf.org/id/draft-varon-hrpc-methodology-00.txt

  Cath:
    title: A case study of codeing rights
    date: 2015
    author:
       - ins: C. Cath

  Clark:    
    title: The Design Philosophy of the DARPA Internet Protocols
    author:
      - ins: D. Clark
    seriesinfo: Proc SIGCOMM 88, ACM CCR Vol 18, Number 4, August
        1988, pp. 106-114.
    date: 1988

  Blumenthal:
    title: Rethinking the design of the Internet The end-to-end arguments vs. the brave new world
    author:
       - ins: M. Blumenthal
       - ins: D.D. Clark
    seriesinfo: ACM Transactions on Internet Technology, Vol. 1, No. 1, August 2001, pp 70-109.
    date: 2001

 
  Liddicoat:
    title: Human Rights and Internet Protocols
    author:
       - ins: J. Liddicoat
       - ins: A. Doria
    target: https://www.apc.org/en/pubs/human-rights-and-internet-protocols-comparing-proc
   
  Denardis:
    title: Protocol Politics
    author:
      - ins: L. Denardis
    date: 2013
   
  Netmundial:
    title: NETmundial Multistakeholder Statement
    date: 2014
    target:  http://netmundial.br/wp-content/uploads/2014/04/NETmundial-Multistakeholder-Document.pdf

  Post:
    title: Internet Infrastructure and IP Censorship
    author:
      - ins: D. Post
    date: 2015
    target:  http://www.ipjustice.org/digital-rights/internet-infrastructure-and-ip-censorship-bydavid-post/

  Zittrain:
    title: The Future of the Internet And How to Stop It
    date: 2008
    author:
      - ins: J. Zittrain

--- abstract

This document gathers the theoretical background for the HRPC as well as anoverview snapshot of the project to map engineering concepts at the protocol level that may be related to promotion and protection of the freedom of expression and association.

It is intended to provide the framework for reporting on the study, results and basic considerations. It will reference the detailed work being done in the Methodology draft as well as the work being done in the case studies. It also folds in discussions from the research literature. The documents, {{HRPC-Method}} and this document, form an interrelated set that may later be combined into a single document.

Discussion on this draft at: hrpc@irtf.org // https://www.irtf.org/mailman/admindb/hrpc

--- middle


Background
============

The recognition that human rights have a role in Internet policies has become part of the general discourse. Several reports from former United Nations (UN) Special Rapporteur on the promotion and protection of the right to freedom of opinion and expression, Frank La Rue, have made such relation explicit, which lead to the approval of the landmark resolution "on the promotion, protection and enjoyment of human rights on the Internet" at the UN Human Rights Council (HRC). And, more recently, to the resolution "The right to privacy in the digital age" at the UN General Assembly. The NETmundial outcome document {{Netmundial}} affirms that human rights, as reflected in the Universal Declaration of Human Rights {{UDHR}}, should underpin Internet governance principles.
Nevertheless, a direct relation between Internet Standards and human rights is still something to be explored and more clearly demonstrated.
Concerns for freedom of expression and association were a strong part of the world-view of the community involved in developing the first Internet protocols. Apparently, by intention or by coincidence, the Internet was designed with freedom and openness of communications as core values. But as the scale and the commercialization of the Internet has grown, the influence of such world-views had to compete with other values, such as ease of development and cost. The purpose of this research is to discover and document the consideration involved in taking human rights into account when creating protocols.
In a manner similar to the work done for RFC 6973 {{RFC6973}} on Privacy Consideration Guidelines, the premise of this research is that some standards and protocols can solidify, enable or threaten user rights.
As stated in RFC 1958 {{RFC1958}}, the Internet aims to be the global network of networks that provides unfettered connectivity to all users at all times and for any content. Open, secure and reliable connectivity is essential for rights such as freedom of expression and freedom of association, as defined in the Universal Declaration of Human Rights {{UDHR}}. Therefore, considering connectivity as the ultimate objective of the Internet, this makes a clear case that the Internet is not only an enabler of human rights, but that human rights lie at the basis of, and are ingrained in, the architecture of the network.
An essential part of maintaining the Internet as a tool for communication and connectivity is security. Indeed, "development of security mechanisms is seen as a key factor in the future growth of the Internet as a motor for international commerce and communication" RFC 1984 [RFC1984] and according to the Danvers Doctrine RFC 3365 {{RFC3365}}, there is an overwhelming consensus in the IETF that the best security should be used and standardized.
In RFC 1984 {{RFC1984}}, the Internet Architecture Board (IAB) and the Internet Engineering Steering Group (IESG), the bodies which oversee architecture and standards for the Internet, expressed: "concern by the need for increased protection of international commercial transactions on the Internet, and by the need to offer all Internet users an adequate degree of privacy." Indeed, the IETF has been doing a significant job in this area {{RFC6973}} {{RFC7258}}, considering privacy concerns as a subset of security concerns. {{RFC6973}}
Besides privacy, it should be possible to highlight other aspects of connectivity embedded in standards and protocols that can have human rights considerations. This report focuses on freedom of expression and the right to association and assembly online.

Terminology
============

The terminology being used in this project is defined in {{HRPC-Method}}.
The process of developing this glossary has involved taking the variety of glossaries defined by the IETF in its various RFCs, comparing the terms both among the various RFC definitions and with terminology for the Human Rights field to produced a synthesized set of definitions after discussion in the research group. The gola is to produce a set of terms, using existing terminology, that can assist clear discussion between engineering experts and human rights experts.
The glossary also includes the definitions of some complex terms, such as security and connectivity that relied of several of the other defined terms. The Methodology goes on to include basic Human rights in terms of the engineering terminology. For example from {{HRPC-Method}}

+ Right to Freedom of Expression builds on definitions of 
 - Connectivity
 - Privacy
 - Security
 - Content Agnosticism
 - Internationalization
 - Censorship resistance
 - Open Standards
 - Heterogeneity support

Link between protocols and human rights
=====================================
+ Include discussion of value laden engineering as discussed in {{Cath}}
+ Include discussion of  \"Values and Networks\" work by Roland Bless
+ Include discussion of principles from NetMundial Multistakeholder Statement

+ Right to Freedom of Assembly and Association builds on the definitions of:
 - Connectivity
 - Decentralization
 - Censorship Resistance
 - Pseudonimity 
 - Anonymity
 - Security


## Universal Declaration of Human Rights (UDHR) and Internet Architecture


This project is focused on two rights defined in the UDHR {{UDHR}}, Article 19 on Freedom of Expression and Article 20 of Freedom of Association.

Article 19
   :   Everyone has the right to freedom of opinion and expression; this right includes freedom to hold opinions without interference and to seek, receive and impart information and ideas through any media and regardless of frontiers.

Article 20
   :  1 Everyone has the right to freedom of peaceful assembly and association.
   :  2 No one may be compelled to belong to an association.


# Theory

When looking at protocols the considerations can apply from several perspectives.

+   The protocol's direct effects on human rights on the Internet.
-   The protocol's direct effect  on human rights in combination with other protocols
-   The effect of specific protocol elements, separately or in combination with other protocol elements on human rights on the Internet
-   The ability to determine when various effects are occurring, i.e. transparency
-   The effect of deployment or non deployment.  While this may be may seem beyond the protocol itself, often the design of protocol, its difficulty in implementation and the degree to which it contains required elements, poison pills or other protocol artifacts that either encourage or discourse implementation or deployment can be significant in the overall human rights affect of a protocol.

Several key pieces of researched are discussed in this section.  Readers/reviewers who have other recommended sources for relevant research that should be discussed in this document are invited to submit such for inclusion.

## Related research

This section will look at the theoretical work that has been done in the are of rights and protocols.  It will include the academic research on the topic including the work of David Post {{Post}}, Jonathan Zittrain {{Zittrain}} and Laura Denardis, among others.


In Protocol Politics {{Denardis09}} Denardis discusses "how values enter, or should enter, Internet protocol design." She describes the "IETF process itself self-consciously expresses certain values." The discussion goes on to define some examples of of IETF values, including:

+ "Universality and competitive openness - one objective of developing a standard is for it to become widely used in the marketplace;
- "participatory openness in the standards=setting process;
- "the end-to-end architectural design principle specifying that intelligence should be located at network end points rather than in media res."


To demonstrate the point, she presents a case study where engineers at the IETF "identified privacy as a value pertinent to IPv6 address design and embedded this design into design choices" with a detailed description of the issue of including Ethernet Addresses as part of the IPv6 address culminating in the design of IPv6 privacy features and changes.  Interestingly she also describes how the IETC engineering community was aware of the privacy challenges, the rights challenges, before media and government discovered the problem and where working on the problem before the fire firestorm began.

The description ended with the following: "this episode is a reminder that some of the most critical Internet governance questions concern individual civil liberties and that design decisions can present an opportunity to advance libertarian and democratic values or to contain these values.  IPv6 privacy design implications and value-conscious design choices reinforce the notion that Internet architecture and virtual resources cannot be understood only through the lens of technical efficiency, scarcity, or economic competition but as an embodiment of human values with social and cultural effects."

## Theory discussed in the research group

+ Value laden engineering as discussed in {{Cath}}

+ "Values and Networks" work by Roland Bless

+ Principles from NetMundial Multistakeholder Statement

NETmundial was a bell-weather event held in October 2014, where stakeholders from academia, business, civil society, governments came together to discuss Principles and a Roadmap for Internet governance.  While the Principles did not address protocol development specifically, they did include a principle on Open Standards:

"Internet governance should promote open standards, informed by individual and
collective expertise and decisions made by rough consensus, that allow for a global,
interoperable, resilient, stable, decentralized, secure, and interconnected network,
available to all. Standards must be consistent with human rights and allow
development and innovation." {{Netmundial}}

The NETmundial Roadmap on the other hand was a bit more specific on certain topics including digital security and arbitrary surveillance:

 - "Initiatives to improve cybersecurity and address digital security threats should
involve appropriate collaboration among governments, private sector, civil society,
academia and technical community. There are stakeholders that still need to
become more involved with cybersecurity, for example, network operators and
software developers."

 - "Mass and arbitrary surveillance undermines trust in the Internet and trust in
the Internet governance ecosystem. Collection and processing of personal data by
state and non-state actors should be conducted in accordance with international
human rights law. More dialogue is needed on this topic at the international level
using forums like the Human Rights Council and IGF aiming to develop a common
understanding on all the related aspects." {{Netmundial}}

# Methodology

The methodology is defined in detail in draft-varon-hrpc-methodology {{HRPC-Method}}.  

The purpose is to map the potential relation between human rights and protocols so that considerations can be derived.

+ the first step involved scoping the research problem
- Translating Human Rights Concept into Technical Definitions
  - Mapping protocols and standards related to Freedom of Expression and Freedom of Assembly as defined in human rights covenants and agreements
  - Extracting concepts from any and all RFCs that use and define these terms
  - Building the common glossary to be used linking engineering and human rights concepts
- Discovering cases of protocols that have an effect on human rights 
  - Enablers of rights
  - Enablers of abuse 
- Working though the cases to determine and describe the issues that affect human rights
- Applying the human rights technical definitions to the cases
- Derivation of possible considerations

## Case Studies

The case studies and their initial status is being documented in draft-varon-hrpc-methodology {{HRPC-Method}}.

In each of the case studies, the behavior of the protocols is analysed for its positive and negative effects.  In some case these effects are due to the design of the protocol itself, in others they are due to existing or absent features.

Initial versions of the analysis on the following protocols are currently being discussed on HRPC list and being describe in the methodology document.  

Additionally, discussion of the rights themselves and the evidence of these rights being implicits in the IETF design principles {{Clark}} and in some of the existing architecture and protocols, Cath and Liddicoat suggest other considerations.


+ IP

Covering issues concerning the network visibility of source and destination, address translation and mobility

+ DNS
- HTTP
  - HTTP code 451
- XMPP
- Peer to peer
- VPN
- Middleboxes
- DDOS


# Possible areas for protocol considerations

Using the definitions derived, for the the rights of freedom of expression and freedom of assembly, a set of questions can be developed that enable a protocol designer to consider whether their design has any positive or negative effects on these human rights.

{{HRPC-Method}} includes a first take on such questions.

## Emergent Issues/Questions

This records some of the question opened in discussion of the group that open broader questions that those centered on protocol considerations.  Often the question involved the manner in which the protocols are deployed or used.


+ Can DDOS be considered freedom of expression when used for advocacy?
+ Even if it does, does this matter?  Is interruption of communication in the Internet such a negative aspect that it is never acceptable? Is DDOS a moral equivalent to "capital" infractions in that its use is never permitted by Human Rights under any situation.
    
+ How do we differentiate between protocol effects that are inherent to the protocol and those that arise from implementation, misuse or from avoidance of non mandatory features. This includes factoring for lack of updating.

#  Next Steps


Once the first take at considerations are defined, what are the next steps for creating something that can be usable for protocol designers and implementers in considering freedom of expression and and freedom of association in their work.
Next Steps
============

Once the first take at consideration are defined, what are the next steps for creating something that can be sesable for protocol designers and implementers in considering freedom of expression and and freedom of association in their work.

Acknowledgement
===============

A section that include the many contributors of text as as commenters and those who are assisitng this project in existing.

IANA considerations
===================

There shouldn't be any.

Security Considerations
=======================

There shouldn't be any.


