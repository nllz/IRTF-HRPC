--- 
title: On the Politics of Standards
abbrev: politix
docname: draft-tenoever-hrpc-political-00
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
#      organization:
       email: ajs@anvilwalrusden.com

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
   RFC0603:
   RFC6973:
   RFC7706:
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
 
    

--- abstract

This document aims to outline different views on the relation between protocols and politics and seeks to answer the question whether protocols are political.

--- middle

{:ajs: source="ajs@anvilwalrusden.com"}

Introduction
============

     "we shape our tools and thereafter they shape us"

                              -John Culkin

The design of the Internet through protocols and standards is a technical issue with great poltical and econmic impacts {{RFC0603}}. The early Internet community already realized that it needed to make decisions on political issues such as Intellectual Property Rights, Internationzalization {{BramanI}}, diversity, access {{RFC0101}} privacy and security {{RFC0049}}, and the military {{RFC0164}} {{RFC0316}}, governmental {{RFC0144}} {{RFC0286}} {{RFC0313}} {{RFC0542}} {{RFC0549}} and non-governmental {{RFC0196}} uses, which has been clearly pointed out by Braman {{BramanII}}. 

Recently there has been an increased discussion on the relation between Internet protocols and human rights {{hrpc}} which spurred the discussion on the political nature of protocols. In this document we aim to outline different views on the relation between protocols and politics and seek to answer the question whether protocols are political.

Vocabulary Used
===============

Literature and Positions
========================

While discussion the impact of protocols on human rights different positions could be differentiated. Without judging them on their internal of external consistency they are represented here.

## Politics
[^1]{:ajs}
[^1]I suspect we have a problem that we haven't defined "politics", which is maybe what's causing some of the angst.  Should we?

## Technology is value neutral
This position starts from the premise that the technical and poltical are differentiated fields and that technology is 'value free'. This is also put more explicitly by Carey: "electronics is neither the arrival of apocalypse nor the dispensation of  grace.  Technology  is  technology;  it  is  a  means  for  communication  and  transportation  over  space, and nothing more." {{Carey}}
In this view technology only become political when it is actually being used by humans. So the technology itself is not political, the use of the technology is. This is view sees technology as instrument; "technologies  are  'tools' standing  ready  to  serve  the  purposes  of  their  users.  Technology  is  deemed  'neutral,' without valuative content of its own.'" {{Feenberg}}. Feenberg continues: "technology  is  not  inherently  good  or  bad,  and  can  be  used  to  whatever  political  or  social  ends  desired  by  the  person  or  institution  in  control.  Technology  is  a  ‘rational entity’ and universally applicable. One may make exceptions on moral grounds, but one must also understand that the "price for the achievement of environmental, ethical, or religious goals...is reduced efficiency." {{Feenberg}}

## Some protocols are political some times
This stance is a pragmatic approach to the problem. It states that some protocols under certain conditions can themselves have a political dimension.  This is different from the claim that a protocol might sometimes be used in a political way; that view is consistent with the idea of the technology being neutral (for the human action using the technology is where the politics lies).  Instead, this position requires that each protocol and use be evaluated for its political dimension, in order to understand the extent to which it is political.

## The network has its own logic and values
While humans create techologies, that does not mean that they are forever under human control.  A technology, once created, has its own logic that is independent of the human actors that either create or use the technology. [^2]{:ajs}  The very existence of the automobile imposes physical forms on the world different from those that come from the electric tram or the horse-cart. Under this view, the technology has its own needs and pressures, independent of those of  human actors.  As it changes, it will change at least in part according to those needs and pressures.

As a result, Internet protocols express at least to some extent the logic and values of the overall Internet technology.  

[^1]It seems like some references are needed here.  Not sure whether we want more generic or less -- Heidegger's "Question" seems like a good start, but it's hardly about protocols.


## Protocols are inherently political
On the other side of the spectrum there are the onces who insist that technology is non-neutral. This is for instance made explicit by Postman where he writes: 'the uses made of technology are largely determined by the structure of the technology itself' {{Postman}}. He states that the medium itself 'contains an ideological bias'. He continues to argue that technology is non-neutral:

(1) because of the symbolic forms in which information is encoded, different media have different intellectual and emotional biases;
(2) because of the accessibility and speed of their information, different media have different political biases;
(3) because of their physical form, different media have different sensory biases;
(4) because of the conditions in which we attend to them, different media have different social biases;
(5) because of their technical and economic structure, different media have different content biases. {{Postman}} 

More recent scholars of Internet infrastructure and governance have also pointed out that Internet processes and protocols have become part and parcel of political processes and public policies: one only has to look at the IANA transition, the RFC on pervasive monitoring[^3]{:ajs} or global innovation policy for concrete examples {{DeNardis}}. According to {{Abbate}}: "protocols are politics by other means". This emphasises the interests that are at play in the process of designing standards. This position holds further that protocols can never be understood without their contextual embeddedness: protocols do not exist solely by themselves but always are to be understood in a more complex context -- the stack, hardware, or nation-state interests and their impact on civil rights. Finally, this view is that that protocols are political because they affect or sometimes effect the socio-technical ordering of reality. The latter observation leads Winner to conclude that the reality of technological progress has too often been a scenario where the innovation has dictated change for society. Those who had the power to introduce a new technology also had the power to create a consumer class  to  use  the  technology, ‘with new practices, relationships, and identities supplanting the old, ---and those who had the wherewithal to implement new technologies often molded society to match the needs of emerging technologies and organizations.’ {{Winner}}

[^3]I have long felt that DeNardis's claim about RFC 7258 embodies a misunderstanding of the IETF's stance.  P3 of sec 1 is pretty clear that the scope is carefully limited to a technical meaning of "attack".  I think this sentence is therefore too glib.  The IANA transition, on the other hand, really was a political thing, but it's politics _about_ protocols rather than protocols _as_ politics.  I think the passage following the Abbate quote is on stronger ground.

The need for a positioning
==========================

It is indisputable that the Internet plays an increasing and increasingly important role in the lives of citizens.  Those who produce interoperability standards for the Internet infrastructure are to some extent automatically implicated in that development. That said, the IETF is not the protocol police. It cannot, and should not, ordain what standards are to be used on the networks. The RFC producing community should not go outside of its mission to advocate for a specific use of protocols. At the same time, it may be useful for those producing Internet standards to take into account the political aspects or implications of that work.  Some structure for doing so may be helpful both to authors of standards documents and for the IETF. 

The risk of not doing doing this is threefold: (1) the IETF might make decisions which have a political impact that was not intended by the community, (2) other bodies or entities might make the decisions for the IETF because the IETF does not have an explicit stance, (3) other bodies that do take these issues into account might increase in importance on behest of the influence of the IETF.

This does not mean the IETF does not have position on particular political issues. The policies for open and diverse participation {{RFC7706}}, the anti-harassment policy {{RFC7776}}, as well as the Guidelines for Privacy Considerations {{RFC6973}} are testament of this.  But these are all examples of positions about the IETF's work processes or product.  What is absent is a way for IETF participants to evaluate their stance with respect to the wider implications of that IETF work. 

The way forward
===============

There are instruments that can help the IETF develop an approach to address the politics of protocls, part of this can be found in draft-irtf-hrpc-research as well as the United National Guiding Principles for Business and Human Rights {{UNGP}}. But there is not a one-size-fits-all solution. The IETF is a particular organization, with a particular mandate, and even if a policy is in place, its success depends on the implementation of the policy by the community. 


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

