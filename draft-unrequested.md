--- 
title: Unrequested Communications
abbrev: hrpcurq
docname: draft-tenoever-unrequested
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
       ins: N. ten Oever
       name: Niels ten Oever
       organization: ARTICLE 19
       email: niels@article19.org


normative:
  
informative: 
   
   RFC4949:

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
   
   Zuckerman: 
     title: Report on Distributed Denial of Service (DDoS) Attacks 
     date: 2010 author: 
        - ins: E. Zuckerman 
        - ins: H. Roberts 
        - ins: R. McGrady 
        - ins: J. York 
        - ins: J. Palfrey 
     target: https://cyber.law.harvard.edu/sites/cyber.law.harvard.edu/files/2010_DDoS_Attacks_Human_Rights_and_Media.pdf seriesinfo: The Berkman Center for Internet and Society at Harvard University

   Sauter: 
     title: The Coming Swarm 
     date: 2014 
     author: 
         - ins: M. Sauter 
     seriesinfo: Bloomsbury, London

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

   Daedalus: 
     title: The Contingent Internet 
     date: 2016 
     author: 
        - ins: D. Clark 
     seriesinfo: Daedalus Winter 2016, Vol. 145, No. 1. p. 9–17 
     target: http://www.mitpressjournals.org/toc/daed/current

--- abstract

This document addresses the topic of unrequested traffic in the form of spam or DDoS attacks. Instead of solely discussing these topics from a mere technical angle, it also addressed human rights implications of unrequested traffic.

--- middle


Introduction
============





Glossary
========



DDOS Attacks
============

Are Distributed Denial of Service (DDoS) attacks a legitimate form of online protest protected by the right to freedom of speech and association? Can they be seen as the equivalent to 'million-(wo)men marches', or sit-ins? Or are they a threat to freedom of expression and access to information, by limiting access to websites and in certain cases the freedom of speech of others? These questions are crucial in our day and age, where political debates, civil disobedience and other forms of activism are increasingly moving online.

Many individuals, not excluding IETF engineers, have argued that DDoS attacks are fundamentally against freedom of speech. Technically DDoS attacks are when one or multiple host overload the bandwidth or resources of another host by flooding it with traffic, causing it to temporarily stop being available to users. One can roughly differentiate three types of DDoS attacks: Volume Based Attacked (This attack aims to make the host unreachable by using up all it's bandwith, often used techniques are: UDP floods and ICMP floods), Protocol Attacks (This attacks aims to use up actual server resources, often used techniques are SYN floods, fragmented packet attacks, and Ping of Death {{RFC4949}}) and Application Layer Attacks (this attack aims to bring down a server, such as the webserver).

In their 2010 report Zuckerman et al argue that DDoS attacks are a bad thing because they are increasingly used by governments to attack and silence critics. Their research demonstrates that in many countries independent media outlets and human rights organizations are the victim of DDoS attacks, which are directly or indirectly linked to their governments. These types of attacks are particularly complicated because attribution is difficult, creating a situation in which governments can effectively censor content, while being able to deny involvement in the attacks {{Zuckerman}}. DDoS attacks can thus stifle freedom of expression, complicate the ability of independent media and human rights organizations to exercise their right to (online) freedom of association, while facilitating the ability of governments to censor dissent. When it comes to comparing DDoS attacks to protests in offline life, it is important to remember that only a limited number of DDoS attacks involved solely willing participants. In most cases, the clients are hacked computers of unrelated parties that have not consented to being part of a DDoS (for exceptions see Operation Abibil {{Abibil}} or the Iranian Green Movement DDoS {{GreenMovement}}).

In addition, DDoS attacks are increasingly used as an extortion tactic, with criminals flooding a website – rendering it inaccessible – until the owner pays them a certain amount of money to stop the attack. The costs of mitigating such attacks, either by improving security to prevent them or paying off the attackers, ends up being paid by the consumer.

All of these issues seem to suggest that the IETF should try to ensure that their protocols cannot be used for DDoS attacks. Decreasing the number of vulnerabilities in the network stacks of routers or computers, reducing flaws in HTTPS implementations, and depreciating non-secure HTTP protocols could address this issue. The IETF can clearly play a role in bringing about some of these changes, and has indicated in {{RFC7258}} its commitment to mitigating 'pervasive monitoring (...) in the design of IETF protocols, where possible.' This means the use of encryption should become standard. Effectively, for the web this means standardized use of HTTPS. The IETF could redirect its work such that HTPPS becomes part-and-parcel of its standards. However, next to the various technical trade-offs that this might lead to it is important to consider that DDoS attacks are sometimes seen as a method for exercising freedom of speech.

DDoS although disruptive, and silencing at times, can also enable as protest and speech. Or as Sauter {{Sauter}} argues: 'though DDoS as a tactic is still relatively novel, it fits within a centuries-long tradition of breaking laws and disrupting business as usual to make a political point. These actions aren't simply disruption for disruption's sake. Rather they serve to help the activist or dissenter to direct the attention of the public through the interpolation of difference into routine.' (30-31). An often heard argument against DDoS attacks is that you cannot construe it as a means to exercise your right to freedom of speech, when the means used effectively impede the right of the party on the receiving end of the attack to exercise that same right. The problem with this line of argumentation is that it conveniently ignores the fact that online DDoS attacks are often one of the few effective ways for activists to gain the attention of the media, the government or other parties of interest. Simply putting up a website for a cause won't garner the same amount of attention as directly confronting the issue via the website of the individual or organization at the heart of the issue. The ability of activists to do so should be protected, especially considering the fact that as Sauter (2014:4) explains: 'Collectively, we have allowed the construction of an entire public sphere, the Internet, which by accidents of evolution and design, has none of the inherent free speech guarantees we have come to expect. Dissenting voices are pushed out of the paths of potential audiences, effectively removing them from the public discourse. There is nowhere online for an activist to stand with her friends and her sign. She might set up a dedicated blog---which may or may not ever be read---but it is much harder for her to stand collectively with others against a corporate giant in the online space.' Although the Internet is often compared to public space, it is not. Rather the opposite. The Internet is almost entirely owned by private entities. And the IETF plays a crucial role in developing this privatized commercialized Internet.

From a legal and political perspective, the IETF does not have the legitimacy to determine when a DDoS is legitimate (in legal or political terms). It does not have the capability to make this judgment as a matter of public policy and subsequently translate it to code. Nor should the IETF try to do so. From a technical perspective, the difference between a 'legitimate' and 'illegitimate' DDoS attack is meaningless because it would be extremely difficult for the IETF to engineer a way to detect that difference. In addition, there is a need for the IETF to be consistent in the face of attacks (an attack is an attack is an attack) to maintain the viability of the network. Arguing that some DDoS attacks should be allowed, based on the motivation of the attackers complicates the work of the IETF. Because it approaches PM regardless of the motivation of the attackers (see {{RFC7258}}) for reasoning), taking the motivation of the attackers into account for DDoS would indirectly undermine the ability of the IETF to protect the right to privacy because it introduces an element of inconsistency into how the IETF deals with attacks.

David Clark recently published a paper warning that the future of the Internet is in danger. He argues that the private sector control over the Internet is too strong, limiting the myriad of ways in which it can be used {{Daedalus}}, including for freedom of speech. But just because freedom of speech, dissent, and protest are human rights, and DDoS is a potential expression of those rights, doesn't mean that DDoS in and of itself is a right. To widen the analogy, just because the Internet is a medium through which the right to freedom of expression can be exercised does not make access to the Internet or specific ICTs or NCTs a human right. Uses of DDoS might or might not be legitimate for political reasons, but the IETF has no means or methods to assess this, and in general enabling DDoS would mean a deterioration of the network and thus freedom of expression.

In summation, the IETF cannot be expected to take a moral stance on DDoS attacks, or create protocols to enable some attacks and inhibit others. But what it can do is critically reflect on its role in creating a commercialized Internet without a defacto public space or inherent protections for freedom of speech.



Security Considerations
========================

As this draft concerns a research document, there are no security considerations.


IANA Considerations
==========================

This document has no actions for IANA.


Research Group Information
==========================

The discussion list for the IRTF Human Rights Protocol Considerations Research Group is located at the e-mail address
<hrpc@ietf.org>. Information on the group and information on how to
subscribe to the list is at <https://www.irtf.org/mailman/listinfo/hrpc>

Archives of the list can be found at:
<https://www.irtf.org/mail-archive/web/hrpc/current/index.html>

