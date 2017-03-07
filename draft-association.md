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
   RFC1958:
   RFC4084:
   RFC4949:
   RFC6973:

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
     title: What Best Explains Successful Protest Cascades? ICTs and the Fuzzy Causes of the Arab Spring
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



--- abstract

This documents aims to document the relation between Internet protocols and the right to freedom of assembly and association. The Internet increasingly mediates our lives and thus the ability to excercise human rights. Since Internet protocols play a central role in the management, development and use of the Internet the relation between the two should be documented and adverse impacts on this human right should be mitigated. On the other hand there have also been methods of protest, a form of freedom of assembly, on the Internet that have been harmful to Internet connectivity and the Internet infrastructure, such as DDoS attacks. This document aims to document forms of protest, association and assembly that do not have a negative impact on the Internet infrastructure.

--- middle


Introduction
============

Freedom of assembly and freedom of association are two human rights that protect and enable collective action and expression. {{UDHR}} {{ICCPR}} Causes and opinions take more force within a group of people that come together for the same means. {{Tocqueville}}

The difference between the freedom of assembly and the freedom of associotiation is merely gradual one. An assembly is an intentional and temporary gathering of a collective in a private or public space for a  specific  purpose:  demonstrations,  inside  meetings,  strikes, processions,  rallies  or  even  sits-in. {{UNHRC}} The right to protest is one of the rights encompassed by freedom of assembly, but also exercised along with freedom of expression and the right to hold an opinion. Nonetheless, protest unlike assembly, implies an element of dissent that can be exercised individually, where as assembly always has a collective component. {{ARTICLE19}}

Association on the other hand has a more formal nature. It refers to a group of individuals or any legal entities brought together in order to collectively act, express, promote, pursue or defend a field of common interests. {{UNGA}} This means civil  society  organizations,  clubs, cooperatives, NGOs,  religious  associations,  political  parties,  trade unions, foundations or even **online associations as the Internet has been instrumental, for instance, in 'facilitating active citizen participation in building democratic societies'.** {{UNHRC}}

In draft-irtf-hrpc-research the relationship between human rights and Internet protocols has been shown, and guidelines for considerations of human rights impact in protocol design have been provided. 

Further research is needed to understand the exact shape, extend and form of Internet protocols on human rights.  This document aims to break down the relationship between Internet protocols and the right to freedom of assembly and association.

The right to privacy and the right to freedom of expression are the most discussed human rights when it comes to the Internet. On the other hand communities, collaboration and joint action lie at the heart of the Internet. But the Internet has also played a central role in worldy events such as the Arab Spring. According to Hussain and Howard the Internet helped to 'build solidarity networks and identification of collective identities and goals', facilitate protest, 'extend the range of local coverage to international broadcast networks' and as platform for contestation for the future of 'the future of civil society and information infrastructure' {{HussainHoward}}. This however goes beyond the use of Internet protocols and flows over into the applications layer, whereas we'll focus on the Internet protocols and architecture.

This can be contrasted with the example of Distributed Denial of Service Attacks (DDoS) in which the infrastructure of the Internet is used to express discontent with a specific cause {{Abibil}} {{GreenMovement}}. Unfortunately more of than not DDoS are used to stifle freedom of expression, complicate the ability of independent media and human rights organizations to  exercise their right to (online) freedom of association, while facilitating the ability of governments to censor dissent. This is one of the reasons protocols should seek to mitigate DDoS attacks {{BCP72}}.

This document will further seek to map how the internet architecture impacts freedom of association and assembly.


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



# communicating
 
## mailinglists
Since the beginning of the Internet mailing lists have been a key site of assembly and association. {{RFC0155}} {{RFC1211}}  One can even argue that mailing lists were one of the Internets first functionalities. 

## multi party video conferencing and risks
https://iranthreats.github.io/resources/webrtc-deanonymization/

## reaching out (spam, logs)
impossibility of providing information, in a proportionate manner, that someone is not expecting/asking for reinforces the filter bubble, is this a inherent consequent on internet infrastructure?

https://motherboard.vice.com/en_us/article/chaos-communication-congress-hackers-invaded-millions-of-servers-with-a-poem

# working together (peer production)

## version control
Ever since developers needed to collaboratively write, maintain and discuss large code basis for the Internet there have been different approaches of doing so. One approach is discussing code through mailing lists, but this has proven to be hard in case of maintaining the most recent versions. There are many different versions and characteristics of version control systems. 

centralization - differences (and gradients) between free (as in beer) and free (as in freedom). Git vs Github.	

# grouping together (identities)

## DNS
advantages and disadvantages (.gay)

## ISPs
No one may be compelled to belong to an association.
 
Notes
=====

So this is where I believe a mention should be given to the fact that we will treat both: the 'good' and the 'bad'. What I think is super interesting is that Article 20. of the UDHR guarantees a 'right to freedom of peaceful assembly and association'. Peaceful!! This could help you make a connection between peaceful = ordre public = not harming (public?) infrastructure (thinking of the DDos attacks example). But then that's a double sword as well, because fuck 'peaceful assembly', or more like 'peaceful protest'. Leaning towards there can also mean not protecting radical speech in the offline world (and infrastructure? any idea?) You see where I'm going?

Article 20. UDHR

(1) Everyone has the right to freedom of *peaceful assembly and association.*

(2) No one may be compelled to belong to an association.

Then this is a 2007 document of best pratices from the OSCE www.osce.org/odihr/73405?download=true] --> *Only peaceful assemblies are protected.* An assembly should be deemed peaceful if its organizers have professed peaceful intentions and the conduct of the assembly is non-violent. The term 'peaceful' should be interpreted to include conduct that may annoy or give offence, and even conduct that temporarily hinders, impedes or obstructs the activities of third parties.

    +-----------------------+-----------------------------------------+ 
    | Connectivity          |                                         |
    | Decentralization      |                                         |
    | Censorship resistance | Right to freedom of assembly            |
    | Pseudonymity          |                     and association     |
    | Anonymity             |                                         |
    | Security              |                                         |
    +-----------------------+-----------------------------------------+
    | Reliability           |                                         |
    | Confidentiality       |                                         |
    | Integrity             | Right to security                       |
    | Authenticity          |                                         |
    | Anonymity             |                                         |
    +-----------------------+-----------------------------------------+ 

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


