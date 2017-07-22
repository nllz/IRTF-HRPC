
##just testing on a Friday night <3
--- 
title: Freedom of Association on the Internet
abbrev: FoA
docname: draft-tenoever-hrpc-association-00
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
       ins: G. Perez de Acha
       name: Gisela Perez de Acha
       organization: Derechos Digitales
       email: gisela@derechosdigitales.org

normative:

informative: 
   RFC0155: 
   RFC1211:
   RFC1287:
   RFC3233:
   RFC1958:
   RFC4084:
   RFC4949:
   RFC6973:
   RFC7858:

   UDHR:
     title: The Universal Declaration of Human Rights
     date: 1948
     author:
        - org: United Nations General Assembly
     target:  http://www.un.org/en/documents/udhr/

   ICCPR:
     title: International Covenant on Civil and Political Rights
     date: 1976
     author:
        - org: United Nations General Assembly
     target: http://www.ohchr.org/EN/ProfessionalInterest/Pages/CCPR.aspx

   Tocqueville:
     title: Democracy in America
     author:
        - ins: A. de Tocqueville
     target: http://classiques.uqac.ca/classiques/De_tocqueville_alexis/democracy_in_america_historical_critical_ed/democracy_in_america_vol_2.pdf p. 304

   Abibil:
     title: Dissecting 'Operation Ababil' - an OSINT Analysis
     date: 2012
     author:
        - ins: D. Danchev
     target: http://ddanchev.blogspot.be/2012/09/dissecting-operation-ababil-osint.html

   GreenMovement:
     title: Iran DDoS
     date: 2009
     author:
        - ins: N. Villeneuve
     target: https://www.nartv.org/2009/06/16/iran-ddos/

   BCP72:
     title: Guidelines for Writing RFC Text on Security Considerations
     date: 2003
     author: 
        - org: IETF
     target: https://datatracker.ietf.org/doc/bcp72/

   HussainHoward:
     title: "What Best Explains Successful Protest Cascades? ICTs and the Fuzzy Causes of the Arab Spring"
     date: 2013
     author:
        - ins: M.M. Hussain
        - ins: P.N. Howard
     target: https://doi.org/10.1111/misr.12020
     seriesinfo: "Int Stud Rev (2013) 15 (1): 48-66."

   UNHRC:
     title: Report of the Special Rapporteur on the rights to freedom of peaceful assembly and of association 
     date: 2012
     author:
        - ins: Maina Kiai
     target: http://freeassembly.net/wp-content/uploads/2013/10/A-HRC-20-27_en-annual-report-May-2012.pdf
     seriesinfo: A/HRC/20/27
      
   APC:
     title: Freedom of assembly and association online in India, Malaysia  and Pakistan. Trends, challenges and recommendations.
     date: 2016
     author:
        - org: Association for Progressive Communications
        - ins: Gayathry Venkiteswaran 
     target: https://www.apc.org/es/system/files/FOAA_online_IndiaMalaysiaPakistan.pdf

   Swire:
     title: "Social Networks, Privacy, and Freedom of Association: Data Empowerment vs. Data Protection"
     date: 2012
     author:
        - ins: Peter Swire
     target: https://ssrn.com/abstract=1989516 or http://dx.doi.org/10.2139/ssrn.1989516
     seriesinfo: "North Carolina Law Review (2012) 90 (1): 104."

   ARTICLE19:
     title: "The Right to Protest Principles: Background Paper"
     date: 2016
     author:
        - org: ARTICLE 19
     target: https://www.article19.org/data/files/medialibrary/38581/Protest-Background-paper-Final-April-2016.pdf page 7

   UNGA:
     title: Human rights defenders
     date: 2004
     author:
        - ins: Hina Jilani
     target: http://www.un.org/en/ga/search/view_doc.asp?symbol=A/59/401 para. 46
     seriesinfo: A/59/401
     
   HafnerandLyon:
     title: Where Wizards Stay Up Late. The Origins of the Internet
     date: 1998
     author:
        - ins: K. Hafnerand
        - ins: M. Lyon
     target: https://doi.org/10.1111/misr.12020
     seriesinfo: "First Touchstone Edition (1998): 93."
   
   Pensado:
     title: Student Activism. Utopian Dreams.
     date: 2012
     author:
        - ins: Jaime Pensado
     target: http://revista.drclas.harvard.edu/book/student-activism
     seriesinfo: "ReVista. Harvard Review of Latin America (2012)."
     
   Abbate:
     title: Inventing the Internet
     date: 2013
     author:
        - ins: Janet Abbate
     target: https://mitpress.mit.edu/books/inventing-internet
     seriesinfo: "Cambridge: MIT Press (2013): 11."

   Pariser:
      title: "The Filter Bubble: How the New Personalized Web Is Changing What We Read and How We Think"
      date: 2012
      author: 
        - ins: E. Pariser
      seriesinfo: Peguin Books, London.

   Melucci:
      title: The Process of Collective Identity
      date: 1995
      author:
        - ins: A. Melucci
      seriesinfo: Temple University Press, Philadelphia

   AckermannKargerZhang:
      title: "Mailing Lists: Why Are They Still Here, What’s Wrong With Them, and How Can We Fix Them?" 
      date: 2017
      author:
        - ins: M. S. Ackerman
        - ins: D. R. Karger
        - ins: A. X. Zhang
      target: https://people.csail.mit.edu/axz/papers/mailinglists.pdf
      seriesinfo: "Mit. edu (2017): 1."

   Marcus:
      title: "Commercial Speech on the Internet: Spam and the first amendment"
      date: 1998
      author: 
        - ins: J. A. Marcus
      target: http://www.cardozoaelj.com/wp-content/uploads/2013/02/Marcus.pdf
#      seriesinfo: "Cardozo Arts & Entertainment"

   Benkler:
      title: Peer Production and Cooperation
      date: 2009
      author:
        - ins: Y. Benkler
      target: http://www.benkler.org/Peer%20production%20and%20cooperation%2009.pdf
#      seriesinfo: "M. Bauer & M. Latzer (eds.), Handbook on the Economics of the Internet, Cheltenham and Northampton, Edward Elgar."

   AndersonGuarnieri:
      title: "Fictitious Profiles and webRTC's Privacy Leaks Used to Identify Iranian Activists"
      date: 2016
      author:
        - ins: C. Anderson
        - ins: C. Guarnieri
      target: https://iranthreats.github.io/resources/webrtc-deanonymization/

--- abstract

This document aims to scope the relation between Internet protocols and the rights to freedom of assembly and association. The Internet increasingly mediates our lives and our ability to excercise human rights. Since Internet protocols play a central role in the management, development and use of the Internet, the relation between the mentioned rights should be documented, and adverse impacts should be mitigated. There have been methods of protest on the Internet -a form of freedom of assembly- that have proven to be harmful to connectivity and infrastructure, such as DDoS attacks. Therefore, this text aims to document forms of protest, association and assembly that do not have a negative impact on the Internet infrastructure.

--- middle


Introduction
============

Freedom of assembly and freedom of association are two human rights that protect and enable collective action and expression {{UDHR}} {{ICCPR}}. Both rights ensure everyone in a society has the opportunity to express the opinions they hold in common with others, which in turn facilitates dialogue within citizens, as well as between them and political leaders or government.[https://www.osce.org/odihr/73405?download=true, page 24]  This becomes crucial in a democracy because causes and opinions take more force within a group of people that come together for the same means {{Tocqueville}}. The rights to freedom of assembly and association thus protect any collective, gathered either permanently or temporarily for peaceful purposes. It is indeed a "freedom" because it is voluntary and uncoerced: anyone can join or leave a group of choice, which in turn means not forcing to do so.

The difference between freedom of assembly and freedom of association is merely gradual one: the former tends to have an informal and ephemeral nature, where as the latter refers to established and permanent bodies with specific objectives. Nonetheless, one and the other are protected to the same degree.

An assembly is an intentional and temporary gathering of a collective in a private or public space for a specific purpose: demonstrations, inside meetings, strikes, processions, rallies or even sits-in {{UNHRC}}. It is essentially a reunion. The right to protest is encompassed by this right, and it is also exercised along with freedom of expression and the right to hold an opinion. Nonetheless protest, unlike assembly, involves an element of dissent that can be exercised individually where as assembly always has a collective component {{ARTICLE19}}. Association on the other hand has a more formal and established nature. It refers to a group of individuals or legal entities brought together in order to collectively act, express, pursue or defend a field of common interests {{UNGA}}. Within this category we can think about civil society organizations, clubs, cooperatives, NGOs, religious associations, political parties, trade unions or foundations.

Rights to assembly and association are crucial for the Internet, even if privacy and freedom of expression are the most discussed human rights when it comes to the online world. It is undeniable that communities, collaboration and joint action lie at the heart of the Internet. Even at at linguistical level, the words "networks” and “associations” are close synonyms. Both interconnected groups and assemblies of people depend on “links” and “relationships” {{Swire}}. One could even argue that as a whole, the networked internet constitutes a big collective, and thus an assembly and an association. 

IETF itself, defined as a 'open global community' of network designers, operators, vendors, and researchers, is also protected by freedom of assembly and association {{RFC3233}}. Discussion, comments and consensus around RFCs are possible because of the collective expression that freedom of association and assembly allow. The very word “protocol” found its way into the language of computer networking based on the need for collective agreement among network users {{HafnerandLyon}}. 

In draft-irtf-hrpc-research the relationship between human rights and Internet protocols has been shown, and guidelines for considerations of human rights impact in protocol design have been provided. Further research is needed to understand the exact shape, extend and form of Internet protocols on human rights, including assembly and association given their importance for the Internet.

In less democratic or authoritarian countries, online association and assembly have been crucial to mobilise groups and people where physical gatherings have been impossible or dangerous {{APC}}. Throughout the world -from the Arab Spring to Latin American student movements- the Internet has also played a crucial role by providing a means for the fast dissemination of information that was otherwise mediated by broadcast media, or even forbidden by the government {{Pensado}}. According to Hussain and Howard the Internet helped to 'build solidarity networks and identification of collective identities and goals', facilitate protest, 'extend the range of local coverage to international broadcast networks' and as platform for contestation for the future of 'the future of civil society and information infrastructure' {{HussainHoward}}. 

However, some of these examples go beyond the use of Internet protocols and flow over into the applications layer or examples in the offline world, whereas the following document aims to break down the relationship between Internet protocols and the right to freedom of assembly and association.


Vocabulary used 
===============

Anonymity
: The condition of an identity being unknown or concealed. {{RFC4949}}

Censorship resistance
: Methods and measures to mitigate Internet censorship.

Connectivity
: The extent to which a device or network is able to reach other devices or networks to exchange data. The Internet is the tool for providing global connectivity {{RFC1958}}. Different types of connectivity are further specified in {{RFC4084}}. The combination of the end-to-end principle, interoperability, distributed architecture, resilience, reliability and robustness are the enabling factors that result in connectivity to and on the Internet.
	
Decentralization
: Implementation or deployment of standards, protocols or systems without one single point of control.

Pseudonymity 
: The ability to disguise one's identity online with a different name than the "real" one, allowing for diverse degrees of disguised identity and privacy. It is strengthened when less personal data can be linked to the pseudonym; when the same pseudonym is used less often and across fewer contexts; and when independently chosen pseudonyms are more frequently used for new actions (making them, from an observer's or attacker's perspective, unlinkable)."  {{RFC6973}}


Research questions
=====================

How does the internet architecture enables and/or inhibits freedom of association and assembly.


Cases and examples
=====================

## Distributed Denial of Service Attacks
##In any case, this DDoS situation should not go in the introduction, but rather as part of the body of the text. So, I moved it. I know you talked about it in the other draft, but some things might be worth repeating, or self-quoting if not. In any case, stating it at the introduction is cheating because you take it as a given, and it's not. (see comments below)

One of the most common examples of association at the infrastructure level are Distributed Denial of Service Attacks (DDoS) in which the infrastructure of the Internet is used to express discontent with a specific cause {{Abibil}} {{GreenMovement}}. Unfortunately DDoS are often used to stifle freedom of expression as they complicate the ability of independent media and human rights organizations to exercise their right to (online) freedom of association, while facilitating the ability of governments to censor dissent. This is one of the reasons protocols should seek to mitigate DDoS attacks {{BCP72}}. 
##I have issues with this paragraph because it seems like you are saying that DDoS itself is not "violent" or "non-peaceful". Your almost-to-be-RFC says "Uses of DDoS might or might not be legitimate for political reasons, but the IETF has no means or methods to assess this, and in general enabling DDoS would mean a deterioration of the network and thus freedom of expression." I think we should summarize the discussion on that draft, and then make an analogy to association. The argument should be concentrated on the latter.
##Something like: If the Internet is an association, any attack should be prevented and mitigated because it prevents the possibility of exercising a right to collective expression. My point is that you were soft on the other document regarding DDoS, and now you just jump to the conclusion that they are not good for infrastructure without properly arguing in terms of human rights. You say: "In summation, the IETF cannot be expected to take a moral stance on DDoS attacks, or create protocols to enable some attacks and inhibit others."
##In fact, it seems quite the opposite. A human right would never prohibit a "means" on itself, but the outcome of it. Not a way of collective gathering per se, but the actual concrete actions that derive from that "assembly". Can we decide that a priori? Wouldn't that be previous censorship? Let's talk it out. Or leave it for discussion. I just don't think this is solid.

When it comes to comparing DDoS attacks to protests in offline life, it is important to remember that only a limited number of DDoS attacks involved solely willing participants.  In most cases, the clients are hacked computers of unrelated parties that have not consented to being part of a DDoS (for exceptions see Operation Abibil [Abibil] or the Iranian Green Movement DDoS [GreenMovement]).
##This is great! Essentially: forced assembly! We can add more recent examples.

## Communicating
 
### Mailinglists

Since the beginning of the Internet mailing lists have been a key site of assembly and association {{RFC0155}} {{RFC1211}}. In fact, mailing lists were one of the Internet's first functionalities {{HafnerandLyon}}.

In 1971, four years after the invention of email, the first mailing list was created to discuss the idea of using Arpanet for discussion. By this time, what had initially propelled the Arpanet project forward as a resource sharing platform was gradually replaced by the idea of a network as a means of bringing people together {{Abbate}}. More than 45 years after, mailing lists are pervasive and help communities to engage, have discussion, share  information, ask questions, and build ties. Even as social media and discussion forums grew, mailing lists continue to be widely used {{AckermannKargerZhang}}. They are a crucial tool to organise groups and individuals around themes and causes {{APC}}.

### Multi party video conferencing and risks

'Beginning in early 2008, Iranian security entities have engaged in operations to identify and arrest administrators of “illicit” websites and social media groups. In recent years, the detention and interrogation of members of online communities has been publicized by state media for propaganda purposes. However, the heavy-handedness of the government has also inadvertently created a situation where Iranian users are better positioned than others to avoid some surveillance activities – increasing the burden of finding pseudonymous users.' {{AndersonGuarnieri}}.

'The WebRTC protocol was designed to enable responsive real-time communications over the Internet, and is instrumental in allowing streaming video and conferencing applications to run in the browser. In order to easily facilitate direct connections between computers (bypassing the need for a central server to act as a gatekeeper), WebRTC provides functionality to automatically collect the local and public IP addresses of Internet users (ICE or STUN). These functions do not require consent from the user, and can be instantiated by sites that a user visits without their awareness. The potential privacy implications of this aspect of WebRTC are well documented, and certain browsers have provided options to limit its behavior.' {{AndersonGuarnieri}}.

'The disclosure of network addresses presents a specific risk to individuals that use privacy tools to conceal their real IP address to sites that they visit. Typically, when a user browses the Internet over a VPN, the only address that should be recorded by sites they visit would be that of the VPN provider itself. Using the WebRTC STUN function allows a site to additionally enumerate the addresses that are associated with the computer that the visitor is using – rather than those of intermediaries. This means that if a user is browsing the Internet on an ADSL connection over a VPN, a malicious site they visit could potentially surreptitious record the home address of the user.' {{AndersonGuarnieri}}.
##Questions: association? or assembly? Second paragraph: forced association? I think we are still missing a link here.

### Reaching out

In the 1990s as the internet became more and more commercial, spam came to be defined as irrelevant or unsolicited messages that were porsted many times to multiple news groups or mailing lists {{Marcus}}. Here the question of consent is crucial. In the 2000s a large part of the discussion revolved around the fact that certain corporations -protected by the right to freedom of association- considered spam to be a form of "comercial speech", thus encompassed by free expression rights {{Marcus}}. Nonetheless, if we consider that the rights to assembly and association also mean that "no one may be compelled to belong to an association" {{UDHR}}, spam infringes both rights if an op-out mechanism is not provided and people are obliged to receive unwanted information, or be reached by people they do not know.

This leaves us with an interesting case: spam is currently handled mostly by mailproviders on behalf of the user, next to that countries are increasingly adopting opt-in regimes for mailinglists and commercial e-mail, with a possibility of serious fines in case of violation.

This protects the user from being confronted with unwanted messages, but it also makes it legally and technically very difficult to communite a message to someone who did not explicitly ask for this. In the public offline spaces we regularly get exposed to flyers, invitations or demonstrations where our opinions get challenged, or we are invited to consider different viewpoints. There is no equivalent on the Internet with the technical and legal regime that currently operates in it. In other words, it is nearly impossible  to provide information, in a proportionate manner, that someone is not explicility expecting or asking for. This reinforces a concept that is regularly discussed on the application level, called ‘filter bubble’: “The proponents of personalization offer a vision of a custom-tailored world, every facet of which fits us perfectly. It’s a cozy place, populated by our favorite people and things and ideas.” {{Pariser}}. “The filter bubble’s costs are both personal and cultural. There are direct consequences for those of us who use personalized filters. And then there are societal consequences, which emerge when masses of people begin to live a filter bubbled-life (…). Left to their own devices, personalization filters serve up a kind of invisible autopropaganda, indoctrinating us with our own ideas, amplifying our desire for things that are familiar and leaving us oblivious to the dangers lurking in the dark territory of the uknown.” {{Pariser}}. It seem that the ‘filter bubble’-effect can also be observed at the infrastructure level, which actually strenghtens the impact and thus hampers the effect of collective expression.

##What will we do with Stephane’s comments? They were good when he was talking about pull/push. Essentially:
* About protest [Note that it is related to the problem of the lack of a public space - think streets and market places - on the Internet.]
* There is here a difference between the Internet and the meat space. In the meat space, it is acceptable to "push" messages to people "who did not explicitly ask for this" because it doesn't scale: Jehovah's witnesses can bang on your door, to talk about Jesus and it is most of the time regarded as acceptable (even if annoying) precisely because it doesn't scale. One Jehovah's witness cannot bang on one million doors at the same time. So, there is little risk that this freedom to push messages will be abused. On the Internet, it is the opposite. The example given in the draft ("a message was distributed to the server logs of millons of servers through the 'masscan'-tool") is spam, pure and simple. One person can do it, with very limited resources. If it were regarded as acceptable, logs would become unusable.

## Working together (peer production)

At the organizational level, peer production is one of the most relevant innovations from Internet mediated social practices. According to Benkler, it implies 'open collaborative innovation and creation, performed by diverse, decentralized groups organized principally by neither price signals nor organizational hierarchy, harnessing heterogeneous motivations, and governed and managed based on principles other than the residual authority of ownership implemented through contract.' {{Benkler}}. 

### Version control

Ever since developers needed to collaboratively write, maintain and discuss large code basis for the Internet there have been different approaches of doing so. One approach is discussing code through mailing lists, but this has proven to be hard in case of maintaining the most recent versions. There are many different versions and characteristics of version control systems. 

## Grouping together (identities)

Collective identities are also protected by freedom of association and assembly rights. Acording to Melucci these are 'shared definitions produced by several interacting individuals who are concerned with the orientation of their action as well as the field of opportunities and constraints in which their action takes place.' {{Melucci}} In this sense, assemblies and associations are an important base in the maintenance and development of culture, as well as preservation of minority identities. [https://www.osce.org/odihr/73405?download=true, page 15] 

### DNS

Domain names allow hosts to be identified by human parsable information. Whereas an IP address might not be the expression of an identity, a domain name can be, and often is. On the other hand the grouping of a certain identity under a specific domain, or even a Top Level Domain, also brings about risks because connecting an identity to a hierarchically structured identifier systems also bring risks about. Risks could be surveillance of the services running on the domain, domain based censorship, or impersonation of the domain through DNS cache poisoning. Several technologies have been developed in the IETF to mitigated these risks such as DNS over TLS {{RFC7858}}, DNSSEC, and TLS. 

The structuring of DNS as a hierarchical authority structure also brings about specific characteristic, namely the possibility of centralized policy making on the management and operation of domain names, which is what (in part) happens at ICANN. The impact of ICANN processes on human rights will not be discussed here. 
 
### ISPs

In order for edge-users to connect to the 'network of networks', the user needs to be connected to a network. This means that in the process of accessing the network of networks the edge-user needs to accept the policies and practices of the network they connect to. There is not necessarily a uniform way in which the policies, practices and principles of the network are communicated to the edge-user. These practices might include filtering, blocking, extensive logging or other invasive practices that are not clearly communicated to the user.
##My god, like five "network" in a paragraph. Could there be sinonyms?

In some cases it also means that there is no other way for the edge-user to connect to the network of networks, and is thus forced into accepting the policies of a specific network, because it is not trivial for an edge-user to operate its own Autonomous System. This design, combined with the increased importance of the Internet to make use of basic services, forces edge-user to engage in association with a specific network eventhough the user does not consent with the policies of the network. 

### Centralization

There is an increasing trend of centralization and consolidation on the Internet, this is trend can be observed on the application level, among Content Distribution Networks, hosting providers, as well as Internet access providers. This trend forms a thread to the distributed nature of the Internet {{RFC1287}} in different ways.

Federation


Example Mastodon. Protocols instead of platforms. 


 
Conclusions
===========



Acknowledgements
================

Security Considerations
=======================

As this draft concerns a research document, there are no security considerations.

IANA Considerations
===================

This document has no actions for IANA.

Research Group Information
==========================
The discussion list for the IRTF Human Rights Protocol Considerations Research Group is located at the e-mail address <hrpc@ietf.org>. Information on the group and information on how to subscribe to the list is at
<https://www.irtf.org/mailman/listinfo/hrpc>

Archives of the list can be found at:
<https://www.irtf.org/mail-archive/web/hrpc/current/index.html>


