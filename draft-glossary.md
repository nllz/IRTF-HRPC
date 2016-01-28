--- 
title: Human Rights Protocol Considerations Glossary
abbrev: hrpcg
docname: draft-dkg-hrpc-glossary-01
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
       ins: D. K. Gillmor
       name: Daniel Kahn Gillmor
       organization: ACLU
       email: dkg@fifthhorseman.net
-
       ins: N. ten Oever
       name: Niels ten Oever
       organization: Article19
       email: niels@article19.org
- 
       ins: A. Doria
       name: Avri Doria
       organization: APC
       email: avri@apc.org


normative:
  
informative: 
   RFC0226:
   RFC0760:
   RFC0791:
   RFC0793:
   RFC1122:
   RFC1958:
   RFC2277:
   RFC2606:	
   RFC2775:
   RFC3724:
   RFC4084:
   RFC4949:
   RFC6365:
   RFC6973:


   UDHR:
     title: The Universal Declaration of Human Rights
     date: 1948
     author:
        org: United Nations General Assembly
     target:  http://www.un.org/en/documents/udhr/

   ICCPR:
     title: International Covenant on Civil and Political Rights
     date: 1976
     author:
        org: United Nations General Assembly
     target: http://www.ohchr.org/EN/ProfessionalInterest/Pages/CCPR.aspx
   
   Berners-Lee:
     title: Weaving the Web,
     author:
       - ins: T. Berners-Lee
       - ins: M. Fischetti
     seriesinfo:
       HarperCollins: p 208
     date: 1999

   Saltzer:
     title: End-to-End Arguments in System Design
     author: 
       - ins: J.H. Saltzer
       - ins: D.P. Reed
       - ins: D.D. Clark
     seriesinfo: ACM TOCS, Vol 2, Number 4, November
        1984, pp 277-288.
     date: 1984

   Clark:     
     title: The Design Philosophy of the DARPA Internet Protocols
     author:
       - ins: D. Clark
     seriesinfo: Proc SIGCOMM 88, ACM CCR Vol 18, Number 4, August
        1988, pp. 106-114.
     date: 1988

   Blumenthal:
     title: "Rethinking the design of the Internet: The end-to-end arguments vs. the brave new world"
     author:
       - ins: M. Blumenthal
       - ins: D.D. Clark
     seriesinfo: ACM Transactions on Internet Technology, Vol. 1, No. 1, August 2001, pp 70-109.
     date: 2001

   WP-Stateless:
     title: Stateless protocol
     target: https://en.wikipedia.org/wiki/Stateless_protocol

   WP-Debugging:
     title: Debugging
     target: https://en.wikipedia.org/wiki/Debugging

   ID:
     title: Proposal for research on human rights protocol considerations
     date: 2015
     author:
        - ins: N. ten Oever
        - ins: A. Doria
        - ins: J. Varon
     target: http://tools.ietf.org/html/draft-doria-hrpc-proposal 

   FIArch:
     title: Future Internet Design Principles
     date: January 2012
     target: http://www.future-internet.eu/uploads/media/FIArch_Design_Principles_V1.0.pdf

   Elahi:
     title: "CORDON - A taxonomy of Internet Censorship Resistance Strategies"
     author:
        - ins: T. Elahi
        - ins: I. Goldberg
     target: http://cacr.uwaterloo.ca/techreports/2012/cacr2012-33.pdf
     date: 2012

   Brown:
     title: "A Prehistory of Internet Governance"
     date: 2013
     author:
        - ins: I. Brown
        - ins: M. Ziewitz
     seriesinfo: Research Handbook on Governance of the Internet. Cheltenham, Edward Elgar.

   FRAMEWORK:
     title: Information technology - Framework for internationalization, prepared by ISO/IEC JTC 1/SC 22/WG 20 ISO/IEC TR 11017
     date: 1997
     author:
        - ins: ISO/IEC

   W3Ci18nDef:
     title: Localization vs. Internationalization
     date: 2010
     author:
        - ins: W3C
     target: http://www.w3.org/International/questions/qa-i18n.en


--- abstract

This document presents a glossary of terms used to map between
concepts common in human rights discussions and engineering
discussions.  It is intended to facilitate work by the proposed Human
Rights Protocol Considerations research group, as well as other
authors within the IETF.

--- middle


Introduction
============

    "There's a freedom about the Internet: As long as we accept the
       rules of sending packets around, we can send packets containing
       anything to anywhere."

{{Berners-Lee}}

The Human Rights Protocol Consideration Proposed Research Group aims
to research whether standards and protocols can enable, strengthen or
threaten human rights, as defined in the Universal Declaration of
Human Rights {{UDHR}} and the International Covenant ons Civil and
Political Rights {{ICCPR}}, specifically, but not limited to the
right to freedom of expression and the right to freedom of assembly.

Comunications between people working on human rights and engineers
working on Internet protocols can be improved with a shared vocabulary.

This document aims to provide a shared vocabulary to facilitate
understanding of the intersection between human rights and Internet
protocol design.

Discussion on this draft at: hrpc@irtf.org // https://www.irtf.org/mailman/admindb/hrpc

This document builds on the previous IDs published within the framework of the proposed hrpc research group {{ID}}

Glossary
========

In the analysis of existing RFCs central design and technical concepts have been found which impact human rights.  This is an initial glossary of concepts that could bridge human rights discourse and technical vocabulary. These definitions should be improved and further aligned with existing RFCs.

Accessibility
: Full Internet Connectivity as described in {{RFC4084}} to provide unfettered access to the Internet 

: The design of protocols, services or implementation that provide an enabling environment for people with disabilities.

: The ability to receive information available on the Internet

Anonymity
: The condition of an identity being unknown or concealed. {{RFC4949}}

Anonymous
: A state of an individual in which an observer or attacker cannot identify the individual within a set of other  individuals (the anonymity set). {{RFC6973}}

Authenticity
: The fact that the data does indeed come from the source it claims to come from. (It is strongly linked with Integrity, see below).

Censorship resistance
: Methods and measures to prevent Internet censorship.

Confidentiality
: The non-disclosure of information to any unintended person or host or party

Connectivity
: The extent to which a device or network is able to reach other devices or networks to exchange data. The Internet is the tool for providing global connectivity {{RFC1958}}. 

Content-agnosticism
: Treating network traffic identically regardless of content.

Debugging
: Debugging is a methodical process of finding and reducing the number of bugs, or defects, or malfunctions in a protocol or its implementation, thus making it behave as expected and analyse the consequences that might have emanated from the error. Debugging tends to be harder when various subsystems are tightly coupled, as changes in one may cause bugs to emerge in another. {{WP-Debugging}}

: The process through which people troubleshoot a technical issue, which may include inspection of program source code or device configurations. Can also include tracing or monitoring packet flow.

Decentralized
: Opportunity for implementation or deployment of standards, protocols or systems without one single point of control.

End-to-End
: The principal of extending characteristics of a protocol or system as far as possible within the system. For example, end-to-end instant message encryption would conceal communications from one user's instant messaging application through any intermediate devices and servers all the way to the recipient's instant messaging application. If the message was decrypted at any intermediate point--for example at a service provider--then the property of end-to-end encryption would not be present.

: One of the key architectural guidelines of the Internet is the end-to-end principle in the papers by Saltzer, Reed, and Clark {{Saltzer}} {{Clark}}. The end-to-end principle was originally articulated as a question of where best not to put functions in a communication system. Yet, in the ensuing years, it has evolved to address concerns of maintaining openness, increasing reliability and robustness, and preserving the properties of user choice and ease of new service development as discussed by Blumenthal and Clark in {{Blumenthal}}; concerns that were not part of the original articulation of the end-to-end principle. {{RFC3724}}

: communication that takes place between communication end-points of the same physical or logical functional level

Federation
: The possibility of connecting autonomous systems into a single distributed system.

Heterogenity
:  The Internet is characterized by heterogeneity on many levels: devices and nodes, router scheduling algorithms and queue management mechanisms, routing protocols, levels of multiplexing, protocol versions and implementations, underlying link layers (e.g., point-to-point, multi-access links, wireless, FDDI, etc.), in the traffic mix and in the levels of congestion at different times and places. Moreover, as the Internet is composed of autonomous
organizations and internet service providers, each with their own separate policy concerns,
there is a large heterogeneity of administrative domains and pricing structures.
As a result, heterogeneity principle is proposed in {{RFC1958}} to be supported by design. {{FIArch}}

Integrity
: Maintenance and assurance of the accuracy and consistency of data to ensure it has not been (intentionally or unintentionally) altered

Internet censorship
:  Internet censorship is the intentional suppression of information originating, flowing
or stored on systems connected to the Internet where that information is relevant for decision making to some entity. {{Elahi}}

Inter-operable
: A property of a documented standard or protocol which allows different independent implementations to work with each other without any restricted negotiation, access or functionality. 

Internet Standards as an Arena for Conflict
: Pursuant to the principle of constant change, since the function and scope of the Internet evolves, so does the role of the IETF in developing standards. Internet standards are adopted on the basis of a series of criteria, including high technical quality, support by community consensus, and their overall benefit to the Internet. The latter calls for an assessment of the interests of all affected parties and the specifications’ impact on the Internet’s users. In this respect, the effective exercise of the human rights of the Internet users is a relevant consideration that needs to be  appreciated in the standardization process insofar as it is directly linked to the reliability and core values of the Internet. {{RFC1958}} {{RFC0226}} {{RFC3724}}

Internationalization (i18n)
: The practice of making protocols, standards, and implementations usable in different languages and scripts.  (see Localization)

: (cf {{RFC6365}}) In the IETF, "internationalization" means to add or improve the handling of non-ASCII text in a protocol. {{RFC6365}}  A different perspective, more appropriate to protocols that are designed for global use from the beginning, is the definition used by W3C:

         "Internationalization is the design and development of a
         product, application or document content that enables easy
         localization for target audiences that vary in culture, region,
         or language."  {{W3Ci18nDef}}

Many protocols that handle text only handle one charset (US-ASCII), or leave the question of what CCS and encoding are used up to local guesswork (which leads, of course, to  interoperability problems).  If multiple charsets are permitted, they must be explicitly identified {{RFC2277}}.  Adding non-ASCII text to a protocol allows the protocol to handle more scripts, hopefully all of the ones useful in the world.  In today's world, that is normally best accomplished by allowing Unicode encoded in UTF-8 only, thereby shifting conversion issues away from individual choices. 

Localization (l10n)
: The practice of translating an implementation to make it functional in a specific language or for users in a specific locale (see Internationalization)

: (cf {{RFC6365}} The process of adapting an internationalized application platform or application to a specific cultural environment.  In localization, the same semantics are preserved while the syntax may be changed. {{FRAMEWORK}}

Localization is the act of tailoring an application for a different language or script or culture.  Some internationalized applications can handle a wide variety of languages.  Typical users only understand a small number of languages, so the program must be tailored to interact with users in just the languages they know.

The major work of localization is translating the user interface and documentation.  Localization involves not only changing the language interaction, but also other relevant changes such as display of numbers, dates, currency, and so on.  The better internationalized an application is, the easier it is to localize it for a particular language and character encoding scheme.

Localization is rarely an IETF matter, and protocols that are merely localized, even if they are serially localized for several locations, are generally considered unsatisfactory for the global Internet.


Open standards
: Conform  {{RFC2606}}: Various national and international standards bodies, such as ANSI,
      ISO, IEEE, and ITU-T, develop a variety of protocol and service
      specifications that are similar to Technical Specifications
      defined here.  National and international groups also publish
      "implementors' agreements" that are analogous to Applicability
      Statements, capturing a body of implementation-specific detail
      concerned with the practical application of their standards.  All
      of these are considered to be "open external standards" for the
      purposes of the Internet Standards Process.

Openness
: The quality of the unfiltered Internet that allows for free access to other hosts

: Absence of centralised points of control – a feature that is assumed to make it easy for new users to join and new uses to unfold {{Brown}}

Permissionless innovation
: The freedom and ability of to freely create and deploy new protocols on top of the communications constructs that currently exist
    
Privacy
: The right of an entity (normally a person), acting in its own behalf, to determine the degree to which it will interact with its environment, including the degree to which the entity is willing to share its personal information with others. {{RFC4949}}

: The right of individuals to control or influence what information related to them may be collected and stored and by whom and to whom that information may be disclosed.

: Privacy is a broad concept relating to the protection of individual autonomy and the relationship between an individual and society, including government, companies and private individuals. It is often summarized as “the right to be left alone” but it encompasses a wide range of rights including protections from intrusions into family and home life, control of sexual and reproductive rights, and communications secrecy.  It is commonly recognized as a core right that underpins human dignity and other values such as freedom of association and freedom of speech.   

The right to privacy is also recognized in nearly every national constitution  and in most international human rights treaties.  It has been adjudicated upon both by international and regional bodies.  The right to privacy is also legally protected at the national level through provisions in civil and/or criminal codes.  

Reliable
: Reliability ensures that a protocol will execute its function consistently and error resistant as described and function without unexpected result. A system that is reliable degenerates gracefully and will have a documented way to announce degradation.  It also has mechanisms to recover from failure gracefully, and if applicable, allow for partial healing. 

Resilience
: The maintaining of dependability and performance in the face of unanticipated changes and circumstances.

Robustness
: The resistance of protocols and their implementations to errors, and to involuntary, legal or malicious attempts to disrupt its mode of operations. {{RFC0760}} {{RFC0791}} {{RFC0793}} {{RFC1122}}

Scalable
: The ability to handle increased or decreased workloads predictably within defined expectations. There should be a clear definition of its scope and applicability.  The limits of a systems scalability should be defined. 

Stateless / stateful 
: In computing, a stateless protocol is a communications protocol that treats each request as an independent transaction that is unrelated to any previous request so that the communication consists of independent pairs of request and response. A stateless protocol does not require the server to retain session information or status about each communications partner for the duration of multiple requests. In contrast, a protocol which requires keeping of the internal state on the server is known as a stateful protocol. {{WP-Stateless}}

Strong encryption / cryptography
: Used to describe a cryptographic algorithm that would require a large amount of computational power to defeat it. {{RFC4949}}

Transparent:
: "transparency" refers to the original Internet concept of a single universal logical addressing scheme, and the mechanisms by which packets may flow from source to destination essentially unaltered. {{RFC2775}}

The combination of reliability, confidentiality, integrity, anonymity, and authenticity is what makes up security on the Internet

	 ( Reliability    )
	(  Confidentiality )
	(  Integrity       ) =  communication and information 
	(  Authenticity    )                  security (technical)
	 ( Anonymity      )


The combination of End-to-End, Interoperability, resilience, reliability and robustness is what makes us connectivity on the Internet


                         ( End-to-End      )   
     connectivity =     (  Interoperability )
                       (   Resilience        )  
                       (   Reliability       )   
                       (   Robustness        )
                        (  Autonomy         ) 
                         ( Simplicity      )   

Security Considerations
========================

As this draft concerns a research document, there are no security considerations.


IANA Considerations
==========================

This document has no actions for IANA.


Research Group Information
==========================

The discussion list for the IRTF Human Rights Protocol Considerations
proposed working group is located at the e-mail address
<hrpc@ietf.org>. Information on the group and information on how to
subscribe to the list is at
<https://www.irtf.org/mailman/listinfo/hrpc>

Archives of the list can be found at:
<https://www.irtf.org/mail-archive/web/hrpc/current/index.html>

