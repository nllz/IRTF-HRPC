--- 
title: Anonymity, Human Rights and Internet Protocols
abbrev: anon
docname: draft-irtf-hrpc-anonymity-01
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
       ins: S. Bortzmeyer
       name: Stephane Bortzmeyer
       organization: AFNIC
       email: bortzmeyer+ietf@nic.fr

-
       ins: N. ten Oever
       name: Niels ten Oever
       organization: University of Amsterdam
       email: mail@nielstenoever.net

normative:
  
informative: 

   RFC3552:
   RFC4949:
   RFC6235:
   RFC6973:
   RFC7258:
   RFC7626:
   RFC7824:
   RFC7844:
   RFC7858:

   AnonTerm:
     title: "A terminology for talking about privacy by data minimization: Anonymity, Unlinkability, Undetectability, Unobservability, Pseudonymity, and Identity Management"
     date: 2010
     author:
        - ins: A. Pfitzmann
        - ins: M. Hansen
     target: http://dud.inf.tu-dresden.de/literatur/Anon_Terminology_v0.34.pdf

   Article29:
    title: "Opinion 05/2014 on Anonymisation Techniques"
    date: 2014
    author:
        - ins: Article29
    target: http://ec.europa.eu/justice/data-protection/article-29/documentation/opinion-recommendation/files/2014/wp216_en.pdf

   GDPR:
    title: "REGULATION (EU) 2016/679 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation)"
    date: 2016
    author:
        - ins: European Parliament and Council
    target: http://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679

   MITdeano:
      title: "Unique in the Crowd: The privacy bounds of human mobility"
      date: 2013
      author:
         - ins: Y. de Montjoye
         - ins: C. A. Hidalgo
         - ins: M. Verleysen 
         - ins: V. Blondel
      target: https://www.nature.com/articles/srep01376

   EUcourt:
      title: "EUCJ Case C-70/10: Scarlet Extended SA vs. Société belge des auteurs, compositeurs et éditeurs SCRL (SABAM)"
      date: 2011
      target: http://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=CELEX:62010CJ0070:EN:HTML&lipi=urn%3Ali%3Apage%3Ad_flagship3_pulse_read%3BSFHas%2FXMRHeHVu46775ezw%3D%3D

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

   torproject:
     title: Tor Project - Anonymity Online
     date: 2007
     author:
        - ins: The Tor Project
     target: https://www.torproject.org/
   
   UNHRC2015:
     title: Anonymity, Privacy, and Security Online (A/HRC/29/32)
     date: 2015
     author:
        - ins: D. Kaye
     target: http://www.ohchr.org/EN/HRBodies/HRC/RegularSessions/Session29/Documents/A.HRC.29.32_AEV.doc

   Utexas:
      title: "Robust De-anonymization of Large Sparse Datasets"
      date: 2008
      author:
         - ins: A. Narayanan
         - ins: V. Shmatikov
      target: http://www.cs.utexas.edu/~shmat/shmat_oak08netflix.pd


--- abstract

Anonymity is less discussed in the IETF than for instance security {{RFC3552}} or privacy {{RFC6973}}. This can be attributed to the fact anonymity is a hard technical problem or that anonymizing user data is not of specific market interest. It remains a fact that 'most internet users would like to be anonymous online at least occasionally' {{Pew}}. 

This document aims to break down the different meanings and implications of anonymity on a mediated computer network.

--- middle


Introduction
============

There seems to be a clear need for anonymity online in an environment where harassment on the Internet is on the increase {{Pew2}} and the UN Special Rapporteur for Freedom of Expression calls anonymity 'necessary for the exercise of the right to freedom of opinion and expression in the digital age' {{UNHRC2015}}. 

Nonetheless anonymity is not getting much discussion at the IETF, providing anonymity does not seem a (semi-)objective for many protocols, even though several documents contribute to improving anonymity such as {{RFC7258}}, {{RFC7626}}, {{RFC7858}}.

There are initiatives on the Internet to improve end users anonymity, most notably {{torproject}}, but these initiatives rely on adding encryption in the application layer. 

This document aims to break down the different meanings and implications of anonymity on a mediated computer network and to see whether (some parts of) anonymity should be taken into consideration in protocol development.

Vocabulary Used
===============

Concepts in this draft currently strongly hinges on {{AnonTerm}}

Anonymity
: A state of an individual in which an observer or attacker cannot identify the individual within a set of other  individuals (the anonymity set). {{RFC6973}} 

Linkability
: Linkability of two or more items of interest (IOIs - Items Of Interest, e.g., subjects, messages, actions, ...) from an attacker’s perspective means that within the system (comprising these and possibly other items), the attacker can sufficiently distinguish whether these IOIs are related or not. {{AnonTerm}}

Official identity
: Government-issued identity, as written on ID cards and passports. We don't use terms like "real names" since a choosen pseudonym, for instance, is not less real than a identity given at birth.

Pseudonymity
: Derived from pseudonym, a persistent identity which is not the same as the entity's given (or official) name. For all IETF protocols, pseudonimity is a given: protocols don't care whether the identity is an official one or not. Even if the protocol allows to use official identities (for instance in the From: header of an Internet email), it does not require it. But it should be noted that, if the user cannot create new pseudonyms easily, pseudonyms suffer from linkability. Unlinkability depends on this ability to create new pseudonyms gratis and at will (good examples are SSH keys or Bitcoin addresses). Easy creation will allow to have one pseudonym per use, thus defeating linkability.

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

It should be noted that the word "anonymity" is both very loaded politically (witness all the headlines about the "darknet") and poorly understood. Most texts talking about anonymity actually refer to pseudonymity (for instance, when people say that "Bitcoin is anonymous"). This confusion is even in the example given in {{RFC4949}} definition of anonymity.

Anonymity is strongly linked to unlinkability: if your actions are linkable, it suffices that one of them is tied to your identity, and anonymity is over.

It should be noted that anonymity is not binary: there have been these recent years a lot of progress of desanonymisation techniques (see also {{GDPR}}, article 26). Data is
never fully "anonymous", it is only more or less anonymous. {{RFC6235}} {{MITdeano}} {{Utexas}} {{Article29}} 

Should protocols promote anonymity?
===================================

The amount of data that is generated by and about individuals is growing exponentially. This can be attributed to the fact that an ever increasing number of actions is digitally mediated, and the increase of connected sensors in the every day environment. Even though these two causes do not fully fall within the scope of the IETF, a significant part of these two examples do. 

TODO add here more examples of the need to anonymity

With the increase of data there is also an increasing ability for third parties to analyze human behaviour. It should be noted that any data that could identify an individual is personally identifiable information (PII). This means that information which can be used to distinguish an indivual from other individuals can be considered as personally identiable information. The access and control of personally identifiable information by a third party is a (potential) liability for both the third party and the individual. This liability could for example translate into a physical risk for the individual or into a legal risk for the third party under information security and privacy laws. 

Some network operators argue that without the opportunity to persistently identify individual users it becomes harder to thwart attacks and troubleshoot network issues. Whereas identification might be helpful to address issues in some cases, it poses an inherent threat to the anonymity of users. Not protecting the anonymity of users leads to a deterioration of the right to privacy, and the right to freedom of opinion and expression. There can be limitations on the right to privacy and freedom of expression, but these should always be provided by law and necessary and proportionate to achieve one of a handful of legitimate objectives. It is clear that anonymity may make system and network administration different. To quote {{RFC7824}}, "Those properties (stable and trackable IP addresses, derived from static identifiers) are convenient for system administrators". Here, there is a clear and fundamental tussle between the protection of the users and the ability of the system and network administrator to continue their work in the same way.

Anonymity will always be a balancing act between user protection (which requires a high level of anonymity) and other requirments for operations and research, such as routing information. Anonymity is by no means achieved by default in an online environment, nor has it been a strong consideration in protocol development in the development of the Internet. Increasing anonymity in the digital environment is not an easy task, exactly because the ubiquity of data that is generated and stored. But exactly the fact that we generate so much data urges us to address this issue. 

Example of use cases
====================

Simultaneous use
----------------

One user may use concurrently several identities, mixing them in operations, while wanting to keep them distinct. The protocol and its implementations should not preclude this use.

Successive use
--------------

One user may switch from one identity to another. In that case, it must be doable without a "bleedover" from the old identity to the new one.

One of the reasons to switch identities might be to make the relationship between this identity and another one (for instance the official one) more difficult. The longer you use a pseudonym, the more clues you give to someone who tries to unveil pseudonymity.

Selective use
-------------

A user might want to retain their anonymity to certain actors / protocols, but identified to others. Also, she may also wish to be identified for some operations but not always.

User analysis
-------------

A user might want to understand which other actors might (potentially) have which level of information about them. This conflicts of course with privacy because the user has to reveal who he is. Example: if a domain name registry does not publish the name of a registrant, the registrant cannot check if the person who did the registration indicated the name of their client, or their own name.

"Wikileaks feature"
------------------

TODO (anonymity when you don't know with whom you're talking to -- the application in mind being leaking materials)

Practical advices
=================

Protocol developers
-------------------

First, the protocol should avoid mandatory persistent identifiers. 

Even without persistent identifiers, anonymity could be broken by examining the patterns of access. If an user visits each morning the three same Web sites, always in the same order, it will be easy to identify them even without persistent identifier. Protocol designers should therefore ask themselves if patterns are easily visible, or obfuscated in some way.

If the protocol collects data and distributes it (see {{RFC6235}}), "anonymizing" the data is often suggested but it is notoriously hard. Do not think that just dropping the last byte of an IP address "anonymizes" data.

Pay attention to the fact that Internet actors do not all see the same thing. Consider the anonymity of the user with respect to:

 - local network operator
 - other networks you connect to
 - your communications peer on the other end of the pipe
 - intermediaries ({{RFC6973}})
 - enablers ({{RFC6973}})
 - someone who is in several roles, for instance a big state
   surveillance agency


Protocol implementors
---------------------

Avoid adding options or configurations that create or might lead to patterns or regularities that are not explicitely required by the protocol. 

An example is DHCP where sending a persistent identifier as the client name was not mandatory but, in practice, done by many implementations,
before {{RFC7844}}.

If an implementation allows for identity management, there should be a clear barrier between the identities to ensure that they cannot (easily) be associated with each other.

If there are anonymization option for the protocol, these should be enabled by default. 

Open Questions
==============

While analyzing protocols for their impact on users anonymity, would it make sense to ask the following questions:

1. How does the protocol impact pseudonymity?
If the protocol limits the creation of new pseudonyms, it can limit
their usefulness to "hide" an user's identity. For instance, IP
addresses are pseudonyms but, since they are not under end users's
control, they have strong linkability. That's why they are rightly
regarded as personal identifiers {{EUcourt}}. On the other hand, Bitcoin addresses
are pseudonyms with limited linkability, since the user can always
create a lot of them.

2. Could there be more advice for protocol developers and implementers
to improve anonymity? (Besides the ones in <xref target="practical-advices"/>.)
   
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

Objections against anonymity
============================

TODO: should be turned into an appendix. This draft is about how to allow anonymity, not about how to fight it.

For a long time, there have been objections against anonymity. This document won't attempt to rebuke them all, since it is concerned about how to ensure that protocols allow anonymity. But it is interesting to keep in mind that protocols never forbid anonymity. If smeones want his or her actions to be trackable, and under her or his official name, they can do so, by adding this information to their messages. In the same way, people are free not to engage with anonymous entities, in the same way that a SIP use, for instance, is free not to pick up a call if it comes from sip:anonymous@anonymous.invalid. This document is concerned about enabling anonymity, not about mandating it.

