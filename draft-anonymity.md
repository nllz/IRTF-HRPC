--- 
title: Anonymity, Human Rights and Internet Protocols
abbrev: anon
docname: draft-tenoever-hrpc-anonymity-00
category: info

ipr: trust200902
area: IRTF
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
       ins: N. ten Oever
       name: Niels ten Oever
       organization: ARTICLE 19
       email: niels@article19.org

normative:
  
informative: 

   RFC3552:
   RFC6235:
   RFC6973:
   RFC7258:
   RFC7626:
   RFC7858:

   torproject:
     title: Tor Project - Anonymity Online
     date: 2007
     author:
        - ins: The Tor Project
     target: https://www.torproject.org/

   Pew:
     title: Anonymity, Privacy, and Security Online
     date: 2013
     author:
        - ins: L. Rainie
        - ins: S. Kiesler
        - ins: R. Kang
        - ins: M. Madden
     target: http://www.pewinternet.org/2013/09/05/anonymity-privacy-and-security-online/

   Pew2:
     title: Online Harassment
     date: 2014
     author:
        - ins: M. Duggan
     target: http://www.pewinternet.org/2014/10/22/online-harassment/

   UNHRC2015:
     title: Anonymity, Privacy, and Security Online (A/HRC/29/32)
     date: 2015
     author:
        - ins: D. Kaye
     target: www.ohchr.org/EN/HRBodies/HRC/RegularSessions/Session29/Documents/A.HRC.29.32_AEV.doc

   AnonTerm:
     title: "A terminology for talking about privacy by data minimization: Anonymity, Unlinkability, Undetectability, Unobservability, Pseudonymity, and Identity Management"
     date: 2010
     author:
        - ins: A. Pfitzmann
        - ins: M. Hansen
     target: http://dud.inf.tu-dresden.de/literatur/Anon_Terminology_v0.34.pdf

   
--- abstract

Anonymity is less discussed in the IETF than for instance security {{RFC3552}} or privacy {{RFC6973}}. This can be attributed to the fact anonymity is a hard technical problem or that anonymizing user data is not of specific market interest. It remains a fact that 'most internet users would like to be anonymous online at least occasionally' {{Pew}}. 

This document aims to break down the different meanings and implications of anonymity on a mediated computer network.

--- middle


Introduction
============

There seems to be a clear need for anonymity when harassment on the Internet on the increase {{Pew2}} and the UN Special Rapporteur for Freedom of Expression call anonymity 'necessary for the exercise of the right to freedom of opinion and expression in the digital age' {{UNHRC2015}}. 

Nonetheless anonymity is not getting much discussion at the IETF, providing anonymity does not seem a (semi-)objective for many protocols, even though several documents contribute to improving anonymity such as {{RFC7258}}, {{RFC7626}}, {{RFC7858}}.

There are initiatives on the Internet to improve end users anonymity, most notably {{torproject}}, but this all relies on adding encryption in the application layer. 

This document aims to break down the different meanings and implications of anonymity on a mediated computer network and to see whether (some parts of) anonymity should be taken into consideration in protocol development.

Vocabulary Used
===============

Concepts in this draft currently strongly hinges on {{AnonTerm}}

Anonymity
: A state of an individual in which an observer or attacker cannot identify the individual within a set of other  individuals (the anonymity set). {{RFC6973}}

Linkability
: Linkability of two or more items of interest (IOIs - Items Of Interest, e.g., subjects, messages, actions, ...) from an attacker’s perspective means that within the system (comprising these and possibly other items), the attacker can sufficiently distinguish whether these IOIs are related or not. {{AnonTerm}}

Pseudonymity
: Derided from pseudonym, a persistent identity which is not the same as the entity's given name.

Unlinkability
: Unlinkability of two or more items of interest (IOIs, e.g., subjects, messages, actions, ...) from an attacker’s perspective means that within the system (comprising these and possibly other items), the attacker cannot sufficiently distinguish whether these IOIs are related or not. {{AnonTerm}}

Undetectability
: The impossibility of being noticed or discovered

: Undetectability of an item of interest (IOI) from an attacker’s perspective means that the 
attacker cannot sufficiently distinguish whether it exists or not {{AnonTerm}}

Unobservability
: Unobservability of an item of interest (IOI) means:
  : undetectability of the IOI against all subjects uninvolved in it and 
  : anonymity of the subject(s) involved in the IOI even against the other subject(s) involved in that IOI. {{AnonTerm}}

It should be noted that the word "anonymity" is both very loaded
politically (witness all the headlines about the "darknet") and poorly
understood. Most texts talking about anonymity actually refer to
pseudonymity (for instance, when people say that "Bitcoin is
anonymous", while Bitcoin actually relies on linkability).

Anonymity is strongly linked to unlinkability: if your actions are
linkable, it suffices that one of them is tied to your identity, and
anonymity is over.

It should be noted that anonymity is not binary: there have been these
recent years a lot of progress of desanonymisation techniques. Data is
never fully "anonymous", it is only more or less anonymous. (See for
instance RFC6235.) TODO examples of big data desanonymisation.

Research Questions
==================

Premise: activity on the network has the ability for is to be anonymous or authenticated

While analyzing protocols for their impact on users anonymity, would it make sense to ask the following questions:

1. How anonymous is the end user to:
 - local network operator
 - other networks you connect to
 - your communications peer on the other end of the pipe

2. How well can they distinguish my identity from somebody else (with a similar communication) (ie linkability)

3. How does the protocol impact pseudonomity?
 - in case of long term pseudonymity
 - in case of short term pseudonymity

4. How does the protocol, in conjunction with other protocols, impact pseudonymity?

5. Could there be advice for protocol developers and implementers to improve anonimity and pseudonymity?

Use Cases
=========

- multiple identities concurrently used, mixing them in operations / keeping them distinct (talking to XMPP, alias, etc)

- when you change identity, do cross stack analysis, so you have no bleedover, anonymity on a cross protocol, cross stack level

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

