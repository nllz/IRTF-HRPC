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
-
       ins: C. Guarnieri
       name: Claudio Guarnieri
       organization: Centre for Internet and Human Rights
       email: nex@nex.sx
-
       ins: W. Scott
       name: Will Scott
       organization: University of Washington
       email: wrs@cs.washington.edu


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

   caida:
     title: Analysis of Country-wide Internet Outages Caused by Censorship
     date: 2013
     author:
       - ins: A. Dainotti
       - ins: C. Squarcella
       - ins: E. Aben
       - ins: K. Claffy
       - ins: M. Chiesa
       - ins: M. Russo
       - ins: A. Pescape
     target: http://www.caida.org/publications/papers/2014/outages_censorship/outages_censorship.pdf

  torproject:
    title: Tor Project: Anonymity Online
    date: 2007
    author:
      - org: The Tor Project
    target: https://www.torproject.org/

   spdy:
     title: SPDY: An experimental protocol for a faster web
     date: 2009
     author:
       - org: The Chromium Project
     target: https://www.chromium.org/spdy/spdy-whitepaper

   quic:
     title: QUIC, a multiplexed stream transport over UDP
     date: 2014
     author:
       - org: The Chromium Project
     target: https://www.chromium.org/quic

   natusage:
     title: NAT usage in Residential Broadband networks
     date: 2011
     author:
       - ins: G. Maier
       - ins: F. Schneider
       - ins: A. Feldmann
     target: http://www.icsi.berkeley.edu/pubs/networking/NATusage11.pdf

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

# IP

The Internet Protocol version 4, known as ‘layer 3’ of the internet, and specified as a common encapsulation and protocol header, is defined by {{RFC791}}. The evolution of Internet communications have led to continued development in this area, encapsulated in the development of version 6 of the protocol in {{RFC2460}}. In spite of this updated protocol, we find that 25 years after the specification of version 6 of the protocol, the older v4 standard continues to account for a sizable majority of internet traffic.

The internet was designed as a platform for free and open communication, most notably encoded in the end-to-end principle, and that philosophy is also present in the technical implementation of the Internet Protocol. {{RFC3724}} While the protocol was designed to exist in an environment where intelligence is at the end hosts, it has proven to provide sufficient information that a more intelligent network core can make policy decisions and enforce policy shaping and restricting the communications of end hosts. These capabilities for network control and limitations of the freedom of expression by end hosts can be traced back to the IPv4 design, helping us understand which technical protocol decisions have led to harm of these human rights.

Two major shifts have occurred to harm freedom of expression through misuse of the Internet Protocol. The first is the network’s exploitation of the public visibility of the host pairs for all communications, and the corresponding ability to discriminate and block traffic as a result of that metadata. The second is the selective development of IP options. Protocol extensions including Mobility and Multicasting have proposed alternate communication modes and suggest that different forms of assemply could be supported by an a robust IP layer. Instead, the protocol has limited the deployability of such extensions by not providing a mechanism for appropriate fallback behavior when unrecognized extensiosn are encountered.

## Network visibility of Source and Destination

The IPv4 protocol header contains fixed location fields for both the source and destination IP addresses {{RFC0791}}. These addresses identify both the host sending and receiving each message, and allow the core network to understand who is talking to whom, and to practically limit communication selectively between pairs of hosts. Blocking of communication based on the pair of source and destination is one of the most common limitations on the ability for hosts to communicate today, [caida] and can be seen as a restriction of the ability for those hosts to assemble or to consensually express themselves.

Inclusion of an Internet-wide identified source in the IP header is not the only possible design, especially since the protocol is most commonly implemented over Ethernet networks exposing only link-local identifiers. {{RFC0894}} A variety of alternative designs including source routing, and spoofing of the source IP address are technicaly supported by the protocol, but neither are regularly allowed on the Internet. While projects like [torproject] provide an alternative implementation of anonymity in connections, they have been developed in spite of the IPv4 protocol design.

## Protocols

The other major feature of the IP protocol header is that it specifies the protocol encapsulated in each message in an easily observable form, and does not encourage a design where the encapsulated protocol is not available to a network observer.  This design has resulted in a proliferation of routers which inspect the inner protocol, and has resulted in a stagnation where only the TCP and UDP protocols are widely supported across the Internet. While the IP protocol was designed as the entire set of metadata needed for routing, subsequent enhanced routers have found value on making policy decisions based on the contents of TCP and UDP headers as well, and are encoded with the assumption that only these protocols will be used for data transfer. [spdy] {{RFC4303}} defines an encrypted encapsulation of additional protocols, but lacks widespread deployment and faces the same challenge as any other protocol of providing sufficient metadata with each message for routers to make positive policy decisions. Protocols like {{RFC4906}} have seen limited wide-area uptake, and these alternate designs are frequently re-implemented on top of UDP. [quic]

## Address Translation and Mobility

A major structural shift in the Internet which has undermined the protocol design of IPv4, and has significantly reduced the freedom of end users to communicate and assemble in the introduction network address translation. {{RFC1631}} Network address translation is a process whereby organizations and autonomous systems to connect two networks by translating the IPv4 source and destination addresses between the two. This process puts the router performing the translation into a privileged position, where it can decide which subset of communications are worthy of translation, and whether an unknown request for communication will be correctly forwarded to a host on the other network.

This process of translation has widespread adoption despite promoting a process that goes against the stated end-to-end process of the underlying protocol [natusage]. In contrast, the proposed mechanism to provide support for mobility and forwarding to clients which may move, encoded instead as an option in the IP protocol in {{RFC5944}}, has failed to gain traction. This situation again suggests that the compromise made in design of the protocol has resulted in a technology which failed to technical encode the freedom of expression goals it was designed to promote.

# DNS

The Domain Name System (DNS), as specified in RFC 1035, acts as a core switchboard for the internet - associating human readable names with services. The DNS system operates a centralized core of ‘Root Resolvers’ , servers run by a set of organizations trusted by IANA to enact the organization’s decisions by accurately communicating which organizations have been delegated to manage registration under each Top Level Domain (TLD). Top Level domains are maintained and determined by IANA, and have evolved to encompass several classes of
services. Some, like ‘.Com’ and ‘.Net’, provide a common space for expression of ideas, though their policies are enacted through US based countries. Other name spaces are delegated to specific nationalities, and may impose limits designed to focus speech in those forums both to promote speech from that nationality, and to comply with local limits on expression and social norms. Finally, the system has been recently expanded with the addition of “generic TLDs”, name spaces with accompanying regulations aimed to promote expression
around specific topics, for instance ‘.travel’ and ‘.ninja’.

DNS has significant privacy issues, as described in RFC 7626. Notably amongst these, the protocol does not offer either encryption to limit the visibility of requests for domain resolution from several intermediary parties, nor does it offer authentication, allowing the
client to know that they have received a correct, “authoritative”, answer to a query. Together, these decisions have resulted in ongoing harm to freedom of expression as the DNS protocol has become one of the central mechanisms used to block access to websites - limiting
both the freedom of expression of the publisher to offer their content, and the freedom of assembly for clients to congregate in a shared virtual space.

There have been several mechanisms used impose these limitations based on the technical design of the DNS protocol. These have led to a number of situations where limits on expression have been imposed through subversion of the DNS protocol. Each of these situations has accompanying aspects of protocol design enabling those limitations.

## Removal of records

There have been a number of cases where the records for a domain are removed from the name system due to real-world events. Examples of this removal include ‘seizure’ of names of illegally operating gambling operations by the United States ICE unit by compelling the
US-based registrar in charge of the .com TLD to hand ownership of those domains over to the government. The same technique has been notably used by Libya to remove sites in violation of “our Country’s Law and Morality [which] do not allow any kind of pornography or its
promotion.” 

At a protocol level, the ability to seize domain names is enabled by the lack of transparency into DNS transfers, or any technical encoding of name ownership. Name ownership is purely a policy decision of registrars. While DNSSEC addresses distortion events described below,
it does not tackle this problem, which is has the cooperation of (or compels) the registrar.

Documentation of this form of harm:
[1] http://news.bbc.co.uk/2/hi/technology/7250916.stm
[2]
http://techyum.com/2010/10/official-vb-ly-link-shortener-seized-by-libya
n-government/

## Distortion of records

The most common mechanism by which the DNS system is abused to limit freedom of expression is through manipulation of protocol messages by the network. One form occurs at an organizational level, where client computers are instructed to use a local DNS resolver controlled by the organization. The DNS resolver will then selectively distort responses
rather than request the authoritative lookup from the upstream system. The second form occurs through the use of deep packet inspection, where all DNS protocol messages are inspected by the network, and objectionable content is distorted.

At the national level, there are additional considerations. The most notable is the interactions between DNS distortion and internet routing. A study on collateral damage showed that the restrictions imposed by China on DNS responses in its network also affected the
availability of sites to users in Germany, since some fraction of requests would transit through the Chinese network, even though none of the participants were located there.

A notable instance of distortion has occurred in Greece [3], where a study found evidence of both of deep packet inspection to distort DNS replies, and overblocking of content, where ISPs prevented clients from resolving the names of domains which they were not instructed to
do through the governmental order prompting the blocking systems there.

At a protocol level, the effectiveness of these attacks is made possible by a lack of authentication in the DNS protocol. The DNSSEC protocol is not widely in use, but provides an extension allowing the client to know that a response is ‘Authoritative’ - that it has been
generated by the server which has technical ownership of the name requested. Even still, there are a range of downgrade attacks, where a client may continue to follow the resolution of an injected message without such a signature, since it may not know that it should expect
the response to be signed. Selective distortion of records has also been made possible by the predictable structure of DNS messages, which make it computationally easy for a network device to watch all passing messages even at high speeds, and the lack of encryption, which allows the network to distort only an objectionable subset of protocol messages.

Documentation of this form of harm:
[1] http://conferences.sigcomm.org/sigcomm/2012/paper/ccr-paper266.pdf
[2] http://policyreview.info/articles/analysis/internet-censorship-turke
y
[3]
https://www.usenix.org/system/files/conference/foci15/foci15-paper-verve
ris-update.pdf
[4] https://tools.ietf.org/html/draft-hall-censorship-tech-01

## Injection of records

Responding incorrectly to requests for name lookups is the most common mechanism that in-network devices use to limit the ability of end users to discover services. A deviation which accomplishes a similar objective, though may be seen as different from a freedom of expression perspective, is the injection of incorrect responses to queries.  The most prominent example of this behavior occurs in China, where requests for lookups of sites which have been deemed inappropriate will trigger the network to respond with a bogus
response, causing the client to ignore the real response when it subsequently arrives. Unlike the other forms of discussion discussed above, injection does not stifle the ability of a server to announce it’s name, it instead provides another voice which answers sooner.
This is effective because of the DNS protocol’s decision to provide whatever answer it receives first, and stop listening for subsequent answers, and enabled by the lack of authentication or encryption in the protocol.

Documentation of this form of harm:
[1]
https://www.usenix.org/system/files/conference/foci14/foci14-anonymous.p
df


# HTTP

The Hypertext Transfer Protocol (HTTP), described in its version 1.1 in RFC2616, is a request-response application protocol developed throughout the 1990s, and factually contributed to the exponential growth of the Internet and the inter-connection of populations around
the world. Because of its simple design, HTTP has become the foundation of most modern Internet platforms and communication systems, from websites, to chat systems, and computer-to-computer applications. In its manifestation with the World Wide Web, HTTP has radically revolutionized the course of technological development and the ways people interact with online content and with each other. 
However, HTTP is also a fundamentally insecure protocol, that doesn't natively provide encryption properties. While the definition of the Secure Sockets Layer (SSL), and later of Transport Layer Security (TLS), also happened during the 1990s, the fact that HTTP doesn't
mandate the use of such encryption layers to developers and service providers, caused a very late adoption. Only in the middle of the 2000s we observed big Internet service providers, such as Google, starting to provide encrypted access to their web services.

The lack of sensitivity and understanding of the critical importance of securing web traffic incentivized malicious and offensive actors to develop, deploy and utilize at large interception systems and later active injection attacks, in order to swipe large amounts of data, compromise Internet-enabled devices. The commercial availability of systems and tools to perform these types of attacks also led to a number of human rights abuses that have been discovered and reported over the years and that painted a dark picture on the current state
of control over the Internet.

Generally we can identify in Traffic Interception and Traffic Manipulation the two most problematic attacks that can be performed against applications employing a clear-text HTTP transport layer.

## Traffic Interception


While we are seeing an increasing trend in the last couple of years to employ SSL/TLS as a secure traffic layer for HTTP-based applications, we are still far from seeing an ubiquitous use of encryption on the World Wide Web. It is important to consider that the adoption of
SSL/TLS is also a relatively recent phenomena. Google introduced an option for its GMail users to navigate with SSL only in 2008[1], and turned SSL on by default later in 2010[2]. It took an increasing amount of scandalous security breaches and revelations on global
surveillance from Edward Snowden to have other Internet service providers to follow Google's lead. For example, Yahoo enabled SSL/TLS by default on its webmail services only towards the end of 2013[3].

As we learned through the Snowden's revelations, intelligence agencies have been intercepting and collecting unencrypted traffic at large for many years. There are documented examples of such mass surveillance programs with GCHQ's TEMPORA and NSA's XKEYSCORE. Through these
programs NSA/GCHQ have been able to swipe large amounts of data including email and instant messaging communications which have been transported by the respective providers in clear for years, unsuspecting of the pervasiveness and scale of governments' efforts and investment into global mass surveillance capabilities.

However, similar mass interception of unencrypted HTTP communications is also often employed at a nation-level by less democratic countries by exercising control over state-owned Internet Service Providers (ISP) and through the use of commercially available monitoring,
collection, and censorship equipment. Over the last few years a lot of information has come to public attention on the role and scale of a surveillance industry dedicated to develop interception gear of different types. We have several records of such equipment being sold and
utilized by oppressive regimes in order to monitor entire segments of population especially at times of social and political distress, uncovering massive human rights abuses. For example, in 2013 the group Telecomix revealed that the Syrian regime was making use of BlueCoat products in order to intercept clear-text traffic as well as to enforce censorship of unwanted content[7]. Similarly in 2012 it was found that the French Amesys provided the Gaddafi's government with equipment able to intercept emails, Facebook traffic, and chat
messages ad a country level. The use of such systems, especially in the context of the Arab
Spring and of civil uprisings against the dictatorships, has caused serious concerns of significant human rights abuses in Libya.

## Traffic Manipulation

The lack of a secure transport layer over HTTP connections not only exposes the users to interception of the content of their communications, but is more and more commonly abused as a vehicle for active compromises of computers and mobile devices. If an HTTP session travels in clear over the network, any node positioned at any point in the network is able to perform man-in-the-middle attacks and observe, manipulate, and hijack the session and modify the content of the communication in order to trigger unexpected behavior by the application
generating the traffic. For example, in the case of a browser the attacker would be able to inject malicious code in order to exploit vulnerabilities in the browser or any of its plugins. Similarly, the attacker would be able to intercept, trojanize, and repackage binary
software updates that are very commonly downloaded in clear by applications such as word processors and media players. If the HTTP session would be encrypted, the tampering of the content would not be possible, and these network injection attacks would not be successful.

While traffic manipulation attacks have been long known, documented, and prototyped especially in the context of WiFi and LAN networks, in the last few years we observed an increasing investment into the production and sale of network injection equipment both available commercially as well as deployed at scale by intelligence agencies.
For example we learned from some of the documents provided by Edward Snowden to the press, that the NSA has constructed a global network injection infrastructure, called QUANTUM, able to leverage mass surveillance in order to identify targets of interests and
subsequently task man-on-the-side attacks to ultimately compromise a selected device. Among other attacks, NSA makes use of an attack called QUANTUMINSERT[8] which intercepts and hijacks an unencrypted HTTP communication and forces the requesting browser to redirect to a
host controlled by NSA instead of the intended website. Normally, the new destination would be an exploitation service, referred in Snowden documents as FOXACID, which would attempt at executing malicious code in the context of the target's browser. The Guardian reported in 2013 that NSA has for example been using these techniques to target users of the
popular anonymity service Tor[9]. The German NDR reported in 2014 that NSA has also been using its mass surveillance capabilities to identify Tor users at large[10].
Recently similar capabilities of Chinese authorities have been reported as well in what has been informally called the "Great Cannon"[11], which raised numerous concerns on the potential curb on human rights and freedom of speech due to the increasing tighter
control of Chinese Internet communications and access to information. 
Network injection attacks are also made widely available to state actors around the world through the commercialization of similar, smaller scale equipment that can be easily acquired and deployed at a country-wide level. Companies like FinFisher and HackingTeam are known
to have network injection gear within their products portfolio, respectively called FinFly ISP and RCS Network Injector[12]. The technology devised and produced by HackingTeam to perform network traffic manipulation attacks on HTTP communications is even the subject of a patent application in the United States[13]. Access to offensive technologies available on the commercial lawful interception market has been largely documented to have lead to human rights abuses and illegitimate surveillance of journalists, human rights defenders,
and political activists in many countries around the world. Companies like FinFisher and HackingTeam have been found selling their products to oppressive regimes with little concern for bad human rights records[14]. While network injection attacks haven't been the subject
of much attention, they do enable even unskilled attackers to perform silent and very resilient compromises, and unencrypted HTTP remains one of the main vehicles.


[1] http://gmailblog.blogspot.de/2008/07/making-security-easier.html
[2]
http://gmailblog.blogspot.de/2010/01/default-https-access-for-gmail.html
[3]
https://www.washingtonpost.com/news/the-switch/wp/2013/10/14/yahoo-to-ma
ke-
ssl-encryption-the-default-for-webmail-users-finally/
[4] http://www.theguardian.com/uk/2013/jun/21/gchq-cables-secret-world-
communications-nsa
[5] https://theintercept.com/2015/07/01/nsas-google-worlds-private-
communications/
[7]
http://en.rsf.org/syria-syria-using-34-blue-coat-servers-23-05-2013,4466
4
.html
[8] http://blog.fox-it.com/2015/04/20/deep-dive-into-quantum-insert/
[9]
http://www.theguardian.com/world/2013/oct/04/tor-attacks-nsa-users-onlin
e-
anonymity
[10] http://daserste.ndr.de/panorama/aktuell/nsa230_page-1.html
[11] https://citizenlab.org/2015/04/chinas-great-cannon/
[12] https://citizenlab.org/2014/08/cat-video-and-the-death-of-clear-tex
t/
[13] http://www.google.com/patents/EP2601774A1?cl=en
[14]
http://www.wired.co.uk/news/archive/2015-07/06/hacking-team-spyware-comp
any-hacked

# XMPP

The Extensible Messaging and Presence Protocol (XMPP), specified in RFC 3920, provides a standard for interactive chat messaging, and has evolved to encompass interoperable text, voice, and video chat. The protocol is structured as a federated network of servers, similar to email, where users register with a local server which acts one their behalf to cache and relay messages. This protocol design has many advantages, allowing servers to shield clients from denial of service and other forms of retribution for their expression, and designed to avoid central entities which could control the ability to communicate or assemble using the protocol.

None-the-less, there are plenty of aspects of the protocol design of XMPP which shape the ability for users to communicate freely, and to assembly through the protocol. In addition to issues of user registration and a lack of protocol specification of the registration policy, the protocol also has facets that may stifle speech as users self-censor for fear of surveillance, or find themselves unable to express themselves naturally.

## User Identification

The XMPP specification specifies that clients are identified with a resource (<node@domain/home> / <node@domain/work>) to distinguish the conversations to specific devices. This has the side effect of enabling tracking of user behavior by a remote friend or server, who are able to track presence not only of the user, but of each individual device. This has proven to be misleading to many users, since many clients only expose user level rather than device level presence. Likewise, user invisibility so that communication can occur while users don’t notify all buddies and other servers of their availability is not part of the formal protocol, and has only been added as an extension within the XML stream rather than enforced by the protocol.

Documentation of this form of harm:
[1] https://developer.pidgin.im/ticket/4322

## Character Encoding

Localization is a source of frustration in many protocols, and appears in some forms of XMPP. The XMPP protocol specifies a requirement for UTF-8 and UTF-16 support [1], though documentation admits that many implementations may not support UTF-16 [2]. In practice, this leads to cases where text encoded outside of a standard english language ascii encoding will fail to render on all clients, limiting the ability of users to communicate in their native languages. Some examples are failure of XMPP servers to handle non-ascii passwords [3], and gateways which simply strip all non-ascii from the conversation stream.

At the protocol level, XMPP only defines the conversation as an XML block, and leaves the implementation of character sets to the XMPP parsers of each individual client and server. While there have been attempts to define UTF-16 support as part of the protocol specification, the lack of actual implementation of the more extensible character set by all clients has shaped the protocol to harm the full range of expression users may desire.

Documentation of this form of harm:
[1] http://mail.jabber.org/pipermail/xmppwg/2003-August/001460.html
[2] http://xmpp.org/rfcs/rfc6120.html#streams-error-conditions-unsupported-encoding
[3] https://support.process-one.net/browse/EJAB-476
[4] https://wiki.bitlbee.org/HowtoFacebookXMPP

## Surveillance of Communication

The XMPP protocol specifies the standard by which communication of channels may be encrypted, but it does not provide visibility to clients of whether their communications are encrypted on each link. In particular, even when both clients ensure that they have an encrypted connection to their XMPP server to ensure that their local network is unable to read or disrupt the messages they send, the protocol does not provide visibility into the encryption status between the two servers. As such, clients may be subject to selective disruption of communications by an intermediate network which disrupts communications based on keywords found through Deep Packet Inspection.

In particular, section 13.14 of the protocol specification [2] explicitly acknowledges the existence of a downgrade attack where an adversary controlling an intermediate network can force the inter domain federation between servers to revert to a non-encrypted protocol were selective messages can then be disrupted.

Documentation of this form of harm:
[1] https://raw.githubusercontent.com/stpeter/manifesto/master/manifesto.txt
[2] https://www.ietf.org/rfc/rfc6120.txt


## Group Chat Limitations

Group chat in the XMPP protocol is defined as an extension within the XML specification of the XMPP protocol [1]. However, it is not encoded or required at a protocol level, and not uniformly implemented by clients.

The design of multi-user chat in the XMPP protocol suffers from extending a protocol that was not designed with assembly of many users in mind. In particular, in the federated protocol provided by XMPP, multi-user communities are implemented with a distinguished ‘owner’, who is granted control over the participants and structure of the conversation.

Multi-user chat rooms are identified by a name specified on a specific server, so that while the overall protocol may be federated, the ability for users to assemble in a given community is moderated by a single server. That server may block the room and prevent assembly unilaterally, even between two users neither of whom trust or use that server directly.

[1] http://xmpp.org/extensions/xep-0045.html



# Peer to Peer

Peer-to-Peer (P2P) is a network architecture (defined in RFC7574) in which all the participant nodes are equally responsible engaged into the storage and dissemination of information. A P2P network is a logical overlay that lives on top of the physical network, and allows nodes (or "peers") participating to it to establish contact and exchange information directly from one to each other. The implementation of a P2P network may very widely: it may be structured or unstructured, and it may implement stronger or weaker cryptographic and anonymity properties. While its most common application has traditionally been file-sharing (and other types of content delivery systems), P2P is increasingly becoming a popular architecture for networks and applications that require (or encourage) decentralization. A prime example is Bitcoin (and similar cryptocurrencies), as well as Skype, Spotify and other proprietary multimedia applications.

In a time of heavily centralized online services, peer-to-peer is often seen as an alternative, more democratic, and resistant architecture that displaces structures of control over data and communications and delegates all peers equally to be responsible for the functioning, integrity, and security of the data. While in principle peer-to-peer remains critical to the design and development of future content distribution, messaging, and publishing systems, it poses numerous security and privacy challenges which are mostly delegated to individual developers to recognize, analyze, and solve in each implementation of a given P2P network.


## Network Poisoning

Since content, and in some occasions peer lists, are safeguarded and distributed by its members, P2P networks are prone to what are generally defined as "poisoning attacks". Poisoning attacks might be directed directly at the data that is being distributed, for example by intentionally corrupting it, or at the index tables used to instruct the
peers where to fetch the data, or at routing tables, with the attempt of providing connecting peers with lists of rogue or non-existing peers, with the intention to effectively cause a Denial of Service on the network.


## Throttling

Peer-to-Peer traffic (and BitTorrent in particular) represents a high percentage of global Internet traffic and it has become increasingly popular for Internet Service Providers to perform throttling of customers lines in order to limit bandwidth usage [torrentfreak1] and sometimes probably as an effect of the ongoing conflict between copyright holders and file-sharing communities [wikileaks].

Throttling the peer-to-peer traffic makes some uses of P2P networks ineffective and it might be coupled with stricter inspection of users' Internet traffic through Deep Packet Inspection techniques which might pose additional security and privacy risks.


## Tracking and Identification


One of the fundamental and most problematic issues with traditional peer-to-peer networks is a complete lack of anonymization of its users. For example, in the case of BitTorrent, all peers' IP addresses are openly available to the other peers. This has lead to an ever-increasing tracking of peer-to-peer and file-sharing users [ars]. As the geographical
location of the user is directly exposed, and so could be his identity, the user might become target of additional harassment and attacks, being of physical or legal nature. For example, it is known that in Germany lawfirms have made extensive use of peer-to-peer and file-sharing
tracking systems in order to identify downloaders and initiate legal actions looking for compensations [torrenfreak2].

It is worth nothing that there are varieties of P2P networks that implement cryptographic practices and that introduce anonymization of its users. Such implementations proved to be successful in resisting censorship of content, and tracking of the network peers. A primary
example is FreeNet [freenet1], a free software application designed to significantly increase the difficulty of users and content identification, and dedicated to foster freedom of speech online[freenet2].


## Conclusions

Encrypted P2P and Anonymous P2P networks already emerged and provided viable platforms for sharing material, publish content anonymously, and communicate securely [bitmessage]. If adopted at large, well-designed and resistant P2P networks might represent a critical component of a futuresecure and distributed Internet, enabling freedom of speech and freedom
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


