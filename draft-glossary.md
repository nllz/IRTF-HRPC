--- 
title: Human Rights Protocol Considerations Glossary
abbrev: hrpcg
docname: draft-dkg-hrpc-glossary
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
   RFC1958:
   RFC2606:	
   RFC2775:
   RFC3724:
   RFC4084:
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
: The fact of not being identified

Authenticity
: The act of confirming the truth of an attribute of a single piece of data or entity.

Confidentiality
: The non-disclosure of information to any unintended person or host or party

Connectivity
: The extent to which a device or network is able to reach other devices or networks to exchange data. The Internet is the tool for providing global connectivity {{RFC1958}}. 

Content-agnosticism
: Treating network traffic identically regardless of content.

Debugging:
: Debugging is a methodical process of finding and reducing the number of bugs, or defects, or malfunctions in a protocol or its implementation, thus making it behave as expected and analyse the consequences that might have emanated from the error. Debugging tends to be harder when various subsystems are tightly coupled, as changes in one may cause bugs to emerge in another. {{WP-Debugging}}

: The process through which people troubleshoot a technical issue, which may include inspection of program source code or device configurations. Can also include tracing or monitoring packet flow.

Decentralized
: Opportunity for implementation or deployment of standards, protocols or systems without a single point of control.

Distributed
: A distributed architecture is a system in which not all processes reside in a single computer.

End-to-End
:The principal of extending characteristics of a protocol or system as far as possible within the system. For example, end-to-end instant message encryption would conceal communications from one user's instant messaging application through any intermediate devices and servers all the way to the recipient's instant messaging application. If the message was decrypted at any intermediate point--for example at a service provider--then the property of end-to-end encryption would not be present.

: One of the key architectural guidelines of the Internet is the end-to-end principle in the papers by Saltzer, Reed, and Clark {{Saltzer}} {{Clark}}. The end-to-end principle was originally articulated as a question of where best not to put functions in a communication system. Yet, in the ensuing years, it has evolved to address concerns of maintaining openness, increasing reliability and robustness, and preserving the properties of user choice and ease of new service development as discussed by Blumenthal and Clark in {{Blumenthal}}; concerns that were not part of the original articulation of the end-to-end principle. {{RFC3724}}

Federation
: The possibility of connecting autonomous systems into a single distributed system.

Integrity
: Maintenance and assurance of the accuracy and consistency of data to ensure it has not been (intentionally or unintentionally) altered

Inter-operable
: A property of a documented standard or protocol which allows different independent implementations to work with each other without any restricted negotiation, access or functionality. 

Internationalization
: The practice of the adaptation and facilitation of protocols, standards, and implementation to different languages and scripts.

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

Permissionless innovation
:  The freedom and ability of to freely create and deploy new protocols on top of the communications constructs that currently exist
    
Privacy
: Please see {{ RFC6973 }}

Reliable
: Reliability ensures that a protocol will execute its function consistently and error resistant as described and function without unexpected result. A system that is reliable degenerates gracefully and will have a documented way to announce degradation.  It also has mechanisms to recover from failure gracefully, and if applicable, allow for partial healing. 

Resilience
: The maintaining of dependability and performance in the face of unanticipated changes and circumstances.

Robust
: The resistance of protocols and their implementations to errors, and to involuntary, legal or malicious attempts to disrupt its mode of operations.

Scalable
: The ability to handle increased or decreased workloads predictably within defined expectations. There should be a clear definition of its scope and applicability.  The limits of a systems scalability should be defined. 

Stateless / stateful 
: In computing, a stateless protocol is a communications protocol that treats each request as an independent transaction that is unrelated to any previous request so that the communication consists of independent pairs of request and response. A stateless protocol does not require the server to retain session information or status about each communications partner for the duration of multiple requests. In contrast, a protocol which requires keeping of the internal state on the server is known as a stateful protocol. {{WP-Stateless}}

Transparent:
: "transparency" refers to the original Internet concept of a single universal logical addressing scheme, and the mechanisms by which packets may flow from source to destination essentially unaltered. {{RFC2775}}

The combination of content agnosticism, connectivity, security, privacy (as defined in {{RFC6973}}, and open standards are the technical principles that underlay freedom of expression on the Internet.


      (  ( End-to-End      )               )                            
     (  (  Interoperability )               )                           
    (   (  Resilience       )  Connectivity  )                          
    (   (  Reliability      )                )   = freedom of expression
    (    ( Robustness      )                 )                          
    (              Privacy                   )                          
    (              Security                  )                           
     (             Content agnosticism      )
      (	       Open Standards          )                            


The combination of reliability, confidentiality, integrity, anonymity, and authenticity is what makes up security on the Internet

                 ( Reliability    ) 	
    security =  (  Confidentiality )	  
                (  Integrity       )
                (  Authenticity    )
                 ( Anonymity      )

Research Group Information
==========================

The discussion list for the IRTF Human Rights Protocol Considerations
proposed working group is located at the e-mail address
<hrpc@ietf.org>. Information on the group and information on how to
subscribe to the list is at
<https://www.irtf.org/mailman/listinfo/hrpc>

Archives of the list can be found at:
<https://www.irtf.org/mail-archive/web/hrpc/current/index.html>

