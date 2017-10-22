--- 
title: On the Politics of Standards
abbrev: politix
docname: draft-tenoever-hrpc-political-01
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
       ins: A. Sullivan
       name: Andrew Sullivan
       organization: Oracle
       email: andrew.s.sullivan@oracle.com
-
       ins: A. Andersdotter
       name: Amelia Andersdotter
       organization: ARTICLE 19
       email: amelia@article19.org
normative:
  
informative: 

   RFC0049:
   RFC0101:
   RFC0144:
   RFC0164:
   RFC0196:
   RFC0286:
   RFC0313:
   RFC0316:
   RFC0542:
   RFC0549:
   RFC0613:
   RFC2804:
   RFC5218:
   RFC6973:
   RFC7258:
   RFC7704:
   RFC7776:

   BramanI:
     title: "Internationalization of the Internet by design: The first decade "
     date: 2012
     author:
        - ins: S. Braman
     target: http://dx.doi.org.proxy.uba.uva.nl:2048/10.1177%2F1742766511434731
     seriesinfo: "Global Media and Communication, Vol 8, Issue 1, pp. 27 - 45"

   BramanII:
     title: "The Framing Years: Policy Fundamentals in the Internet Design Process, 1969–1979"
     date: 2010
     author:
        - ins: S. Braman
     target: http://dx.doi.org.proxy.uba.uva.nl:2048/10.1080/01972243.2011.607027
     seriesinfo: "The Information Society Vol. 27, Issue 5, 2011" 
  
   Contreras:
     title:  "Technical Standards and Ex Ante Disclosure: Results and Analysis of an Empirical Study"
     date: 2013
     author:
        - ins: J.L. Contreras
     target:
     seriesinfo: "Jurimetrics: The Journal of Law, Science & Technology, vol. 53, p. 163-211"

   hrpc:
     title: Research into Human Rights Protocol Considerations
     date: 2017
     author:
        - ins: N. ten Oever
        - ins: C. Cath
     target: https://tools.ietf.org/html/draft-irtf-hrpc-research-13 

   Feenberg:
     title: Critical Theory of Technology
     date: 1991
     author:
       - ins: A. Feenberg
     seriesinfo: p.5-6
   
   Carey:
     title: Communication As Culture
     date: 1992
     author:
       - ins: J. Carey
     seriesinfo: p. 139

   Postman:
     title: "Technopoly: the Surrender of Culture to Technology"
     date: 1992
     author:
       - ins: N. Postman
     seriesinfo: "Vintage: New York. pp. 3–20."

   DeNardis:
     title: The Internet Design Tension between Surveillance and Security
     date: 2015
     author:
       - ins: L. Denardis
     target: http://is.gd/7GAnFy
     seriesinfo: IEEE Annals of the History of Computing (volume 37-2)

   Winner:
     title: Who will we be in cyberspace?
     date: 1995
     author: 
         - ins: L. Winner
     target: iwcenglish1.typepad.com/iwc_media_ecology/Documents/Who_will_we_be_in_cyberspace.doc

   UNGP:
     title: United Nations Guiding Principles for Business and Human Rights
     date: 2011
     author:
        - ins: J. Ruggie
        - org: United Nations
     target: http://www.ohchr.org/Documents/Publications/GuidingPrinciplesBusinessHR_EN.pdf

   Abbate:
      title: Inventing the Internet
      date: 2000
      author:
        - ins: J. Abbate
      target: https://mitpress.mit.edu/books/inventing-internet
      seriesinfo: MIT Press

   Heidegger:
      title: "The Question Concerning Technology and Other Essays"
      date: 1977
      author:
        - ins: M. Heidegger
      target: "http://ssbothwell.com/documents/ebooksclub.org__The_Question_Concerning_Technology_and_Other_Essays.pdf"
      seriesinfo: "Garland: New York, 1977"
 
   Nadvi:
      title: Making sense of global standards
      date: 2004
      author:
        - ins: K. Nadvi
        - ins: F. Wältring
      seriesinfo: "In: H. Schmitz (Ed.), Local enterprises in the global economy (pp. 53–94). Cheltenham, UK: Edward Elgar."

   Russell:
      title: "Open standards and the digital age: History, ideology, and networks"
      date: 2014
      author:
        - ins: A.M. Russell
      seriesinfo: "Cambridge, UK: Cambridge University Press"

   RogersEden:
      title: "The Snowden Disclosures, Technical Standards, and the Making of Surveillance Infrastructures"
      date: 2017
      author: 
        - ins: M. Rogers
        - ins: G. Eden
      seriesinfo: "International Journal of Communication 11(2017), 802-823"
      target: "http://ijoc.org/index.php/ijoc/article/view/5525/1941"

   CJEU2004:
      title: "ECLI:EU:C:2004:257, C-418/01 IMS Health"
      date: 2004
      author:
        - ins: Court of Justice of the European Union
      target: "http://curia.europa.eu/juris/liste.jsf?num=C-418/01"
      seriesinfo: "Cambridge, UK: Cambridge University Press"

   CJEU2007:
      title: "ECLI:EU:T:2007:289, T-201/04 Microsoft Corp."
      date: 2007
      author:
        - ins: Court of Justice of the European Union
      target: "http://curia.europa.eu/juris/liste.jsf?num=T-201/04"
      seriesinfo: "Cambridge, UK: Cambridge University Press"

   draft-finance-thoughts:
      title: "Thoughts on IETF Finance Arrangements"
      date: 2017
      author:
        - ins: J. Arkko
      target: "https://datatracker.ietf.org/doc/html/draft-arkko-ietf-finance-thoughts"

   xkcd927:
      title: "Standards"
      date: 2011
      author:
        - ins: Randall Munroe
      target: "https://xkcd.com/927/"
      seriesinfo: "xkcd.com, a web comic"

   Ahlborn:
      title: "Implications of the Proposed Framework and Antitrust Rules for Dynamically Competitive Industries"
      date: 2006
      author:
        - ins: C. Ahlborn
        - ins: V. Denicoló
        - ins: D. Geradin
        - ins: A.J. Padilla
      target: "http://curia.europa.eu/juris/liste.jsf?num=T-201/04"
      seriesinfo: "DG Comp’s Discussion Paper on Article 82, DG COMP, European Commission"

--- abstract

This document aims to outline different views on the relation between protocols and politics and seeks to answer the question whether protocols are political.

--- middle

Introduction
============

     "we shape our tools and thereafter they shape us"

                              -John Culkin

The design of the Internet through protocols and standards is a technical issue with great political and economic impacts {{RFC0613}}. The early Internet community already realized that it needed to make decisions on political issues such as Intellectual Property, Internationzalization {{BramanI}}, diversity, access {{RFC0101}} privacy and security {{RFC0049}}, and the military {{RFC0164}} {{RFC0316}}, governmental {{RFC0144}} {{RFC0286}} {{RFC0313}} {{RFC0542}} {{RFC0549}} and non-governmental {{RFC0196}} uses, which has been clearly pointed out by Braman {{BramanII}}. 

Recently there has been an increased discussion on the relation between Internet protocols and human rights {{hrpc}} which spurred the discussion on the political nature of protocols. The network infrastructure is on the one hand designed, described, developed, standardized and implemented by the Internet community, but the Internet community and Internet users are also shaped by the affordances of the technology. Companies, citizens, governments, standards developing bodies, public opinion and public interest groups all play a part in these discussions. In this document we aim to outline different views on the relation between protocols and politics and seek to answer the question whether protocols are political, and if so, how.

Vocabulary Used
===============

Politics
: (from Greek: Politiká: Politika, definition "affairs of the commons") is the process of making decisions applying to all members of a group. More narrowly, it refers to achieving and exercising positions of governance or organized control over a community. Furthermore, politics is the study or practice of the distribution of power and resources within a given community as well as the interrelationship(s) between communities. (adapted from )


Literature and Positions
========================

While discussion the impact of protocols on human rights different positions could be differentiated. Without judging them on their internal of external consistency they are represented here.

## Technology is value neutral
This position starts from the premise that the technical and poltical are differentiated fields and that technology is 'value free'. This is also put more explicitly by Carey: "electronics is neither the arrival of apocalypse nor the dispensation of  grace.  Technology  is  technology;  it  is  a  means  for  communication  and  transportation  over  space, and nothing more." {{Carey}}
In this view technology only become political when it is actually being used by humans. So the technology itself is not political, the use of the technology is. This is view sees technology as instrument; "technologies  are  'tools' standing  ready  to  serve  the  purposes  of  their  users.  Technology  is  deemed  'neutral,' without valuative content of its own.'" {{Feenberg}}. Feenberg continues: "technology  is  not  inherently  good  or  bad,  and  can  be  used  to  whatever  political  or  social  ends  desired  by  the  person  or  institution  in  control.  Technology  is  a  ‘rational entity’ and universally applicable. One may make exceptions on moral grounds, but one must also understand that the "price for the achievement of environmental, ethical, or religious goals...is reduced efficiency." {{Feenberg}}

## Some protocols are political some times
This stance is a pragmatic approach to the problem. It states that some protocols under certain conditions can themselves have a political dimension.  This is different from the claim that a protocol might sometimes be used in a political way; that view is consistent with the idea of the technology being neutral (for the human action using the technology is where the politics lies).  Instead, this position requires that each protocol and use be evaluated for its political dimension, in order to understand the extent to which it is political.

## The network has its own logic and values
While humans create techologies, that does not mean that they are forever under human control.  A technology, once created, has its own logic that is independent of the human actors that either create or use the technology.

Consider, for instance, the way that the very existence of the automobile imposes physical forms on the world different from those that come from the electric tram or the horse-cart.  The logic of the automobile means speed and the rapid covering of distance, which encourages suburban development and a tendency toward conurbation.  But even if that did not happen, widespread automotobile use requires paved roads, and parking lots and structures. These are pressures that come from the automotive technology itself, and would not arise without that technology.

Certain kinds of technology shape the world in this sense.  As Martin Heidegger says, "The hydroelectric plant is not built into the Rhine River as was the old wooden bridge that joined bank with bank for hundreds of years. Rather the river is dammed up into the power plant. What the river is now, namely, a water power supplier, derives from out of the essence of the power station." {{Heidegger}} (p 16)  The dam in the river changes the world in a way the bridge does not, because the dam alters the nature of the river.

In much same way, then, networking technology once created makes its own demands. One of the most important conditions for protocol success is that the protocol is incremental deployability {{RFC5218}}.  This means that the network already deployed constrains what can be delployed into it.  Moreover, one interpretation of {{RFC7258}} is that pervasive monitoring is an "attack" in the narrow sense precisely because of the network's need not to leak traces of online exchanges. A different network with a different design might not have been subject to this kind of attack.

## Protocols are inherently political
On the other side of the spectrum there are the ones who insist that technology is non-neutral. This is for instance made explicit by Postman where he writes: 'the uses made of technology are largely determined by the structure of the technology itself' {{Postman}}. He states that the medium itself 'contains an ideological bias'. He continues to argue that technology is non-neutral:

(1) because of the symbolic forms in which information is encoded, different media have different intellectual and emotional biases;
(2) because of the accessibility and speed of their information, different media have different political biases;
(3) because of their physical form, different media have different sensory biases;
(4) because of the conditions in which we attend to them, different media have different social biases;
(5) because of their technical and economic structure, different media have different content biases. {{Postman}} 

More recent scholars of Internet infrastructure and governance have also pointed out that Internet processes and protocols have become part and parcel of political processes and public policies: one only has to look at the IANA transition or global innovation policy for concrete examples {{DeNardis}}. Similarly one can look at the Raven process in which the IETF after a long discussion refused to standardize wiretapping (which resulted in {{RFC2804}}. That was an instance where the IETF took a position that was largely political, although driven by a technical argument.  It was similar to the process that led to {{RFC6973}}, in which something that occurred in the political space (Snowden disclosures) engendered the IETF to act. This is summarized in {{Abbate}} who says: "protocols are politics by other means". This emphasises the interests that are at play in the process of designing standards. This position holds further that protocols can never be understood without their contextual embeddedness: protocols do not exist solely by themselves but always are to be understood in a more complex context -- the stack, hardware, or nation-state interests and their impact on civil rights. Finally, this view is that that protocols are political because they affect or sometimes effect the socio-technical ordering of reality. The latter observation leads Winner to conclude that the reality of technological progress has too often been a scenario where the innovation has dictated change for society. Those who had the power to introduce a new technology also had the power to create a consumer class  to  use  the  technology, ‘with new practices, relationships, and identities supplanting the old, ---and those who had the wherewithal to implement new technologies often molded society to match the needs of emerging technologies and organizations.’ {{Winner}}.

Examples and approaches
=======================

# Competition and collaboration

Standards exist for nearly everything: processes, technologies, safety, hiring, elections, and training. Standards provide blue-prints for how to accomplish a particular task in a similar way to others trying to accomplish the same thing, while reducing overhead and inefficiencies. Formal technical standardisation, then, is the process whereby the expected features or functionalities of a particular technology are codified in writing. It is a way of ensuring that different technological systems can interoperate, or work in tandem and exchange functionality.

A formalised standard does not stop competition between entities working to realise those standards in practical implementations of that technological base. If the standard is well-crafted, it will even help entities cooperate and construct products and services on top of the commonly shared technological base. In these circumstances, standardisation is seen as beneficient for competition in downstream markets, meaning those markets making used of the standardised technologies. Standards have long been used as a tool to lay groundworks, a certain minimal commonality, that helps countries, companies or individuals cooperate to reach the next level of technological advancements more quickly.

Standards may not only exist in the form of a formal document laid down by an organisation gathering many different parties of different backgrounds behind a single, converging process. We also speak of de facto standards: the rules governing a technological base used by downstream market actors, such that, even if the rules have not been decided by many different entities they still constitute the effective boundary within which downstream innovation and development occurs. De facto standards can arise in market situations where one entity is particularly dominant, and may or may not lead to technical difficulties in challenging the dominant entity's technological base {{Ahlborn}}. Under EU anti-trust law, de facto standards have been found to be able to restrict competition for downstream services for PC software products {{CJEU2007}}, as well as downstream services dependent on health information {{CJEU2004}}. If such restrictions are found to apply, the resolution may entail obligations on the restrictive party to grant a license (if a failure to grant a license to the standard was the cause of the restriction) or arrange the technical solution in such a way that restrictions do not arise.

Standards development faces a number of economic and organisational challenges that are well-studied: the cost and difficulty of organising many entities around a mutual goal, as well as the cost of research and development leading up to a mutually beneficial technological platform. The first problem may, on the one hand, be described as just the sheer organisational costs: how do you create platforms, especially global platforms, that are accessible in terms of price and time, when implementors affected by the standards produced may include any range of entities with different economic means and resources (in the specific context of the IETF some issues of this nature are considered in {{draft-finance-thoughts}} and its references, but challenges are clearly universal in nature). It also incorporates the problem of too many cooks spoiling the broth: if the interests of a large number of entities need to converge around a single solution, by which mechnism does one mitigate the inconvenience of differing opinions or preferences between the parties reducing the over-all utility of the final compromise {{xkcd927}} .

The standards enabling interoperating networks, what we think of today as the Internet, were created as open, formal and voluntary standards. With openness, we understand that the standards were available at no cost to anyone around the world. Internet standardisation set itself apart from traditional standard bodies by not requiring implementors to pay a subscription fee to have access to the texts of codified standards. A platform for internet standardisation, the Internet Engineering Task Force (IETF), was created in 1992 to enable the continuation of such standardisation work.

On the one hand, this enables anyone willing and able to fulfill any standard requirement produced in the IETF. On the other hand, the costs and difficulties of organising many different entities in the standardisation process itself do not disappear only by making standards open and accessible to anyone seeking to implement them.

The IETF has sought to make the standards process transparent (by ensuring everyone can access standards, mailing-lists and meetings), predictable (by having clear procedures and reviews) and of high quality (by having draft documents reviewed by members from its own epistemic community). This is all aimed at increasing the accountability of the process and the quality of the standard. The IETF implements what has been referred to as an "informal ex ante disclosure policy" for patents {{Contreras, 2013}}, which includes the possibility for participants to disclose the existence of a patent relevant for the standard, royalty-terms which would apply to the implementors of that standard should it enter into effect, as well as other licensing terms that may be interesting for implementors to know. The community ethos in the IETF seems to lead to 100% royalty-free disclosures of prior patents {{Contreras, 2013}} which is a record number, even among other comparable standard organisations.

In spite of a strong community ethos and transparent procedures, the IETF is not immune to externalities. Sponsorship to the IETF is varied, but is also of the nature that ongoing projects that are in the specific interest of one or some group of corporations may be given more funding than other projects (see {{draft-finance-thoughts}}).

# More legacy, more politics?
Roman engineers complained about inadequate legacy standards they needed to comply with, which hampered them in their engineering excellence. In that sense not much has changed in the last 2100 years. When starting from a tabula rasa, one does not need to take other systems, layers or standards into account. The need for interoperability, and backward compatability makes engineering work harder. And once a standard is designed, it does not automatically means it will be broadly adopted at as fast pace. Examples of this are IPv6, DNSSEC, DKIM, etc. The need for interoperability means that a new protocol needs to take into account a much more diverse environment than early protocols, and also be amendable to different needs: protocols needs to relate and negotiate in a busy agora, as do the protocol developers. This means that some might get priority, whereas others get dropped.

# Infrastructure studies
Ironic loss in political and economical triumph of certain applications, because it becomes ossified and easier to attack. 

# Layers of politics
There is a competition between layers, and even contestation about what the borders of different layers are. This leads to competition between layers and different solutions for similar problems on different layers, which in its turn leads to further ossification, which leads to more contestation. 

# How voluntary are open standards?
Coordinating transnational stakeholders in a process of negotiation and
agreement through the development of common rules is a form of global governance {{Nadvi}}. Standards are among the mechanisms by which this governance is achieved. Conformance to certain standards is often a basic condition of participation in international trade and communication, so there are strong economic and political incentives to conform, even in the absence of legal requirements {{Russell}}. {{RogersEden}} argue: 
    As unequal participants compete to define standards, technological compromises emerge, which add complexity to standards. For instance, when working group participants propose competing solutions, it may be easier for them to agree on a standard that combines all the proposals rather than choosing any single proposal. This shifts the responsibility for selecting a solution onto those who implement the standard, which can lead to complex implementations that may not be interoperable. On its face this appears to be a failure of the standardization process, but this outcome may benefit certain participants— for example, by allowing an implementer with large market share to establish a de facto standard within the scope of the documented standard.


The need for a positioning
==========================

It is indisputable that the Internet plays an increasing and increasingly important role in the lives of individuals.  Those who produce interoperability standards for the Internet infrastructure are to some extent automatically implicated in that development. It cannot ordain what standards are to be used on the networks. The RFC producing community should not go outside of its mission to advocate for a specific use of protocols. At the same time, it may be useful for those producing Internet standards to take into account the political aspects or implications of that work.  Some structure for doing so may be helpful both to authors of standards documents and for the IETF. 

The risk of not doing this is threefold: (1) the IETF might make decisions which have a political impact that was not intended by the community, (2) other bodies or entities might make the decisions for the IETF because the IETF does not have an explicit stance, (3) other bodies that do take these issues into account might increase in importance on behest of the influence of the IETF.

This does not mean the IETF does not have position on particular political issues. The policies for open and diverse participation {{RFC7704}}, the anti-harassment policy {{RFC7776}}, as well as the Guidelines for Privacy Considerations {{RFC6973}} are testament of this.  But these are all examples of positions about the IETF's work processes or product.  What is absent is a way for IETF participants to evaluate their stance with respect to the wider implications of that IETF work. 

The way forward
===============

There are instruments that can help the IETF develop an approach to address the politics of protocols. Part of this can be found in draft-irtf-hrpc-research as well as the United National Guiding Principles for Business and Human Rights {{UNGP}}. But there is not a one-size-fits-all solution. The IETF is a particular organization, with a particular mandate, and even if a policy is in place, its success depends on the implementation of the policy by the community. 


Security Considerations
========================

As this draft concerns a research document, there are no security considerations.


IANA Considerations
==========================

This document has no actions for IANA.


Acknowledgements
================

Research Group Information
==========================

The discussion list for the IRTF Human Rights Protocol Considerations working group is located at the e-mail address <hrpc@ietf.org>. Information on the group and information on how to subscribe to the list is at: 
<https://www.irtf.org/mailman/listinfo/hrpc>

Archives of the list can be found at:
<https://www.irtf.org/mail-archive/web/hrpc/current/index.html>

