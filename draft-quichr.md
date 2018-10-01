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
       organization: Harvard University
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

   draft-huitema-quic-dnsoquic-05:
      title: Specification of DNS over Dedicated QUIC Connections (working document)
      author:
         - ins: C. Huitema
         - ins: M. Shore
         - ins: A. Mankin
         - ins: S. Dickinson
         - ins: J. Iyengar
      target: https://tools.ietf.org/html/draft-huitema-quic-dnsoquic-05

   draft-ietf-quic-manageability-02:
      title: Manageability of the QUIC Transport Protocol (working document)
      author:
         - ins: M. Kuehlewind
         - ins: B. Trammell
      target: https://datatracker.ietf.org/doc/draft-ietf-quic-manageability/

   EFF:
      title: "Verizon Injecting Perma-Cookies to Track Mobile Customers, Bypassing Privacy Controls"
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

--- abstract

The QUIC protocol presents a significant innovation on the transport layer. This document assesses the potential human rights implication that emanate from the deployment of QUIC according to the methodology laid out in {{RFC8280}}.

--- middle

Introduction
============


This is a review done within the framework of the Human Rights Review Team, it was done by Beatrice Martini and Niels ten Oever. The Human Rights Review Team aims to implement and improve the guidelines for human rights considerations provided in {{RFC8280}}, and seek to mitigate potentially adverse human rights impacts that IETF and IRTF documents might have.

Human Rights reviews are developed by a group of individuals in the IRTF and IETF. They work together to encourage each other to do these detailed reviews as contributions to the IETF open review process. Human Rights reviews are individual contributions. The authors hope that the comments will be taken into consideration by the draft authors, groups and IESG.


This review concerns the QUIC protocol in general and the following drafts in particular:
draft-ietf-quic-transport, draft-ietf-quic-tls, draft-ietf-quic-invariants.


Vocabulary Used
===============

Ossification
: The increasing inflesibility of the network which results in the inability to deploy a new protocol or protocol extensions due to the unchangeable nature of infrastructure components that have come to rely on a particular feature of the current protocols



Human Rights Considerations
===========================

For this review we analyzed all the active drafts of the QUIC Working Group in the IETF and invited Working Group chairs and document authors for interviews during IETF102. Inferential reading of the drafts resulted in the basis for a questionnaire, which was used to guide the semi-structured interviews. After the interviews, which took on average between 60 and 90 minutes, the interviews were transcribed and concerns and (potential) postive or negative impacts on human rights were categorized according to the Guidelines for Human Rights Protocol Considerations as outlined in {{RFC8280}}. 

The Human Rights in Protocols Research Group welcomes the drafts draft-ietf-quic-transport, draft-ietf-quic-tls, draft-ietf-quic-invariants. In particular, we welcome the efforts to improve connectivity on high latency, low bandwith and high loss connections and the enabling of encryption by default. The final conclusions and recommendations can be found at the end of the document.

Upon consideration of the draft report, no implications for Anonymity ({{RFC8280}}, sec. 6.2.9), Pseudonymity ({{RFC8280}}, sec. 6.2.10), Accessibility ({{RFC8280}}, sec. 6.2.11), Localization ({{RFC8280}}, sec. 6.2.12), Decentralization ({{RFC8280}}, sec. 6.2.13), have been found.

## Connectivity

The QUIC protocol was designed as a new transport protocol to provide connections with lower latency than previous protocols. QUIC performs better than TCP on high latency and high loss connections because it allows for zero round trip time resumption of connections, often abbreviated as 0-RTT, and new congestional control algorhitms . This means that a users who have recently visited a site or are resuming a connection do not need to renegotiate the initial handshake, and thus needing to make less roundtrips. Because of the integrated usage of TLS1.3 in QUIC, this also saves 1 round-trip in comparison to TLS1.2 in in the handshake. On top of that QUIC runs its own congestion control algorithms which are designed to more recent understandings and observations of packet loss, especially in wireless links. This means that QUIC is expected to result in a great improvement for many users around the world, especially those who do not have high bandwith or lossless connections. In this sense places that are not well connected can expect improved connectivity, which will enable more users to exercise human rights such as freedom of expression, freedom of association and other connected rights. 

Connections currently regularly get interrupted by so called middle-boxes {{RFC3234}} {{RFC3724}}, which can also hamper the deployment of new protocols. The deployment of middle-boxes has led to ossification in the network, which in turn hampered the deployment of new transport protocols in the recent past (eg SCTP {{RFC4960}}). This experience has led to the development of QUIC on top of UDP and the usage of encryption where possible to seek to prevent future ossification from happening. 

QUICs design is explicitly modular, which means that while current QUIC development is using TLS for encryption and is optimized to facilitate HTTP as application layer protocol, it is an explicit design objective to allow for future changes and to enable other kind of applications to run over QUIC (one example currently being discussed is DNS-over-QUIC {{draft-huitema-quic-dnsoquic-05}}. In this sense the QUIC protocol is not just the development of a new transport protocol, but it also aims to support and enable new innovations and experiments in the future, which has in part been hampered by ossification. In this sense QUIC can be seen as a return to the end-to-end to principle in network design, which enables new forms of connectivity. 

There is a current discussion in the QUIC Working Group to include a spin bit {{draft-trammell-quic-spin-03}} to improve passive measureability of traffic that has been hampered by the inclusion of encryption. The spin bit would allow for characterization of certain kinds of traffic flows. While this could be used for traffic optimization, it might also lead to the blocking of certain traffic. It is expected that most reliable streams are going to require ACKs, similar to TCP, but one could imagine unreliable statements in QUIC that don't get AKCs, such as in the case of one-way logging for instance when a host it too low powered to even cope with a resend if it is not received. A network operator might find this traffic conspicuous and discriminate against this type of traffic flow because no return is observed which might lead to the blocking of legitimate traffic. 

## Privacy

QUIC has key positive implications on the right to privacy.

### End-to-end encryption
The fact that the protocol is end-to-end encrypted is definitely a win for human rights. While encryption does not solve by any means all human rights concerns on the Internet, it does make it easier to protect the privacy of communications between two intentional parties, by not allowing any other party to be involved in the exchange.

### Transparent proxy
Being encrypted end-to-end, QUIC circumvents privacy violations as well as transparent proxying and content modification by middleboxes. As such, it protects the integrity of both the application-layer content (e.g. HTTP) and the transport-layer headers.

### Multiple streams
By establishing connection with multiple streams, QUIC creates higher opacity for the observer.
Comparing QUIC to TLS over TCP, QUIC significantly reduces the amount of information about communication that an observer can get. In TCP, all of the information of the protocol flow at a transport layer is exposed, and can be used to find out what communication is happening.
An interesting example documenting the greater vulnerability of TCP has been recently provided by Andrew Reed and Michael Kranch in their paper "Identifying HTTPS-Protected Netflix Videos in Real-Time" {{NETFLIX}}. After Netflix had upgraded their infrastructure to provide HTTPS encryption of video stream in order to protect the privacy of their veiwers, they demostrated that it was still possible to accurately identify Netflix videos from passive traffic capture in real-time, and with very limited hardware requirements. What they did was developing a system that could report the Netflix video being delivered by a TCP connection using only the information provided by TCP/IP headers {{NETFLIX}}.  With QUIC, this would not be not possible.

In short: In QUIC it's possible to have an established connection with an endpoint and to run multiple streams over that connection. Consequently, an adversary who is looking at someone's connection, would not be able to tell the difference between the streams. They can see that a user is talking and how many packets are passed, but they can’t tell which packets are part of which stream. This provides one more opportunity to hide metadata and protect users from unwanted metadata analysis.

QUIC is not completely opaque, as timing information is still available to the observer. Still, the level of opacity it achieves is unprecedented, and it is a critical relevance to circumvent monitoring at the hands of state actors and companies, which analyze the behavior of network protocols based upon heuristics on the transport metadata. Officially, the reason why corporations demand access to this metadata is to identify malware based on its communications patterns. But the same information can easily be sold to third parties, including government agencies, to monitor and surveil Internet users.

### Connection ID
Through the use connection ID in case of connection migration, QUIC decreases linkability.

The connection ID is used to allow rebinding of a connection after one of the endpoint’s addresses changes, usually the client's, in the case of the HTTP binding. [see: {{draft-ietf-quic-manageability-02}}]

The client set a Connection ID in the Initial Client packet that will be used during the handshake. A new connection ID is then provided by the server during connection establishment: this will be used in the short header after the handshake. Furthermore, a server might provide additional connection IDs that can the used by the client at any time during the connection. Therefore, if a flow changes one of its IP addresses, it may keep the same connection ID, or the connection ID may also change together with the IP address migration, avoiding linkability.

However, even if its occurence is decreased, linkability cannot be completely avoided. In most cases of linkability attacks the anonymity set is low enough that the attacker can make use of timing information to accomplish its objective.

### Packet number encryption
A compelling debate with human rights implications is the one about packet number encryption.
From an objective standpoint, the number assigned to each packet carries very little information. For example, it is possible to observe that a packet sent a certain time and the packet that was sent immediately after probably have increasing packet numbers.

But when traffic is carried over multiple paths, it becomes observable at many points, and this has privacy implications. "For example, if packets belonging to a given connection carry some unique identifiers, observers could use these identifiers to track client migrations through several paths, and thus potentially expose the successive locations of a particular user." (see https://tools.ietf.org/html/draft-huitema-quic-mpath-req-01)

### Padding
Bit padding is the addition of one or more extra bits to a transmission or storage unit to make it conform to a standard size. In QUIC, padding can be used to increase an initial client packet to the minimum required size, or to provide protection against traffic analysis for protected packets.

An example of its functionality can be given by the connection to a high-traffic site like Wikipedia.
What modern web browsers typically do, is to set up multiple TLS channels and then make one request on one channel. While it’s coming down, when they realize they need another request, they send out requests from other channels. This means that an adversary can monitor a user talking to Wikipedia. They can see the user's initial request, and then a number of additional requests popping out on the other channels.
An adversary could take a set of all the Wikipedia pages – which is not difficult to get and download – and understand which pages have which content on them. They could also see how big is the content, how many bytes each page has, therefore obtaining a fairly high dimensional description of the page, as there are not many pages that can duplicate that. This means that looking at the traffic analysis of a user's connections to Wikipedia, anyone could roughly tell what page the user is looking at.

In QUIC though, padding allows to provide protection against traffic analysis for protected packets,therefore offering an additional defense on top of the encryption layer against metadata analysis. 

### Timing
QUIC reduces a substantial amount of information that be obtained from the transport flow. It allows to change the timing. It allows to change the sizes of packets and frames. So if you really wanted to created a connection that largely looks like white noise to an observer it’s possible to do that in QUIC. This is not something that is required in the protocol though, because these options, like padding as well, have performance costs, and not everybody is going to be willing to pay those for deployment. 

### Legal intervention
If an adversary wants to monitor or collect a user's data, with QUIC this is either visible through technical means, or the third party would need to use the legal route to obtain access. This enhances the right to due process.

### Spinbit
One of the key discussions currently carried within the QUIC Working Group regards the demand that network operators have for the protocol to provide them with information about the network itself. Operators motivate their requirement with the need to have visibility of their networks in order to operate them most efficiently. Following upon their demand, some members of the QUIC Working Group have proposed the adoption of a spin bit.

The spin bit is a bit in the header that flips once a round trip, so that observers can estimate RTT, designed for explicit passive measurability of the protocol.

The key argument against the adoption of the spin bit is that it reveals information about the distance of the endpoints from each other to anybody who happens to be sitting on the path, therefore violating user privacy through passive network management.

The argument in its favor says that since it is decoupled from the application’s state, it does not appear to leak any information about the endpoints, beyond an extremely rough estimate of location. Also, as devices move around the network and manage to retain the same QUIC connection, timings could anyway be seen in the QUIC handshake message, and consequently the use of the spin bit should not be considered as a privacy infringement.

But if a QUIC connection is maintained while moving across the network, then there would be no handshake message to review. A network operator could see traffic that suddenly appears looking like it’s part of the middle of a stream, and might block that traffic because thinking that it's part of an attack, or because they can’t distinguish it from an attack. But if they allow that traffic to go through then they don't actually have the handshake messages which they can identify and measure roundtrip time from.

Another argument against the adoption of the spinbin points out that network operators can anyway measure inside of their own network actively with minimal cost, or collect data from their own routers. It is only in case they want to measure information outside of their own administrative domain that they would need to use something like parameters or protocol metadata. This would require more work from their side, and this is why they prefer a much more straightforward alternative like the spin bit.

### Packet injection
It is viable for network operators to add data to packets in order to do traffic monitoring and/or management.
It is not uncommon for network operators to routinely tag packets as they enter the network for their own purposes, and simply erase the tag when they leave the network. An example of this practice can be represent by a privacy violation carried out by Verizon Wireless in 2014. With the purpose to better serve advertisers, Verizon Wireless modified its users' web traffic on its network to inject tracker. This tracker was included in an HTTP header called X-UIDH, and was sent to every unencrypted website a Verizon customer visited from a mobile device. As reported by the Electronic Frontier Foundation, this allowed "third-party advertisers and websites to assemble a deep, permanent profile of visitors' web browsing habits without their consent." {{EFF}}


## Content agnosticism
                
The QUIC protocol itself is content agnostic. While is currently is being optimized for HTTP traffic, it can also be used with other application layer protocols (eg. see {{draft-huitema-quic-dnsoquic-05}}. In its adoption of encryption by default QUIC also makes discrimination based on the content harder and is thus strenghtening content agnosticism. This creates and enabling environment for the right to freedom of expression, the right to non-discrimination and right to equal protection.

## Security

QUIC improvees security by making encryption an inherent part of the transport protocol, instead of adding it as a optional layer on top of it. This protects the integrity of the data by preventing tampering on the path, and ensures end-to-end confidentitality between the two communicating hosts. Furthermore it ensure that no on-path attacker can emulate an endpoint.

By encrypting all Internet traffic by default it is harder for researchers and network operators to analyze network traffic. This was a specific design goal, but it also makes research into the promulgation of malware, cookies and other artefacts much harder, because now access to the stream will need to be provided by the end-point.

## Internationalization

In terms of internationalization there are two issues with QUIC. The transport protocol does not define human readable strings, except for where draft-ietf-quic-transport states that the Reason Phrase in the CONNECTION_CLOSE and APPLICATION_CLOSE frames "SHOULD be a UTF-8 encoded string {{RFC3629}}", this can be a 'human-readable explanation for why the connection was closed'. The QUIC protocol demands that this SHOULD be an UTF-8 string, while UTF-8 is not required, there is also no space to declare the charset used. So it is recommended that this SHOULD becomes a MUST.
Another aspect of internationalization in which the specification is lacking is the lack of availability of the specification of the protocol in any other language than English.

## Censorship resistance

End-to-end encryption make monitoring and filtering of the traffic harder, this makes fine-grained censorship harder. Of course it does not change actors that engage in IP-based filtering. Next to that it is also harder to terminal connections because in QUIC, the only parties that can terminate the connection are those actually involved in the connection once the connection exists. This means that a middlebox cannot reset a connection but needs to keep blocking it, which means it needs to keep state and thus it makes censorship harder because it demands more resources from the censor.

QUIC is also providing protection against DDoS protection through observation of the handshake for connection confirmation, and through the needs to validate new connections in case of a connection migration.

If the spin bit is on, and if we take into account devices that are relatively new to each other, traversing a couple of networks would reveal something about the locality of the endpoint. Some of that locality might also be revealed by the IP addresses that are involved, but some of it might not. If this is coming across a tunnel, and one endpoint appears to have a particular value, this might give a hint that there’s a tunnel in use versus a tunnel not in use. 
If a user needs to use tunnels, they might be at risk of getting their communications shut off by network operators who do decide to refuse to pass tunnel traffic,therefore incurring in a violation of their right of access.

## Open Standards

QUIC is published as open standard.

## Heterogeneity Support

QUIC is currently optimized to use TLS1.3 and serve HTTP2 traffic. It is explicitly constructed in a modular manner and has as a design goal that it should support other application layer protocols as well. 

## Reliability

Because of the use of 0-RTT (as described above) connection become more reliable on high-latency and high-loss connections.

## Confidentiality

Through QUICs use of cryptography it integrates security, confidentiality, authenticity, and integrity directly into the transport protocol rather than having them layered on top of the transport protocol. This also make it not-optional, but obligatory if you want to use QUIC, and benefit from the latency improvements.

## Integrity

The use of TLS1.3 in QUIC will make on-path attacks either visible or nearly impossible to pull off. So in the case when an actor forces all traffic to go through one middlebox and decrypt all the traffic, at least it would be explicit. This also protects the integirity of the datastream, and prevents tampering with it, and prevents the injection of extra data in the stream.

## Authenticity

Except for the initial handshake, the encryption in QUIC is provided by TLS1.3, which uses asymmetric cryptography to authenticate the hosts. This enables verification of authenticity. 

## Adaptability

The QUIC design allows for adaption, the modular approach to the design of the transport protocol allows for improvements of mistakes that might be made during development, or new insights in the future. The only commitment in the protocol is in the fact that it runs on UDP, the packet header, and the version negotiation phase. The remainder of the protocol is quite flexible and can be adapted for future use. As a transport protocol QUIC tries to be agnostic for application layer protocols, even though it is currently optimized for HTTP2.

QUIC aims to address ossification and thus enhancing adaptability in the architecture, it does so by encrypting transport headers and greasing. The IP headers could not be encrypted because NATs routinely change UP addresses, and if QUIC would authentincate against an IP address and it would change, the stream would collapse. It could be considered to encrypt IP headers on IPv6 network to dissuade the deployment of NATs on those networks. 

## Outcome Transparency

If QUIC will be succesfully widely deployed, which already seems to be happening {{Ruethetal}}, it is a significant evolution of the transport layer which has equally significant impacts on the Internet architecture. The potential impacts on the wider protocol milieu and the Internet infrastructure and its users will be discussed here, as well as some lessons learned about the development of the QUIC protocol. 

The IETF reached consensus in {{RFC7258}} that pervasive monitoring is an attack, a response to mitigate this was to use ubiquitous encryption which would also reinforce the end-to-end nature of the network {{RFC2775}} {{RFC3724}} {{RFC7754}}. With the advent of QUIC encryption becomes the default on the transport level. This has an impact on network operators that previously used visible parts of protocols to, among other things, manage, operate, and secure their networks {{RFC8404}}, on the other hand it also improves the integrity of datastream because now, for instance, users are protected against injections of ads by networkoperators.

### Permissionless Innovation and its discontents
The development of QUIC was inspired in part by the less significant uptake of SCTP. The protocol has been developed by a large content provider which was able to deploy the protocol after a significant amount of A/B-testing to understand who the protocol would interact with the network and the responses by middleboxes. This has been a non-trivial effort by a significant team, which shows that on the one hand permissionless innovation is still possible, but on the other hand it also shows the amount of effort and resources that are needed to be able to do that. While permissionless innovation thus still exists, the threshold and costs for innovation seem to have significantly risen. Next to that it should perhaps not be underestimated that another party might be able to muster a similar amount of resources needed for such an innovation, the network might respond differently if the developing party did not have an already existing enormous userbase and traffic stream as Google has at the time of development. 

### Privacy, power and consolidation
The biggest privacy win for protection from network providers is for users who have different kinds of traffic relations with one end-point, so there can be no easy differentiation made between for instance HTTP requests, DNS requests and real time voice packets, so there would be less need for padding. On the other hand this would of course concentrate different kinds of traffic with one end-point, which would then have access to more categories of privacy sensitive information. In that sense the user always needs to make a trade-off in the new consolidated reality of the Internet where most other hosts are controlled by large, consolidated, trans-national corporations. This creates an extreme power differential between end-users on the one hand, and service providers and content operators on the other hand. While ubiquitous encryption changes the relation between the latter two, it remains to be seen whether the overal balance between end-users and the rest of the Internet, can be tilted back to control by the user. QUIC could contribute to this if running a QUIC server by endpoint would be relatively easy, and thus diversifying end-points. But it is expected that running a QUIC infrastructure is likely to be more difficult and a little bit more complex than running an HTTP/2 infrastructure or an HTTP/1 infrastructure, this could be addressed by the development and release of publicly available tooling.

### Transparency and IoT
As mentioned before, end-to-end encryptionon the transport layer does not only force network operators to adopt new practices vis a vis security and network management, if IoT devices adopt QUIC, it will be harder for the owners of IoT devices to understand what data these devices are communicating with third parties. Furthermore, research into the dissemination of cookies, malware, etc might also become harder because it would probably need the buy-in from users. Tooling for the latter has not satisfactory been developed and dpeloyed in a privacy presering manner.

Conclusions and Recommendations
===============================

There are several significant human rights improvements noticeable for end-users based on QUIC. The first significant improvement will be mostly noticed by people on high-loss, high-latency connections, who generally are not the focus of protocol designers. These users will benefit from lower latencies and won't need to restart sessions as often, and if they do, that can do so without having to re-do the initial handshake. The second significant improvement is made through the use of encryption which provides authentication, stream integrity, adaptability of the protocol by overcoming ossification, and last but not least improved privacy from third-parties, including protection from meta-data analysis. 

The protocol could enable human rights better by considering to: add language tagging and charset identification in the case of Reason Phrase in the CONNECTION_CLOSE and APPLICATION_CLOSE, the translation of the QUIC specification to other languages, to make tooling publicly availbale for running QUIC servers, to reconsider the addition of the spinbit, to continue to monitor and discuss the implications for the power relation between end-user on the one hand and network operators and service providers on the other, without solely focusing on the relation between the latter two. The working group could also consider deploying IP header encryption on IPv6 networks, where NATs are not as widely deployed as on IPv4 networks, potentially as an optional extension.

Acknowledgements
================

We would like to thank (in alphabetical order): Mike Bishop, dkg, Jana Iyengar, Mirja Kuehlewind, Mark Nottingham, Martin Thompson, and Brian Trammel for their contributions to this document (this document does not necessarily reflect their opinion, but solely that of the authors). 



   
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

