--- 
title: QUIC Human Rights Review
abbrev: QUIC-HR
docname: draft-martini-hrpc-quichr-00
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
       ins: B. Martini
       name: Beatrice Martini
       organization: Harvard Kennedy School
       email: mail@beatricemartini.it

-
       ins: N. ten Oever
       name: Niels ten Oever
       organization: University of Amsterdam
       email: mail@nielstenoever.net

normative:
  
informative: 

   RFC1958:
   RFC2026:
   RFC2775:
   RFC3629:
   RFC3724:
   RFC4084:
   RFC4949:
   RFC4960:
   RFC6582:
   RFC6973:
   RFC7258:
   RFC7754:
   RFC8404:
   RFC8280:

   Brown:
     title: "A Prehistory of Internet Governance"
     date: 2013
     author:
        - ins: I. Brown
        - ins: M. Ziewitz
     seriesinfo: Research Handbook on Governance of the Internet. Cheltenham, Edward Elgar.

   UDHR:
     title: The Universal Declaration of Human Rights
     date: 1948
     author:
        - org: United Nations General Assembly
     target: http://www.un.org/en/documents/udhr/

   ICESCR:
     title: International Covenant on Economic, Social and Cultural Rights
     date: 1966
     author:
        - org: United Nations General Assembly
     target: http://www.ohchr.org/EN/ProfessionalInterest/Pages/CESCR.aspx

   ICCPR:
     title: International Covenant on Civil and Political Rights
     date: 1976
     author:
        org: United Nations General Assembly
     target: http://www.ohchr.org/EN/ProfessionalInterest/Pages/CCPR.aspx

   draft-trammell-quic-spin-03:
      title: The Addition of a Spin Bit to the QUIC Transport Protocol (working document)
      author:
         - ins: B. Trammell
         - ins: P. De Vaere
         - ins: R. Evem
         - ins: G. Ficcola
         - ins: T. Fossati
         - ins: M. Ihlar
         - ins: A. Morton
         - ins: E. Stephan
      date: 2018
      target: https://tools.ietf.org/html/draft-trammell-quic-spin-03

   draft-huitema-quic-dnsoquic-05:
      title: Specification of DNS over Dedicated QUIC Connections (working document)
      author:
         - ins: C. Huitema
         - ins: M. Shore
         - ins: A. Mankin
         - ins: S. Dickinson
         - ins: J. Iyengar
      date: 2018
      target: https://tools.ietf.org/html/draft-huitema-quic-dnsoquic-05

   Ruethetal:
      title: A First Look at QUIC in the Wild
      author:
         - ins: J. Rueth
         - ins: I. Poese
         - ins: C. Dietzel
         - ins: O. Hohlfeld
      date: 2018
      target: https://arxiv.org/abs/1801.05168

   draft-ietf-quic-transport-12:
      title: "QUIC: A UDP-Based Multiplexed and Secure Transport (working document)"
      author:
         - ins: J. Iyengar
         - ins: M. Thomson
      date: 2018
      target: https://tools.ietf.org/html/draft-ietf-quic-transport-12

   draft-huitema-quic-mpath-req-01:
      title: QUIC Multipath Requirements (working document)
      author:
         - ins: C. Huitema
      date: 2018
      target: https://tools.ietf.org/html/draft-huitema-quic-mpath-req-01

   draft-joseph-quic-comparison-quic-sctp-00:
      title: A Comparison between SCTP and QUIC (working document)
      author:
        - ins: A. Joseph
        - ins: T. Li
        - ins: Z. He
        - ins: Y. Cui
        - ins: L. Zhang
      date: 2018
      target: https://tools.ietf.org/html/draft-joseph-quic-comparison-quic-sctp-00

   geekfeminism:
     title: Pseudonymity
     date: 2015
     author: 
        - org: Geek Feminism Wiki 
     target: http://geekfeminism.wikia.com/wiki/Pseudonymity

   FIArch:
     title: Future Internet Design Principles
     date: January 2012
     target: http://www.future-internet.eu/uploads/media/FIArch_Design_Principles_V1.0.pdf

   draft-ietf-quic-spin-exp-00:
      title: The QUIC Latency Spin Bit (working document)
      date: 2018
      author:
         - ins: B. Trammell
         - ins: M. Kuehlewind 
      target: https://tools.ietf.org/html/draft-ietf-quic-spin-exp-00

   Hall:
     title: A Survey of Worldwide Censorship Techniques (working document)
     date: 2015
     author:
        - ins: J. Hall
        - ins: M. Aaron
        - ins: B. Jones
     target: https://tools.ietf.org/html/draft-hall-censorship-tech-01

   Behretal:
      title: Introducing QUIC support for HTTPS load balancing
      author:
         - ins: M. Behr
         - ins: I.Swett
      date: 2018
      target: https://cloudplatform.googleblog.com/2018/06/Introducing-QUIC-support-for-HTTPS-load-balancing.html

   Kuehlewindetal:
      title: "A Path Layer for the Internet: Enabling Network Operations on Encrypted Protocol"
      author:
         - ins: M. Kuehlewind
         - ins: T. Buehler
         - ins: B.Trammell
         - ins: S. Neuhaus
         - ins: R. Muentener
         - ins: G. Fairhurst
      date: 2017
      target: https://nsg.ee.ethz.ch/fileadmin/user_upload/CNSM_2017.pdf 

   Ruethetal:
      title: A First Look at QUIC in the Wild
      author:
         - ins: J. Rueth
         - ins: I. Poese
         - ins: C. Dietzel
         - ins: O. Hohlfeld
      date: 2018
      target: https://arxiv.org/abs/1801.05168

   MolaviKakhkietal:
      title: Taking a Long Look at QUIC
      author:
         - ins: A. Molavi Kakhki
         - ins: S. Jero
         - ins: D. Choffnes
         - ins: C. Nita-Rotaru
         - ins: A. Mislove
      date: 2017
      target: https://david.choffnes.com/pubs/long-look-at-quic-imc17.pdf

   Wilketal:
      title: A QUIC update on Google’s experimental transport
      author:
         - ins: A. Wilk
         - ins: R.Hamilton
         - ins: I. Swett
      date: 2015
      target: https://blog.chromium.org/2015/04/a-quic-update-on-googles-experimental.html

   SpinBit:
      title: Explicit passive measurability and the QUIC Spin Bit
      author:
         - ins: B. Trammell
      date: 2018
      target: https://blog.apnic.net/2018/05/11/explicit-passive-measurability-and-the-quic-spin-bit/

   YetItSpins:
      title: And yet, it spins
      author:
         - ins: B. Trammell
      date: 2018
      target: https://trammell.ch/post/2018-03-29-and-yet-it-spins

--- abstract

QUIC (Quick UDP Internet Connections) is a new transport protocol that provides low-latency communication, security, and rapid deployment. QUIC’s key features include establishing connections faster, stream-based multiplexing, improved loss recovery, and no head-of-line blocking. QUIC is designed with mobility in mind, and supports migrating connections from WiFi to Cellular and back. {{Behretal}}

This document assesses the potential human rights implications emerging from the deployment of QUIC according to the methodology laid out in {{RFC8280}}.

--- middle

Introduction
============

This is a review done within the framework of the Human Rights Review Team, and it was conducted by Beatrice Martini and Niels ten Oever. The Human Rights Review Team aims to implement and improve the guidelines for human rights considerations provided in {{RFC8280}}, and seeks to mitigate potentially adverse human rights impacts that IETF and IRTF documents might have.

Human Rights Reviews are developed by a group of individuals in the IRTF and IETF. They work collaboratively and provide their knowledge and input to the assessments, in an effort to contribute to the IETF open review process. Human Rights Reviews are individual contributions. The authors hope that the comments will be taken into consideration by the draft authors, involved Working Groups and IESG.

This review concerns the QUIC protocol in general and the following drafts in particular:
draft-ietf-quic-transport, draft-ietf-quic-tls, draft-ietf-quic-invariants.

Vocabulary Used
===============

Anonymity
: The condition of an identity being unknown or concealed {{RFC4949}}.

Censorship
: Technical mechanisms, including both blocking and filtering, that certain political or private actors around the world use to block or degrade Internet traffic. For further details on the various elements of Internet censorship, see {{Hall}}.

Censorship resistance
: Methods and measures to mitigate Internet censorship.

Confidentiality
: The property that data is not disclosed to system entities unless they have been authorized to know the data {{RFC4949}}.

Connectivity
: The extent to which a device or network is able to reach other devices or networks to exchange data.  The Internet is the tool for providing global connectivity {{RFC1958}}. Different types of connectivity are further specified in {{RFC4084}}.

Content agnosticism: 
: Treating network traffic identically regardless of content.

Heterogeneity
: "The Internet is characterized by heterogeneity on  many levels: devices and nodes, router scheduling algorithms and queue management mechanisms, routing protocols, levels of multiplexing, protocol versions and implementations, underlying link layers (e.g., point-to-point, multi-access links, wireless, FDDI, etc.), in the traffic mix and in the levels of congestion at different times and places.  Moreover, as the Internet is composed of autonomous organizations and internet service providers, each with their own separate policy concerns, there is a large heterogeneity of administrative domains and pricing structures." {{FIArch}}

As a result, per {{FIArch}}, the heterogeneity principle proposed in {{RFC1958}} needs to be supported by design.

Human rights
: Principles and norms that are indivisible, interrelated, unalienable, universal, and mutually reinforcing. Human rights have been codified in national and international bodies of law.  The Universal Declaration of Human Rights {{UDHR}} is the most well-known document in the history of human rights. The aspirations from {{UDHR}} were later codified into treaties such as the International Covenant on Civil and Political Rights {{ICCPR}} and the International Covenant on Economic, Social and Cultural Rights {{ICESCR}}, after which signatory countries were obliged to reflect them in their national bodies of law.  There is also a broad recognition that not only states have obligations in relation to human rights, but non-state actors do as well.

Integrity
: The property that data has not been changed, destroyed, or lost in an unauthorized or accidental manner {{RFC4949}}.

Linkability
: Establishing the identity of a host across several IP addresses

Open standards
: Conform with {{RFC2026}}, which states the following: "Various national and international standards bodies, such as ANSI, ISO, IEEE, and ITU-T, develop a variety of protocol and service specifications that are similar to Technical Specifications defined here.  National and international groups also publish 'implementors' agreements' that are analogous to Applicability Statements, capturing a body of implementation-specific detail concerned with the practical application of their standards.  All of these are considered to be 'open external standards' for the purposes of the Internet Standards Process."

Openness
: Absence of centralized points of control -- "a feature that is assumed to make it easy for new users to join and new uses to unfold" {{Brown}}.

Ossification
: The increasing inflexibility of the network which results in the inability to deploy a new protocol or protocol extensions due to the unchangeable nature of infrastructure components that have come to rely on a particular feature of the current protocols.

Permissionless innovation
: The freedom and ability to freely create and deploy new protocols on top of the communications constructs that currently exist.

Privacy
: The right of an entity (normally a person), acting on its own behalf, to determine the degree to which it will interact with its environment, including the degree to which the entity is willing to share its personal information with others {{RFC4949}}.

: The right of individuals to control or influence what information related to them may be collected and stored, and by whom and to whom that information may be disclosed.

: Privacy is a broad concept relating to the protection of individual or group autonomy and the relationship between an individual or group and society, including government, companies, and private individuals.  It is often summarized as "the right to be left alone", but it encompasses a wide range of rights, including protections from intrusions into family and home life, control of sexual and reproductive rights, and communications secrecy.  It is commonly recognized as a core right that underpins human dignity and other values such as freedom of association and freedom of speech. The right to privacy is also recognized in nearly every national constitution and in most international human rights treaties.  It has been adjudicated upon by both international and regional bodies.  The right to privacy is also legally protected at the national level through provisions in civil and/or criminal codes.

Pseudonymity
: Pseudonymity is the ability to use a persistent identifier that is not immediately linked to one's offline identity -- is an important feature for many end users, as it allows them different degrees of disguised identity and privacy online.

: Pseudonymity means using a pseudonym instead of one's "real" name.  There are many reasons for users to use pseudonyms -- for instance, to hide their gender; protect themselves against harassment; protect their families' privacy; frankly discuss sexuality; or develop an artistic or journalistic persona without retribution from an employer, (potential) customers, or social surroundings {{geekfeminism}}.  The difference between anonymity and pseudonymity is that a pseudonym is often persistent. "Pseudonymity is strengthened when less personal data can be linked to the pseudonym; when the same pseudonym is used less often and across fewer contexts; and when independently chosen pseudonyms are more frequently used for new actions (making them, from an observer's or attacker's perspective, unlinkable)." {{RFC6973}}


Human Rights Considerations
===========================

We analyzed all the drafts of the IETF QUIC Working Group which were active at the time of review (July 2018), and invited Working Group chairs and document authors for interviews during IETF102. Inferential reading of the drafts resulted in the baseline for a questionnaire, which was used to guide the interviews. The interviews were conducted as 60-90-minute discussions, which were then transcribed and analyzed. The analysis focused on the identification of potential positive or negative impacts on human rights, and the categorization of the same according to the Guidelines for Human Rights Protocol Considerations outlined in {{RFC8280}}.

The Human Rights Protocols Considerations Research Group (HRPC) welcomes the drafts draft-ietf-quic-transport, draft-ietf-quic-tls, draft-ietf-quic-invariants. In particular, we welcome the efforts to improve connectivity on high latency, low bandwidth and high loss connections, and the application of end-to-end encryption by default. Final conclusions and recommendations can be found at the end of this document.

No implications for Accessibility ({{RFC8280}}, sec. 6.2.11), Localization ({{RFC8280}}, sec. 6.2.12), Decentralization ({{RFC8280}}, sec. 6.2.13), have been found.

## Connectivity

Overall, QUIC is expected to result in a greatly improved Internet service for users worldwide, and in particular for those who currently do not have high bandwidth or lossless connections. Regions that currently do not benefit from reliable connectivity, would be provided with a significantly improved service. These advancements have positive implications in regards to human rights such as freedom of expression, freedom of association, right to political participation.

### Latency

QUIC was designed as a new transport protocol to provide connections with lower latency than previous protocols. 

One of the most important differences between TCP and QUIC connections is that in QUIC connection establishment takes 0 RTTs when a server is known by a client and 1 RTT for the first connection to an unknown server.

By allowing for Zero-Round Trip (0-RTT) resumption of connections, QUIC performs better than TCP on high latency and high loss connections. When a web client uses TCP and TLS, it requires two to three round trips with a server to establish a secure connection before the browser can send a request. With QUIC, if a client has communicated with a server before (within a specific time period), it can start sending data without any round trips, so that web pages will load faster. 

An example of QUIC’s performance can be observed on a well-optimized site like Google Search, where connections are often pre-established, and QUIC’s faster connections can only speed up some requests. Still, QUIC improves mean page load time by 8% globally, and up to 13% in regions where latency is higher. {{Behretal}}

### Congestion control and loss recovery

QUIC’s congestion control is based on TCP NewReno {{RFC6582}}, a congestion window based congestion control. The signals QUIC provides for congestion control are generic and are designed to support different algorithms. In this way, QUIC can be configured to fit best in different contexts.

Compared to TCP, QUIC offers more detailed feedback information for loss detection.
For example, it uses a monotonically increasing packet number but does not retransmit on the packet-level. This allows QUIC to distinguish retransmissions from the originally sent packets, avoiding retransmission ambiguities.

Overall, comparing it to previously existing protocols, QUIC implements better estimation of connection RTTs and detects and recovers from loss more efficiently.

### Reduced head-of-line blocking

HTTP/2 allows multiple objects to be fetched over the same connection, using multiple streams within a single flow.

In TCP, if a loss occurs in one stream, all streams stall while waiting for packet recovery. Differently, QUIC allows other streams to continue to exchange packets even if one stream is blocked due to a missing packet {{MolaviKakhkietal}}.

## Privacy

### End-to-end encryption

QUIC incorporates the key negotiation features of TLS 1.3, requiring all connections to be encrypted.

Encryption improves the security and privacy of user data. It is built into QUIC, using AEAD algorithms such as AES-GCM and ChaCha20 for both privacy and integrity. QUIC authenticates the parts of its headers that it does not encrypt, so attackers cannot modify any part of a message {{Behretal}}.

Furthermore, in addition to improving privacy, encryption helps to address the ossification of network protocols caused by middleboxes that assume certain information to be present in the clear {{Kuehlewindetal}}.

### Transparent proxying

Many cellular and high-latency networks use transparent TCP proxies to reduce end-to-end delays and improve loss recovery. However, by encrypting the transport headers, QUIC prevents transparent proxying, thus protecting their integrity {{MolaviKakhkietal}}.

### Multiple streams

By establishing connection with multiple streams, QUIC creates higher opacity for the observer.

Comparing QUIC to TLS over TCP, QUIC significantly reduces the amount of information that an observer can acquire about communications they are looking at.

In TCP, all of the information regarding the protocol flow at a transport layer is exposed, and can be used to identify active communications.

In QUIC, it is possible to have an established connection with an end point and to run multiple streams over that connection. Consequently, an observer who is looking at someone's connection, would not be able to tell the difference between the streams.

### Packet number encryption

A compelling debate with human rights implications which is happening in the QUIC Working Group regards packet number encryption.

From a general standpoint, the number assigned to each packet carries very little information. For example, it is possible to observe that a packet sent a certain time and the packet that was sent immediately after probably have increasing packet numbers.

But when traffic is carried over multiple paths, it becomes observable at many points, and this has privacy implications. For example, as stated in {{draft-huitema-quic-mpath-req-01}}: "[...] if packets belonging to a given connection carry some unique identifiers, observers could use these identifiers to track client migrations through several paths, and thus potentially expose the successive locations of a particular user."

### Padding

Bit padding is the addition of one or more extra bits to a transmission or storage unit to make it conform to a standard size.

QUIC (like HTTP/2 and TLS) offers a padding mechanism that can be used as a defense against traffic analysis for protected packets. It is important to note that its use is discretionary by implementations.

### Lawful intercept

The lawful intercept of content in QUIC works similarly to TLS over TCP. Intercept can: force the acceptance of an alternate certificate; cooperate with or coerce the non-monitored endpoints to obtain session keys for decryption of traffic; exploit endpoint vulnerabilities to place monitoring devices directly on the endpoint on the other side of the crypto boundary. 

Forcing TLS 1.3 avoids some common exploit vectors in TLS 1.2 and strengthens the ciphersuites.

### Spin bit

When Google offered the IETF the opportunity to take the work on QUIC and produce an open standard that could be used by all {{Wilketal}}, it sparked off a debate within the IETF as to how much transport information should be deliberately kept unknown to the network.

As an explicit design goal, QUIC provides far less information about its operation to devices on path than TCP does. In TCP, the sequence and acknowledgement numbers and timestamps (if the respective option is in use) can be seen by on-path observers, and used to estimate end-to-end latency.

Differently from previous transport protocols, QUIC splits the information it uses for its own operation from its wire image. As a consequence, QUIC's wire image currently does not expose any information that can be used for passive latency measurement techniques {{draft-ietf-quic-spin-exp-00}}.

At the June 2017 interim meeting of the QUIC Working Group, a proposal was made to add a latency spin bit back into QUIC's wire image, in order to allow for passive measurability of RTT equivalent to TCP {{SpinBit}}.	

The spin bit is an explicit signal for passive measurability of round-trip time. It causes one bit in the header to ‘spin’, generating one edge (a transition from 0 to 1 or from 1 to 0) once per end-to-end RTT.

During the following months, the proposal to add this facility to the QUIC protocol has been further discussed and researched. At IETF101 the Working Group agreed upon the reservation of three bits for experimentation with passive RTT measurement, with the result of this experimentation to inform an eventual working group decision to include the bit in the “shipping” version 1 of the protocol, scheduled to be complete by November 2018. {{YetItSpins}}

From its designers' perspective, the spin bit was formulated to be a minimal-risk, maximum-utility signal fit for a single purpose: on-path measurement of end-to-end RTT, to generate RTT samples for a variety of passive latency measurement tasks.

The key argument in favor of the spin bit originates from the notion that measurement is fundamental to the operation of networks and at-scale services, whether for management, security, optimization, and that if it is at all possible to safely design passive measurability of any metric explicitly into a protocol, this signal represents how to do it. {{https://blog.apnic.net/2018/05/11/explicit-passive-measurability-and-the-quic-spin-bit}}

The argument made by those who are not in favor of the addition of the spin bit to the protocol, is that the exposure of any information beyond the IP header and the base essentials of a UDP header is not necessary and not safe. They point out that how this bit may be used, were it to be added to the protocol, is unknown, and that the bits could end up exposing the same level of session control information that was in the now encrypted TCP header.

This would represent an infringement of the user privacy. Furthermore, from this perspective, QUIC’s efforts to elude the intrusive and ossifying grip of network middleware would be lost. {{https://blog.apnic.net/2018/03/28/just-one-quic-bit}}

## Content agnosticism
               
The QUIC protocol itself is content agnostic. While it is currently being optimized for HTTP traffic, it can also be used with other application layer protocols (e.g. see {{draft-huitema-quic-dnsoquic-05}}).

## Security

QUIC improves security by making end-to-end encryption an inherent part of the transport protocol, instead of adding it as a optional layer on top of it. This protects the integrity of the data by preventing tampering on the path, and ensures end-to-end confidentiality between the two communicating hosts. Furthermore, it ensure that no on-path party can emulate an endpoint.

By encrypting all Internet traffic by default it is harder for researchers and network operators to analyze network traffic. This is a specific design goal, but it also makes research into the promulgation of malware, cookies and other artefacts much harder, since in this case access to the stream needs to be provided by the end point.

## Internationalization

QUIC raises two issues in terms of internationalization.

The first issues regards the fact that {{draft-ietf-quic-transport-12}} does not define human readable strings, except for where it states that the Reason Phrase in the CONNECTION_CLOSE and APPLICATION_CLOSE frames "SHOULD be a UTF-8 encoded string {{RFC3629}}". The QUIC protocol demands that this SHOULD be an UTF-8 string, while UTF-8 is actually not required. Also, there is currently no space to declare the charset used. So it is recommended that this SHOULD becomes a MUST.

The second issue concerns the lack of availability of language tags. This would allow implementations to signal in which language Reason Phrases are rendered.

## Censorship resistance

End-to-end encryption makes monitoring and filtering of the traffic more complex, thus hindering fine-grained censorship. Furthermore, in QUIC it is also harder to terminate connections, since in the protocol the only parties that can terminate the connection are those actually involved in the connection once it exists. This means that a middlebox cannot reset a connection, but needs to continue to block it, keeping state. Considering this, it can be stated that QUIC makes censorship harder because it requires the censor to invest more resources and efforts.

QUIC is also providing protection against DDoS through observation of the handshake for connection confirmation, and through the need to validate new connections in case of a connection migration.

## Open Standards

QUIC is published as open standard.

## Heterogeneity Support

QUIC is currently optimized to use TLS1.3 and serve HTTP2 traffic. It is explicitly constructed in a modular manner and is designed to support other application layer protocols as well.

## Anonymity

Persistent static identitifiers are the 

6.11.5.  Privacy Implications of Connection Migration

Using a stable connection ID on multiple network paths allows a passive observer to correlate activity between those paths.  An endpoint that moves between networks might not wish to have their activity correlated by any entity other than their peer, so different connection IDs are used when sending from different local addresses, as discussed in Section 6.1.  For this to be effective endpoints need to ensure that connections IDs they provide cannot be linked by any other entity.

This eliminates the use of the connection ID for linking activity from the same connection on different networks.  Protection of packet numbers ensures that packet numbers cannot be used to correlate activity.  This does not prevent other properties of packets, such as timing and size, from being used to correlate activity. Clients MAY move to a new connection ID at any time based on implementation-specific concerns.  For example, after a period of network inactivity NAT rebinding might occur when the client begins sending data again.

A client might wish to reduce linkability by employing a new connection ID and source UDP port when sending traffic after a period of inactivity.  Changing the UDP port from which it sends packets at the same time might cause the packet to appear as a connection migration.  This ensures that the mechanisms that support migration are exercised even for clients that don't experience NAT rebindings or genuine migrations.  Changing port number can cause a peer to reset its congestion state (see Section 6.11.4), so the port SHOULD only be changed in frequently.

Endpoints that use connection IDs with length greater than zero could have their activity correlated if their peers keep using the same destination connection ID after migration.  Endpoints that receive packets with a previously unused Destination Connection ID SHOULD change to sending packets with a connection ID that has not been used on any other network path.  The goal here is to ensure that packets sent on different paths cannot be correlated.  To fulfill this privacy requirement, endpoints that initiate migration and use connection IDs with length greater than zero SHOULD provide their peers with new connection IDs before migration.

Caution:  If both endpoints change connection ID in response to seeing a change in connection ID from their peer, then this can trigger an infinite sequence of changes.

## Pseudonymity

ADD STUFF

## Confidentiality

Through the use of cryptography, QUIC integrates security, confidentiality, authenticity, and integrity directly into the transport protocol rather than having them layered on top of it.
Any network operator who will use QUIC to benefit from its latency improvements will automatically provide all the aforementioned attributes to their user.

## Integrity

The use of TLS1.3 in QUIC makes on-path attacks either visible or nearly impossible to carry out. So, if an actor forces the traffic to go through one middlebox and decrypt the traffic itself, their action is made detectable.
This also protects the integrity of the datastream, prevents tampering, and averts the injection of extra data in the stream.

## Authenticity

Except for the initial handshake, the encryption in QUIC is provided by TLS1.3, which uses asymmetric cryptography to authenticate the hosts. This enables verification of authenticity.

## Adaptability

QUIC has a modular approach, and is designed for adaptation. The only commitments in the protocol are the requirement to run on UDP, the packet header, and the version negotiation phase. The remainder of the protocol is quite flexible and can be further adapted.

By preventing the ossification of the protocol by middleboxes through the encryption of transport headers, QUIC enhances the adaptability of the architecture.

As a transport protocol, QUIC tries to be agnostic for application layer protocols, even though it is currently optimized for HTTP2.

## Outcome Transparency

If QUIC will be successfully and widely deployed, as it seems to be the case {{Ruethetal}}, it will represent a remarkable evolution of the transport layer with equally significant impact on the Internet architecture. The following section will discuss the potential effects of QUIC on the wider protocol milieu, the Internet infrastructure and its users, and well as the key takeaways emerged during the review process in regards to the development of the protocol itself.

The IETF has reached consensus on the fact that pervasive monitoring is an attack (see {{RFC7258}}), and that a response to mitigate this is represented by ubiquitous encryption, which would also reinforce the end-to-end nature of the network {{RFC2775}} {{RFC3724}} {{RFC7754}}. With the advent of QUIC, encryption becomes the default on the transport level. This has an impact on network operators that previously used visible parts of protocols to, among other things, manage, operate, and secure their networks {{RFC8404}}. At the same time, it also improves the integrity of the datastream, as QUIC allows to protect users against injections of ads by network operators.

### Permissionless innovation and its challenges

As also stated by interviewees during the research phase of this review, the development of QUIC was partly inspired by the less pronounced uptake of SCTP (Stream Control Transmission Protocol), a protocol for transmitting multiple streams of data at the same time between two end points that have established a connection in a network, standardized in {{RFC4960}}.

As outlined in the comparison between SCTP and QUIC presented in {{draft-joseph-quic-comparison-quic-sctp-00}}, the deployment of SCTP is not particularly widespread. In-network devices, like NAT gateways for example, do not support SCTP well. NAT gateways need to be upgraded to be SCTP-aware, the modification of middleboxes is very expensive, and Internet service providers, focusing on the sustainability of their business, update the devices in accordance with the benefit that this can represent for their revenues.

Furthermore, QUIC was designed by a large content provider, Google. In was implemented in 2012, and the company invested significant resources to develop it, for example conducting thorough A/B-testing in order to assess how the protocol would interact with the network, and how the middleboxes would respond. QUIC is now widely used in Chrome clients accessing Google services.

In 2015, an Internet Draft of a specification for QUIC was submitted to the IETF for standardization, and the following year the QUIC Working Group was established. A growing number of contributors from the corporate, academic, nonprofit sector have joined the protocol development work since, and what has been achieved to date is the result of a notable and labor-intensive collaborative effort.

So, on one hand, the history of QUIC shows that permissionless innovation is still possible. On the other hand, it also shows what remarkable efforts and resources are needed to carry out such an ambitious project.
While permissionless innovation still exists, the threshold and costs for innovation seem to rise significantly and increasingly.

Also, a look at the actors and dynamics involved in QUIC’s history should not underestimate the power of Google’s authority. A different developing actor might have been able to invest a similar amount of resources into the development of a protocol. Still, without an impressive user base and traffic stream as Google's, they might have received a less supportive response from network operators.

### Privacy, power and consolidation

The most relevant privacy win provided by QUIC is for users who have different kinds of traffic relations with one end point. QUIC does not allow network providers to easily differentiate between, for instance, HTTP requests, DNS requests and real time voice packets, thus strengthening the user's right to privacy.

On the other hand, this creates a concentration of different kinds of traffic with one end point, thus giving the service provider access to more categories of privacy sensitive information.

In the current reality of the Internet, the biggest hosts are controlled by large, consolidated, transnational corporations. This creates an extreme power differential between end users on the one hand, and service providers and content operators on the other hand.

In order to protect privacy and secure information, it is important that the user makes a careful and informed decision about the hosting provider and plan they choose.

While ubiquitous encryption changes the relation between service providers and content operators, placing them at the same end of the spectrum, it remains to be seen whether if it can help users take and retain control within the overall power structures of Internet governance and economics.

One of the problems with deploying fully encrypted protocols like QUIC is that deployment is far easier for organizations that already have integrated observability, traceability, and tooling in their backends, which not surprisingly happen to be the big players.

If there was any chance to make running a QUIC server relatively easy, thus enabling a greater diversification of end points, QUIC could contribute to a power shift in favor of the end user.

However, running a QUIC infrastructure is currently expected to be more demanding than running a HTTP/2 or HTTP/1 infrastructure. It would be truly compelling if this consideration could be discussed further, and ideally addressed by the development and release of openly available tooling allowing for more accessible ways to run a QUIC server.

### Transparency and IoT

As discussed, end-to-end encryption on the transport layer makes monitoring and filtering of the traffic more complex, thus forcing network operators to adopt new and more onerous network management practices.

This has implications also on the management of IoT (Internet of Things) devices. If an IoT device adopts QUIC, it will be harder for the company owning it to monitor what data is communicated with third parties. Moreover, also making research into the dissemination of cookies and malware might become more complex.

Adequate tooling to protect the right to privacy of IoT users has not yet been developed.

Conclusions and Recommendations
===============================

The QUIC protocol provides significant human rights improvements for end users.

First of all, it dramatically improves connectivity for users on high-loss, high-latency connections, whose needs are not frequently enough addressed by protocol design. They will benefit from lower latencies and will not need to restart sessions as often. And in those cases in which they will need to restart a session, they will able to do so without having to re-do the initial handshake.

Another key improvement is represented by the use of end-to-end encryption by default, which provides authentication, stream integrity, adaptability of the protocol by overcoming ossification, and improved protection from third party monitoring and metadata analysis.

The following is a list of potential improvements that we invite the QUIC Working group to take into consideration, wishing for the protocol to have even greater positive implications for human rights.

* Since the spin bit is supposed to be ruled either into the main spec or removed at IETF 103, we suggest to consider its removal, in light of the concerns raised in regards to its implications on the rights to privacy and access.

* Consider deploying IP header encryption on IPv6 networks, where NATs are not as widely deployed as on IPv4 networks, potentially as an optional extension.

* Add language tagging and charset identification in the case of Reason Phrase in the CONNECTION_CLOSE and APPLICATION_CLOSE.

* Translate the QUIC specification into other languages.

* Make tooling for running QUIC servers openly available.

* Recurrently monitor and discuss the implications of QUIC on the power relations between end user on one end of the spectrum, and network operators and service providers on the other one.

Acknowledgements
================

We would like to thank (in alphabetical order): Mike Bishop, dkg, Jana Iyengar, Mirja Kuehlewind, Mark Nottingham, Martin Thomson, and Brian Trammell for their contributions to this document (this document does not necessarily reflect their opinion, but solely that of the authors).

 
Security Considerations
========================

As this draft concerns a research document, there are no security considerations.


IANA Considerations
==========================

This document has no actions for IANA.


Research Group Information
==========================

The discussion list for the IRTF Human Rights Protocol Considerations working group is located at the e-mail address <hrpc@ietf.org>. Information on the group and information on how to subscribe to the list is at
<https://www.irtf.org/mailman/listinfo/hrpc>

Archives of the list can be found at:
<https://www.irtf.org/mail-archive/web/hrpc/current/index.html>

