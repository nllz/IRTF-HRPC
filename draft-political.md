---
title: On Value Neutrality and the Politics of Standards
abbrev: politix
docname: draft-tenoever-hrpc-political-06
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
       organization: University of Amsterdam
       email: mail@nielstenoever.net
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
   RFC1097:
   RFC1958:
   RFC2026:
   RFC2804:
   RFC3552:
   RFC3935:
   RFC5218:
   RFC6973:
   RFC7704:
   RFC7776:
   RFC8280:

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
     seriesinfo: "Jurimetrics: The Journal of Law, Science &amp; Technology, vol. 53, p. 163-211"

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

   IAOC69:
      title: "IAOC Report Chicago"
      date: 2007
      author:
        - ins: IAOC
      target: "https://iaoc.ietf.org/documents/IAOC-Report-Chicago-69.pdf"

   IAOC77:
      title: "IAOC Report Anaheim"
      date: 2010
      author:
        - ins: IAOC
      target: "https://iaoc.ietf.org/documents/IAOC-Report-Anaheim-77.pdf"

   IAOC99:
      title: "IAOC Report Prague"
      date: 2017
      author:
        - ins: IAOC
      target: "https://iaoc.ietf.org/documents/IAOCReportinAdvanceofIETF99.pdf"


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

   Hanseth:
      title: Insribing Behaviour in Information Infrastructure Standards
      date: 1997
      author:
        - ins: O. Hanseth
        - ins: E. Monteiro
      seriesinfo: Accounting, Management and Infomation Technology 7 (14) p.183-211

   Woolgar:
      title: "Configuring the user: the case of usability trials"
      date: 1991
      author:
         - ins: S. Woolgar
      seriesinfo: "A sociology of monsters. Essays on power, technology and dominatior, ed: J. Law, Routeledge p. 57-102."

   Winner:
      title: "Upon openig the black box and finding it empty: Social constructivism and the philosophy of technology"
      date: 1993
      author:
        - ins: L. Winner
      seriesinfo: Science, Technology, and Human Values 18 (3) p. 362-378

   Webster:
      title: Networks of Collaboration or Conflict? The Development of EDI
      date: 1995
      author:
        - ins: J. Webster
      seriesinfo: "The social shaping of inter-organizational IT systems and data interchange, eds: I. McLougling &amp; D. Mason, European Commission PICT/COST A4"

   Sisson:
     title: Standards and Protocols
     date: 2000
     author:
       - ins: D. Sisson
     target: https://philosophe.com/design/standards/

   HagueHarrop:
     title: "Comparative Government and Politics: An Introduction"
     date: 2013
     author:
      - ins: R. Hague
      - ins: M. Harrop
     seriesinfo: "Macmillan International Higher Education. pp. 1–. ISBN 978-1-137-31786-5."

   BijkerLaw:
     title: "Shaping Technology/ Building Society: Studies in Sociotechnical Change"
     date: 1992
     author:
      - ins: W. Bijker
      - ins: J. Law
     seriesinfo: "Cambridge, MA: MIT Press"

   Bloor:
     title: Knowledge and Social Imagery
     date: 1976
     author:
      - ins: D. Bloor
     seriesinfo: "London: Routeledge & Kegan Paul"

--- abstract

The IETF cannot ordain which standards or protocols are to be used on network, but the standards developing process in the IETF has a normative effect. Among other things the standardisation work at the IETF has implications on what is perceived as technologically possible and useful where networking technologies are being deployed, and its standards output reflect was is considered by the technical community as feasible and good practice. Because it mediates many aspects of modern life, and therefore contributes to the ordering of societies and communities, the consideration of the politics and (potential) impact of protocols should be part of the standardization and development process.

--- middle

Introduction
============

    "Science and technology lie at the heart of social asymmetry.
       Thus technology both creates systems which close off other
       options and generate  novel, unpredictable and indeed
       previously unthinkable, option. The game of technology is
       never finished, and its ramifications are endless."

                                   - Michel Callon

    "The Internet isn't value-neutral, and neither is the IETF."

                                   -{{RFC3935}}

The design of the Internet through protocols and standards is a technical issue with great political and economic impacts {{RFC0613}}. The early Internet community already realized that it needed to make decisions on political issues such as Intellectual Property, Internationalization {{BramanI}}, diversity, access {{RFC0101}} privacy and security {{RFC0049}}, and the military {{RFC0164}} {{RFC0316}}, governmental {{RFC0144}} {{RFC0286}} {{RFC0313}} {{RFC0542}} {{RFC0549}} and non-governmental {{RFC0196}} uses, which has been clearly pointed out by Braman {{BramanII}}.

Recently there has been an increased discussion on the relation between Internet protocols and human rights {{RFC8280}} which spurred the discussion on the the value neutrality and political nature of standards. The network infrastructure is on the one hand designed, described, developed, standardized and implemented by the Internet community, but the Internet community and Internet users are also shaped by the affordances of the technology. Companies, citizens, governments, standards developing bodies, public opinion and public interest groups all play a part in these discussions. In this document we aim to outline different views on the relation between standards and politics and seek to answer the question whether standards are political, and if so, how.

Vocabulary Used
===============

Politics
: (from Greek: Politiká: Politika, definition "affairs of the commons") is the process of making decisions applying to all members of a diverse group with conflicting interests. More narrowly, it refers to achieving and exercising positions of governance or organized control over a community. Furthermore, politics is the study or practice of the distribution of power and resources within a given community as well as the interrelationship(s) between communities. (adapted from {{HagueHarrop}})

Affordances
: The possibilities that are provided to an actors through the ordering of an environment by a technology.

Protocols
: 'Protocols are rules governing communication between devices or applications, and the creation or manipulation of any logical or communicative artifacts concomitant with such communication.' {{Sisson}}

Standards
: 'An Internet Standard is a specification that is stable and well-understood, is technically competent, has multiple, independent, and interoperable implementations with substantial operational experience, enjoys significant public support, and is recognizably useful in some or all parts of the Internet.' {{RFC2026}}


Research Question
=================

Are protocols political? If so, should the politics of protocols need to be taken into account in their development process?

Technology and Politics: a review of literature and community positions
=======================================================================

In 1993 the Computer Professionals for Social Responsibility stated that 'the Internet should meet public interest objectives', similarly {{RFC3935}} states that 'The Internet isn't value-neutral, and neither is the IETF.'. Ethics and the Internet was already a topic of an RFC by the IAB in 1989 {{RFC1097}}. Nonetheless there has been a recent uptick in discussions around the impact of Internet protocols on human rights {{RFC8280}} in the IETF and more general about the impact of technology on society in the public debate.

This document aims to provide an overview of the spectrum of different positions that have been observed in the IETF and IRTF community, during participatory observation, through 39 interviews with members of the community, the Human Rights Protocol Considerations Research Group mailinglist and during and after the Technical Plenary on Protocols and Human Rights during IETF98.
Without judging them on their internal or external consistency they are represented here, where possible we sought to engage with academic literature on this topic.

## Technology is value neutral
This position starts from the premise that the technical and political are differentiated fields and that technology is 'value free'. This is also put more explicitly by Carey: "electronics is neither the arrival of apocalypse nor the dispensation of  grace.  Technology  is  technology;  it  is  a  means  for  communication  and  transportation  over  space, and nothing more." {{Carey}}. In this view protocols only become political when it is actually being used by humans. So the technology itself is not political, the use of the technology is. This view sees technology as instrument; "technologies  are  'tools' standing  ready  to  serve  the  purposes  of  their  users.  Technology  is  deemed  'neutral,' without valuative content of its own.'" {{Feenberg}}. Feenberg continues: "technology  is  not  inherently  good  or  bad,  and  can  be  used  to  whatever  political  or  social  ends  desired  by  the  person  or  institution  in  control.  Technology  is  a  ‘rational entity’ and universally applicable. One may make exceptions on moral grounds, but one must also understand that the "price for the achievement of environmental, ethical, or religious goals...is reduced efficiency." {{Feenberg}}.

## Some protocols are political some times
This stance is a pragmatic approach to the problem. It states that some protocols under certain conditions can themselves have a political dimension.  This is different from the claim that a protocol might sometimes be used in a political way; that view is consistent with the idea of the technology being neutral (for the human action using the technology is where the politics lies).  Instead, this position requires that each protocol and use be evaluated for its political dimension, in order to understand the extent to which it is political.

## All protocols are political sometimes
While not an absolutist standpoint it recognizes that all design decisions are subject to the law of unintended consequences. The system consisting of the Internet and its users is vastly too complex to be predictable; it is chaotic in nature; its emergent properties cannot be predicted. This concept strongly hinges on the general purpose aspect of information technology and its malleability. Whereas not all (potential) behaviours, affordances and impacts of protocols can possible be predicted, one could at least consider the impact of proposed implementations.

## The network has its own logic and values
While humans create technologies, this does not mean that they are forever under human control. A technology, once created, has its own logic that is independent of the human actors that either create or use the technology.

From this perspective, technologies can shape the world. As Martin Heidegger says, "The hydroelectric plant is not built into the Rhine River as was the old wooden bridge that joined bank with bank for hundreds of years. Rather the river is dammed up into the power plant. What the river is now, namely, a water power supplier, derives from out of the essence of the power station." {{Heidegger}} (p 16)  The dam in the river changes the world in a way the bridge does not, because the dam alters the nature of the river.

In the same way --in another and more recent example-- the very existence automobiles impose physical forms on the world different from those that come from the electric tram or the horse-cart. The logic of the automobile means speed and the rapid covering of distance, which encourages suburban development and a tendency toward conurbation. But even if that did not happen, widespread automobile use requires paved roads, and parking lots and structures. These are pressures that come from the automotive technology itself, and would not arise without that technology.

In much same way, then, networking technology, such as protocols, creates its own demands. One of the most important conditions for protocol success is its incremental deployability {{RFC5218}}.  This means that the network already contains constraints on what can be deployed into it. In this sense the network creates its own paths, but also has its own objective. According to this view the goal of the network is interconnection and connectivity; more connectivity is good for the network. Proponents of this positions also often describe the Internet as an organism with its own unique ecosystem.

In this position it is not necessarily clear where the 'social' ends and the 'technical' begins, and it could be argued that the distinction itself is a social construction {{BijkerLaw}} or that a real-life distinction between the two is hard to be made {{Bloor}}.

## Protocols are inherently political
This position argues the opposite of 'technological neutrality'. This position can be illustrated with Postman where he writes: 'the uses made of technology are largely determined by the structure of the technology itself' {{Postman}}. He states that the medium itself 'contains an ideological bias'. He continues to argue that technology is non-neutral:

(1) because of the symbolic forms in which information is encoded, different media have different intellectual and emotional biases;
(2) because of the accessibility and speed of their information, different media have different political biases;
(3) because of their physical form, different media have different sensory biases;
(4) because of the conditions in which we attend to them, different media have different social biases;
(5) because of their technical and economic structure, different media have different content biases.

Recent scholars of Internet infrastructure and governance have also pointed out that Internet processes and standards have become part and parcel of political processes and public policies. Several concrete examples are found within this approach, for instance, the IANA transition or global innovation policy {{DeNardis}}. The Raven process in which the IETF refused to standardize wiretapping --which resulted in {{RFC2804}}-- was an instance where an international governance body took a position that was largely political, although driven by a technical argument. The process that led to {{RFC6973}} is similar: the Snowden disclosures which occured in the political space, engendered the IETF to act. This is summarized in {{Abbate}} who says: "protocols are politics by other means", emphasizing the interests that are at play in the process of designing standards.

This position further holds that protocols can never be understood without their contextual embeddedness: protocols do not exist solely by themselves but always are to be understood in a more complex context -- the stack, hardware, or nation-state interests and their impact on civil rights. Finally, this view is that that protocols are political because they affect or sometimes effect the socio-technical ordering of reality. The latter observation leads Winner to conclude that the reality of technological progress has too often been a scenario where the innovation has dictated change for society. Those who had the power to introduce a new technology also had the power to create a consumer class  to  use  the  technology ‘with new practices, relationships, and identities supplanting the old, ---and those who had the wherewithal to implement new technologies often molded society to match the needs of emerging technologies and organizations.’ {{Winner}}.

IETF: Protocols as Standards
============================

In the previous section we gave an overview of the different existing positions of the impact of Internet protocols in the Internet community. In the following section we will consider the standards setting process and its consequences for the politics of protocols.

Standards enabling interoperating networks, what we think of today as the Internet, were created as open, formal and voluntary standards. A platform for internet standardisation, the Internet Engineering Task Force (IETF), was created in 1992 to enable the continuation of such standardisation work. The IETF has sought to make the standards process transparent (by ensuring everyone can access standards, mailing-lists and meetings), predictable (by having clear procedures and reviews) and of high quality (by having draft documents reviewed by members from its own epistemic community). This is all aimed at increasing the accountability of the process and the quality of the standard.

The IETF implements what has been referred to as an "informal ex ante disclosure policy" for patents {{Contreras}}, which includes the possibility for participants to disclose the existence of a patent relevant for the standard, royalty-terms which would apply to the implementors of that standard should it enter into effect, as well as other licensing terms that may be interesting for implementors to know. The community ethos in the IETF seems to lead to 100% royalty-free disclosures of prior patents which is a record number, even among other comparable standard organisations {{Contreras}}.

## Competition and collaboration

Standards exist for nearly everything: processes, technologies, safety, hiring, elections, and training. Standards provide blue-prints for how to accomplish a particular task in a similar way for others that are trying to accomplish the same thing, while reducing overhead and inefficiencies. Although there are different types and configurations of standards, they all enhance competition by allowing different entities to work from a commonly accepted baseline.

On the first types of standards than can be found are "informal" ones --agreed upon normal ways of interacting within a specific community. For example, the process through which greetings to a new acquaintance are expressed through a bow, a handshake or a kiss. On the other hand "formal" standards, are normally codified in writing. The next subsection will ----

Within economy studies, _de facto_ standards arise in market situations where one entity is particularly dominant; downstream competitors are therefore tied to the dominant entity's technological solutions {{Ahlborn}}. Under EU anti-trust law, de facto standards have been found to restrict competition for downstream services in PC software products {{CJEU2007}}, as well as downstream services dependent on health information {{CJEU2004}}.

Even in international law, the World Trade Organisation (WTO) uses standards, although it recognises a difference between standards and technical regulations. The former are voluntary formal codes to which products or services may conform, while technical regulations are mandatory requirements to be fullfilled for a product to be accessible on one of the WTO country markets. These rules have implications for how nation states bounded by the WTO agreements can impose specific technical requirements on companies. Nonetheles, there are many standardisation groups that were originally launched by nation states or groups of nation states. ISO, BIS, CNIS, NIST, ABNT and ETSI are examples of institutions that are, wholly or partially, sponsored by public money in order to ensure smooth development of formal standards. Even if under WTO rules these organisations cannot create the equivalent of a technical regulation, they have important normative functions in their respective countries. No matter what form, all standards enhance competition and collaboration because they define a common approach to a problem. This potentially allows different instances to interoperate or be evaluated according to the same indicators.

The development of formal standards faces a number of economic and organisational challenges. Mainly, the cost and difficulty of organising many entities around a mutual goal, as well as the cost of research and development leading up to a mutually beneficial technological platform. In addition, deciding what the mutual goal is can also be a problem. These challenges may be described as inter-organisational costs. Even after a goal is decided upon, coordination of multiple entities requires time and money. One needs communication platforms, processes and a commitment to mutual investment in a higher good. They are not simple tasks, and the more different communities are affected by a particular standardisation process, the more difficult the organisational challenges become.

## IETF standards setting externalities

In spite of a strong community ethos and transparent procedures, the IETF is not immune to externalities.

### Finance
Sponsorship to the IETF is varied, but is also of the nature that ongoing projects that are in the specific interest of one or some group of corporations may be given more funding than other projects (see {{draft-finance-thoughts}}). The IETF has faced three periods of decreased commitment from participants in funding its meetings in the past ten years, leading, naturally, to self-scrutiny, see for instance {{IAOC69}}, {{IAOC77}}, {{IAOC99}}.

### Interoperability and backward compatability
The need for interoperability, and backward compatability makes engineering work harder. And once a standard is designed, it does not automatically mean it will be broadly adopted at a fast pace. Examples of this are IPv6, DNSSEC, DKIM, etc. The need for interoperability means that a new protocol needs to take into account a much more diverse environment than early protocols, and also be amendable to different needs: protocols needs to relate and negotiate in a busy agora, as do the protocol developers. This means that some might get priority, whereas others get dropped.

### Competition between layers
There is a competition between layers, and even contestation about what the borders of different layers are. This leads to competition between layers and different solutions for similar problems on different layers, which in its turn leads to further ossification, which leads to more contestation.

## How voluntary are open standards?

Coordinating transnational stakeholders in a process of negotiation and agreement through the development of common rules is a form of global governance {{Nadvi}}. Standards are among the mechanisms by which this governance is achieved. Conformance to certain standards is often a basic condition of participation in international trade and communication, so there are strong economic and political incentives to conform, even in the absence of legal requirements {{Russell}}. {{RogersEden}} argue:

   "As unequal participants compete to define standards, technological compromises emerge, which add complexity to standards. For instance, when working group participants propose competing solutions, it may be easier for them to agree on a standard that combines all the proposals rather than choosing any single proposal. This shifts the responsibility for selecting a solution onto those who implement the standard, which can lead to complex implementations that may not be interoperable. On its face this appears to be a failure of the standardization process, but this outcome may benefit certain participants— for example, by allowing an implementer with large market share to establish a de facto standard within the scope of the documented standard."


The need for a positioning
==========================

It is indisputable that the Internet plays an increasingly important role in the lives of individuals.  The community that produces standards for the Internet therefore also has an impact on society, which it itself has recognised in a number of previously adopted documents {{RFC1958}}.

The IETF cannot ordain which standards are to be used on the networks, and it specifically does not determine the laws of regions or countries where networks are being used, but it does set open standards for interoperability on the Internet, and has done so since the inception of the Internet. Because a standard is the blue-print for how to accomplish a particular task in a similar way to others, the standards adopted have a normative effect. The standardisation work at the IETF will have implications on what is perceived as technologically possible and useful where networking technologies are being deployed, and its standards output reflect was is considered by the technical community as feasible and good practice.

This calls for providing a methodology in the IETF community to evaluate which routes forward should indeed be feasible, what constitutes the "good" in "good practice" and what trade-offs between different feasible features of technologies are useful and should therefore be made possible. Such an analysis should take societal implication into account.

The risk of not doing this is threefold: (1) the IETF might make decisions which have a political impact that was not intended by the community, (2) other bodies or entities might make the decisions for the IETF because the IETF does not have an explicit stance, (3) other bodies that do take these issues into account might increase in importance to the detriment of the influence of the IETF.

This does not mean the IETF does not have a position on particular political issues. The policies for open and diverse participation {{RFC7704}}, the anti-harassment policy {{RFC7776}}, as well as the Guidelines for Privacy Considerations {{RFC6973}} are proof of this. Nonetheless, these are all examples of positions about the IETF's work processes or product. What is absent is a way for IETF participants to evaluate their role with respect to the wider implications of that IETF work.

Conclusion
==========

Economics, competition, collaboration, openness, and political impact have been an inherent part of the work of the IETF since its early beginnings, by its nature as standards developing organization, through the contributions of the members of the Internet community, and because the ordering effect the Internet has on society. Whereas there might not be agreement in the Internet community on what the specific political nature is of technological development, it is undisputed that standards and protocols are both product of a political process, and they can also be used for political means. Therefore protocols and standards are not value neutral. Whereas there is no need for a unified philosophy of Internet protocols, it is in the benefit of the IETF, the Internet and arguably society at large to take this into account in the standards development process.

The way forward
===============

There are instruments that can help the IETF develop an approach to address the politics of standards. Part of this can be found in {{RFC8280}} as well as the United National Guiding Principles for Business and Human Rights {{UNGP}}. But there is not a one-size-fits-all solution. The IETF is a particular organization, with a particular mandate, and even if a policy is in place, its success depends on the implementation of the policy by the community.

Since 'de facto standardization is reliant on market forces' {{Hanseth}} we need to live with the fact standards bodies have a political nature {{Webster}} and are not value neutral. This does not need to be problematic as long as there are sufficient accountability and transparency mechanisms in place. The importance of these mechanisms increases with the importance of the standards and their implementations. The complexity of the work inscribes a requirement of competence in the work in the IETF, which forms an inherent barrier for end-user involvement. Even though this might not be intentional, it is a result of the interplay between the characteristics of the epistemic community in the IETF and the nature of the standard setting process.

Instead of splitting hairs about whether 'standards are political' {{Winner}} {{Woolgar}} we argue that we need to look at the politics of individual standards and invite document authors and reviewers to take these dynamics into account.

Security Considerations
=======================

As this draft concerns a research document, there are no security considerations as described in {{RFC3552}}, which does not mean that not addressing the issues brought up in this draft will not impact the security of end-users or operators.


IANA Considerations
===================

This document has no actions for IANA.


Acknowledgements
================

Thanks to Andrew Sullivan, Brian Carpenter, Mark Perkins and all contributors and reviewers on the hrpc mailinglist. Special thanks to Gisela Perez de Acha for some thorough editing rounds.

Research Group Information
==========================

The discussion list for the IRTF Human Rights Protocol Considerations working group is located at the e-mail address <hrpc@ietf.org>. Information on the group and information on how to subscribe to the list is at:
<https://www.irtf.org/mailman/listinfo/hrpc>

Archives of the list can be found at:
<https://www.irtf.org/mail-archive/web/hrpc/current/index.html>
