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

 RFC2775:
 RFC3234:
 RFC3629:
 RFC3724:
 RFC4960:
 RFC7258:
 RFC7754:
 RFC8404:
 RFC8280:

 draft-ietf-quic-transport-12:
    title: QUIC: A UDP-Based Multiplexed and Secure Transport (working document)
    author:
       - ins: J. Iyengar
       - ins: M. Thomson
    target: https://datatracker.ietf.org/doc/draft-ietf-quic-transport

 draft-ietf-quic-tls-12:
    title: Using Transport Layer Security (TLS) to Secure QUIC (working document)
    author:
       - ins: M. Thomson
       - ins: S. Turner
    target: https://datatracker.ietf.org/doc/draft-ietf-quic-tls

 draft-ietf-quic-invariants-01:
    title: Version-Independent Properties of QUIC (working document)
    author:
       - ins: M. Thomson
    target: https://datatracker.ietf.org/doc/draft-ietf-quic-invariants

 draft-huitema-quic-dnsoquic-05:
    title: Specification of DNS over Dedicated QUIC Connections (working document)
    author:
       - ins: C. Huitema
       - ins: M. Shore
       - ins: A. Mankin
       - ins: S. Dickinson
       - ins: J. Iyengar
    target: https://tools.ietf.org/html/draft-huitema-quic-dnsoquic-05

 NETFLIX:
    title: Identifying HTTPS-Protected Netflix Videos in Real-Time
    date: 2017
    author:
       - ins: A. Reed
       - ins: M. Kranch
    target: https://www.mjkranch.com/docs/CODASPY17_Kranch_Reed_IdentifyingHTTPSNetflix.pdf
    seriesinfo: "CODASPY '17 Proceedings of the Seventh ACM on Conference on Data and Application Security and Privacy, Pages 361-368"

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
    target: https://tools.ietf.org/html/draft-trammell-quic-spin-03

 draft-ietf-quic-manageability-02:
    title: Manageability of the QUIC Transport Protocol (working document)
    author:
       - ins: M. Kuehlewind
       - ins: B. Trammell
    target: https://datatracker.ietf.org/doc/draft-ietf-quic-manageability/

 draft-huitema-quic-mpath-req-01:
    title: A Comparison between SCTP and QUIC (working document)
    author:
       - ins: C. Huitema
    target: https://datatracker.ietf.org/doc/draft-huitema-quic-mpath-req/

 EFF:
    title: Verizon Injecting Perma-Cookies to Track Mobile Customers, Bypassing Privacy Controls
    author:
       - ins: J. Hofman-Andrews
    target: https://www.eff.org/deeplinks/2014/11/verizon-x-uidh

 Ruethetal:
    title: A First Look at QUIC in the Wild
    author:
       - ins: J. Rueth
       - ins: I. Poese
       - ins: C. Dietzel
       - ins: O. Hohlfeld
    target: https://arxiv.org/abs/1801.05168

 draft-joseph-quic-comparison-quic-sctp-00:
    title: QUIC Multipath Requirements (working document)
    author:
       - ins: A. Joseph
       - ins: T. Li
       - ins: Z. He
       - ins: Y. Cui
       - ins: L. Zhang
    target: https://datatracker.ietf.org/doc/draft-joseph-quic-comparison-quic-sctp

--- abstract

The QUIC protocol presents a significant innovation on the transport layer. Unlike TCP, which resides in the operating system kernel, QUIC can be implemented in the application, thus providing increased flexibility in terms of congestion control selection and implementation of new features. Furthermore, it offers Zero-Round Trip Time (0-RTT) connection setup, stream multiplexing, improved congestion control and connection migration, and encryption by default.

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

Ossification
: The increasing inflexibility of the network which results in the inability to deploy a new protocol or protocol extensions due to the unchangeable nature of infrastructure components that have come to rely on a particular feature of the current protocols.



Human Rights Considerations
===========================

We analyzed all the drafts of the IETF QUIC Working Group which were active at the time of review (July 2018), and invited Working Group chairs and document authors for interviews during IETF102. Inferential reading of the drafts resulted in the baseline for a questionnaire, which was used to guide the interviews. The interviews were conducted as 60-90-minute discussions, which were then transcribed and analyzed. The analysis focused on the identification of potential positive or negative impacts on human rights, and the categorization of the same according to the Guidelines for Human Rights Protocol Considerations outlined in {{RFC8280}}. 

The Human Rights Protocols Considerations Research Group (HRPC) welcomes the drafts draft-ietf-quic-transport, draft-ietf-quic-tls, draft-ietf-quic-invariants. In particular, we welcome the efforts to improve connectivity on high latency, low bandwidth and high loss connections, and the application of end-to-end encryption by default. Final conclusions and recommendations can be found at the end of this document.

No implications for Anonymity ({{RFC8280}}, sec. 6.2.9), Pseudonymity ({{RFC8280}}, sec. 6.2.10), Accessibility ({{RFC8280}}, sec. 6.2.11), Localization ({{RFC8280}}, sec. 6.2.12), Decentralization ({{RFC8280}}, sec. 6.2.13), have been found.

## Connectivity

QUIC was designed as a new transport protocol to provide connections with lower latency than previous protocols. QUIC performs better than TCP on high latency and high loss connections because it allows for Zero-Round Trip Time (0-RTT) resumption of connections, and new congestion control ‎algorithms. This means that a user who has recently visited a site, or is resuming a connection, is not required to renegotiate the initial handshake, thus needing to make less round trips. Because of the integrated usage of TLS1.3 in QUIC, 1 round trip is saved in comparison to TLS1.2 in the handshake.

On top of that, QUIC uses congestion control algorithms, which are optimized to address packet loss, especially in wireless links. This means that QUIC is expected to result in a greatly improved Internet service for users worldwide, and in particular for those who currently do not have high bandwidth or lossless connections. In this sense, areas that currently do not benefit from efficient connectivity, can expect to be provided with a significantly improved service. This enables a growing number of users to exercise human rights such as freedom of expression, freedom of association, right to political participation.

At present, connections get regularly interrupted by so called middleboxes {{RFC3234}} {{RFC3724}}, which can also hamper the deployment of new protocols. The deployment of middleboxes has led to ossification in the network, which in turn has hampered the deployment of new transport protocols in the recent past (e.g. SCTP {{RFC4960}}). This experience has led to the development of QUIC on top of UDP, and to the use of encryption, where possible, in an attempt to prevent future ossification from happening. 

The design of QUIC is explicitly modular. This means that while the current QUIC development is using TLS for encryption and is optimized to facilitate HTTP as application layer protocol, it is an explicit design objective to allow for future changes and to enable other kinds of applications to run over QUIC (one example currently being discussed is DNS over QUIC {{draft-huitema-quic-dnsoquic-05}}.

## Privacy

### End-to-end encryption
The fact that the protocol is end-to-end encrypted by default is definitely a positive implication for human rights. End-to-end encryption makes it easier to protect the privacy of communications between two parties by not allowing any other party to be involved in the exchange.

### Transparent proxy
Being encrypted end-to-end, QUIC circumvents privacy violations as well as transparent proxying and content modification by middleboxes. As such, it protects the integrity of both the application layer content (e.g. HTTP) and the transport layer headers.

### Multiple streams
By establishing connection with multiple streams, QUIC creates higher opacity for the observer.
Comparing QUIC to TLS over TCP, QUIC significantly reduces the amount of information that an observer can acquire about communications they are looking at. In TCP, all of the information regarding the protocol flow at a transport layer is exposed, and can be used to identify active communications.
An interesting example documenting the greater vulnerability has been recently provided by Andrew Reed and Michael Kranch in their paper "Identifying HTTPS-Protected Netflix Videos in Real-Time" {{NETFLIX}}. After Netflix had upgraded their infrastructure to provide HTTPS encryption of video stream in order to protect the privacy of their viewers, the researchers demonstrated that it was still possible to accurately identify Netflix videos from passive traffic capture in real time, and with very limited hardware requirements. What they did was developing a system that could report the Netflix video being delivered by a TCP connection using only the information provided by TCP/IP headers {{NETFLIX}}. With QUIC, this would not be possible.

In essence, in QUIC it is possible to have an established connection with an end point and to run multiple streams over that connection. Consequently, an observer who is looking at someone's connection, would not be able to tell the difference between the streams. The observer can see that a user is talking, and how many packets are passed, but they cannot see addresses changes, usually the client's, in the case of the HTTP binding (see: {{raft-ietf-quic-transport-12}}).

The client sets a connection ID in the initial client packet that will be used during the handshake. A new connection ID is then provided by the server during connection establishment: this will be used in the short header after the handshake. A server might also provide additional connection IDs that can the used by the client at any time during the connection. Therefore, if a flow changes one of its IP addresses, it may keep the same connection ID, or the connection ID may also change together with the IP address migration, thus avoiding linkability.

It is critical to notice, though, that even if its occurrence is decreased, linkability cannot be completely avoided. In most cases of linkability attacks the anonymity set is low enough that the attacker can make use of timing information to accomplish their objective.

### Packet number encryption
A compelling debate with human rights implications which is happening in the QUIC Working Group regards packet number encryption.

From a general standpoint, the number assigned to each packet carries very little information. For example, it is possible to observe that a packet sent a certain time and the packet that was sent immediately after probably have increasing packet numbers.

But when traffic is carried over multiple paths, it becomes observable at many points, and this has privacy implications. For example, as stated in {{draft-huitema-quic-mpath-req-01}}: "[...] if packets belonging to a given connection carry some unique identifiers, observers could use these identifiers to track client migrations through several paths, and thus potentially expose the successive locations of a particular user."

### Padding
Bit padding is the addition of one or more extra bits to a transmission or storage unit to make it conform to a standard size. In QUIC, padding can be used to increase an initial client packet to the minimum required size, or to provide defense against traffic analysis for protected packets.

An example of its functionality can be given by observing the connection to a high traffic site like Wikipedia. With TLS, an observer can see a user's initial request to connect to the site, and then a number of additional requests suddenly appear on the other channels, thus acquiring the ability to monitor their connection. Furthermore, simply by downloading all Wikipedia pages, the observer can also obtain a fairly high dimensional description of the pages, and roughly tell what page the user is looking at.

Such violation of privacy would not be possible in QUIC. In QUIC, padding allows to provide protection against traffic analysis for protected packets, therefore offering an additional defense on top of the encryption layer against metadata analysis.

However innovatory, it is also important to notice that padding is not a mandatory feature in QUIC, as it has non trivial performance costs that might not be affordable for deployment.

### Timing
QUIC substantially reduces the amount of information that can be obtained from the transport flow. It allows to change the timing, and the sizes of packets and frames. If wished, this provides an opportunity to create a connection that largely looks like white noise to an observer. This is not something that is required in the protocol though, as it has non trivial performance costs that might not be affordable for deployment.

### Legal intervention
If an adversary wants to monitor or collect a user's data, with QUIC this is either visible through technical means, or the third party would need to use the legal route to obtain access. This enhances the right to due process.

### Spin bit
One of the key discussions currently carried within the QUIC Working Group regards the demand that network operators have for the protocol to provide them with information about the network itself. Operators motivate their requirement with the need to have visibility of their networks in order to operate them most efficiently. Following up on their demand, some members of the QUIC Working Group have proposed the adoption of a spin bit, as outlined in {{draft-trammell-quic-spin-03}}.

The spin bit is a bit in the header that flips once a round trip, so that observers can estimate RTT, designed for explicit passive measurability of the protocol.

The debate about the spin bit regards its ability to reveal information about the distance of the endpoints from each other to anybody who happens to be sitting on the path.

The argument in favor of the spin bit says that since it is decoupled from the application’s state, it does not appear to leak any information about the endpoints, beyond an extremely rough estimate of location. Also, as devices move around the network and manage to retain the same QUIC connection, timings could anyway be seen in the QUIC handshake message, and consequently the use of the spin bit should not be considered as a privacy infringement.

The argument against the adoption of the spin bit observes that by revealing information about the distance of the end points from each other to anybody on the path, it violates user privacy through passive network management.

If a QUIC connection is maintained while moving across the network, then there would be no handshake message to review. A network operator could see traffic that suddenly appears looking like it is part of the middle of a stream, and might block that traffic thinking that it is part of an attack, or because they cannot distinguish it from an attack. But if they allow that traffic to go through then they do not actually have the handshake messages which they can identify and measure round trip time from.

Another argument against the adoption of the spin bit points out that network operators could anyway measure inside of their own network actively with minimal cost, or collect data from their own routers, with no need to have the spin bit at their disposal. It is only in case they want to measure information outside of their own administrative domain that they would need to use something like parameters or protocol metadata. But all this would require more efforts from their side, and this likely explains why they prefer a much more straightforward alternative like the spin bit.

### Packet injection
It is viable for network operators to add data to packets in order to do traffic monitoring and/or management.
It is not uncommon for network operators to routinely tag packets as they enter the network for their own purposes, and simply erase the tag when they leave the network. An example of this practice can be represent by a privacy violation carried out by Verizon Wireless in 2014. With the purpose to better serve advertisers, Verizon Wireless modified its users' web traffic on its network to inject tracker. This tracker was included in an HTTP header called X-UIDH, and was sent to every unencrypted website a Verizon customer visited from a mobile device. As reported by the Electronic Frontier Foundation, this allowed "third-party advertisers and websites to assemble a deep, permanent profile of visitors' web browsing habits without their consent." {{EFF}}

## Content agnosticism
               
The QUIC protocol itself is content agnostic. While it is currently being optimized for HTTP traffic, it can also be used with other application layer protocols (e.g. see {{draft-huitema-quic-dnsoquic-05}}).

## Security

QUIC improves security by making end-to-end encryption an inherent part of the transport protocol, instead of adding it as a optional layer on top of it. This protects the integrity of the data by preventing tampering on the path, and ensures end-to-end confidentiality between the two communicating hosts. Furthermore, it ensure that no on-path attacker can emulate an endpoint.

By encrypting all Internet traffic by default it is harder for researchers and network operators to analyze network traffic. This is a specific design goal, but it also makes research into the promulgation of malware, cookies and other artefacts much harder, since in this case access to the stream needs to be provided by the end point.

## Internationalization

QUIC raises two issues in terms of internationalization.

The first issues regards the fact that {{draft-ietf-quic-transport}} does not define human readable strings, except for where it states that the Reason Phrase in the CONNECTION_CLOSE and APPLICATION_CLOSE frames "SHOULD be a UTF-8 encoded string {{RFC3629}}". The QUIC protocol demands that this SHOULD be an UTF-8 string, while UTF-8 is actually not required. Also, there is currently no space to declare the charset used. So it is recommended that this SHOULD becomes a MUST.

The second issue concerns the lackof availability of language tags. This would allow implementations to signal in which language Reason Phrases are rendered.

## Censorship resistance

End-to-end encryption makes monitoring and filtering of the traffic more complex, thus hindering fine-grained censorship. Furthermore, in QUIC it is also harder to terminate connections, since in the protocol the only parties that can terminate the connection are those actually involved in the connection once it exists. This means that a middlebox cannot reset a connection, but needs to continue to block it, keeping state. Considering this, it can be stated that QUIC makes censorship harder because it requires the censor to invest more resources and efforts.

QUIC is also providing protection against DDoS protection through observation of the handshake for connection confirmation, and through the need to validate new connections in case of a connection migration.

If the spin bit is on, and if we take into account devices that are relatively new to each other, traversing a couple of networks would reveal something about the locality of the endpoint. Some of that locality might also be revealed by the IP addresses that are involved, but some of it might not. If this is coming across a tunnel, and one end point appears to have a particular value, this might suggest an observer that there is a tunnel in use.
If a user needs to use tunnels for their security, they might be at risk of getting their communications shut down by network operators who may decide to refuse to pass tunnel traffic, therefore incurring in a violation of the user's right of access.

## Open Standards

QUIC is published as open standard.

## Heterogeneity Support

QUIC is currently optimized to use TLS1.3 and serve HTTP2 traffic. It is explicitly constructed in a modular manner and is designed to support other application layer protocols as well.

## Reliability

Thanks to the use of 0-RTT (as described above) the connectivity on high-latency and high-loss connections becomes more reliable.

## Confidentiality

Through the use of cryptography, QUIC integrates security, confidentiality, authenticity, and integrity directly into the transport protocol rather than having them layered on top of it.
Any network operator who will use QUIC to benefit from its latency improvements will automatically provide all the aforementioned attributes to their user.

## Integrity

The use of TLS1.3 in QUIC makes on-path attacks either visible or nearly impossible to carry out. So, if an actor forces the traffic to go through one middlebox and decrypt the traffic itself, their action is made detectable.
This also protects the integrity of the datastream, prevents tampering, and averts the injection of extra data in the stream.

## Authenticity

Except for the initial handshake, the encryption in QUIC is provided by TLS1.3, which uses asymmetric cryptography to authenticate the hosts. This enables verification of authenticity.

## Adaptability

The QUIC design allows for adaptation. More specifically, the modular approach to the design of the transport protocol allows for improvements of mistakes that might have been made during development, and for the integration of potential future advancements. The only commitments in the protocol are the requirement to run on UDP, the packet header, and the version negotiation phase. The remainder of the protocol is quite flexible and can be adapted for future use. As a transport protocol QUIC tries to be agnostic for application layer protocols, even though it is currently optimized for HTTP2.

QUIC aims to address ossification and thus to enhance adaptability in the architecture. It does so by encrypting transport headers and greasing. The IP headers could not be encrypted because NATs routinely change UP addresses. If QUIC would authenticate against an IP address and this would change, the stream would collapse. An option that could be considered, would be the encryption of IP headers on IPv6 networks to dissuade the deployment of NATs on those same networks.

## Outcome Transparency

If QUIC will be successfully and widely deployed, as it seems to be the case {{Ruethetal}}, it will represent a remarkable evolution of the transport layer with equally significant impact on the Internet architecture. The following section will discuss the potential effects of QUIC on the wider protocol milieu, the Internet infrastructure and its users, and well as the key takeaways emerged during the review process in regards to the development of the protocol itself.

The IETF has reached consensus on the fact that pervasive monitoring is an attack (see {{RFC7258}}), and that a response to mitigate this is represented by ubiquitous encryption, which would also reinforce the end-to-end nature of the network {{RFC2775}} {{RFC3724}} {{RFC7754}}. With the advent of QUIC, encryption becomes the default on the transport level. This has an impact on network operators that previously used visible parts of protocols to, among other things, manage, operate, and secure their networks {{RFC8404}}. At the same time, it also improves the integrity of the datastream, as QUIC allows to protect users against injections of ads by network operators.

### Permissionless innovation and its challenges
As also stated by interviewees during the research phase of this review, the development of QUIC was partly inspired by the less pronounced uptake of SCTP (Stream Control Transmission Protocol), a protocol for transmitting multiple streams of data at the same time between two end points that have established a connection in a network, standardized in {{RFC4960}}.

As outlined in the comparison between SCTP and QUIC presented in {{draft-joseph-quic-comparison-quic-sctp-00}}, the deplyoment of SCTP is not particularly widespread. In-network devices, like NAT gateways for example, do not support SCTP well. NAT gateways need to be upgraded to be SCTP-aware, the modification of middleboxes is very expensive, and Internet service providers, focusing on the sustainability of their business, update the devices in accordance with the benefit that this can represent for their revenues.

QUIC is more friendly to middleboxes than SCTP. Since it works in the application layer, it is supposed to be upgraded much more frequently than TCP stack in kernel.

Furthermore, QUIC was designed by a large content provider, Google. In was implemented in 2012, and the company invested significant resources to develop it, for example conducting thorough A/B-testing in order to assess how the protocol would interact with the network, and how the middleboxes would respond. QUIC is now widely used in Chrome clients accessing Google services.

In 2015, an Internet Draft of a specification for QUIC was submitted to the IETF for standardization, and the following year the QUIC Working Group was established. A growing number of contributors from the corporate, academic, nonprofit sector have joined the protocol development work since, and what has been achieved to date is the result of a notable and labor-intensive collaborative effort.

So, on one hand, the history of QUIC shows that permissionless innovation is still possible. On the other hand, it also shows what remarkable efforts and resources are needed to carry out such an ambitious project.
While permissionless innovation still exists, the threshold and costs for innovation seem to rise significantly and increasingly.

It should also not be underestimated that even if another developing actor might be able to muster an amount of resources similar to the one invested by Google for QUIC, the network might still respond differently to that effort, as the developing actor might have not an impressive user base and traffic stream as Google's.

### Privacy, power and consolidation
The most relevant privacy win provided by QUIC is for users who have different kinds of traffic relations with one end point. QUIC does not allow network providers to easily differentiate between, for instance, HTTP requests, DNS requests and real time voice packets, thus strengthening the user's right to privacy.

On the other hand, this creates a concentration of different kinds of traffic with one end-point, thus giving the service provider access to more categories of privacy sensitive information.

In the current reality of the Internet, the biggest hosts are controlled by large, consolidated, transnational corporations. This creates an extreme power differential between end users on the one hand, and service providers and content operators on the other hand.

In order to protect privacy and secure information, it is important that the user makes a careful and informed decision about the hosting provider and plan they choose.

While ubiquitous encryption changes the relation between service providers and content operators, placing them at the same end of the spectrum, it remains to be seen whether if it can help users take and retain control within the overall power structures of Internet governance and economics.

If running a QUIC server was made relatively easy, thus enabling a greater diversification of end points, QUIC could contribute to a power shift in favor of the end user. But running a QUIC infrastructure is currently expected to be more demanding than running a HTTP/2 or HTTP/1 infrastructure. It would be truly compelling if this consideration could be addressed by the development and release of openly available tooling allowing for more accessible ways to run a QUIC server.

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

* Reconsider the addition of the spin bit in light of the concerns raised in regards to its implications on the rights to privacy and access.

* Consider deploying IP header encryption on IPv6 networks, where NATs are not as widely deployed as on IPv4 networks, potentially as an optional extension.

* Add language tagging and charset identification in the case of Reason Phrase in the CONNECTION_CLOSE and APPLICATION_CLOSE.

* Translate the QUIC specification into other languages.

* Make tooling for running QUIC servers openly available.

* Recurrently monitor and discuss the implications of QUIC on the power relations between end user on one end of the spectrum, and network operators and service providers on the other one.

Acknowledgements
================

We would like to thank (in alphabetical order): Mike Bishop, dkg, Jana Iyengar, Mirja Kuehlewind, Mark Nottingham, Martin Thompson, and Brian Trammel for their contributions to this document (this document does not necessarily reflect their opinion, but solely that of the authors).

 
Security Considerations
========================

As this draft concerns a research document, there are no security considerations.


IANA Considerations
===================

This document has no actions for IANA.


Research Group Information
==========================

The discussion list for the IRTF Human Rights Protocol Considerations working group is located at the e-mail address <hrpc@ietf.org>. Information on the group and information on how to subscribe to the list is at
<https://www.irtf.org/mailman/listinfo/hrpc>

Archives of the list can be found at:
<https://www.irtf.org/mail-archive/web/hrpc/current/index.html>
