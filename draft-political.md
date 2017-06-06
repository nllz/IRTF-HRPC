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


Introduction
============

     "we shape our tools and thereafter they shape us"

                              -John Culkin

The design of the Internet through protocols and standards is a technical issues with great poltical and econmic impacts {{RFC0603}}. The early Internet community already realized that it needed to make decisions on political issues such as Intellectual Property Rights, Internationzalization {{BramanI}}, diversity, access {{RFC0101}} privacy and security {{RFC0049}}, and the military {{RFC0164}} {{RFC0316}}, governmental {{RFC0144}} {{RFC0286}} {{RFC0313}} {{RFC0542}} {{RFC0549}} and non-governmental {{RFC0196}} uses, which has been clearly pointed out by Braman {{BramanII}}. 

Recently there has been an increased discussion on the relation between Internet protocols and human rights {{hrpc}} which spurred the discussion on the political nature of protocols. In this document we aim to outline different views on the relation between protocols and politics and seeks to answer the question whether protocols are political.

Vocabulary Used
===============

Literature and Positions
========================

While discussion the impact of protocols on human rights different positions could be differentiated. Without judging them on their internal of external consistency they are represented here. 

## Technology is neutral
This position starts from the premise that the technical and poltical are differentiated fields and that technology is 'value free'. This is also put more explicitly by Carey: "electronics is neither the arrival of apocalypse nor the dispensation of  grace.  Technology  is  technology;  it  is  a  means  for  communication  and  transportation  over  space, and nothing more." {{Carey}}
In this view technology only become political when it is actually being used by humans. So the technology itself is not political, the use of the technology is. This is view sees technology as instrument; "technologies  are  'tools' standing  ready  to  serve  the  purposes  of  their  users.  Technology  is  deemed  'neutral,' without valuative content of its own.'" {{Feenberg}}. Feenberg continues: "technology  is  not  inherently  good  or  bad,  and  can  be  used  to  whatever  political  or  social  ends  desired  by  the  person  or  institution  in  control.  Technology  is  a  ‘rational entity’ and universally applicable. One may make exceptions on moral grounds, but one must also understand that the "price for the achievement of environmental, ethical, or religious goals...is reduced efficiency." {{Feenberg}}

## Some protocols are political some times
This stance is a pragmatic approach to the problem. It states that some protocols under certain conditions can have a political impact.

## The network has its own politics

## Protocols are political
On the other side of the spectrum there are the onces who insist that technology is non-neutral. This is for instance made explicit by Postman where he writes: 'the uses made of technology are largely determined by the structure of the technology itself' {{Postman}}. He states that the medium itself 'contains an ideological bias'. He continues to argue that technology is non-neutral:

(1) because of the symbolic forms in which information is encoded, different media have different intellectual and emotional biases;
(2) because of the accessibility and speed of their information, different media have different political biases;
(3) because of their physical form, different media have different sensory biases;
(4) because of the conditions in which we attend to them, different media have different social biases;
(5) because of their technical and economic structure, different media have different content biases. {{Postman}} 

More recent scholars of Internet infrastructure and governance have also pointed out that Internet processes and protocols have become part and parcel of political processes and public policies: one only has to look at the IANA transition, the RFC on pervasive monitoring or global innovation policy for concrete examples {{DeNardis}}. According to {{Abbate}}: "protocols are politics by other means". This emphasises the interest that are at play in the process of designing standards. Furthermore it is argued that protocols can never be understood without their contextual embeddedness, protocols do not exist solely by themselves but always are to be understood in a more complex context; the stack, hardware, state-interests and their impact on civil rights. Finally it is argued that protocols are political because they do impact the socio-technical ordering of reality. This lead Winner to conclude that: the reality of technological progress has too often been a scenario where the innovation has dictated change for society. Those who had the power to introduce a new technology also had the power to create a consumer class  to  use  the  technology, ‘with new practices, relationships, and identities supplanting the old, ---and those who had the wherewithal to implement new technologies often molded society to match the needs of emerging technologies and organizations.’ {{Winner}}

The need for a positioning
==========================

With an increasing role of the Internet in the lives of citizens, the RFC producing community has a role, as an organization that is setting the standards for this infrastructure. That said, the IETF is not the protocol police. It cannot, and should not, ordain what standards are to be used on the networks. The RFC producing community should not go outside of its mission to advocate for a specific use of protocols, that said, it should take into account the political aspect of its work and provide a structured approach for this, in both the process of standards development as well as the standards themselves. 

The risk of not doing doing this is threefold: (1) the IETF might make decisions which have a political impact that was not intended by the community, (2) other bodies or entities might make the decisions for the IETF because the IETF does not have an explicit stance, (3) other bodies that do take these issues into account might increase in importance on behest of the influence of the IETF.

This does not mean the IETF does not have position on particular political issues. The policies for open and diverse participation {{RFC7706}}, the anti-harassment policy {{RFC7776}}, as well as the Guidelines for Privacy Considerations {{RFC6973}} are testament of this, but these are not a holistic, structured approach. 

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

The discussion list for the IRTF Human Rights Protocol Considerations
proposed working group is located at the e-mail address
<hrpc@ietf.org>. Information on the group and information on how to
subscribe to the list is at
<https://www.irtf.org/mailman/listinfo/hrpc>

Archives of the list can be found at:
<https://www.irtf.org/mail-archive/web/hrpc/current/index.html>

