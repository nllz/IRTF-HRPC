--- 
title: Anonymity, Human Rights and Internet Protocols
abbrev: anon
docname: draft-tenoever-hrpc-anonymity-01
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

-
       ins: S. Bortzmeyer
       name: Stephane Bortzmeyer
       organization: AFNIC
       email: bortzmeyer+ietf@nic.fr

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
: Derided from pseudonym, a persistent identity which is not the same
as the entity's given (or official) name. For most (TODO all?) IETF
protocols, pseudonimity is a given: protocols don't care whether the
identity is an official one or not. But it should be noted that, if
the user cannot create new pseudonyms easily, pseudonyms suffer from
linkability. Unlikability depends on this ability to create new
pseudonyms. TODO: or decide that pseudonyms *require* this ability to
be created at will?

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
anonymous").

Anonymity is strongly linked to unlinkability: if your actions are
linkable, it suffices that one of them is tied to your identity, and
anonymity is over.

It should be noted that anonymity is not binary: there have been these
recent years a lot of progress of desanonymisation techniques. Data is
never fully "anonymous", it is only more or less anonymous. (See for
instance RFC6235.) TODO examples of big data desanonymisation.

Should we promote / accept / reject anonymity?
==============================================

Any data that could identify an individual is personally identifiable information. This means that information which can be used to distinguish an indivual from other individuals can be considered as personally identiable information. The access and control of personally identifiable information by a third party is a (potential) liability for both the third party and the individual. This liability could for example translate into a physical risk for the individual or into a legal risk for the third party under information security and privacy laws. 

Network operators argue that without opportunities to persistently identify individual users it becomes harder to thwart attack and troubleshoot network issues. 

TODO operations issues

Example of use cases
===================

Simultaneous use
----------------

One user may use concurrently several identities, mixing them in
operations, while wanting to keep them distinct. The protocol and its
implementations should not preclude this use.

Successive use
--------------

One user may switch from one identity to another. In that case, it
must be doable without a "bleedover" from the old identity to the new
one.

Research Questions
==================

Premise: activity on the network can be anonymous or not.

While analyzing protocols for their impact on users anonymity, would it make sense to ask the following questions:

1. How anonymous is the end user to:
 - local network operator
 - other networks you connect to
 - your communications peer on the other end of the pipe
 - intermediaries (RFC6973)
 - enablers (RFC6973)

2. Anonymity of the server

TODO Tor .onion

3. How well can they distinguish my identity from somebody else (with a similar communication) (ie linkability)?

4. How does the protocol impact pseudonomity?
If the protocol limits the creation of new pseudonyms, it can limit
their usefulness to "hide" an user's identity. For instance, IP
addresses are pseudonyms but, since they are not under end users's
control, they have strong linkability. That's why they are righly
regarded as personal identifiers TODO reference. On the other hand, Bitcoin addresses
are pseudonyms with limited linkability, since the user can always
create a lot of them.

5. Could there be advice for protocol developers and implementers to improve anonymity?

First, the protocol should avoid to have mandatory persistent
identifiers.

TODO patterns

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

