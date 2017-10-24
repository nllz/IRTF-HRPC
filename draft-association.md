--- 
title: Freedom of Association on the Internet
abbrev: FoA
docname: draft-tenoever-hrpc-association-02
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
   RFC0001:
   RFC0155: 
   RFC1211:
   RFC1287:
   RFC1930:
   RFC3233:
   RFC1958:
   RFC4084:
   RFC4033:
   RFC4880:
   RFC4949:
   RFC5246:
   RFC5694:
   RFC5751:
   RFC6176:
   RFC6973:
   RFC7118:
   RFC7754:
   RFC7858:

   UDHR:
     title: The Universal Declaration of Human Rights
     date: 1948
     author:
        - org: United Nations General Assembly
     target:  http://www.un.org/en/documents/udhr/

   ICCPR:
     title: International Covenant on Civil and Political Rights
     date: 1966
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
     
   Lessig:
     title: Code and Other Laws of Cyberspace
     date: 1999
     author:
        - ins: Lawrence Lessig
     seriesinfo: "Basic Books, Inc. New York, NY, USA."

   Boyle:
     title: Foucault in Cyberspace: Surveillance, Sovereignty, and Hardwired Censors
     date: 1997
     author:
        - ins: James Boyle
     target: http://scholarship.law.duke.edu/faculty_scholarship/619/
     seriesinfo: "66 University of Cincinnati Law Review 177-205 (1997)"
     
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
      title: "Fictitious Profiles and WebRTC's Privacy Leaks Used to Identify Iranian Activists"
      date: 2016
      author:
        - ins: C. Anderson
        - ins: C. Guarnieri
      target: https://iranthreats.github.io/resources/webrtc-deanonymization/

   Hildebrandt:
      title: The rule of law in cyberspace?
      date: 2013
      author:
        - ins: Mireille Hildebrandt
      target: https://works.bepress.com/mireille_hildebrandt/48/download/
      seriesinfo: "Inaugural Lecture at Institute of Computing and Information Sciences (iCIS), Radboud University Nijmegen, 22 December 2011"

   OSCE:
      title: Guidelines on Freedom of Peaceful Assembly 
      date: 2010
      author:
         - org: OSCE Office for Democratic Institutions and Human Rights
      target: https://www.osce.org/odihr/73405?download=true
      seriesinfo: page 24

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

   NelsonHedlun:
     title: "A Network of Peers: Models Through the History of the Internet"
     date: 2001
     author:
        - ins: N. Minar
        - ins: M. Hedlun
     target: "http://library.uniteddiversity.coop/REconomy_Resource_Pack/More_Inspirational_Videos_and_Useful_Info/Peer_to_Peer-Harnessing_the_Power_of_Disruptive_Technologies.pdf"
     seriesinfo: "Peer to Peer: Harnessing the Power of Disruptive Technologies, ed: Andy Oram"

   Vu:
     title: "Peer-to-Peer Computing: Principles and Applications"
     date: 2010
     author:
        - ins: Vu, Quang Hieu
        - ins: Lupu, Mihai
        - ins: Ooi, Beng Chin 
     target: "https://www.springer.com/cn/book/9783642035135"

   Star:
     title: The Ethnography of Infrastructure
     date: 1999
     author:
        - ins: S.L. Star
     target: http://journals.sagepub.com/doi/abs/10.1177/00027649921955326
     seriesinfo: "American Behavioral Scientist, Volume 43 (3), 377-391."

   Schleuder:
     title: "Schleuder - A gpg-enabled mailinglist with remailing-capabilities."
     author:
        - org: Nadir
     date: 2017
     target: https://schleuder.nadir.org/

   Crawford:
     title: "The WebRTC VPN “Bug” and How to Fix"
     date: 2015
     author: 
        - ins: D. Crawford
     target: https://www.bestvpn.com/the-webrtc-vpn-bug-and-how-to-fix-it/

   RPZ:
     title: "DNS Response Policy Zones (RPZ)"
     date: 2017
     author:
        - ins: P. Vixie
        - ins: V. Schyver
     target: https://tools.ietf.org/html/draft-ietf-dnsop-dns-rpz-00

   Sink:
     title: Version Control by Example
     date: 2011
     author:
        - ins: E. Sink
     target: http://ericsink.com/vcbe/

--- abstract

This document aims to scope the relation between Internet protocols and the right to freedom of assembly and association. The Internet increasingly mediates our lives and our ability to excercise human rights. Since Internet protocols play a central role in the management, development and use of the Internet, the relation between protocols and the aforementioned rights should be documented and adverse impacts should be mitigated. As there have been methods of protest on the Internet -a form of freedom of assembly- that have proven to be harmful to connectivity and infrastructure, such as DDoS attacks, this text aims to document forms of protest, association and assembly that do not have a negative impact on the Internet infrastructure.

--- middle


Introduction
============

The right to freedom of assembly and association protects collective expression, in turn, systems and protocols than enable communal communication between people and servers allow these rights to prosper. The Internet itself was originally designed as "a medium of communication for machines that share resources with each other as equals" {{NelsonHedlun}}, the Internet thus forms a basic infrastructure for the right freedom of assembly and association. 

The manner in which communication is designed and implemented impacts the ways in which rights can be excercised. For instance a decentralized and resilient architecture that protects anonimity and privacy, offers a strong protection for the exercise of such freedoms in the online environment. At the same time, centralized solutions have enabled people to group together in recognizable places and helped the visbility of groups. 

draft-irtf-hrpc-research established the relationship between human rights and Internet protocols, and it provides guidelines for considerations on the human rights impact of protocols. 

This draft aims to take continue the work started in draft-irtf-hrpc-research by investigating the exact impact of Internet protocols on a specific human rights, namely the right to freedom of assembly and association given their importance for the Internet, in order to mitigate (potential) negative impacts. 


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

1. How does the internet architecture enable and/or inhibit freedom of association and assembly?

2. Is the Internet an assembly or association? Should it be protected as such? 


Methodology
============

In order to answer the research questions, first a number of cases have been collected to analyze where Internet infrastructure and protocols have either enabled or inhibited groups of people to collaborate, cooperate or communicate. This overview does not aim to cover all possible ways in which people can collectively organize or reach out to each other using Internet infrastructure and Internet protocols, but rather cover typical uses in an effort of doing an ethnography of infrastructure {{Star}}. Subsequently we analyze the cases with the theoretical framework provided in the literature review and provide recommendations based on the findings.

The scope of this research is open protocols and architectures developed in the IETF, thus closed and centralized Internet platforms such as Facebook do not fall within the scope of this research.

Literature Review
=================

The right to freedom of assembly and association protects and enables collective action and expression {{UDHR}} {{ICCPR}}. These rights ensures everyone in a society has the opportunity to express the opinions they hold in common with others, which in turn facilitates dialogue among citizens, as well as with political leaders or governments {{OSCE}}. They are relevant because in the process of democratic delibration, causes and opinions are more widely heard when a group of people come together behind the same cause or issue {{Tocqueville}}. 

In international law, the right to freedom of assembly and association protects any collective, gathered either permanently or temporarily for "peaceful" purposes. We will later expand on the definitions and limits of "peacefulness" within these rights. For now it is important to underline the propery of "freedom" because the rights to freedom of association and assembly is voluntary and uncoerced: anyone can join or leave a group of choice, which in turn means one should not be forced to either join, stay or leave.

The difference between freedom of assembly and freedom of association is merely a gradual one: the former tends to have an informal and ephemeral nature, whereas the latter refers to established and permanent bodies with specific objectives. Both freedoms are, regardless, protected to the same degree.

An assembly is an intentional and temporary gathering of a collective in a private or public space for a specific purpose: demonstrations, indoor meetings, strikes, processions, rallies or even sits-in {{UNHRC}}. The right to protest is a conglomerate of various rights, and the right to assembly is one of them. Nonetheless protest, unlike assembly, involves an element of dissent that can be exercised individually whereas assembly always has a collective component {{ARTICLE19}}. 

Association on the other hand has a more formal and established nature. It refers to a group of individuals or legal entities brought together in order to collectively act, express, pursue or defend a field of common interests {{UNGA}}. Within this category we can think about civil society organizations, clubs, cooperatives, NGOs, religious associations, political parties, trade unions or foundations.

Internet-enabled technologies are increasingly being used as a platform for protest. Digital technologies play an important role "by helping individuals and groups to organise and plan effectively and quickly, respond to certain events, or document and report on protests "{{ARTICLE19}}. According to Hussain and Howard the Internet helped to "build solidarity networks and identification of collective identities and goals", facilitate protest, "extend the range of local coverage to international broadcast networks" and as platform for contestation for the future of "the future of civil society and information infrastructure" {{HussainHoward}}. 

Protests are no longer limited to public physical spaces: squares, streets or parks. Technology "makes it possible for people to 'gather' in online spaces and engage in new forms of 'virtual' protest" {{ARTICLE19}}. Online association and assembly are crucial to mobilise groups and people where physical gatherings have been impossible or dangerous {{APC}}. Throughout the world -from the Arab Spring to Latin American student movements- the Internet has also played a crucial role by providing a means for the fast dissemination of information that was otherwise mediated by broadcast media, or even forbidden by the government {{Pensado}}. 

Protocols are a part of the socio-technical ordering of the world. In this research paper, we recognize that the line between protocols and applications, implementations, policies and offline realities are often blurried and hard (if not impossible) to differentiate.

## Freedom of Association in the IETF context

The right to freedom of assembly and association is crucial for the Internet, even if privacy and freedom of expression have this far been most prominently explored in the online world. The IETF itself, defined as a 'open global community' of network designers, operators, vendors, and researchers, is protected by freedom of assembly and association {{RFC3233}}. The voluntary nature of the IETF, as well as the freedom not to be coerced by the IETF to act against one's will, is protected by freedom of assembly and association. Discussions, comments and consensus around RFCs are possible because of the collective expression that freedom of association and assembly allow. The very word “protocol” found its way into the language of computer networking based on the need for collective agreement among network users {{HafnerandLyon}}. 

While individual Internet-enabled services or platforms may be public or private to varying degrees, and thereby enable to effective enjoyment of the right to freedom of assembly and association in different ways and to various extents {{Lessig}}, {{Boyle}}, the standardised technical underpinnings of those services or platforms may influence the ease with which private or public platforms can choose to lend themselves to such public enjoyment. Within the framework of {{Hildebrandt}} it could be argued that protocols nudge (or empower) implementors to enable certain forms of enjoyments of these rights. Or that specifications for the protocols may at least attempt to void the specification of the protocol of any nudging or empowerment one way or the other. If a technical architecture can be made such that nudging, or empowerment, to the effect of making the enjoyment of the freedom to assembly and association by individual end-users or independent entities more difficult (consider, for instance, Videotex), the opposite may be true as well.

In this view, it becomes relevant to assess the degree to which particular protocol design choices enable spaces opened up by the implementation of that protocol, to be spaces where freedom of assembly and association may be enjoyed.

Cases and examples
==================

The Internet has become a central mediator for collective action and collaboration. This means the Internet has become a strong enabler of the rights to freedom of association and assembly. 

Here we will discuss different cases to bring out the characteristics and consequences of different protocols, technologies and architectural features. This issue is particularly timely since an increasing trend of centralization and consolidation on the Internet can be observed. This trend can be parallely observed on the application level, among Content Distribution Networks, hosting providers, as well as Internet access providers. Through the discussion of specific case we will try to further understand how this impact freedom of assembly, freedom of association as well as the distributed nature of the Internet {{RFC1287}}.

## Communicating

The ability to produce, receive and spread information is an essential pre-requisite for discussing and organizing. Protocols that enable private, open, collaborative and non-excluding communication models are the best fitted to foster and enable assembly and association rights. 

### Mailing Lists

Since the beginning of the Internet mailing lists have been a key site of assembly and association {{RFC0155}} {{RFC1211}}. In fact, mailing lists were one of the Internet's first functionalities {{HafnerandLyon}}.

In 1971, four years after the invention of email, the first mailing list was created to talk about the idea of using Arpanet for discussion. By this time, what had initially propelled the Arpanet project forward as a resource sharing platform was gradually replaced by the idea of a network as a means of bringing people together {{Abbate}}. More than 45 years after, mailing lists are pervasive and help communities to engage, have discussion, share  information, ask questions, and build ties. Even as social media and discussion forums grew, mailing lists continue to be widely used {{AckermannKargerZhang}}. They are a crucial tool to organise groups and individuals around themes and causes {{APC}}.

Mailinglist are still in wide use, also in the IETF because they allow for easy association and allow people to subscribe (join) and unsubscribe (leave) as they please. They also allow for association of specific groups on closed lists. Finally the archival function allows for accountabilty. The downsides of mailinglists are similar to the ones generally associated with e-mail, except that end-to-end encryption such as OpenPGP {{RFC4880}} and S/MIME {{RFC5751}} is not possible because the final recipients are not known. There have been expirimental solutions to address this issues such as Schleuder {{Schleuder}}, but this has not been standardized or widely deployed.

### Multi-party video conferencing and risks

Multi-party video conferencing protocols such as WebRTC {{RFC6176}} {{RFC7118}} allow for robust, bandwidth-adaptive, wideband and super-wideband video and audio discussions in groups. 'The WebRTC protocol was designed to enable responsive real-time communications over the Internet, and is instrumental in allowing streaming video and conferencing applications to run in the browser. In order to easily facilitate direct connections between computers (bypassing the need for a central server to act as a gatekeeper), WebRTC provides functionality to automatically collect the local and public IP addresses of Internet users (ICE or STUN). These functions do not require consent from the user, and can be instantiated by sites that a user visits without their awareness. The potential privacy implications of this aspect of WebRTC are well documented, and certain browsers have provided options to limit its behavior.' {{AndersonGuarnieri}}.

'The disclosure of network addresses presents a specific risk to individuals that use privacy tools to conceal their real IP address to sites that they visit. Typically, when a user browses the Internet over a VPN, the only address that should be recorded by sites they visit would be that of the VPN provider itself. Using the WebRTC STUN function allows a site to additionally enumerate the addresses that are associated with the computer that the visitor is using – rather than those of intermediaries. This means that if a user is browsing the Internet on an ADSL connection over a VPN, a malicious site they visit could potentially surreptitious record the home address of the user.' {{AndersonGuarnieri}}.

While facilitating freedom of assembly and association multi-party video conferencing tools might pose concrete risks for those who use them. One the one hand WebRTC is providing a resilient channels of communications, but on the other hand it also exposes information about those who are using the tool which might lead to increased surveillance, identification and the consequences that might be derived from that. This is especially concerning because the usage of a VPN does not protect against the exposure of IP addresses {{Crawford}}. 

The risk of surveillance is also true in an offline space, but this is generally easy to analyze for the end-user. Security and privacy expectations of the end-user could be made more clear to the user (or improved) which would result in a more secure and/or private excercise or the right to freedom of assembly or association.


## Peer-to-peer networks and systems

At the organizational level, peer production is one of the most relevant innovations from Internet mediated social practices. According to {{Benkler}}, it implies 'open collaborative innovation and creation, performed by diverse, decentralized groups organized principally by neither price signals nor organizational hierarchy, harnessing heterogeneous motivations, and governed and managed based on principles other than the residual authority of ownership implemented through contract.' {{Benkler}}. 

In his book The Wealth of Networks, Benkler significantly expands on his definition of commons-based peer production. According to Benkler, what distinguishes commons-based production is that it doesn't rely upon or propagate proprietary knowledge: "The inputs and outputs of the process are shared, freely or conditionally, in an institutional form that leaves them equally available for all to use as they choose at their individual discretion." {{Benkler}} To ensure that the knowledge generated is available for free use, commons-based projects are often shared under an open license.

### Peer-to-peer system achitectures

Peer-to-peer (P2P) is esentially a model of how people interact in real life because "we deal directly with one another whenever we wish to" {{Vu}}. Usually if we need something we ask our peers, who in turn refer us to other peers. In this sense, the ideal definition of P2P is that "nodes are able to directly exchange resources and services between themselves without the need for centralized servers" and where each participating node typically acts both as a server and as a client {{Vu}}. In RFC 5694 P2P has been defined as peers or nodes that should be able to communicate directly between themselves without passing intermediaries, and that the system should be self-organizing and have decentralized control {{RFC5694}}. With this in mind, the ultimate model of P2P is a completely decentralized system, which is more resistant to speech regulation, immune to single points of failure and have a higher performance and scalability. Nonetheless, in practice some P2P systems are supported by centralized servers and some others have hybrid models where nodes are organized into two layers: the upper tier servers and the lower tier common nodes {{Vu}}.

Since the ARPANET project, the original idea behind the Internet was conceived as what we would now call a peer-to-peer system {{RFC0001}}. Over time it has increasingly shifted towards a client/server model with "millions of consumer clients communicating with a relatively priviledged set of servers" {{NelsonHedlun}}. Whether for resource sharing or data sharing, P2P systems are a form of enabling freedom of assembly and association. Not only they allow for effective dissemination of information, but they also because leverage computing resources by diminishing costs allowing for the formation of open collectives at the network level. At the same time, in completely descentralized systems the nodes are autonomous and can join or leave the network as they want also makes the system unpredicable: a resource might be only sometimes available, and some others it might be missing or incomplete {{Vu}}. Lack of information might in turn make association or assembly more difficult. 

Additionally, when one architecturally asseses the role of P2P systems on can say that: "The main advantage of centralized P2P systems is that they are able to provide a quick and reliable resource locating. Their limitation, however, is that the scalability of the systems is affected by the use of servers. While decentralized P2P systems are better than centralized P2P systems in this aspect, they require a longer time in resource locating. As a result, hybrid P2P systems have been introduced to take ad- vantages of both centralized and decentralized architectures. Basically, to maintain the scalability, similar to decentralized P2P systems, there are no servers in hybrid P2P systems. However, peer nodes that are more powerful than others can be se- lected to act as servers to serve others. These nodes are often called super peers. In this way, resource locating can be done by both decentralized search techniques and centralized search techniques (asking super peers), and hence the systems benefit from the search techniques of centralized P2P systems." {{Vu}}

## Version control

Ever since developers needed to collaboratively write, maintain and discuss large code basis for the Internet there have been different approaches of doing so. One approach is discussing code through mailing lists, but this has proven to be hard in case of maintaining the most recent versions. There are many different versions and characteristics of version control systems. 

A version control system is a piece of software that enables developers on a software team to work together and also archive a complete history of their work {{Sink}}. This allows teams to be working simultaneously on updated. According to Sink, broadly speaking, the history of version control tools can be dividied into three generations. In the first one, concurrent development meant that only one person could be working on a file at a time. The second generation tools permit simultaneous modifications as long as users merge the current revisions into their work before they are allowed to commit. The hird generation tools allow merge and commit to be separated {{Sink}}.

Interestingly no version control system has ever been standardized in the IETF whereas the version control systems like Subversion and Git have are widely used within the community, as well as by working groups. There has been a spirited discussion on whether working groups should use centralized forms of the Git protocol, such as those offered by Gitlab or Github. Proponents argue that this simplifies the workflow and allows for a more transparent workflow. Opponents argue that the relience on a centralized service which is not merely using the Git protocol, but also used non-standardize options like an Issue-Tracker, makes the process less transparent and reliant on a third party. 

The IETF has not made a decision on the use of centralized instances of git, such as Github or Gitlab. There have been two efforts to standardize the workflow vis a vis these third party services, but these haven't come to fruition:
https://www.ietf.org/archive/id/draft-nottingham-wugh-services-00.txt
https://www.ietf.org/archive/id/draft-thomson-github-bcp-00.txt

## Reaching out

In meatspace, handing out pamphlets and reaching out to unknown people is the most common way for growing a cause and seeking collective support. The characteristics of the Internet infrastructure and online space make reaching out more difficult.

### Spam, filter bubbles, and unrequested messaging

In the 1990s as the internet became more and more commercial, spam came to be defined as irrelevant or unsolicited messages that were porsted many times to multiple news groups or mailing lists {{Marcus}}. Here the question of consent is crucial. In the 2000s a large part of the discussion revolved around the fact that certain corporations -protected by the right to freedom of association- considered spam to be a form of "comercial speech", thus encompassed by free expression rights {{Marcus}}. Nonetheless, if we consider that the rights to assembly and association also mean that "no one may be compelled to belong to an association" {{UDHR}}, spam infringes both rights if an op-out mechanism is not provided and people are obliged to receive unwanted information, or be reached by people they do not know.

This leaves us with an interesting case: spam is currently handled mostly by mailproviders on behalf of the user, next to that countries are increasingly adopting opt-in regimes for mailinglists and commercial e-mail, with a possibility of serious fines in case of violation.

While this protects the user from being confronted with unwanted messages, it also makes it legally and technically very difficult to communicate a message to someone who did not explicitly ask for this. In public offline spaces we regularly get exposed to flyers, invitations or demonstrations where our opinions get challenged, or we are invited to consider different viewpoints. There is no equivalent on the Internet with the technical and legal regime that currently operates in it. In other words, it is nearly impossible  to provide information, in a proportionate manner, that someone is not explicility expecting or asking for. This reinforces a concept that is regularly discussed on the application level, called ‘filter bubble’: “The proponents of personalization offer a vision of a custom-tailored world, every facet of which fits us perfectly. It’s a cozy place, populated by our favorite people and things and ideas.” {{Pariser}}. “The filter bubble’s costs are both personal and cultural. There are direct consequences for those of us who use personalized filters. And then there are societal consequences, which emerge when masses of people begin to live a filter bubbled-life (…). Left to their own devices, personalization filters serve up a kind of invisible autopropaganda, indoctrinating us with our own ideas, amplifying our desire for things that are familiar and leaving us oblivious to the dangers lurking in the dark territory of the uknown.” {{Pariser}}.

It seems that the ‘filter bubble’-effect can also be observed at the infrastructure level, which actually strenghtens the impact and thus hampers the effect of collective expression. This could be interpretated as an argument for the injection of unrequested messages, spam or other unrequested notifications. But the big difference between the proliferation of such messages offline and online is the investment that is needed. It is not hard for a single person to message a lot of people, whereas if that person needed to go house by house the scale and impact of their actions would be much smaller. Inversely if it were a common practice to expose people to unwanted messages online, users would be drowned in such messages, and no expression would be possible anymore.  Allowing illimited sending of unsolicited messages would be a blow against freedom of speech: when everyone talks, nobody listens. 

Here the argument is very similar to DDoS attacks: whereas one could argue for legitimate uses in limited specific cases, these would be drowned out by a malicious use which constitutes an attack on the internet infrastructure and thus the assembly or association itself.

### Distributed Denial of Service Attacks

One of the most common examples of an association at the infrastructure level are the Distributed Denial of Service Attacks (DDoS) in which the infrastructure of the Internet is used to express discontent with a specific cause {{Abibil}} {{GreenMovement}}. Unfortunately DDoS are often used to stifle freedom of expression as they complicate the ability of independent media and human rights organizations to exercise their right to (online) freedom of association, while facilitating the ability of governments to censor dissent. This is one of the reasons protocols should seek to mitigate DDoS attacks {{BCP72}}. 

As described in draft-irtf-hrpc-research: "Uses of DDoS might or might not be legitimate for political reasons, but the IETF has no means or methods to assess this, and in general enabling DDoS would mean a deterioration of the network and thus freedom of expression". This is argued from the vector of freedom of expression, but if we would analyze it from the perspective of freedom of association the argument could be as follows: If the Internet is an association, any attack should be prevented and mitigated because it prevents the possibility of exercising a right to collective expression, which is consistent with {{BCP72}}. More will be said on this topic in the last section of the present text.

 On the other hand, it must be taken into consideration that DDoS attacks are a form of forced assembly when done without the agreement -or even knowledge- of the involved parts. This point was also described in draft-irtf-hrpc-research: "When it comes to comparing DDoS attacks to protests in offline life, it is important to remember that only a limited number of DDoS attacks involved solely willing participants.  In most cases, the clients are hacked computers of unrelated parties that have not consented to being part of a DDoS (for exceptions see Operation Abibil {{Abibil}} or the Iranian Green Movement DDoS {{GreenMovement}}).


## Grouping together (identities)

Collective identities are also protected by freedom of association and assembly. Acording to Melucci these are 'shared definitions produced by several interacting individuals who are concerned with the orientation of their action as well as the field of opportunities and constraints in which their action takes place.' {{Melucci}} In this sense, assemblies and associations are an important base in the maintenance and development of culture, as well as preservation of minority identities {{OSCE}}. 

### DNS

Domain names allow hosts to be identified by human parsable information. Whereas an IP address might not be the expression of an identity, a domain name can be, and often is. On the other hand the grouping of a certain identity under a specific domain or even a Top Level Domain brings about risks, for connecting an identity to a hierarchically structured identifier systems creates a central attack surface. Some of these risks are the surveillance of the services running on the domain, domain based censorship {{RFC7754}}, or impersonation of the domain through DNS cache poisoning. Several technologies have been developed in the IETF to mitigated these risks such as DNS over TLS {{RFC7858}}, DNSSEC {{RFC4033}}, and TLS {{RFC5246}}. These mitigations would, when implemented, not make censorship impossible, but rather make it visible. The use of a centralized authority always makes censorship through a registry or registrar possible, as well as by using a fake resolver or using proposed standards such as DNS Response Policy Zones {{RPZ}}.

The structuring of DNS as a hierarchical authority structure also brings about specific characteristic, namely the possibility of centralized policy making on the management and operation of domain names, which is what (in part) happens at ICANN. The impact of ICANN processes on human rights will not be discussed here. 
 
### ASes

In order for edge-users to connect to the Internet, a user needs to be connected to an Automous System (AS) which, in turn, has peering or transit relations with other AS'es. This means that in the process of accessing the Internet the edge-user needs to accept the policies and practices of the intermediary that provides them access to the other networks. In other words, for users to be able to join the 'network of networks', they always need to connect through an intermediary. 

While accessing the Internet through an intermediary, the user is forced to accept the policies, practices and principles of a network. This could impede the rights of the edge-user, depending on the implemented policies and practices on the network and how (if at all) they are communicated to them. For example: filtering, blocking, extensive logging or other invasive practices that are not clearly communicated to the user.

In some cases it also means that there is no other way for the edge-user to connect to the network of networks, and is thus forced into accepting the policies of a specific network, because it is not trivial for an edge-user to operate an AS and engage in peering relation with other ASes. This design, combined with the increased importance of the Internet to make use of basic services, forces edge-user to engage in association with a specific network eventhough the user does not consent with the policies of the network. 


Discussion: The Internet as an association
==========================================

It is undeniable that communities, collaboration and joint action lie at the heart of the Internet. Even at at linguistical level, the words "networks” and “associations” are close synonyms. Both interconnected groups and assemblies of people depend on “links” and “relationships” {{Swire}}. Taking this definition and the previous analysis into consideration, we argue that the Internet constitutes a an assembly and an association. What are the implications of this? Does it mean that every network is an assembly and has absolute freedom to implement its own rules? Or does the importance of a functioning 'larger' assembly (the Internet) has prevails over the preferences of the smaller ones (individual AS'es)? 
The demands that have been set for ASes is very limited and are based on routing principles: an AS must be used for exchanging external routing information with other ASes through BGP, should therefore use BGP and IP and have a routing policy {{RFC1930}}. So in order to be able to connect to the Internet as an AS, which means to engage in peering or transit relations, there are basic rules one needs to adhere to.  But theses rules do not say anything on how the AS will or should treat traffic on its network. In this regard, we must take into consideration that even things that are private, need to live up to standards because they have public consequences. If we take the example of ASes, we could say they are private infrastructure (therefore souvereign with the ability to set their own policies), but jointly they form a type of public infrastructure, from the moment the receive an Autonomous Systems Number. 

The Internet is made of up interconnected ASes (one would argue that this doesn't include IXPs, but most modern IXPs will have an ASN for their route server (and possibly a separate ASN for their management infrastructure), which jointly form an assembly and an association. This assembly and association should be protected. This means that rights and obligations that sterm from this organizational form, should also be protected and respected.
 
Conclusions
===========

The Internet has an impact on the ability for people to excercise their right to freedom of association and assembly. The Internet, since its inception has enabled people to jointly communicate, collaborate and collaborate. The same could also be argued with relation to freedom of expression, some have argued that the text in article 19 of the {{UDHR}} reads like a description of the Internet:

   [the] freedom to hold opinions without interference and to seek, receive and impart information and ideas through any media and regardless of frontiers. {{UDHR}}

The difference between freedom of expression and freedom of association and assembly is that the Internet itself takes the form on an association and assembly; it reproduces its features of collaboration. Recognizing this is a crucial step in determining architectural features of the Internet and its usage. 


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


