---
title: Human Rights Protocol Considerations Methodology
abbrev: hrpcm
docname: draft-varon-hrpc-methodology-01
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
       ins: J. Varon 
       name: Joana Varon 
       organization: Coding Rights
       email: joana@codingrights.org
-
       ins: C.J.N. Cath
       name: Corinne Cath
       organization: Oxford Internet Institute
       email: corinne.cath@oii.ox.ac.uk

-
       ins: N. ten Oever
       name: Niels ten Oever
       organization: Article19
       email: niels@article19.org


normative:

informative:

   RFC1958:
   RFC1984:
   RFC2026:
   RFC2639:
   RFC2919:
   RFC3365:
   RFC3724:
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

   ID:
     title: Proposal for research on human rights protocol considerations
     date: 2015
     author:
        - ins: N. ten Oever
        - ins: A. Doria
        - ins: J. Varon
     target: http://tools.ietf.org/html/draft-doria-hrpc-proposal 

   torrentfreak1:
     title: Proposal for research on human rights protocol considerations
     date: 2015
     author:
        - ins: E. Van der Sar
     target: https://torrentfreak.com/is-your-isp-messing-with-bittorrent-traffic-find-out-140123/
   
   wikileaks:
     title: - Market Survey - Detection & Filtering Solutions to Identify File Transfer of Copyright Protected Content for Warner Bros. and movielabs
     date: 2011
     author:
        - ins: T. Sladek 
        - ins: E. Bröse
     target: https://wikileaks.org/sony/docs/05/docs/Anti-Piracy/CDSA/EANTC-Survey-1.5-unsecured.pdf

   ars:
     title: P2P researchers: use a blocklist or you will be tracked… 100% of the time
     date: 2007
     author:
        - ins: N. Anderson
     target: http://arstechnica.com/uncategorized/2007/10/p2p-researchers-use-a-blocklist-or-you-will-be-tracked-100-of-the-time/

   torrentfreak2:
     title: LAWYERS SENT 109,000 PIRACY THREATS IN GERMANY DURING 2013
     date: 2014
     author:
        - ins: Andy
     target: https://torrentfreak.com/lawyers-sent-109000-piracy-threats-in-germany-during-2013-140304/

   freenet1:
     title: What is Freenet?
     author:
        - ins: Freenet
     target: https://freenetproject.org/whatis.html

   freenet2:
     title: The Philosphy behind Freenet?
     author:
        - ins: Ian Clarke
     target: https://freenetproject.org/philosophy.html

   bitmessage:
     title: Bitmessage Wiki?
     date: 2014
     author:
        - ins: Bitmessage
     target: https://bitmessage.org/wiki/Main_Page

--- abstract

This document presents steps undertaken for developing a methodology to map engineering concepts at the protocol level that may be related to promotion and protection of Human Rights, particularly the right to freedom of expression and association.  It feeds upon and is intended to facilitate the work done by the proposed Human Rights Protocol Considerations research group, as well as other authors within the IETF.

Exemplary work {{RFC1984}} {{RFC6973}} {{RFC7258}} has already been done in the IETF on privacy issues that should be considered when creating an Internet protocol. But, beyond privacy considerations, concerns for freedom of expression and association were also a strong part of the world-view of the community involved in developing the first Internet protocols. Indeed, promoting open, secure and reliable connectivity is essential for these rights. But how are this concepts addressed in the protocol level? Are there others? This ID is intended to explain research work done so far and to explore possible methodological approaches to move further on exploring and exposing the relations between standards and protocols and the promotion and protection of the rights to freedom of expression and association. 

Discussion on this draft at: hrpc@irtf.org // https://www.irtf.org/mailman/admindb/hrpc


--- middle

Introduction
============

In a manner similar to the work done for {{RFC6973}} on Privacy Consideration Guidelines, the premise of this research is that some standards and protocols can solidify, enable or threaten human rights.

As stated in {{RFC1958}}, the Internet aims to be the global network of networks that provides unfettered connectivity to all users at all times and for any content. Our research hypothesis is that Internet's objective of connectivity makes it an enabler of human rights and that its architectural design tends to converge in protecting and promoting the human rights framework. 

Open, secure and reliable connectivity is essential for human rights such as freedom of expression and freedom of association, as defined in the Universal Declaration of Human Rights {{UDHR}}.  Therefore, considering connectivity as the ultimate objective of the Internet, makes a clear case that the Internet is not only an enabler of human rights, but that human rights lie at the basis of, and are ingrained in, the architecture of the network.

But, while the Internet was designed with freedom and openness of communications as core values, as the scale and the commercialization of the Internet has grown greatly, the influence of such world-views started to compete with other values. Therefore, decisive and human rights enabling characteristics of the Internet might be degraded if they're not properly defined, described and protected as such. And, on the other way around, not protecting these characteristics could also result in (partial) loss of functionality and connectivity, thus, in the internet architecture design itself.

An essential part of maintaining the Internet as a tool for communication and connectivity is security. Indeed, "development of security mechanisms is seen as a key factor in the future growth of the Internet as a motor for international commerce and communication" {{RFC1984}} and according to the Danvers Doctrine {{RFC3365}}, there is an overwhelming consensus in the IETF that the best security should be used and standardized.

In {{RFC1984}}, the Internet Architecture Board (IAB) and the Internet Engineering Steering Group (IESG), the bodies which oversee architecture and standards for the Internet, expressed: "concern by the need for increased protection of international commercial transactions on the Internet, and by the need to offer all Internet users an adequate degree of privacy."  Indeed, the IETF has been doing a significant job in this area {{RFC6973}} {{RFC7258}}, considering privacy concerns as a subset of security concerns.

Besides privacy, it should be possible to highlight other aspects of connectivity embedded in standards and protocols that can have human rights considerations, such as freedom of expression and the right to association and assembly online. This ID is willing to explain research work done so far and explore possible methodological approaches to move further on exploring and exposing these relations between standards and protocols and the promotion and protection of the rights to freedom of expression and association.

To move this debate further, information has been compiled at the https://datatracker.ietf.org/rg/hrpc/ and discussions are happening through the list hrpc@irtf.org

This document builds on the previous IDs published within the framework of the proposed hrpc research group {{ID}}

Research Topic
==============

The growing impact of the Internet on the lives of individuals makes Internet standards and protocols increasingly important to society. The IETF itself, in {{RFC2026}}, specifically states that the ‘interests of the Internet community need to be protected’. There are various examples of protocols and standards having a direct impact on society, and by extension the human rights of end-users. Privacy is just one example. Therefore, this proposal for research methodology is addressing as research topics the rights to freedom of expression and association and it's relations to standards and protocols.
 
These two rights are described in the Universal Declaration of Human Rights:


Article 19 - Freedom of Expression (FoE)
"Everyone has the right to freedom of opinion and expression; this right includes freedom to hold opinions without interference and  to seek, receive and impart information and ideas through any  media and regardless of frontiers."

Article 20 - Freedom of Association (FoA)
"Everyone has the right to freedom of peaceful assembly and association."

But how to talk about human rights in an engineering context? 

But can we translate these concepts into Internet architecture technical terms?

What standards and protocols could have any relationship with freedom of expression and association?

What are the possible relationships between them?


Methodology
===========

Mapping the relation between human rights and protocols and architectures is a new research challenge, which requires a good amount of interdisciplinary and cross organizational cooperation to develop a consistent methodology.  While the authors of this first draft are involved in  both human rights advocacy and research on Internet technologies - we believe that bringing this work into the IRTF facilitates and  improves this work by bringing human rights experts together with the  community of researchers and developers of Internet standards and technologies.

In order to map the potential relation between human rights and protocols, so far, the HRPC proposed research group has been gathered the data from three specific sources:

a. Discourse analysis of RFCs
To start addressing the issue, a mapping exercise analyzing Internet architecture and protocols features, vis-a-vis possible impact on human rights is being undertaken. Therefore, research on the language used in current and historic RFCs and mailing list discussions is underway to expose core architectural principles, language and deliberations on human rights of those affected by the network.

b. Interviews with members of the IETF community during the Dallas meeting of March 2015
Interviews with the current and past members of the Internet Architecture Board (IAB), current and past members of the Internet Engineering Steering Group(IESG) and chairs of selected working groups and RFC authors. To get an insider understanding of how they view the relationship (if any) between human rights and protocols to play out in their work.

c. Participant observation in Working Groups
By participating in various working groups information was gathered about the IETFs day-to-day work. From which which general themes and use-cases about human rights and protocols were extracted.


All this data was then processed using the following three consecutive strategies:

Translating Human Rights Concept into Technical Definitions
-----------------------------------------------------------

Step 1.1 - Mapping protocols and standards related to FoE and FoA
Activity: Mapping of protocols and standards that potentially enable the internet as a tool for freedom of expression
Expected Outcome: list of RFCs that describe standards and protocols that are potentially more closely related to FoE and FoA.

Step 1.2 - Extracting concepts from mapped RFCs
Activity: Read the selected RFCs to highlight central design and technical concepts which impact human rights.
Expected Outcome 1: a list of technical terms that combined create the enabling environment for freedom of expression and freedom of association.
Expected Outcome 2: Possible translations of human rights concepts to technical terms.

Step 1.3 - Building a common glossary
In the analysis of existing RFCs, central design and technical concepts shall be found which impact human rights.
Expected Outcome: a Glossary for human rights protocol considerations with a list of concepts and definitions of technical concepts


Map cases of protocols being exploited or enablers 
------------------------------------------------------

Step 1.1 - Cases of protocols being exploited
Activity 1: Map cases in which users rights have been exploited, violated or compromised, analyze which protocols or vulnerabilities in protocols are invovled with this.
Activity 2: Understand technical rationale for the use of particular protocols that undermine human rights. 
Expected Outcome: list of protocols that have been exploited to expose users to rights violation and rationale.

Step 1.2 - Cases of protocols being enablers
Activity: Map cases in which users rights have been enabled, promoted and protected and analyze which characteristics in the protocols are involved with this.
Expected Outcome: list of characteristics in the protocols that have been key to promote and protect the rights to freedom of expression and association that could be added to our glossary


Apply human rights technical definitions to the cases mapped
---------------------------------------------------------------

Step 1 - Glossary and Cases
Activity: Investigate alternative technical options from within list of technical design principle (see {{HRPC-GLOSSARY}}) that could have been applied in the mapped cases to strengthen our technical definition of FoE and FoA, and hence human rights and connectivity of the network.

Expected Outcome: Identify best (and worst) current practices. Develop procedures to systematically evaluate protocols for potential human rights impact.



Preliminary findings achieved by applying current proposed methodology
=======================================================================


Current status: Translating Human Rights Concept into Technical Definitions
-----------------------------------------------------------

Step 1.1 - Mapping protocols and standards related to FoE and FoA

Below are some examples of these protocols and standards that might be related to FoE and FoA and FoE:

HTTP
Websites made it extremely easy for individuals to publish their ideas, opinions and thoughts.  Never before has the world seen an infrastructure that made it this easy to share information and ideas with such a large group of other people.  The HTTP architecture and standards, including {{RFC7230}}, {{RFC7231}}, {{RFC7232}}, {{RFC7234}}, {{RFC7235}}, {{RFC7236}}, and {{RFC7237}}, are essential for the publishing of information.  The HTTP protocol, therefore, forms an crucial enabler for freedom of expression, but also for the right to freely participate in the culture life of the community (Article 27) {{UDHR}}, to enjoy the arts and to share in scientific advancement and its benefits.


Real time communications through XMPP and WebRTC
Collaborations and cooperation via the Internet have take a large step forward with the progress of chat and other other real time communications protocols.  The work on XMPP {{RFC6162}} has enabled new methods of global interactions, cooperation and human right advocacy.  The WebRTC work being done to standardize the API and protocol elements to support real-time communications for browsers, mobile applications and IoT by the World Wide Consortium (W3C) and the IETF is another artifact enabling human rights globally on the Internet.

Mailing lists
Collaboration  and cooperation have been part of the Internet since its early  beginning, one of the instruments of facilitating working together in  groups are mailing lists (as described in {{RFC2639}}, {{RFC2919}}, and {{RFC6783}}.  Mailing lists are critical  instruments and enablers for group communication and organization, and  therefore form early artifacts of the (standardized) ability of Internet standards to enable the right to freedom of assembly and association.


IDNs
English has been the lingua franca of the Internet, but for many Internet user English is not their first language.  To have a true global Internet, one that serves the whole world, it would need to reflect the languages of these different communities.  The Internationalized Domain Names IDNA2008 ({{RFC5890}}, {{RFC5891}}, {{RFC5892}}, and {{RFC5893}}), describes standards for the use of a broad range of strings and characters (some also written from right to left).  This enables users who use other characters than the standard LDH ascii typeset to have their own URLs.  This shows the ambition of the Internet community to reflect the diversity of users and to be in line with Article 2 of the Universal Declaration of Human Rights which clearly stipulates that "everyone is entitles to all rights and freedoms `[...]`, without distinction of any kind, such as `[...]` language `[...]`." {{UDHR}}


Current Status: Mapping protocols and standards related to FoE and FoA
---------------

Based on these standards and protocols as well as an analysis of existing RFCs and literature, a listing of architectural concepts has been made. 

Step 1.2 - Extracting concepts from mapped RFCs
The list of RFCs as well as relevant literature has used to extract key architectural principles. The main architectural concepts were subsequently listed in the glossary {{HRPC-GLOSSARY}}. 

Current Status: Extracting concepts from mapped RFCs
---------------
Expected Outcome 1:  a list of  technical terms that combined create the enabling environment for human rights, such a freedom of expression and freedom of association.

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
     =    Simplicity   |     Graceful degradation    =                  |
     =                 |          Connectivity       =                  |
     =                 |          Heterogenity       =                  |
     =                 |                             =                  |
     =                 |                             =                  |
     =                 \------------------------------------------------/
     =                                               =
     +===============================================+

Current status: Translating human rights to technical terms
---------------

Expected outcome 2: This analysis aims to translate human rights concepts that impact or are impacted by the Internet as follows:

The combination of content agnosticism, connectivity, security, privacy (as defined in {{RFC6973}}, and open standards are the technical principles that underlay freedom of expression on the Internet.

      (        Connectivity         ) 
     (         Privacy               )
     (         Security              )   = freedom of expression
     (         Content agnosticism   )
     (	      Internationalization   )
     (        Censorship resistance  )
     (	      Open Standards         )
      (       Heterogeneity support )
	                           

     (		Anonymity           )
    (		Privacy              )   = Non-discrimination
    (		Pseudonymity         )
     (		Content agnosticism )	

			
    ( 	      Content Agnosticism  )
    (	      Security             ) 	= Equal protection

    
     (	      Anonymity       ) 
    (	      Privacy          )   = Right to be presumed innocent
     (	      Security        )	


	 (	Accessibility         )
	(	Internationalization   ) = Right to political participation
	(	Censorship resistance  )
	 (      

					
	 (  Open standards         )
	(   Localization            ) = Rights for cultural life, 
	(   Internationalization    )             arts and science
	 (  Censorship resistance  )


	 (	Connectivity         )  
	(	Decentralization      )
	(     Censorship resistance ) = Right to freedom of assembly 
	(  	Pseudonymity          )                   and association     
	(	Anonymity             )
	 ( 	Security             )
	
        ( Reliability    ) 
       (  Confidentiality )	  
       (  Integrity       ) = Right to security
       (  Authenticity    )
        ( Anonymity      )


Step 1.3 - Build a common glossary

Current status: Building of a common glossary
---------------
Expected Outcome: A glossary has been developed, which aims to build on other relevant published glossaries by the IETF and relevant literature: {{HRPC-GLOSSARY}}). This document aims to provide a description of relevant architectural principals as well as technical concepts that are relevant for describing the impact of protocols on human rights. 


Current status: Map cases of protocols being exploited or enablers 
------------------------------------------------------------------

IP
=====
The Internet Protocol version 4, known as ‘layer 3’ of the internet, and specified as a common encapsulation and protocol header, is defined by RFC 791. The evolution of Internet communications have led to continued development in this area, encapsulated in the development of version 6 of the protocol in RFC 2460. In spite of this updated protocol, we find that 25 years after the specification of version 6 of the protocol, the older v4 standard continues to account for a sizable majority of internet traffic.

The internet was designed as a platform for free and open communication, most notably encoded in the end-to-end principle, and that philosophy is also present in the technical implementation of the Internet Protocol. {{RFC3724}} While the protocol was designed to exist in an environment where intelligence is at the end hosts, it has proven to provide sufficient information that a more intelligent network core can make policy decisions and enforce policy shaping and restricting the communications of end hosts. These capabilities for network control and limitations of the freedom of expression by end hosts can be traced back to the IPv4 design, helping us understand which technical protocol decisions have led to harm of these human rights.

Two major shifts have occurred to harm freedom of expression through misuse of the Internet Protocol. The first is the network’s exploitation of the public visibility of the host pairs for all communications, and the corresponding ability to discriminate and block traffic as a result of that metadata. The second is the selective development of IP options, so that protocol extensions promoting assembly and expression like Mobility and Multicasting can fail to receive support from IP compatible devices. This lack of forward compatibility where extensions can receive a baseline level of support needed to extend the design has stymied forms of expression which could have been extended to support these human rights.

Network visibility of Source and Destination
-----
The IPv4 protocol header contains fixed location fields for both the source and destination IP addresses {{RFC0791}}. These addresses identify both the host sending and receiving each message, and allow the core network to understand who is talking to whom, and to practically limit communication selectively between pairs of hosts. Blocking of communication based on the pair of source and destination is one of the most common limitations on the ability for hosts to communicate today, [2] and can be seen as a restriction of the ability for those hosts to assemble or to consensually express themselves.

We have seen from other instantiations of protocols, even those comparable to IPv4, that other designs are possible. IPv4 even encodes a defined option and specification for source routing of packets, where the source can specify or suggest a routing path, and as the message passes through those paths, the part of the path it has completed are removed from the path. This design has the potential to make it much more difficult for an individual router in the network to stifle speech, since it will cannot do the same level of differentiation on the source of the messages.  Unfortunately, many networks prevent the use of source routing, and the protocol is not designed such that support of that ability is required in order for the protocol to be implemented.

Documentation of this form of harm: {{RFC0791}}, 
[1] https://tools.ietf.org/html/rfc791
[2] http://www.caida.org/publications/papers/2014/outages_censorship/outages_censorship.pdf
[3] http://www.ipjustice.org/digital-rights/internet-infrastructure-and-ip-censorship-by-david-post/

Protocols
-----
The other major feature of the IP protocol header is that it specifies the protocol encapsulated in each message in an easily observable form, and does not encourage a design where the encapsulated protocol is not available to a network observer.  This design has resulted in a proliferation of routers which inspect the inner protocol, and has resulted in a stagnation where only the TCP and UDP protocols are widely supported across the Internet. While the IP protocol was designed as the entire set of metadata needed for routing, subsequent enhanced routers have found value on making policy decisions based on the contents of TCP and UDP headers as well, and are encoded with the assumption that only these protocols will be used for data transfer. [1] This has prevented development of more secure protocols, since there’s a need to provide sufficient metadata with each message for routers to make positive policy decisions if you hope the protocol will be available to all users.

Documentation of this form of harm:
[1] https://www.chromium.org/spdy/spdy-whitepaper
[2] https://www.chromium.org/quic
[3] https://tools.ietf.org/html/rfc4960

Address Translation and Mobility
-----
A major structural shift in the Internet which has undermined the protocol design of IPv4, and has significantly reduced the freedom of end users to communicate and assemble in the introduction network address translation. {{RFC1631}} Network address translation is a process whereby organizations and autonomous systems to connect two networks by translating the IPv4 source and destination addresses between the two. This process puts the router performing the translation into a privileged position, where it can decide which subset of communications are worthy of translation, and whether an unknown request for communication will be correctly forwarded to a host on the other network.

This process of translation has widespread adoption despite promoting a process that goes against the stated end-to-end process of the underlying protocol [2]. In contrast, the proposed mechanism to provide support for mobility and forwarding to clients which may move, encoded instead as an option in the IP protocol [3], has failed to gain traction. This situation again suggests that the compromise made in design of the protocol has resulted in a technology which failed to technical encode the freedom of expression goals it was designed to promote.

Documentation of this form of harm:
{{RFC1631}}
[2] http://www.icsi.berkeley.edu/pubs/networking/NATusage11.pdf
[3] https://tools.ietf.org/html/rfc5944



DNS
under discussion on the list nosupw

HTTP
under discussion on the list now

XMPP
====
The Extensible Messaging and Presence Protocol (XMPP), specified in RFC 3920, provides a standard for interactive chat messaging, and has evolved to encompass interoperable text, voice, and video chat. The protocol is structured as a federated network of servers, similar to email, where users register with a local server which acts one their behalf to cache and relay messages. This protocol design has many advantages, allowing servers to shield clients from denial of service and other forms of retribution for their expression, and designed to avoid central entities which could control the ability to communicate or assemble using the protocol.

None-the-less, there are plenty of aspects of the protocol design of XMPP which shape the ability for users to communicate freely, and to assembly through the protocol. In addition to issues of user registration and a lack of protocol specification of the registration policy, the protocol also has facets that may stifle speech as users self-censor for fear of surveillance, or find themselves unable to express themselves naturally.

User Identification
------
The XMPP specification specifies that clients are identified with a resource (<node@domain/home> / <node@domain/work>) to distinguish the conversations to specific devices. This has the side effect of enabling tracking of user behavior by a remote friend or server, who are able to track presence not only of the user, but of each individual device. This has proven to be misleading to many users, since many clients only expose user level rather than device level presence. Likewise, user invisibility so that communication can occur while users don’t notify all buddies and other servers of their availability is not part of the formal protocol, and has only been added as an extension within the XML stream rather than enforced by the protocol.

Documentation of this form of harm:
[1] https://developer.pidgin.im/ticket/4322

Character Encoding
-----
Localization is a source of frustration in many protocols, and appears in some forms of XMPP. The XMPP protocol specifies a requirement for UTF-8 and UTF-16 support [1], though documentation admits that many implementations may not support UTF-16 [2]. In practice, this leads to cases where text encoded outside of a standard english language ascii encoding will fail to render on all clients, limiting the ability of users to communicate in their native languages. Some examples are failure of XMPP servers to handle non-ascii passwords [3], and gateways which simply strip all non-ascii from the conversation stream.

At the protocol level, XMPP only defines the conversation as an XML block, and leaves the implementation of character sets to the XMPP parsers of each individual client and server. While there have been attempts to define UTF-16 support as part of the protocol specification, the lack of actual implementation of the more extensible character set by all clients has shaped the protocol to harm the full range of expression users may desire.

Documentation of this form of harm:
[1] http://mail.jabber.org/pipermail/xmppwg/2003-August/001460.html
[2] http://xmpp.org/rfcs/rfc6120.html#streams-error-conditions-unsupported-encoding
[3] https://support.process-one.net/browse/EJAB-476
[4] https://wiki.bitlbee.org/HowtoFacebookXMPP

Surveillance of Communication
-----
The XMPP protocol specifies the standard by which communication of channels may be encrypted, but it does not provide visibility to clients of whether their communications are encrypted on each link. In particular, even when both clients ensure that they have an encrypted connection to their XMPP server to ensure that their local network is unable to read or disrupt the messages they send, the protocol does not provide visibility into the encryption status between the two servers. As such, clients may be subject to selective disruption of communications by an intermediate network which disrupts communications based on keywords found through Deep Packet Inspection.

In particular, section 13.14 of the protocol specification [2] explicitly acknowledges the existence of a downgrade attack where an adversary controlling an intermediate network can force the inter domain federation between servers to revert to a non-encrypted protocol were selective messages can then be disrupted.

Documentation of this form of harm:
[1] https://raw.githubusercontent.com/stpeter/manifesto/master/manifesto.txt
[2] https://www.ietf.org/rfc/rfc6120.txt



Group Chat Limitations
-----
Group chat in the XMPP protocol is defined as an extension within the XML specification of the XMPP protocol [1]. However, it is not encoded or required at a protocol level, and not uniformly implemented by clients.

The design of multi-user chat in the XMPP protocol suffers from extending a protocol that was not designed with assembly of many users in mind. In particular, in the federated protocol provided by XMPP, multi-user communities are implemented with a distinguished ‘owner’, who is granted control over the participants and structure of the conversation.

Multi-user chat rooms are identified by a name specified on a specific server, so that while the overall protocol may be federated, the ability for users to assemble in a given community is moderated by a single server. That server may block the room and prevent assembly unilaterally, even between two users neither of whom trust or use that server directly.

[1] http://xmpp.org/extensions/xep-0045.html



Peer to Peer
====
Peer-to-Peer (P2P) is a network architecture (defined in RFC7574) in
which all the participant nodes are equally responsible engaged into the
storage and dissemination of information. A P2P network is a logical
overlay that lives on top of the physical network, and allows nodes (or
"peers") participating to it to establish contact and exchange
information directly from one to each other. The implementation of a P2P
network may very widely: it may be structured or unstructured, and it
may implement stronger or weaker cryptographic and anonymity properties.
While its most common application has traditionally been file-sharing
(and other types of content delivery systems), P2P is increasingly
becoming a popular architecture for networks and applications that
require (or encourage) decentralization. A prime example is Bitcoin (and
similar cryptocurrencies), as well as Skype, Spotify and other
proprietary multimedia applications.

In a time of heavily centralized online services, peer-to-peer is often
seen as an alternative, more democratic, and resistant architecture that
displaces structures of control over data and communications and
delegates all peers equally to be responsible for the functioning,
integrity, and security of the data. While in principle peer-to-peer
remains critical to the design and development of future content
distribution, messaging, and publishing systems, it poses numerous
security and privacy challenges which are mostly delegated to individual
developers to recognize, analyze, and solve in each implementation of a
given P2P network.


Network Poisoning
-----
Since content, and in some occasions peer lists, are safeguarded and
distributed by its members, P2P networks are prone to what are generally
defined as "poisoning attacks". Poisoning attacks might be directed
directly at the data that is being distributed, for example by
intentionally corrupting it, or at the index tables used to instruct the
peers where to fetch the data, or at routing tables, with the attempt of
providing connecting peers with lists of rogue or non-existing peers,
with the intention to effectively cause a Denial of Service on the network.


Throttling
-----
Peer-to-Peer traffic (and BitTorrent in particular) represents a high
percentage of global Internet traffic and it has become increasingly
popular for Internet Service Providers to perform throttling of
customers lines in order to limit bandwidth usage [torrentfreak1] and sometimes
probably as an effect of the ongoing conflict between copyright holders
and file-sharing communities [wikileaks].

Throttling the peer-to-peer traffic makes some uses of P2P networks
ineffective and it might be coupled with stricter inspection of users'
Internet traffic through Deep Packet Inspection techniques which might
pose additional security and privacy risks.


Tracking and Identification
-----

One of the fundamental and most problematic issues with traditional
peer-to-peer networks is a complete lack of anonymization of its users.
For example, in the case of BitTorrent, all peers' IP addresses are
openly available to the other peers. This has lead to an ever-increasing
tracking of peer-to-peer and file-sharing users [ars]. As the geographical
location of the user is directly exposed, and so could be his identity,
the user might become target of additional harassment and attacks, being
of physical or legal nature. For example, it is known that in Germany
lawfirms have made extensive use of peer-to-peer and file-sharing
tracking systems in order to identify downloaders and initiate legal
actions looking for compensations [torrenfreak2].

It is worth nothing that there are varieties of P2P networks that
implement cryptographic practices and that introduce anonymization of
its users. Such implementations proved to be successful in resisting
censorship of content, and tracking of the network peers. A primary
example is FreeNet [freenet1], a free software application designed to
significantly increase the difficulty of users and content
identification, and dedicated to foster freedom of speech online[freenet2].


Conclusions
-----

Encrypted P2P and Anonymous P2P networks already emerged and provided
viable platforms for sharing material, publish content anonymously, and
communicate securely [bitmessage]. If adopted at large, well-designed and
resistant P2P networks might represent a critical component of a future
secure and distributed Internet, enabling freedom of speech and freedom
of information at scale.



Next Steps of the Methodology still to be applied
=================================================

Apply human rights technical definitions to the cases mapped
------------------------------------------------------------


Next Steps of the Methodology still to be developed
===================================================

Future research questions
-------------------------
All of the steps mentioned above raise the following question that need to be addressed after the research methodological steps outlined above have been completed:

How can the rights enabling environment be safeguarded in (future) protocol development?

How  can (nontransparent) human rights violations be minimized in (future) protocol development?

Can we propose guidelines to protect the Internet as a human-rights-enabling environment in future protocol development, specially in relation to freedom of expression and freedom of  association, in a manner similar to the work done for Privacy Considerations in {{RFC6973}}?

Assuming that the research produces useful results, can the objective evolve into the creation of a set of recommended considerations for the protection of applicable human rights?


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


