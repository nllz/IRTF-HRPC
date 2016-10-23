---
title: Research into Human Rights Protocol Considerations
abbrev: hrpcr
docname: draft-irtf-hrpc-research-03
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
       ins: C.J.N. Cath
       name: Corinne Cath
       organization: Oxford Internet Institute
       email: corinnecath@gmail.com


normative:

informative: 
   RFC0226:
   RFC0760:
   RFC0791:
   RFC0793:
   RFC0894:
   RFC1035:
   RFC1122:
   RFC1631:
   RFC1766:
   RFC1958:
   RFC1984:
   RFC2026:
   RFC2277:
   RFC2460:
   RFC2606:
   RFC3365:
   RFC3536:
   RFC3724:
   RFC3935:
   RFC3979:
   RFC4084:
   RFC4033:
   RFC4101:
   RFC4949:
   rfc5246:
   RFC5321:
   RFC5944:
   RFC6101:
   RFC6108:
   RFC6120:
   RFC6365:
   RFC6797:
   RFC6698:
   RFC6701:
   RFC6973:
   RFC7258:
   RFC7469:
   RFC7540:
   RFC7574:
   RFC7624:
   RFC7626:
   RFC7725:
   RFC7858:


   UNGA2013:
     title: UN General Assembly Resolution "The right to privacy in the digital age" (A/C.3/68/L.45)
     date: 2013
     author:
        - org: United Nations General Assembly
     target: http://daccess-ods.un.org/TMP/1133732.05065727.html

   HRC2012:
     title: UN General Assembly Resolution "The right to privacy in the digital age" (A/C.3/68/L.45)
     date: 2011
     author:
        - org: United Nations Human Rights Council
     target: http://daccess-ods.un.org/TMP/554342.120885849.html

   NETmundial:
     title: NETmundial Multistakeholder Statement
     date: 2014
     author:
        - org: NETmundial
     target: http://netmundial.br/wp-content/uploads/2014/04/NETmundial-Multistakeholder-Document.pdf

   UDHR:
     title: The Universal Declaration of Human Rights
     date: 1948
     author:
        - org: United Nations General Assembly
     target: http://www.un.org/en/documents/udhr/

   ICESCR:
     title: International Covenant on Economic, Social and Cultural Rights
     date: 1966
     author:
        - org: United Nations General Assembly
     target: http://www.ohchr.org/EN/ProfessionalInterest/Pages/CESCR.aspx

   caida:
     title: Analysis of Country-wide Internet Outages Caused by Censorship
     date: 2013
     author:
        - ins: A. Dainotti
        - ins: C. Squarcella
        - ins: E. Aben
        - ins: K. Claffy
        - ins: M. Chiesa
        - ins: M. Russo
        - ins: A. Pescape
     target: http://www.caida.org/publications/papers/2014/outages_censorship/outages_censorship.pdf

   torproject:
     title: Tor Project - Anonymity Online
     date: 2007
     author:
        - ins: The Tor Project
     target: https://www.torproject.org/

   natusage:
     title: NAT usage in Residential Broadband networks
     date: 2011
     author:
        - ins: G. Maier
        - ins: F. Schneider
        - ins: A. Feldmann
     target: http://www.icsi.berkeley.edu/pubs/networking/NATusage11.pdf

   bbc-wikileaks:
     title: Whistle-blower site taken offline
     date: 2008
     author:
        - org: BBC
     target: http://news.bbc.co.uk/2/hi/technology/7250916.stm

   techyum:
     title: Official - vb.ly Link Shortener Seized by Libyan Government
     date: 2010
     author:
        - ins: Violet
     target: http://techyum.com/2010/10/official-vb-ly-link-shortener-seized-by-libyan-government/

   ververis:
     title: Understanding Internet Censorship Policy - The Case of Greece
     date: 2015
     author:
        - ins: V. Vasilis
        - ins: G. Kargiotakis
        - ins: A. Filasto
        - ins: B. Fabian
        - ins: A. Alexandros
     target: https://www.usenix.org/system/files/conference/foci15/foci15-paper-ververis-update.pdf

   hall:
     title: A Survey of Worldwide Censorship Techniques
     date: 2015
     author:
        - ins: J. Hall
        - ins: M. Aaron
        - ins: B. Jones
     target: https://tools.ietf.org/html/draft-hall-censorship-tech-01

   greatfirewall:
     title: Towards a Comprehensive Picture of the Great Firewall's DNS Censorship
     date: 2014
     author:
        - ins: Anonymous
     target: https://www.usenix.org/system/files/conference/foci14/foci14-anonymous.pdf

   torrentfreak1:
     title: Proposal for research on human rights protocol considerations
     date: 2015
     author:
        - ins: E. Van der Sar
     target: https://torrentfreak.com/is-your-isp-messing-with-bittorrent-traffic-find-out-140123/

   wikileaks:
     title: "Market Survey : Detection & Filtering Solutions to Identify File Transfer of Copyright Protected Content for Warner Bros. and movielabs"
     date: 2011
     author:
        - ins: T. Sladek
        - ins: E. Bröse
     target: https://wikileaks.org/sony/docs/05/docs/Anti-Piracy/CDSA/EANTC-Survey-1.5-unsecured.pdf

   ars:
     title: P2P researchers - use a blocklist or you will be tracked... 100% of the time
     date: 2007
     author:
        - ins: N. Anderson
     target: http://arstechnica.com/uncategorized/2007/10/p2p-researchers-use-a-blocklist-or-you-will-be-tracked-100-of-the-time/

   torrentfreak2:
     title: LAWYERS SENT 109,000 PIRACY THREATS IN GERMANY DURING 2013
     date: 2014
     author:
        - ins: Andy
     target: https://torrentfreak.com/lawyers-sent-109000-piracy-threats-in-germany-during-2013-140304/

   freenet1:
     title: What is Freenet?
     author:
        - org: Freenet
     target: https://freenetproject.org/whatis.html

   freenet2:
     title: The Philosphy behind Freenet?
     author:
        - ins: Ian Clarke
     target: https://freenetproject.org/philosophy.html

   bitmessage:
     title: Bitmessage Wiki?
     date: 2014
     author:
        - org: Bitmessage
     target: https://bitmessage.org/wiki/Main_Page

   tribler:
     title: About Tribler
     date: 2013
     author:
        - org: Delft University of Technology, Department EWI/PDS/Tribler
     target: https://www.tribler.org/about.html

   PETS2015VPN:
     title: A Glance through the VPN Looking Glass
     date: 2015
     author:
        - ins: V.C. Pera
        - ins: M.V. Barbera
        - ins: G. Tyson
        - ins: H. Haddadi
        - ins: A. Mei
     target: http://www.eecs.qmul.ac.uk/~hamed/papers/PETS2015VPN.pdf

   spiegel:
     title: Prying Eyes - Inside the NSA's War on Internet Security
     date: 2014
     author:
        - org: SPIEGEL
     target: http://www.spiegel.de/international/germany/inside-the-nsa-s-war-on-internet-security-a-1010361.html

   Rideout:
     title: Making security easier
     date: 2008
     author:
        - ins: A. Rideout
     target: http://gmailblog.blogspot.de/2008/07/making-security-easier.html

   Schillace:
     title: Default https access for Gmail
     date: 2010
     author:
        - ins: S. Schillace
     target: http://gmailblog.blogspot.de/2010/01/default-https-access-for-gmail.html

   Peterson:
     title: Yahoo to make SSL encryption the default for Webmail users. Finally.
     date: 2013
     author:
        - ins: A. Peterson
        - ins: B. Gellman
        - ins: A. Soltani
     target: http://gmailblog.blogspot.de/2010/01/default-https-access-for-gmail.html

   Collins:
     title: Hacking Team's oppressive regimes customer list revealed in hack
     date: 2015
     author:
        - ins: K. Collins
     target: http://www.wired.co.uk/news/archive/2015-07/06/hacking-team-spyware-company-hacked

   Cath:
     title: "A Case Study of Coding Rights: Should Freedom of Speech Be Instantiated in the Protocols and Standards Designed by the Internet Engineering Task Force?"
     date: 2015
     author:
        - ins: C. Cath
     target: https://www.ietf.org/mail-archive/web/hrpc/current/pdf36GrmRM84S.pdf

   CathFloridi:
     title: "The Design of the Internet's Architecture by the Internet Engineering Task Force (IETF) and Human Rights"
     date: forthcoming
     author:
        - ins: C. Cath
        - ins: L. Floridi

   Haagsma:
     title: "Deep dive into QUANTUM INSERT"
     date: 2015
     author:
        - ins: L. Haagsma
     target: http://blog.fox-it.com/2015/04/20/deep-dive-into-quantum-insert/

   WynsbergheMoura:
     title: The concept of embedded values and the example of internet security
     date: 2013
     author:
        - ins: A. Wynsberghe 
        - ins: G. Moura
     target: http://doc.utwente.nl/87095/

   RSF:
     title: Syria using 34 Blue Coat Servers to spy on Internet users
     date: 2013
     author:
        - org: RSF
     target: https://rsf.org/en/news/syria-using-34-blue-coat-servers-spy-internet-users

   Schneier:
     title: Attacking Tor - how the NSA targets users' online anonymity
     date: 2013
     author:
        - ins: B. Schneier
     target: http://www.theguardian.com/world/2013/oct/04/tor-attacks-nsa-users-online-anonymity

   Appelbaum:
     title: NSA targets the privacy-conscious
     date: 2015
     author:
        - ins: J. Appelbaum
        - ins: A. Gibson
        - ins: V. Kabish
        - ins: L. Kampf
        - ins: L. Ryge
     target: http://daserste.ndr.de/panorama/aktuell/nsa230_page-1.html

   Marcak:
     title: China's Great Fire Cannon
     date: 2015
     author:
        - ins: B. Marcak
        - ins: N. Weaver
        - ins: J. Dalek
        - ins: R. Ensafi
        - ins: D. Fifield
        - ins: S. McKune
        - ins: A. Rey
        - ins: J. Scott-Railton
        - ins: R. Deibert
        - ins: V. Paxson
     target: https://citizenlab.org/2015/04/chinas-great-cannon/

   Googlepatent:
     title: Method and device for network traffic manipulation
     date: 2012
     author:
        - ins: Google
     target: https://www.google.com/patents/EP2601774A1?cl=en

   Marquis-Boire:
     title: Schrodinger's Cat Video and the Death of Clear-Text
     date: 2014
     author:
        - ins: M. Marquis-Boire
     target: https://citizenlab.org/2014/08/cat-video-and-the-death-of-clear-text/

   pidgin:
     title: -XMPP- Invisible mode violating standard
     date: 2015-07
     author:
       - ins: js
       - org: Pidgin Developers
     target: https://developer.pidgin.im/ticket/4322

   xmppmanifesto:
     title: A Public Statement Regarding Ubiquitous Encryption on the XMPP Network
     date: 2014
     author:
       - ins: P. Saint-Andre
       - ins: XMPP Operators
     target: https://raw.githubusercontent.com/stpeter/manifesto/master/manifesto.txt

   namecoin:
     title: Namecoin - Decentralized secure names
     date: 2015
     author:
        - org: Namecoin
     target: https://namecoin.info/

   Douceur:
     title: The Sybil Attack
     date: 2002
     author:
        - ins: J.R. Douceur
     target: http://research.microsoft.com:8082/pubs/74220/IPTPS2002.pdf

   Bray:
     title: A New HTTP Status Code for Legally-restricted Resources
     date: 2016
     author:
        - ins: T. Bray
     target: https://tools.ietf.org/html/draft-ietf-httpbis-legally-restricted-status-04

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

   ICCPR:
     title: International Covenant on Civil and Political Rights
     date: 1976
     author:
        org: United Nations General Assembly
     target: http://www.ohchr.org/EN/ProfessionalInterest/Pages/CCPR.aspx

   Berners-Lee:
     title: Weaving the Web,
     author:
        - ins: T. Berners-Lee
        - ins: M. Fischetti
     seriesinfo:
       HarperCollins: p 208
     date: 1999

   Saltzer:
     title: End-to-End Arguments in System Design
     author:
        - ins: J.H. Saltzer
        - ins: D.P. Reed
        - ins: D.D. Clark
     seriesinfo: ACM TOCS, Vol 2, Number 4, November
        1984, pp 277-288.
     date: 1984

   Clark:
     title: The Design Philosophy of the DARPA Internet Protocols
     author:
       - ins: D. Clark
     seriesinfo: Proc SIGCOMM 88, ACM CCR Vol 18, Number 4, August
        1988, pp. 106-114.
     date: 1988

   Blumenthal:
     title: "Rethinking the design of the Internet: The end-to-end arguments vs. the brave new world"
     author:
        - ins: M. Blumenthal
        - ins: D.D. Clark
     seriesinfo: ACM Transactions on Internet Technology, Vol. 1, No. 1, August 2001, pp 70-109.
     date: 2001

   Franklin:
     title: The Real World of Technology
     date: 1999
     author:
        - ins: U. M. Franklin
     target: http://houseofanansi.com/products/the-real-world-of-technology-digital
    
   Dutton:
     title: "Freedom of Connection, Freedom of Expression: the Changing legal and regulatory Ecology Shaping the Internet."
     date: 2011
     author:
        - ins: W. Dutton
     target: http://portal.unesco.org/ci/en/ev.php-URL_ID=31397%26URL_DO=DO_TOPIC%26URL_SECTION=201.html
    
   Kaye:
     title: Report of the Special Rapporteur on the promotion and protection of the right to freedom of opinion and expression
     date: 2016
     author:
        - ins: D. Kaye
     target: http://www.ohchr.org/EN/Issues/FreedomOpinion/Pages/Privatesectorinthedigitalage.aspx

   FIArch:
     title: Future Internet Design Principles
     date: January 2012
     target: http://www.future-internet.eu/uploads/media/FIArch_Design_Principles_V1.0.pdf

   Elahi:
     title: "CORDON - A taxonomy of Internet Censorship Resistance Strategies"
     author:
        - ins: T. Elahi
        - ins: I. Goldberg
     target: http://cacr.uwaterloo.ca/techreports/2012/cacr2012-33.pdf
     date: 2012

   Brown:
     title: "A Prehistory of Internet Governance"
     date: 2013
     author:
        - ins: I. Brown
        - ins: M. Ziewitz
     seriesinfo: Research Handbook on Governance of the Internet. Cheltenham, Edward Elgar.

   FRAMEWORK:
     title: Information technology - Framework for internationalization, prepared by ISO/IEC JTC 1/SC 22/WG 20 ISO/IEC TR 11017
     date: 1997
     author:
        - ins: ISO/IEC

   W3Ci18nDef:
     title: Localization vs. Internationalization
     date: 2010
     author:
        - org: W3C
     target: http://www.w3.org/International/questions/qa-i18n.en

   W3CAccessibility:
     title: Accessibility
     date: 2015
     author:
        - org: W3C
     target: https://www.w3.org/standards/webdesign/accessibility

   Rachovitsa:
     title: Engineering 'Privacy by Design' in the Internet Protocols - Understanding Online Privacy both as a Technical and a Human Rights Issue in the Face of Pervasive Monitoring
     date: 2015
     author:
        - ins: A. Rachovitsa
     target: https://www.ietf.org/mail-archive/web/hrpc/current/pdfRBnRYFeVsm.pdf
     seriesinfo: International Journal of Law and Information Technology

   Davidsonetal:
     title: Strangers in a strange land
     date: 2002
     author:
        - ins: A. Davidson
        - ins: J. Morris
        - ins: R. Courtney
     target: https://www.cdt.org/files/publications/piais.pdf
     seriesinfo: Telecommunications Policy Research Conference

   Clarketal:
     title: Tussle in cyberspace - defining tomorrow's Internet
     date: 2005
     author:
        - ins: D.D. Clark
        - ins: J. Wroclawski
        - ins: K.R. Sollins
        - ins: R. Braden
     target: https://dl.acm.org/citation.cfm?id=1074049
     seriesinfo: ACM Digital Library

   Broeders:
      title: The public core of the Internet
      date: 2015
      author:
         - ins: D. Broeders
      target: http://www.wrr.nl/en/publications/publication/article/de-publieke-kern-van-het-internet-1/
      seriesinfo: WRR

   Musiani:
      title:  Giants, Dwarfs and Decentralized Alternatives to Internet-based Services - An Issue of Internet Governance
      date: 2015
      author:
        - ins: F. Musiani
      target: http://doi.org/10.16997/wpcc.214
      seriesinfo: Westminister Papers in Communication and Culture

   BrownMarsden:
      title: Regulating code
      date: 2013
      author:
        - ins: I. Brown
        - ins: C. Marsden
      target: https://mitpress.mit.edu/books/regulating-code
      seriesinfo: MIT Press

   Brownetal:
      title: Should specific values be embedded in the Internet Architecture?
      date: 2010
      author:
        - ins: I. Brown
        - ins: D. Clark
        - ins: D. Trossen
      target: http://conferences.sigcomm.org/co-next/2010/Workshops/REARCH/ReArch_papers/10-Brown.pdf
      seriesinfo: Sigcomm

   Abbate:
      title: Inventing the Internet
      date: 2000
      author:
        - ins: J. Abbate
      target: https://mitpress.mit.edu/books/inventing-internet
      seriesinfo: MIT Press

   Zittrain:
      title: The Future of the Internet - And How to Stop It
      date: 2008
      author:
        - ins: J. Zittrain
      target: https://dash.harvard.edu/bitstream/handle/1/4455262/Zittrain_Future%20of%20the%20Internet.pdf?sequence=1
      seriesinfo: Yale University Press

   Denardis15:
      title: The Internet Design Tension between Surveillance and Security
      date: 2015
      author:
        - ins: L. Denardis
      target: http://is.gd/7GAnFy
      seriesinfo: IEEE Annals of the History of Computing (volume 37-2)

   Denardis14:
      title: The Global War for Internet Governance
      date: 2014
      author:
        - ins: L. Denardis
      target: https://www.jstor.org/stable/j.ctt5vkz4n
      seriesinfo: Yale University Press

   Lessig:
      title: Code - And Other Laws of Cyberspace, Version 2.0.
      date: 2006
      author:
        - ins: L. Lessig
      target: http://codev2.cc/
      seriesinfo: New York Basic Books

   Mueller:
      title: Networks and States
      date: 2010
      author:
        - ins: M. Mueller
      target: https://mitpress.mit.edu/books/networks-and-states
      seriesinfo: MIT Press

   Bless:
      title: Values and Networks
      date: 2015
      author:
        - ins: R. Bless
        - ins: C. Orwat

   Benkler:
     title: The wealth of Networks - How social production transforms markets and freedom
     date: 2006
     author:
        - ins: Y. Benkler
     target: http://is.gd/rxUpTQ
     seriesinfo: New Haven and London - Yale University Press

   Babbie:
     title: The Basics of Social Research
     date: 2010
     author:
        - ins: E. Babbie
     seriesinfo: Belmont CA Cengage

   Denzin:
     title: Handbook of Qualitative Research
     date: 2000
     author:
        - ins: N.K. Denzin
        - ins: Y.S. Lincoln
     target: http://www.amazon.com/SAGE-Handbook-Qualitative-Research-Handbooks/dp/1412974178
     seriesinfo: Thousand Oaks CA Sage

   Geertz:
     title: Kinship in Bali
     date: 1975
     author:
        - ins: G. Clifford
     target: http://press.uchicago.edu/ucp/books/book/chicago/K/bo3625088.html
     seriesinfo: Chicago University of Chicago Press.

   Jabri:
     title: Discourses on Violence - conflict analysis reconsidered
     date: 1996
     author:
        - ins: V. Jabri
     seriesinfo: Manchester University Press

   King:
     title: Power, Social Violence and Civil Wars
     date: 2007
     author:
        - ins: C. King
     seriesinfo: Washington D.C. United States Institute of Peace Press

   Schroeder:
     title: Introduction - Violent Imaginaries and Violent Practice
     date: 2001
     author:
        - ins: I.W. Schroeder
        - ins: B. Schmidt
     target: http://resourcelists.st-andrews.ac.uk/items/BFC20363-67B0-B3EF-EA48-13E5230E7899.html
     seriesinfo: London and New York Routledge

   Richie:
     title: Qualitative Research Practice - A Guide for Social Science Students and Researchers
     date: 2003
     author:
        - ins: J. Richie
        - ins: J. Lewis
     target: http://www.amazon.co.uk/Qualitative-Research-Practice-Students-Researchers/dp/0761971106
     seriesinfo: London Sage

   Doty:
     title: Automated text analysis of Requests for Comment (RFCs)
     date: 2014
     author:
        - ins: N. Doty
     target: https://github.com/npdoty/rfc-analysis

   Pouwelse:
     title: Media without censorship
     date: 2012
     author:
        - ins: J. Pouwelse, Ed.
     target: https://tools.ietf.org/html/draft-pouwelse-censorfree-scenarios

   Penney:
     title: "Chilling Effects: Online Surveillance and Wikipedia Use"
     date: 2016
     author:
        - ins: J. Penney
     target: http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2769645

   BernersLeeHalpin:
     title: Defend the Web
     date: 2012
     author:
        - ins: T. Berners-Lee
        - ins: H. Halpin
     target: http://www.ibiblio.org/hhalpin/homepage/publications/def-timbl-halpin.pdf

   Bhargavan:
     title: "Triple Handshakes and Cookie Cutters: Breaking and Fixing Authentication over TLS"
     date: 2014
     author: 
        - ins: K. Bhargavan 
        - ins: A. Delignat-Lavaud 
        - ins: C. Fournet 
        - ins: A. Pironti
        - ins: P. Strub
     seriesinfo: "IEEE Symposium on Security and Privacy 2014: 98-113"

   Adrian:
     title: "Imperfect Forward Secrecy: How Diffie-Hellman Fails in Practice"
     date: 2015
     author:
        - ins: D. Adrian
        - ins: K. Bhargavan
        - ins: Z. Durumeric
        - ins: P. Gaudry
        - ins: M. Green
        - ins: J.A. Halderman
        - ins: N. Heninger
        - ins: D. Springall
        - ins: E. Thomé 
        - ins: L. Valenta
        - ins: B. VanderSloot
        - ins: E. Wustrow
        - ins: S. Zanella Béguelin
        - ins: P. Zimmermann 
     seriesinfo: "ACM Conference on Computer and Communications Security 2015: 5-17"

   sslstrip:
     title: "Software >> sslstrip"
     date: 2011
     author: 
        - ins: M. Marlinspike
     target: https://moxie.org/software/sslstrip/

   newegg:
     title: "Newegg on trial: Mystery company TQP rewrites the history of encryption"
     date: 2013
     author: 
        - ins: J. Mullin
     target: http://arstechnica.com/tech-policy/2013/11/newegg-on-trial-mystery-company-tqp-re-writes-the-history-of-encryption/

   notewell: 
     title: Note Well
     date: 2015
     author:
        - org: IETF
     target: https://www.ietf.org/about/note-well.html

   patentpolicy:
     title: W3C Patent Policy
     date: 2004
     author:
        - org: W3C
     target: https://www.w3.org/Consortium/Patent-Policy-20040205/

   FOC:
     title: The Tallinn Agenda - Recommendations for Freedom Online
     date: 2014
     author:
        - org: Ministers of the Freedom Online Coalition
     target: https://www.freedomonlinecoalition.com/wp-content/uploads/2014/04/FOC-recommendations-consensus.pdf

   Meyer:
     title: "Defining and Evaluating Resilience: A Performability Perspective, presentation at International Workshop on Performability Modeling of Computer and Communication Systems."
     date: 2009
     author:
        - ins: J.F. Meyer 

   dict:
     title: Reliability (dictionary entry)
     date: 2016
     author:
        - org: BusinessDictionary.com. WebFinance, Inc. 
     target: http://www.businessdictionary.com/definition/reliability.html

   Farrow:
     title: Source Address Spoofing
     date: 2016
     author: 
        - ins: R. Farrow
     target: https://technet.microsoft.com/library/cc723706.aspx
     
   WSJ:
     title: Firms Aided Libyan Spies
     date: 2011
     author: 
        - ins: P. Sonne
        - ins: M. Coker
     target: http://www.wsj.com/articles/SB10001424053111904199404576538721260166388

   Insinuator:
     title: "Vulnerabilities & attack vectors of VPNs (Pt 1)"
     date: 2013
     author: 
        - ins: N. Schiess
     target: https://www.insinuator.net/2013/08/vulnerabilities-attack-vectors-of-vpns-pt-1/

   Alshalanetal:
     title: A Survey of Mobile VPN Technologies
     date: 2016
     author: 
        - ins: A. Alshalan
        - ins: S. Pisharody
        - ins: D. Huang
     target: "http://ieeexplore.ieee.org.proxy.uba.uva.nl:2048/stamp/stamp.jsp?arnumber=7314859"

   HTML5:
     title: HTML5
     date: 2014
     author: 
        - org: W3C
     target: https://www.w3.org/TR/html5/

   Greenwald:
     title: "XKeyscore: NSA tool collects 'nearly everything a user does on the internet'"
     date: 2013
     author: 
        - ins: G. Greenwald
     target: https://www.theguardian.com/world/2013/jul/31/nsa-top-secret-program-online-data

   WP-Tempora:
     title: Tempora
     date: 2016
     author: 
        - org: Wikipedia
     target: https://en.wikipedia.org/wiki/Tempora

   BCP72:
     title: Guidelines for Writing RFC Text on Security Considerations
     date: 2003
     author: 
        - org: IETF
     target: https://datatracker.ietf.org/doc/bcp72/

--- abstract

This document provides a proposal for a vocabulary to discuss the relation between human rights and Internet protocols, an overview of the discussion in technical and academic literature and communities, a proposal for the mapping of the relation between human rights and technical concepts, and a proposal for guidelines for human rights considerations, similar to the work done on the guidelines for privacy considerations {{RFC6973}}.

This document is not an Internet Standards Track specification; it is published for informational purposes.

This document is a product of the Internet Research Task Force (IRTF). The IRTF publishes the results of Internet-related research and development activities. This documents aims to be a consensus document of the Human Rights Protocol Consideration Research Group of the Internet Research Task Force (IRTF).

Discussion of this draft at: hrpc@irtf.org // https://www.irtf.org/mailman/listinfo/hrpc

--- middle

Introduction
============

    "There's a freedom about the Internet: As long as we accept the
       rules of sending packets around, we can send packets containing
       anything to anywhere."

{{Berners-Lee}}

    "The Internet isn't value-neutral, and neither is the IETF."

{{RFC3935}}

The evergrowing interconnectedness of Internet and society increases the impact of the Internet on the lives of individuals. Because of this, the design and development of the architecture of the Internet also has a growing impact on society. This has led to an broad recognition that human rights {{UDHR}} {{ICCPR}} {{ICESCR}} have a role in the development and management of the Internet {{HRC2012}} {{UNGA2013}} {{NETmundial}}. It has also been argued that the Internet should be strengthened as a human rights enabling environment {{Brown}}.

This document aims to expose the relation between protocols and human rights, propose possible guidelines to protect the Internet as a human-rights-enabling environment in future protocol development, in a manner similar to the work done for Privacy Considerations in {{RFC6973}}, and to increase the awareness in both the human rights community and the technical community on the importance of the technical workings of the Internet and its impact on human rights. 

Open, secure and reliable connectivity is necessary (although not sufficient) to excercise the human rights such as freedom of expression and freedom of association {{FOC}}, as defined in the Universal Declaration of Human Rights {{UDHR}}. The purpose of the Internet to be a global network of networks that provides unfettered connectivity to all users and for any content {{RFC1958}}. This objective of stimulating global connectivity contributes to the Internet's role as an enabler of human rights. Next to that, the strong commitment to security {{RFC1984}} {{RFC3365}} and privacy {{RFC6973}} {{RFC7258}} in the Internet's architectural design contribute to the strengthening of the Internet as a human rights enabling environment. One could even argue that the Internet is not only an enabler of human rights, but that human rights lie at the basis of, and are ingrained in, the architecture of the network. Internet connectivity increases the capacity for individuals to exercise their rights, the core of the Internet, its architectural design is therefore closely intertwined with the human rights framework {{CathFloridi}}. The quintessential link between the Internet's architecture and human rights has been argued by many. {{Bless}} for instance argues that, 'to a certain extent, the Internet and its protocols have already facilitated the realization of human rights, e.g., the freedom of assembly and expression. In contrast, measures of censorship and pervasive surveillance violate fundamental human rights.' {{Denardis15}} argues that 'Since the first hints of Internet commercialization and internationalization, the IETF has supported strong security in protocol design and has sometimes served as a force resisting protocol-enabled surveillance features.' By doing so, the IETF enabled the manifestation of the right to privacy, through the Internet's architecture. Additionally, access to information gives people access to knowledge that enables them to help satisfy other human rights, as such the Internet  increasingly becoming a pre-condition for human rights rather than a supplement.

Human rights can be in conflict with each other, such as the right to freedom of expression and the right to privacy. In such as case the different affected rights need to be balanced. In order to do this it is crucial that the rights impacts are clearly documented in order to mitigate the potential harm in a proportional way. Making that process tangible and practical for protocol developers is what this research aims to ultimately contribute to.

The open nature of the initial technical design (open standards, open source, etc) fostered freedom of communication as a core value, everyone could join and everyone could submit code. However as the scale and the commercialization of the Internet grew, topics like access, rights and connectivity are forced to compete with other values. Therefore, important human rights enabling characteristics of the Internet might be degraded if they're not properly defined, described and protected as such. And, the other way around, not protecting human right enabling characteristics could also result in (partial) loss of functionality and connectivity, and other inherent parts of the Internet's architecture. New protocols, particularly those that upgrade the core infrastructure of the network, should be designed to continue to enable fundamental human rights.

The IETF has produced guidelines and procedures to ensure and galvanize the privacy and security of the network in protocol development. This document aims to explore the possibility of the development of similar procedures for guidelines for human rights considerations to ensure that protocols developed in the IETF do not have an adverse impact on the realization of human rights on the Internet. By carefully considering the answers to the questions posed in the final part of this document, document authors should be able to produce a comprehensive analysis that can serve as the basis for discussion on whether the protocol adequately protects against human rights threats.

This document has been developed within the framework of the Human Rights Protocols Considerations Research Group, based on discussions on the hrpc mailinglist and during hrpc sessions, where this document also has been extensively discussed. The draft in its current form and iteration has received five in-depth reviews on list, and received many comments from inside and outside the IRTF and IETF community.  The authors believe that the issues that have been raised by the reviewers have been addressed. 

Vocabulary used
===============

In the discussion of human rights and Internet architecture concepts developed in computer science, networking, law, policy-making and advocacy are coming together {{Dutton}},{{Kaye}},{{Franklin}}, {{RFC1958}}. The same concepts might have a very different meaning and implications in other areas of expertise. In order to foster a constructive interdisciplinary debate, and minimize differences in interpretation, the following glossary is provided, building as much as possible on existing definitions, and where these were not available definitions have been developed. 

Accessibility
: Full Internet Connectivity as described in {{RFC4084}} to provide unfettered access to the Internet

: The design of protocols, services or implementation that provide an enabling environment for people with disabilities.

: The ability to receive information available on the Internet

Anonymity
: The condition of an identity being unknown or concealed. {{RFC4949}}

Anonymous
: A state of an individual in which an observer or attacker cannot identify the individual within a set of other  individuals (the anonymity set). {{RFC6973}}

Authenticity
: The fact that the data does indeed come from the source it claims to come from. (It is strongly linked with Integrity, see below).

Censorship resistance
: Methods and measures to mitigate Internet censorship.

Confidentiality
: The non-disclosure of information to any unintended person or host or party {{RFC4949}}.

Connectivity
: The extent to which a device or network is able to reach other devices or networks to exchange data. The Internet is the tool for providing global connectivity {{RFC1958}}. Different types of connectivity are further specified in {{RFC4084}}.

Content-agnosticism
: Treating network traffic identically regardless of content.

Decentralized
: Implementation or deployment of standards, protocols or systems without one single point of control.

End-to-End
: The principal of extending characteristics of a protocol or system as far as possible within the system. technically this means that intermediaries should not modify messages but simply route them to their desired end-points as capabilities should be given by the end-points, that the network then interconnects rather than controls.
For example, end-to-end instant message encryption would conceal communications from one user's instant messaging application through any intermediate devices and servers all the way to the recipient's instant messaging application. If the message was decrypted at any intermediate point--for example at a service provider--then the property of end-to-end encryption would not be present.

: One of the key architectural guidelines of the Internet is the end-to-end principle in the papers by Saltzer, Reed, and Clark {{Saltzer}} {{Clark}}. The end-to-end principle was originally articulated as a question of where best not to put functions in a communication system. Yet, in the ensuing years, it has evolved to address concerns of maintaining openness, increasing reliability and robustness, and preserving the properties of user choice and ease of new service development as discussed by Blumenthal and Clark in {{Blumenthal}}; concerns that were not part of the original articulation of the end-to-end principle. {{RFC3724}}

Federation
: The possibility of connecting autonomous and possibly centralized systems into single system without a central authority.

Heterogeinity
:  The Internet is characterized by heterogeneity on many levels: devices and nodes, router scheduling algorithms and queue management mechanisms, routing protocols, levels of multiplexing, protocol versions and implementations, underlying link layers (e.g., point-to-point, multi-access links, wireless, FDDI, etc.), in the traffic mix and in the levels of congestion at different times and places. Moreover, as the Internet is composed of independent organizations and Internet service providers, each with their own separate policy concerns,there is a large heterogeneity of administrative domains and pricing structures. As a result, the heterogeneity principle proposed in {{RFC1958}} needs to be supported by design. {{FIArch}}

Integrity
: Maintenance and assurance of the accuracy and consistency of data to ensure it has not been (intentionally or unintentionally) altered {{RFC4949}}. 

Internet censorship
:  Internet censorship is the intentional suppression of information originating, flowing or stored on systems connected to the Internet where that information is relevant for decision making to some entity. {{Elahi}}

Interoperable
: A property of a documented standard or protocol which allows different independent implementations to work with each other without any restricted access or functionality.

Internationalization (i18n)
: The practice of making protocols, standards, and implementations usable in different languages and scripts (see Localization).

: "In the IETF, "internationalization" means to add or improve the handling of non-ASCII text in a protocol" {{RFC6365}}.  A different perspective, more appropriate to protocols that are designed for global use from the beginning, is the definition used by W3C:

: "Internationalization is the design and development of a
product, application or document content that enables easy
localization for target audiences that vary in culture, region,
or language."  {{W3Ci18nDef}}

: Many protocols that handle text only handle one charset (US-ASCII), or leave the question of encoding up to local guesswork (which leads, of course, to  interoperability problems) {{RFC3536}}. If multiple charsets are permitted, they must be explicitly identified {{RFC2277}}.  Adding non-ASCII text to a protocol allows the protocol to handle more scripts, hopefully all of the ones useful in the world.  In today's world, that is normally best accomplished by allowing Unicode encoded in UTF-8 only, thereby shifting conversion issues away from individual choices.

Localization (l10n)
: The practice of translating an implementation to make it functional in a specific language or for users in a specific locale (see Internationalization).

: (cf {{RFC6365}}): The process of adapting an internationalized application platform or application to a specific cultural environment.  In localization, the same semantics are preserved while the syntax may be changed. {{FRAMEWORK}}

: Localization is the act of tailoring an application for a different language or script or culture.  Some internationalized applications can handle a wide variety of languages.  Typical users only understand a small number of languages, so the program must be tailored to interact with users in just the languages they know.
The major work of localization is translating the user interface and documentation.  Localization involves not only changing the language interaction, but also other relevant changes such as display of numbers, dates, currency, and so on.  The better internationalized an application is, the easier it is to localize it for a particular language and character encoding scheme.

Open standards
: Conform  {{RFC2606}}: Various national and international standards bodies, such as ANSI, ISO, IEEE, and ITU-T, develop a variety of protocol and service
      specifications that are similar to Technical Specifications
      defined here.  National and international groups also publish
      "implementors' agreements" that are analogous to Applicability
      Statements, capturing a body of implementation-specific detail
      concerned with the practical application of their standards.  All
      of these are considered to be "open external standards" for the
      purposes of the Internet Standards Process.

Openness
: The quality of the unfiltered Internet that allows for free access to other hosts.

: Absence of centralized points of control &#x2013; a feature that is assumed to make it easy for new users to join and new uses to unfold {{Brown}}.

Permissionless innovation
: The freedom and ability to freely create and deploy new protocols on top of the communications constructs that currently exist.

Privacy
: The right of an entity (normally a person), acting in its own behalf, to determine the degree to which it will interact with its environment, including the degree to which the entity is willing to share its personal information with others. {{RFC4949}}

: The right of individuals to control or influence what information related to them may be collected and stored and by whom and to whom that information may be disclosed.

: Privacy is a broad concept relating to the protection of individual or group autonomy and the relationship between an individual or group and society, including government, companies and private individuals. It is often summarized as "the right to be left alone" but it encompasses a wide range of rights including protections from intrusions into family and home life, control of sexual and reproductive rights, and communications secrecy.  It is commonly recognized as a core right that underpins human dignity and other values such as freedom of association and freedom of speech.
: The right to privacy is also recognized in nearly every national constitution and in most international human rights treaties. It has been adjudicated upon both by international and regional bodies. The right to privacy is also legally protected at the national level through provisions in civil and/or criminal codes.

Reliable
: Reliability ensures that a protocol will execute its function consistently and error resistant as described and function without unexpected result. A system that is reliable degenerates gracefully and will have a documented way to announce degradation. It also has mechanisms to recover from failure gracefully, and if applicable, allow for partial healing {{dict}}.

Resilience
: The maintaining of dependability and performance in the face of unanticipated changes and circumstances {{Meyer}}.

Robustness
: The resistance of protocols and their implementations to errors, and to involuntary, legal or malicious attempts to disrupt its mode of operations. {{RFC0760}} {{RFC0791}} {{RFC0793}} {{RFC1122}}. Or framed more positively, a system can provide functionality consistently and without errors despite  involuntary, legal or malicious attempts to disrupt its mode of operations.

Scalable
: The ability to handle increased or decreased workloads predictably within defined expectations. There should be a clear definition of its scope and applicability. The limits of a systems scalability should be defined.

Strong encryption / cryptography
: Used to describe a cryptographic algorithm that would require a large amount of computational power to defeat it. {{RFC4949}}

Communication and information security
: A combination of reliability, confidentiality, integrity, anonymity, and authenticity is what makes up security on the Internet.

Connectivity
: The combination of the end-to-end principle, interoperability, resilience, reliability and robustness are the enableing factors that result in connectivity to and on the Internet.


Research Questions
==================
The Human Rights Protocol Considerations Research Group (hrpc) in the Internet Research Taskforce (IRTF) embarked on its mission to answer the following two questions which are also the main two questions which this documents seeks to answer:

1. How can Internet protocols and standards impact human rights, either by enabling them or by creating a restrictive environment?

2. Can guidelines be developed to improve informed and transparent decision making about potential human rights impact of protocols?

Literature and Discussion Review
================================

Protocols and standards are regularly seen as merely performing technical functions. However, these protocols and standards do not exist outside of their technical context nor outside of their political, historical, economic, legal or cultural context. This is best exemplified by the way in which protocols have become part and parcel of political processes and public policies: one only has to look at the IANA transition, the RFC on pervasive monitoring or global innovation policy for concrete examples {{Denardis15}}. To quote {{Abbate}}: "protocols are politics by other means". Since the late 1990's a burgeoning group of academics and practitioners researched questions surrounding the societal impact of protocols. These studies vary in focus and scope: some focus on specific standards {{Davidsonetal}} {{Musiani}}, others look into the political, legal, commercial or social impact of protocols {{BrownMarsden}} {{Lessig}}, {{Mueller}} and yet others look at how the engineers' personal set of values get translated into technology {{Abbate}},{{CathFloridi}} {{Denardis15}} {{WynsbergheMoura}}.

Commercial and political influences on the management of the Internet's architecture are well-documented in the academic literature and will thus not be discussed here {{Benkler}}  {{Brownetal}}  {{Denardis15}}  {{Lessig}}  {{Mueller}}  {{Zittrain}}. It is sufficient to say that the IETF community consistently tries to push back against the standardization of surveillance and certain other issues that negatively influence end-users' experience of and trust in the Internet {{Denardis14}}. The role human rights play in engineering, architecture maintenance and protocol design is much less clear.

It is very important to understand how protocols and standards impact human rights. In particular because Standard Developing Organizations (SDOs) are increasingly becoming venues where social values (like human rights) are discussed, although often from a technological point of view. These SDOs are becoming a new focal point for discussions about values-by-design, and the role of technical engineers in protecting or enabling human rights {{Brownetal}} {{Clarketal}} {{Denardis14}} {{CathFloridi}} {{Lessig}} {{Rachovitsa}}.

In the academic literature five clear positions can be discerned, in relation to the role of human rights in protocol design and how to account for these human rights in protocol development: Clark et al. argue that there is a need to 'design for variation in outcome, so that the outcome can be different in different places, and the tussle takes place within the design (...) [as] Rigid designs will be broken; designs that permit variation will flex under pressure and survive {{Clarketal}}.' They hold that human rights should not be hard-coded into protocols because of four reasons: first, the rights in the UDHR are not absolute. Second, technology is not the only tool in the tussle over human rights. Third, there are inherent dangers to using the UDHR. What the authors mean by this is that  if the IETF were to bake the UDHR into its protocols, countries who do not agree with that might completely withdraw from the standard setting process.  And last but not least, it is dangerous to make promises that can't be kept. The open nature of the Internet will never, they argue, be enough to fully protect individuals' human rights.

Conversely, Brown et al. {{Brownetal}} state that 'some key, universal values - of which the UDHR is the most legitimate expression - should be baked into the architecture at design time.' They argue that design choices have offline consequences, and are able shape the power positions of groups or individuals in society. As such, the individuals making these technical decisions have a moral obligation to take into account the impact of their decisions on society, and by extension human rights. Brown et al recognise that values and the implementation of human rights vary across the globe. Yet they argue that all members of the United Nations have found 'common agreement on the values proclaimed in the Universal Declaration of Human Rights. In looking for the most legitimate set of global values to embed in the future Internet architecture, the UDHR has the democratic assent of a significant fraction of the planet's population, through their elected representatives."

The main disagreement between these two academic positions lies mostly in the question on whether a particular value system should be embedded into the Internet's architecture or whether the architecture needs to account for a varying set of values.

A third position that is similar to that of Brown et al., is taken by {{Broeders}} who argues that 'we must find ways to continue guaranteeing the overall integrity and functionality of the public core of the Internet.' He argues that the best way to do this is by declaring the backbone of the Internet - which includes the TCP/IP protocol suite, numerous standards, the Domain Name System (DNS), and routing protocols - a common public good. This is a different approach than that of {{Clarketal}} and {{Brownetal}} because Broeders does not suggest that social values should (or should not) be explicitly coded into the Internet's architecture, but rather that the existing architecture should be seen as an entity of public value.

Bless and Orwat {{Bless}} represent a fourth position. They argue that it is too early to make any definitive claims, but that there is a need for more careful analysis of the impact of protocol design choices on human rights. They also argue that it is important to search for solutions that 'create awareness in the technical community about impact of design choices on social values. And work towards a methodology for co-design of technical and institutional systems.'

Berners-Lee and Halpin argue that the Internet could lead to even new capacities, and these capacities may over time be viewed as new kinds of rights. For example, Internet access may be viewed as a human right in of itself if it is taken to be a pre-condition for other rights, even if it could not have been predicted at the declaration of the UNHDR after the end of World War 2.{{BernersLeeHalpin}}. This last position is interesting to keep in mind, but beyond the remit of this document.

It is important to give some background to the academic discussion on this issue. They also are important to document as they inform the position of the authors of this document. Our position is that hard-coding human rights into protocols is very complicated as each situation is dependent on its context. At this point is difficult to say whether hard-coding human rights into protocols is wise (or feasible). It is however important to make conscious and explicit design decisions that take into account the human rights protocol considerations guidelines developed below. This will ensure that the impact protocols can have on human rights is clear and explicit, both for developers and for users. In addition, it ensures that the impact of specific protocol on human rights is carefully considered and that concrete design decisions are documented in the protocol.

Pursuant to the principle of constant change, since the function and scope of the Internet evolves, so does the role of the IETF in developing standards. Internet standards are adopted on the basis of a series of criteria, including high technical quality, support by community consensus, and their overall benefit to the Internet. The latter calls for an assessment of the interests of all affected parties and the specifications' impact on the Internet's users. In this respect, the effective exercise of the human rights of the Internet users is a relevant consideration that needs to be appreciated in the standardization process insofar as it is directly linked to the reliability and core values of the Internet. {{RFC1958}} {{RFC0226}} {{RFC3724}}

This document details the steps taken in the research into human rights protocol considerations by the hrpc research group to clarify the relation between technical concepts used in the IETF and human rights. This document sets out some preliminary steps and considerations for engineers to take into account when developing standards and protocols.


Methodology
===========

Mapping the relation between human rights, protocols and architectures is a new research challenge, which requires a good amount of interdisciplinary and cross organizational cooperation to develop a consistent methodology. 

The methodological choices made in this document are based on the political science-based method of discourse analysis and ethnographic research methods {{Cath}}. This work departs from the assumption that language reflects the understanding of concepts. Or as {{Jabri}} holds, policy documents are 'social relations represented in texts where language is used to construct meaning and representation'. This process happens in 'the social space of society' {{Schroeder}} and manifests itself in institutions and organizations {{King}}, exposed using the ethnographic methods of semi-structured interviews and participant observation. Or in non-academic language, the way the language in IETF/IRTF documents describes and approaches the issues they are trying to address is an indicator for the underlying social assumptions and relations of the engineers to their engineering. By reading and analyzing these documents, as well as interviewing engineers and participating in the IETF/IRTF working groups, it is possible to distill the relation between human rights, protocols and the Internet's architecture as it pertains to the work of the IETF.

The discourse analysis was operationalized using qualitative and quantitative means. The first step taken by the authors and contributors was reading RFCs and other official IETF documents. The second step was the use of a python-based analyzer, using the tool Big Bang, adapted by Nick Doty {{Doty}} to scan for the concepts that were identified as important architectural principles (distilled on the initial reading and supplemented by the interviews and participant observation). Such a quantitative method is very precise and speeds up the research process {{Richie}}. But this tool is unable to understand 'latent meaning' {{Denzin}}. In order to mitigate these issues of automated word-frequency based approaches, and to get a sense of the 'thick meaning' {{Geertz}} of the data, a second qualitative analysis of the data set was performed. These various rounds of discourse analysis were used to inform the interviews and further data analysis. As such the initial rounds of quantitative discourse analysis were used to inform the second rounds of qualitative analysis.The results from the qualitative interviews were again used to feed new concepts into the quantitative discourse analysis. As such the two methods continued to support and enrich each other. 

The ethnographic methods of the data collection and processing allowed the research group to acquire the data necessary to 'provide a holistic understanding of research participants' views and actions' {{Denzin}} that highlighted ongoing issues and case studies where protocols impact human rights. The interview participants were selected through purposive sampling {{Babbie}}, as the research group was interested in getting a wide variety of opinions on the role of human rights in guiding protocol development. This sampling method also ensured that individuals with extensive experience working at the IETF in various roles were targeted. The interviewees included individuals in leadership positions (Working Group (WG) chairs, Area Directors (ADs)), 'regular participants', individuals working for specific entities (corporate, civil society, political, academic) and represented various backgrounds, nationalities and genders.




Data Sources
------------

In order to map the potential relation between human rights and protocols, the HRPC research group gathered data from three specific sources:

### Discourse analysis of RFCs
To start addressing the issue, a mapping exercise analyzing Internet architecture and protocols features, vis-a-vis their possible impact on human rights was undertaken. Therefore, research on the language used in current and historic RFCs and mailing list discussions was undertaken to expose core architectural principles, language and deliberations on human rights of those affected by the network. This process continues, and the group keeps a living document of the RFCs and mailinglists it has been tracking.

### Interviews with members of the IETF community
Over 30 interviews with the current and past members of the Internet Architecture Board (IAB), current and past members of the Internet Engineering Steering Group (IESG) and chairs of selected working groups and RFC authors were done at the IETF92 Dallas meeting in March 2015. To get an insider understanding of how they view the relationship (if any) between human rights and protocols to play out in their work. Several of the participants opted to remain anonymous, if you are interested in this data set please contact the list.

### Participant observation in Working Groups
By participating in various working groups, in person at IETF meetings and on mailinglists, information was gathered about the IETFs day-to-day workings. From which general themes, technical concepts, and use-cases about human rights and protocols were extracted. This process started at the IETF91 meeting and continues today.


Data analysis strategies
------------------------

The data above was processed using three consecutive strategies: mapping protocols related to human rights, extracting concepts from these protocols, and creation of a common glossary (detailed under <xref target="vocabulary-used" />). Before going over these strategies some elaboration on the process of identifying technical concepts as they relate to human rights needs to be given:


### Identifying qualities of technical concepts that relate to human rights

#### Mapping protocols and standards related to human rights
By combining data from the three data sources named above, an extensive list of  protocols and standards that potentially enable the Internet as a tool for freedom of expression and association. In order to determine the enabling (or inhibiting) features we relied on direct references of such impact in the RFCs, as well as input from the community. On the basis of this analysis a list of RFCs that describe standards and protocols that are potentially closely related to human rights was compiled.

#### Extracting concepts from mapped RFCs
Mapping the protocols and standards that are related to human rights and create a human rights enabeling environment was the first step. For that we needed to focus on specific technical concepts that underlie these protocols and  standards. On the basis of this list a number of technical concepts that appeared frequently was extracted, and used to create a second list of technical terms that, when combined, create an enabling environment for excercising human rights on the Internet.

#### Building a common vocabulary of technical concepts that impact human rights
While interviewing experts, mapping RFCs and compiling technical definitions several concepts of convergence and divergence were identified. To ensure that the discussion was based on a common understanding of terms and vocabulary, a list of definitions was created. The definitions are based on the wording found in various IETF documents, and if these were unavailable definitions were taken from definitions from other Standards Developing Organizations or academic literature, as indicated in the vocabulary section.

#### Translating Human Rights Concepts into Technical Definitions
The previous steps allowed for the clarification of relation between human rights and technical concepts. The steps taken show how the research process zoomed in, from compiling a broad lists of protocols and standards that relate to human rights to extracting the precise technical concepts that make up these protocols and standards, in order to understand the relationship between the two. This sub-section presents the next step: translating human rights to technical concepts by matching the individuals components of the rights to the accompanying technical concepts, allowing for the creation of a list of technical concepts that when combined create an enabling environment for human rights.

#### List technical terms that combined create enabling environment for human rights
On the basis of the prior steps the following  list of  technical terms, that when combined create an enabling environment for human rights, such a freedom of expression and freedom of association, was drafted.

      Architectural principles                    Enabling features
        and characteristics                        for user rights

                       /------------------------------------------------\
                       |                                                |
     +=================|=============================+                  |
     =                 |                             =                  |
     =                 |           End to end        =                  |
     =                 |          Reliability        =                  |
     =                 |           Resilience        =  Access as       |
     =                 |        Interoperability     =   Human Right    |
     =    Good enough  |          Transparency       =                  |
     =     principle   |       Data minimization     =                  |
     =                 |  Permissionless innovation  =                  |
     =    Simplicity   |     Graceful degradation    =                  |
     =                 |          Connectivity       =                  |
     =                 |          Heterogeneity      =                  |
     =                 |                             =                  |
     =                 |                             =                  |
     =                 \------------------------------------------------/
     =                                               =
     +===============================================+

figure 1 - relation between architectural principles and enabling features for user rights.


### Translating human rights to technical terms

The combination of the technical concepts that have been gathered the steps above have been grouped according to their impact on specific rights as they have been mentioned in the interviews done at IETF92 as well as study of literature (see literature and discussion review above).

This analysis aims to assist protocol developers by better understanding the roles specific technical concepts with regards to their contribution to an enabeling environment for people to excise their human rights.

This analysis does not claim to be an complete or exhaustive mapping of all possible ways in which a protocols could potentially impact human rights, but it presents an initial concept mapping based on interviews and literature and discussion review.


     +-----------------------+-----------------------------------------+
     | Technical Concepts    | Rights potentially impacted             |
     +-----------------------+-----------------------------------------+
     | Connectivity          |                                         |
     | Privacy               |                                         |
     | Security              |                                         |
     | Content agnosticism   | Right to freedom of expression          |
     | Internationalization  |                                         |
     | Censorship resistance |                                         |
     | Open Standards        |                                         |
     | Heterogeneity support |                                         |
     +-----------------------+-----------------------------------------+
     | Anonymity             |                                         |
     | Privacy               |                                         |
     | Pseudonymity          | Right to non-discrimination             |
     | Accessibility         |                                         |
     +-----------------------+-----------------------------------------+
     | Content agnosticism   |                                         |
     | Security              | Right to equal protection               |
     +-----------------------+-----------------------------------------+
     | Accessibility         |                                         |
     | Internationalization  | Right to political participation        |
     | Censorship resistance |                                         |
     | Accessibility         |                                         |
     +-----------------------+-----------------------------------------+
     | Open standards        |                                         |
     | Localization          | Right to participate in cultural life,  |
     | Internationalization  |                  arts and science &     |
     | Censorship resistance | Right to education                      |
     | Accessibility         |                                         |
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
     |                       |                                         |
     +-----------------------+-----------------------------------------+

figure 2 - relation between specific technical concepts with regards to their contribution to an enabeling environment for people to excise their human rights

### Map cases of protocols that adversely impact human rights or are enablers thereof
Given the information above, the following list of cases of protocols that adversely impact or enable human rights was formed.

It is important to note that the assessment here is not a general judgment on these protocols. When they were conceived, there were many criteria to take into account. For instance, relying on an external server can be bad for freedom of speech (it creates one more control point, where censorship could be applied) but it may be a necessity if the endpoints are not connected and reachable permanently. So, when we say "protocol X has feature Y, which may endanger the freedom of speech", it does not mean that protocol X is bad and even less that its authors were evil. The goal here is to show, with actual examples, that the design of protocols have practical consequences for some human rights and these consequences have to be considered at design time.

#### IPv4

The Internet Protocol version 4 (IPv4), also known as 'layer 3' of the Internet, and specified as a common encapsulation and protocol header, is defined in {{RFC0791}}. The evolution of Internet communications led to continued development in this area, encapsulated in the development of version 6 (IPv6) of the protocol in {{RFC2460}}. In spite of this updated protocol, we find that 25 years after the specification of version 6 of the protocol, the older v4 standard continues to account for a sizeable majority of Internet traffic, and most of the issues discussed here (with the big exception of NAT, see Address Translation) are valid for IPv4 as well as IPv6.

The Internet was designed as a platform for free and open communication, most notably encoded in the end-to-end principle, and that philosophy is also present in the technical implementation of the Internet Protocol. {{RFC3724}} While the protocol was designed to exist in an environment where intelligence is at the end hosts, it has proven to provide sufficient information that a more intelligent network core can make policy decisions and enforce policy shaping and restricting the communications of end hosts. These capabilities for network control and limitations of the freedom of expression by end hosts can be traced back to the IPv4 design, helping us understand which technical protocol decisions have led to harm of this human rights.
A feature that can harm freedom of expression as well as the right to privacy through misuse of the Internet Protocol is the exploitation of the public visibility of the host pairs for all communications, and the corresponding ability to discriminate and block traffic as a result of that metadata. 

##### Network visibility of Source and Destination

The IPv4 protocol header contains fixed location fields for both the source and destination IP addresses {{RFC0791}}. These addresses identify both the host sending and receiving each message, and allow the core network to understand who is talking to whom, and to practically limit communication selectively between pairs of hosts. Blocking of communication based on the pair of source and destination is one of the most common limitations on the ability for people to communicate today, {{caida}} and can be seen as a restriction of the ability for people to assemble or to consensually express themselves.

Inclusion of an Internet-wide identified source in the IP header is not the only possible design, especially since the protocol is most commonly implemented over Ethernet networks exposing only link-local identifiers {{RFC0894}}. A variety of alternative designs including source routing, which would allow for the sender to choose a per defined (safe) route, and spoofing of the source IP address are technically supported by the protocol, but neither are considered good practice on the Internet {{Farrow}}. While projects like {{torproject}} provide an alternative implementation of anonymity in connections, they have been developed in spite of the IPv4 protocol design.

##### Address Translation and Mobility

A major structural shift in the Internet which undermined the protocol design of IPv4, and significantly reduced the freedom of end users to communicate and assemble is the introduction of network address translation. {{RFC1631}} Network address translation is a process whereby organizations and autonomous systems connect two networks by translating the IPv4 source and destination addresses between the two. This process puts the router performing the translation into a privileged position, where it can decide which subset of communications are worthy of translation, and whether an unknown request for communication will be correctly forwarded to a host on the other network.

This process of translation has widespread adoption despite promoting a process that goes against the stated end-to-end process of the underlying protocol {{natusage}}. In contrast, the proposed mechanism to provide support for mobility and forwarding to clients which may move, encoded instead as an option in the IP protocol in {{RFC5944}}, has failed to gain traction. In this situation the compromise made in the design of the protocol resulted in a technology that is not coherent with the end-to-end principles and thus creates and extra possible hurdle for freedom of expression in its design, even though a viable alternative that would do this exists. There is a particular problem surrounding NATs and VPN (as well as other connections used for privacy purposes) as they sometimes cause these not to work.


#### DNS

The Domain Name System (DNS) {{RFC1035}}, provides service discovery capabilities, and provides a mechanism to associate human readable names with services. The DNS system is organized around a set of independently operated 'Root Servers' run by organizations around the web which function in line with ICANN's policy by answering queries for which organizations have been delegated to manage registration under each Top Level Domain (TLD). The DNS is organized as a rooted tree, and this brings up political and social concerns over control.  Top Level domains are maintained and determined by ICANN. These namespaces encompass several classes of services. The initial name spaces including '.Com' and '.Net', provide common spaces for expression of ideas, though their policies are enacted through US based companies. Other name spaces are delegated to specific nationalities, and may impose limits designed to focus speech in those forums both to promote speech from that nationality, and to comply with local limits on expression and social norms. Finally, the system has recently been expanded with additional generic and sponsored name spaces, for instance '.travel' and '.ninja', which are operated by a range of organizations which may independently determine their registration policies. This new development has both positive and negative implications in terms of enabling human rights. Some individuals argue that it undermines the right to freedom of expression because some of these new gtlds have restricted policies on registration and particular rules on hate speech content. Others argue that precisely these properties are positive because they enable certain (mostly minority) communities to build safer spaces for association, thereby enabling their right to freedom of association. An often mentioned example is an application like .gay.

DNS has significant privacy issues per {{RFC7626}}. Most notable the lack of encryption to limit the visibility of requests for domain resolution from intermediary parties, and a limited deployment of DNSSEC to provide authentication, allowing the client to know that they received a correct, "authoritative", answer to a query. In response to the privacy issues, the IETF DNS PRIVate Exchange (DPRIVE) Working Group is developing mechanisms to provide confidentiality to DNS transactions, to address concerns surrounding pervasive monitoring {{RFC7258}}.

Authentication through DNSSEC creates a validation path for records. This authentication protects against forged or manipulated DNS data. As such DNSSEC protects the directory look-up and makes hijacking of a session harder. This is important because currently interference with the operation of the DNS is becoming one of the central mechanisms used to block access to websites. This interference limits both the freedom of expression of the publisher to offer their content, and the freedom of assembly for clients to congregate in a shared virtual space. Even though DNSSEC doesn't prevent censorship, it makes it clear that the returned information is not the information that was requested, which contributes to the right to security and increases trust in the network. It is however important to note that DNSSEC is currently  not widely supported or deployed by domain name registrars, making it difficult to authenticate and use correctly.

##### Removal of records

There have been a number of cases where the records for a domain are removed from the name system due to real-world events. Examples of this removal includes the 'seizure' of wikileaks {{bbc-wikileaks}} and the names of illegally operating gambling operations by the United States Immigrations and Customs Enforcement unit, which compelled the US-based registry in charge of the .com TLD to hand ownership of those domains over to the US government. The same technique has been used in Libya to remove sites in violation of "our Country's Law and Morality (which) do not allow any kind of pornography or its promotion." {{techyum}}

At a protocol level, there is no technical auditing for name ownership, as in alternate systems like {{namecoin}}. As a result, there is no ability for users to differentiate seizure from the legitimate transfer of name ownership, which is purely a policy decision of registrars. While DNSSEC addresses network distortion events described below, it does not tackle this problem.

(While mentioning alternative techniques, this is not a complete comparison of DNS with Namecoin: the latter has its own problems and limitations. The idea here is to show that there are several possible choices, and they have consequences for human rights.)

##### Distortion of records

The most common mechanism by which the DNS system is abused to limit freedom of expression is through manipulation of protocol messages by the network. One form occurs at an organizational level, where client computers are instructed to use a local DNS resolver controlled by the organization. The DNS resolver will then selectively distort responses rather than request the authoritative lookup from the upstream system. The second form occurs through the use of deep packet inspection, where all DNS protocol messages are inspected by the network, and objectionable content is distorted, as can be observed in Chinese network.

A notable instance of distortion occurred in Greece {{ververis}}, where a study found evidence of both of deep packet inspection to distort DNS replies, and overblocking of content. ISPs prevented clients from resolving the names of domains which they were instructed to do through a governmental order, prompting this particular blocking systems there.

At a protocol level, the effectiveness of these attacks is made possible by a lack of authentication in the DNS protocol. DNSSEC provides the ability to determine authenticity of responses when used, but it is not regularly checked by resolvers. DNSSEC is not effective when the local resolver for a network is complicit in the distortion, for instance when the resolver assigned for use by an ISP is the source of injection. Selective distortion of records is also been made possible by the predictable structure of DNS messages, which make it computationally easy for a network device to watch all passing messages even at high speeds, and the lack of encryption, which allows the network to distort only an objectionable subset of protocol messages. Specific distortion mechanisms are discussed further in {{hall}}.

Users can switch to another resolver, for instance a public one such as those operated by  Telecomix (http://dns.telecomix.org/). The distorter can then try to block or hijack the connection to this resolver. This may start an arm's race, the user switching to secured connections to this alternative resolver ({{RFC7858}}), the disruptor then trying to find more sophisticated ways to block or hijack. In some cases, this research to find an alternative, non-disrupting resolver, may lead to more centralisation, many people going to a few big commercial public resolvers.

##### Injection of records

Responding incorrectly to requests for name lookups is the most common mechanism that in-network devices use to limit the ability of end users to discover services. A deviation, which accomplishes a similar objective may be seen as different from a freedom of expression perspective, is the injection of incorrect responses to queries. The most prominent example of this behavior occurs in China, where requests for lookups of sites deemed inappropriate will trigger the network to respond with a false
response, causing the client to ignore the real response when it subsequently arrives. {{greatfirewall}} Unlike the other forms of discussion mentioned above, injection does not stifle the ability of a server to announce it's name, it instead provides another voice which answers sooner. This is effective because without DNSSEC, the protocol will respond to whichever answer is received first, without listening for subsequent answers.


#### HTTP

The Hypertext Transfer Protocol (HTTP), described in its version 1.1 in RFC 7230 to 7237, is a request-response application protocol developed throughout the 1990s, and factually contributed to the exponential growth of the Internet and the inter-connection of populations around the world. Its simple design strongly contributed to the fact that HTTP has become the foundation of most modern Internet platforms and communication systems, from websites, to chat systems, and computer-to-computer applications. In its manifestation with the World Wide Web, HTTP radically revolutionized the course of technological development and the ways people interact with online content and with each other.

However, HTTP is also a fundamentally insecure protocol, that doesn't natively provide encryption properties. While the definition of the Secure Sockets Layer (SSL) {{RFC6101}}, and later of Transport Layer Security (TLS){{RFC5246}}, also happened during the 1990s, the fact that HTTP doesn't mandate the use of such encryption layers to developers and service providers, was one of the reasons for a very late adoption of encryption. Only in the middle of the 2000s did we observed big Internet service providers, such as Google, starting to provide encrypted access to their web services.

The lack of sensitivity and understanding of the critical importance of securing web traffic incentivized certain (offensive) actors to develop, deploy and utilize at large interception systems and later active injection attacks, in order to swipe large amounts of data, compromise Internet-enabled devices. The commercial availability of systems and tools to perform these types of attacks also led to a number of human rights abuses that have been discovered and reported over the years.

Generally we can identify in Traffic Interception and Traffic Manipulation the two most problematic attacks that can be performed against applications employing a clear-text HTTP transport layer. That being said, the IETF is taking steady steps to move to the encrypted version of HTTP, HTTPSecure (HTTPS).

##### Traffic Interception

While we are seeing an increasing trend in the last couple of years to employ SSL/TLS as a secure traffic layer for HTTP-based applications, we are still far from seeing an ubiquitous use of encryption on the World Wide Web. It is important to consider that the adoption of SSL/TLS is also a relatively recent phenomena. E-mail providers such as riseup.net were the first ones to enable SSL by default. Google introduced an option for its GMail users to navigate with SSL only in 2008 {{Rideout}}, and turned TLS on by default later in 2010 {{Schillace}}. It took an increasing amount of security breaches and revelations on global surveillance from Edward Snowden to have other mail service providers to follow suit. For example, Yahoo enabled SSL/TLS by default on its webmail services only towards the end of 2013 {{Peterson}}.

TLS itself has been subject to many attacks and bugs which can be attributed to some fundamental design weaknesses such as lack of a state machine, which opens a vulnerability for a Triple Handshake Attack, and flaws caused by early U.S. government restrictions on cryptography, leading to cipher-suite downgrade attacks (Logjam attack). These vulnerabilities are being corrected in TLS1.3. {{Bhargavan}} {{Adrian}}

HTTP upgrading to HTTPS is also vulnerable to having an attacker remove the "S" in any links to HTTPS URIs from a web-page transferred in cleartext over HTTP, an attack called "SSL Stripping" {{sslstrip}}. Thus, for high security use of HTTPS IETF standards such as HSTS {{RFC6797}}, certificate pinning  {{RFC7469}} and/or DANE {{RFC6698}} should be used.

As we learned through the Snowden's revelations, intelligence agencies have been intercepting and collecting unencrypted traffic at large for many years. There are documented examples of such mass surveillance programs with GCHQ's TEMPORA {{WP-Tempora}} and NSA's XKEYSCORE {{Greenwald}}. Through these programs NSA/GCHQ have been able to swipe large amounts of data including email and instant messaging communications which have been transported by the respective providers in clear for years, unsuspecting of the pervasiveness and scale of governments' efforts and investment into global mass surveillance capabilities.

However, similar mass interception of unencrypted HTTP communications is also often employed at a nation-level by some democratic countries by exercising control over state-owned Internet Service Providers (ISP) and through the use of commercially available monitoring, collection, and censorship equipment. Over the last few years a lot of information has come to public attention on the role and scale of a surveillance industry dedicated to develop interception gear of different types, making use of known and unknown weaknesses in existing protocols {{RFC7258}}. We have several records of such equipment being sold and utilized by some regimes in order to monitor entire segments of population especially at times of social and political distress, uncovering massive human rights abuses. For example, in 2013 the group Telecomix revealed that the Syrian regime was making use of BlueCoat products in order to intercept clear-text traffic as well as to enforce censorship of unwanted content {{RSF}}. Similarly in 2012 it was found that the French Amesys provided the Gaddafi's government with equipment able to intercept emails, Facebook traffic, and chat messages at a country level {{WSJ}}. The use of such systems, especially in the context of the Arab Spring and of civil uprisings against the dictatorships, has caused serious concerns of significant human rights abuses in Libya.

##### Traffic Manipulation

The lack of a secure transport layer under HTTP connections not only exposes the users to interception of the content of their communications, but is more and more commonly abused as a vehicle for actively comprosing computers and mobile devices. If an HTTP session travels in the clear over the network, any node positioned at any point in the network is able to perform man-in-the-middle attacks and observe, manipulate, and hijack the session and modify the content of the communication in order to trigger unexpected behavior by the application generating the traffic. For example, in the case of a browser the attacker would be able to inject malicious code in order to exploit vulnerabilities in the browser or any of its plugins. Similarly, the attacker would be able to intercept, add malware, and repackage binary software updates that are very commonly downloaded in clear by applications such as word processors and media players. If the HTTP session would be encrypted, the tampering of the content would not be possible, and these network injection attacks would not be successful.

While traffic manipulation attacks have been long known, documented, and prototyped especially in the context of WiFi and LAN networks, in the last few years we observed an increasing investment into the production and sale of network injection equipment both available commercially as well as deployed at scale by intelligence agencies.

For example, we learned from some of the documents provided by Edward Snowden to the press, that the NSA has constructed a global network injection infrastructure, called QUANTUM, able to leverage mass surveillance in order to identify targets of interests and subsequently task man-on-the-side attacks to ultimately compromise a selected device. Among other attacks, NSA makes use of an attack called QUANTUMINSERT {{Haagsma}} which intercepts and hijacks an unencrypted HTTP communication and forces the requesting browser to redirect to a host controlled by NSA instead of the intended website. Normally, the new destination would be an exploitation service, referred in Snowden documents as FOXACID, which would attempt at executing malicious code in the context of the target's browser. The Guardian reported in 2013 that NSA has for example been using these techniques to target users of the popular anonymity service Tor {{Schneier}}. The German NDR reported in 2014 that NSA has also been using its mass surveillance capabilities to identify Tor users at large {{Appelbaum}}.

Recently similar capabilities of Chinese authorities have been reported as well in what has been informally called the "Great Cannon" {{Marcak}}, which raised numerous concerns on the potential curb on human rights and freedom of speech due to the increasing tighter control of Chinese Internet communications and access to information.

Network injection attacks are also made widely available to state actors around the world through the commercialization of similar, smaller scale equipment that can be easily acquired and deployed at a country-wide level. Certain companies are known to have network injection gear within their products portfolio {{Marquis-Boire}}. The technology devised and produced by some of them to perform network traffic manipulation attacks on HTTP communications is even the subject of a patent application in the United States {{Googlepatent}}. Access to offensive technologies available on the commercial lawful interception market has led to human rights abuses and illegitimate surveillance of journalists, human rights defenders, and political activists in many countries around the world {{Collins}}. While network injection attacks haven't been the subject of much attention, they do enable even unskilled attackers to perform silent and very resilient compromises, and unencrypted HTTP remains one of the main vehicles.

There is a new version of HTTP, called HTTP/2, which was published as {{RFC7540}} and which aimed to be largely backwards compatible but also offer new option such as data compression of HTTP headers and pipelining of request and multiplexing multiple requests over a single TCP connection. In addition to decreasing latency to improve page loading speeds it also facilitates more efficient use of connectivity in low-bandwith environments, which is an enabler for freedom of expression, the right to assembly, right to political participation and the right to participate in cultural life, art and science.
{{RFC7540}} does not mandate Transport Layer Security or any other form of encryption, is also does not support opportunistic encryption, so the vulnerabilities listed above for HTTP/1 are also valid for HTTP/2 as defined in {{RFC7540}}.

#### XMPP

The Extensible Messaging and Presence Protocol (XMPP), specified in {{RFC6120}}, provides a standard for interactive chat messaging, and has evolved to encompass interoperable text, voice, and video chat. The protocol is structured as a federated network of servers, similar to email, where users register with a local server which acts one their behalf to cache and relay messages. This protocol design has many advantages, allowing servers to shield clients from denial of service and other forms of retribution for their expression, and designed to avoid central entities which could control the ability to communicate or assemble using the protocol.

None-the-less, there are plenty of aspects of the protocol design of XMPP which shape the ability for users to communicate freely, and to assembly through the protocol. 

##### User Identification

The XMPP specification dictates that clients are identified with a resource (<node@domain/home> / <node@domain/work>) to distinguish the conversations to specific devices. While the protocol does not specify that the resource must be exposed by the client's server to remote users, in practice this has become the default behavior. In doing so, users can be tracked by remote friends and their servers, who are able to monitor presence not just of the user, but of each individual device the user logs in with. This has proven to be misleading to many users, {{pidgin}} since many clients only expose user level rather than device level presence. Likewise, user invisibility so that communication can occur while users don't notify all buddies and other servers of their availability is not part of the formal protocol, and has only been added as an extension within the XML stream rather than enforced by the protocol.

##### Surveillance of Communication

The XMPP protocol specifies the standard by which communication of channels may be encrypted, but it does not provide visibility to clients of whether their communications are encrypted on each link. In particular, even when both clients ensure that they have an encrypted connection to their XMPP server to ensure that their local network is unable to read or disrupt the messages they send, the protocol does not provide visibility into the encryption status between the two servers. As such, clients may be subject to selective disruption of communications by an intermediate network which disrupts communications based on keywords found through Deep Packet Inspection. While many operators have commited to only establishing encrypted links from their servers in recognition of this vulnerability, it remains impossible for users to audit this behavior and encrypted connections are not required by the protocol itself {{xmppmanifesto}}.

In particular, section 13.14 of the protocol specification {{RFC6120}} explicitly acknowledges the existence of a downgrade attack where an adversary controlling an intermediate network can force the inter domain federation between servers to revert to a non-encrypted protocol were selective messages can then be disrupted.

##### Group Chat Limitations

Group chat in the XMPP protocol is defined as an extension within the XML specification of the XMPP protocol (https://xmpp.org/extensions/xep-0045.html). However, it is not encoded or required at a protocol level, and not uniformly implemented by clients.

The design of multi-user chat in the XMPP protocol suffers from extending a protocol that was not designed with assembly of many users in mind. In particular, in the federated protocol provided by XMPP, multi-user communities are implemented with a distinguished 'owner', who is granted control over the participants and structure of the conversation.

Multi-user chat rooms are identified by a name specified on a specific server, so that while the overall protocol may be federated, the ability for users to assemble in a given community is moderated by a single server. That server may block the room and prevent assembly unilaterally, even between two users neither of whom trust or use that server directly.


#### Peer to Peer 

Peer-to-Peer (P2P) is a distribet network architecture in which all the participant nodes can be responsible for the storage and dissemination of information from any other node (defined in {{RFC7574}}, an IETF standard that used a P2P architecture). A P2P network is a logical overlay that lives on top of the physical network, and allows nodes (or "peers") participating to it to establish contact and exchange information directly from one to each other. The implementation of a P2P network may very widely: it may be structured or unstructured, and it may implement stronger or weaker cryptographic and anonymity properties. While its most common application has traditionally been file-sharing (and other types of content delivery systems), P2P is a popular architecture for networks and applications that require (or encourage) decentralization. A prime example is Bitcoin (and similar cryptocurrencies), as well as Bitcoin and proprietary multimedia applications.

In a time of heavily centralized online services, peer-to-peer is regularly described as an alternative, more democratic, and resistant option  that displaces structures of control over data and communications and delegates all peers equally to be responsible for the functioning, integrity, and security of the data. While in principle peer-to-peer remains imporant to the design and development of future content distribution, messaging, and publishing systems, it poses numerous security and privacy challenges which are mostly delegated to individual developers to recognize, analyze, and solve in each implementation of a given P2P network.

##### Network Poisoning

Since content, and in some occasions peer lists, are safeguarded and distributed by its members, P2P networks are prone to what are generally defined as "poisoning attacks". Poisoning attacks might be aimed directly at the data that is being distributed, for example by intentionally corrupting it, or at the index tables used to instruct the
peers where to fetch the data, or at routing tables, with the attempt of providing connecting peers with lists of rogue or non-existing peers, with the intention to effectively cause a Denial of Service on the network.

##### Throttling

Peer-to-Peer traffic (and BitTorrent in particular) represents a high percentage of global Internet traffic and it has become increasingly popular for Internet Service Providers to perform throttling of customers lines in order to limit bandwidth usage {{torrentfreak1}} and sometimes probably as an effect of the ongoing conflict between copyright holders and file-sharing communities {{wikileaks}}. Such throttling undermines the end-to-end principle.

Throttling the peer-to-peer traffic makes some uses of P2P networks ineffective and it might be coupled with stricter inspection of users' Internet traffic through Deep Packet Inspection techniques which might pose additional security and privacy risks.

##### Tracking and Identification

One of the fundamental and most problematic issues with traditional peer-to-peer networks is a complete lack of anonymization of its users. For example, in the case of BitTorrent, all peers' IP addresses are openly available to the other peers. This has lead to an ever-increasing tracking of peer-to-peer and file-sharing users {{ars}}. As the geographical
location of the user is directly exposed, and so could be his identity, the user might become target of additional harassment and attacks, being of physical or legal nature. For example, it is known that in Germany law firms have made extensive use of peer-to-peer and file-sharing tracking systems in order to identify downloaders and initiate legal actions looking for compensations {{torrentfreak2}}.

It is worth noting that there are varieties of P2P networks that implement cryptographic practices and that introduce anonymization of its users. Such implementations may be proved to be successful in resisting censorship of content, and tracking of the network peers. A primary example is FreeNet {{freenet1}}, a free software application designed to significantly increase the difficulty of users and content identification, and dedicated to foster freedom of speech online {{freenet2}}.

##### Sybil Attacks

In open-membership P2P networks, a single attacker can pretend to be many participants, typically by creating multiple fake identities of whatever kind the P2P network uses {{Douceur}}.  Attackers can use Sybil attacks to bias choices the P2P network makes collectively toward the attacker's advantage, e.g., by making it more likely that a particular data item (or some threshold of the replicas or shares of a data item) are assigned to attacker-controlled participants.  If the P2P network implements any voting, moderation, or peer review-like functionality, Sybil attacks may be used to "stuff the ballots" toward the attacker's benefit.  Companies and governments can use Sybil attacks on discussion-oriented P2P systems for "astroturfing" or creating the appearance of  mass grassroots support for some position where there is none in reality. It is important to know that there are no known complete, environmentally sustainable, and fully distributed solutions to Sybil attacks, and routing via 'friends' allows users to be de-anonymized via their social graph. It is important to note that Sybil attacks in this context (e.f. astroturfing) are relevant to more than P2P protocols. And are also common on web based systems, and exploited by governments and commercial entitities. 

Encrypted P2P and Anonymous P2P networks already emerged and provided viable platforms for sharing material {{tribler}}, publish content anonymously, and communicate securely {{bitmessage}}. These platforms are not perfect, and more research needs to be done.
If adopted at large, well-designed and resistant P2P networks might represent a critical component of a future secure and distributed Internet, enabling freedom of speech and freedom
of information at scale.


#### Virtual Private Network

The Virtual Private Networks (VPN) that are being discussed here are point-to-point connections that enables two computers to communicate over an encrypted tunnel. There are multiple implementations and protocols used in the deployment of VPNs, and they generally diversify by encryption protocol or particular requirements, most commonly in proprietary and enterprise solutions. VPNs are used commonly either to enable some devices to communicate through peculiar network configurations, or in order to use some privacy and security properties in order to protect the traffic generated by the end user; or both. VPNs have also become a very popular technology among human rights defenders, dissidents, and journalists worldwide to avoid local monitoring and eventually also to circumvent censorship. Among human rights defenders VPNs are often debated as a potential alternative to Tor or other anonymous networks. Such comparison is misleading, as some of the privacy and security properties of VPNs are often misunderstood by less tech-savvy users, which could ultimately lead to unintended problems.

As VPNs increased in popularity, commercial VPN providers have started growing in business and are very commonly picked by human rights defenders and people at risk, as they are normally provided with an easy-to-use service and sometimes even custom applications to establish the VPN tunnel. Not being able to control the configuration of the network, and even less so the security of the application, assessing the general privacy and security state of common VPNs is very hard. Often such services have been discovered leaking information, and their custom applications have been found flawed. While Tor and similar networks receive a lot of scrutiny from the public and the academic community, commercial or non-commercial VPN networks are way less analyzed and understood {{Insinuator}} {{Alshalanetal}} , and it might be valuable to establish some standards to guarantee a minimal level of privacy and security to those who need them the most.


##### No anonymity against VPN provider

One of the common misconception among users of VPNs is the level of anonymity VPN can provide. This sense of anonymity can be betrayed by a number of attacks or misconfigurations of the VPN provider. It is important to remember that, contrarily to Tor and similar systems, VPN was not designed to provide anonymity properties. From a technical point of view, the VPN might leak identifiable information, or might be subject of correlation attacks that could expose the originating address of the connecting user. Most importantly, it is vital to understand that commercial and non-commercial VPN providers are bound by the law of the jurisdiction they reside in or in which their infrastructure is located, and they might be legally forced to turn over data of specific users if legal investigations or intelligence requirements dictate so. In such cases, if the VPN providers retain logs, it is possible that the information of the user is provided to the user's adversary and leads to his or her identification.


##### Logging

With VPN being point-to-point connections, the service providers are in fact able to observe the original location of the connecting users and they are able to track at what time they started their session and eventually also to which destinations they're trying to connect to. If the VPN providers retain logs for long enough, they might be forced to turn over the relevant data or they might be otherwise compromised, leading to the same data getting exposed. A clear log retaining policy could be enforced, but considering that countries enforce very different levels of data retention policies, VPN providers would at least be transparent on what information do they store and for how long is being kept.


##### 3rd Party Hosting

VPN providers very commonly rely on 3rd parties to provision the infrastructure that is later going to be used to run VPN endpoints. For example, they might rely on external dedicated server hosting providers, or on uplink providers. In those cases, even if the VPN provider itself isn't retaining any significant logs, the information on the connecting users might be retained by those 3rd parties instead, introducing an additional collection point for the adversary.


##### IPv6 Leakage

Some studies proved that several commercial VPN providers and applications suffer of critical leakage of information through IPv6 due to improper support and configuration {{PETS2015VPN}}. This is generally caused by a lack of proper configuration of the client's IPv6 routing tables. Considering that most popular browsers and similar applications have been supporting IPv6 by default, if the host is provided with a functional IPv6 configuration, the traffic that is generated might be leaked if the VPN application isn't designed to manipulate such traffic properly.


##### DNS Leakage

Similarly, VPN services that aren't handling DNS requests and are not running DNS servers of their own, might be prone to DNS leaking which might not only expose sensitive information on the activity of the user, but could also potentially lead to DNS hijacking attacks and following compromises.


##### Traffic Correlation

Some implementations of VPN appear to be particularly vulnerable to identification and collection of key exchanges which, some Snowden documents revealed, are systematically collected and stored for future reference. The ability of an adversary to monitor network connections at many different points over the Internet, can allow them to perform traffic correlation attacks and identify the origin of certain VPN traffic by cross referencing the connection time of the user to the endpoint and the connection time of the endpoint to the final destination. These types of attacks, although very expensive and normally only performed by very resourceful adversaries, have been documented {{spiegel}} to be already in practice and could completely vanify the use of a VPN and ultimately expose the activity and the identity of a user at risk.


#### HTTP Status Code 451

Every Internet user has run into the '404 Not Found' Hypertext Transfer Protocol (HTTP) status code when trying, and failing, to access a particular website {{Cath}}. It is a response status that the server sends to the browser, when the server cannot locate the URL. '403 Forbidden' is another example of this class of code signals that gives users information about what is going on. In the '403' case the server can be reached, but is blocking the request because the user is trying to access content forbidden to them. This can be because the specific user is not allowed access to the content (like a government employee trying to access pornography on a work-computer) or because access is restricted to all users (like social network sites in certain countries).
As surveillance and censorship of the Internet is becoming more commonplace, voices were raised at the IETF to introduce a new status code that indicates when something is not available for 'legal reasons' (like censorship):

The 451 status code would allow server operators to operate with greater transparency in circumstances where issues of law or public policy affect their operation. This transparency may be beneficial both to these operators and to end-users {{Bray}}.

The status code is named '451', a reference to Bradbury's famous novel on censorship, and the temperature (in Fahrenheit) at which bookpaper autoignites. 

During the IETF92 meeting in Dallas, there was discussion about the usefulness of '451'. The main tension revolved around the lack of an apparent machine-readable technical use of the information. The extent to which '451' is just 'political theatre' or whether it has a concrete technical use was heatedly debated. Some argued that 'the 451 status code is just a status code with a response body' others said it was problematic because 'it brings law into the picture'. Again others argued that it would be useful for individuals, or organizations like the 'Chilling Effects' project, crawling the web to get an indication of censorship (IETF discussion on '451' - author's field notes March 2015). There was no outright objection during the Dallas meeting against moving forward on status code '451', and on December 18, 2015 the Internet Engineering Steering Group approved publication of 'An HTTP Status Code to Report Legal Obstacles'. It is now an IETF approved HTTP status code to signal when resource access is denied as a consequence of legal demands {{RFC7725}}.

What is interesting about this particular case is that not only technical arguments but also the status code's outright potential political use for civil society played a substantial role in shaping the discussion, and the decision to move forward with this technology.

It is nonetheless important to note that HTTP status code 451 is not a solution to detect all occasions of censorship. A large swath of Internet filtering occurs in the network rather than the server itself. For these forms of censorship 451 plays a limited role, as the servers will not be able to send the code, because they haven't received the requests (as is the case with servers with resources blocked by the Chinese Golden shield). Such filtering regimes are unlikely to voluntarily inject a 451 status code. The use of 451 is most likely to apply in the case of cooperative, legal versions of content removal resulting from requests to providers. One can think of content that is removed or blocked for legal reasons, like copyright infringement, gambling laws, child abuse, et cetera. Large Internet companies and search engines are constantly asked to censor content in various jurisdictions. 451 allows this to be easily discovered, for instance by initiatives like the Lumen Database. 

Overall, the strength of 451 lies in its ability to provide transparency by giving the reason for blocking, and giving the end-user the ability to file a complaint. It allows organizations to easily measure censorship in an automated way, and prompts the user to access the content via another path (e.g. TOR, VPNs) when (s)he encounters the 451 status code.

Status code 451 impact human rights by making censorship more transparent and measurable. The status code increases transparency both by signaling the existence of censorship (instead of a much more broad HTTP error message like HTTP status code 404) as well as providing details of the legal restriction, which legal authority is imposing it, and what class of resources it applies to. This empowers the user to seek redress.

#### DDoS attacks
Many individuals, not excluding IETF engineers, have argued that DDoS attacks are fundamentally against freedom of expression. Technically DDoS attacks are when one or multiple host overload the bandwidth or resources of another host by flooding it with traffic or making resource intensive requests, causing it to temporarily stop being available to users. One can roughly differentiate three types of DDoS attacks: Volume Based Attacked (This attack aims to make the host unreachable by using up all it's bandwith, often used techniques are: UDP floods and ICMP floods), Protocol Attacks (This attacks aims to use up actual server resources, often used techniques are SYN floods, fragmented packet attacks, and Ping of Death {{RFC4949}}) and Application Layer Attacks (this attack aims to bring down a server, such as the webserver).

DDoS attacks can thus stifle freedom of expression, complicate the ability of independent media and human rights organizations to exercise their right to (online) freedom of association, while facilitating the ability of governments to censor dissent.  When it comes to comparing DDoS attacks to protests in offline life, it is important to remember that only a limited number of DDoS attacks involved solely willing participants. In most cases, the clients are hacked computers of unrelated parties that have not consented to being part of a DDoS (for exceptions see Operation Abibil {{Abibil}} or the Iranian Green Movement DDoS {{GreenMovement}}). In addition, DDoS attacks are increasingly used as an extortion tactic.

All of these issues seem to suggest that the IETF should try to ensure that their protocols cannot be used for DDoS attacks, which is consistent with the long-standing IETF consensus that DDoS is an attack that protocols should mitigate them to the extent they can {{BCP72}}. Decreasing the number of vulnerabilities in protocols and (outside of IETF) the number of bugs in the network stacks of routers or computers could address this issue. The IETF can clearly play a role in bringing about some of these changes but the IETF cannot be expected to take a positive stance on (specific) DDoS attacks, or create protocols to enable some attacks and inhibit others. What the IETF can do is critically reflect on its role in the development of the Internet, and how this impacts the ability of people to excercise their human rights, such as freedom of expression.


Model for developing human rights protocol considerations
---------------------------------------------------------

In the previous steps we have established that human rights relate to standards and protocols and offered a common vocabulary of technical concepts that impact human rights and how these technical concept can be combined to ensure that the Internet remains an enabling environment for human rights. With this the contours of a model for developing human rights protocol considerations has taken shape. This subsection provides the last step by detailing how specific technical concepts identified above relate to human rights, and what questions engineers should ask themselves when developing or improving protocols. In short, it presents a set of human rights protocol considerations.


### Human rights threats
Human rights threats on the Internet come in a myriad of forms. Protocols and standards can harm or enable the right to freedom of expression, right to non-discrimination, right to equal protection, right to participate in cultural life, arts and science, right to freedom of assembly and association, and the right to security. An end-user who is denied access to certain services, data or websites may be unable to disclose vital information about the malpractices of a government or other authority. A person whose communications are monitored may be prevented from exercising their right to freedom of association or participate in political processes {{Penney}}. In a worst-case scenario, protocols that leak information can lead to physical danger. A realistic example to consider is when opposition group members (or those identified as such) in totalitarian regimes are subjected to torture on the basis of information gathered by the regime through information leakage in protocols.

This sections details several 'common' threats to human rights, indicating how each of these can lead to human rights violations/harms and present several examples of how these threats to human rights materialize on the Internet. This threat modeling is inspired by {{RFC6973}} Privacy Considerations for Internet Protocols, which is based on the security threat analysis. This method is by no means a perfect solution for assessing human rights risks in Internet protocols and systems; it is however the best approach currently available. Certain specific human rights threats are indirectly considered in Internet protocols as part of the security considerations {{BCP72}}, but privacy guidelines {{RFC6973}} or reviews, let alone human rights impact assessments of protocols are not standardized or implemented. 

Many threats, enablers and risks are linked to different rights. This is not unsurprising if one takes into account that human rights are interrelated, interdependent and indivisible. Here however we're not discussing all human rights because not all human rights are relevant to ICTs in general and protocols and standards in particular {{Bless}}. This is by no means an attempt to exclude specific rights or proritize some rights over others, if other rights seem relevant, please contact the research group mailinglist.

### Guidelines for human rights considerations
This section provides guidance for document authors in the form of a questionnaire about protocols and their (potential) impact. The questionnaire may be useful at any point in the design process, particularly after document authors have developed a high-level protocol model as described in {{RFC4101}}.

Protocols and Internet Standard might benefit from a documented discussion of potential human rights risks arising from potential misapplications of the protocol or technology described in the RFC. This might be coupled with an Applicability Statement for that RFC.

Note that the guidance provided in this section does not recommend specific practices. The range of protocols developed in the IETF is too broad to make recommendations about particular uses of data or how human rights might be balanced against other design goals.  However, by carefully considering the answers to the following questions, document authors should be able to produce a comprehensive analysis that can serve as the basis for discussion on whether the protocol adequately protects against specific human rights threats.  This guidance is meant to help the thought process of a human rights analysis; it does not provide specific directions for how to write a human rights protocol considerations section (following the example set in {{RFC6973}}), and the addition of a human rights protocol considerations section has also not yet been proposed. 


#### Technical concepts as they relate to human rights

##### Connectivity
Question(s):
Does your protocol add application-specific functions to intermediary nodes? Could this functionality be added to end nodes instead of intermediary nodes?

Explanation:
The end-to-end principle {{Saltzer}} which aims to extend characteristics of a protocol or system as far as possible within the system, or in other words 'the intelligence is end to end rather than hidden in the network' {{RFC1958}}. Middleboxes (which can be Content Delivery Networks, Firewalls, NATs or other intermediary nodes that provide other 'services' than routing), and the protocols guiding them, influence individuals' ability to communicate online freely and privately. The potential for abuse and intentional and unintentional censoring and limiting permissionless innovation, and thus ultimately the impact of middleboxes on the Internet as a place of unfiltered, unmonitored freedom of speech, is real.

Example:
End-to-end instant message encryption would conceal the content of communications from one user's instant messaging application through any intermediate devices and servers all the way to the recipient's instant messaging application. If the message was decrypted at any intermediate point--for example at a service provider--then the property of end-to-end encryption would not be present.

Impacts:

- Right to freedom of expression
- Right to freedom of assembly and association

##### Privacy

Question(s):
Did you have a look at the Guidelines in the Privacy Considerations for Internet Protocols {{RFC6973}} section 7? Could your protocol in any way impact the confidentiality of protocol metadata? Could your protocol counter traffic analysis? Could you protocol improve data minimization?  Does your document identify potentially sensitive logged data by your protocol and/or for how long that needs to be retained for technical reasons?

Explanation:
Privacy refers to the right of an entity (normally a person), acting in its own behalf, to determine the degree to which it will interact with its environment, including the degree to which the entity is willing to share its personal information with others. {{RFC4949}}. If a protocol provides insufficient privacy it may stifle speech as users self-censor for fear of surveillance, or find themselves unable to express themselves freely.

Example:
See {{RFC6973}}

Impacts:

- Right to freedom of expression
- Right to non-discrimination

##### Content agnosticism

Question(s):
If your protocol impacts packet handling, does it look at the packet payload? Does it look at Is it making decisions based on the payload of the packet? Does your protocol prioritize certain content or services over others in the routing process ? Is the protocol transparent about the priotization that is made (if any)?

Explanation:
Content agnosticism refers to the notion that network traffic is treated identically regardless of content.

Example:
Content agnosticism prevents content-based discrimination against packets. This is important because changes to this principle can lead to a two-tiered Internet, where certain packets are prioritized over others on the basis of their content. Effectively this would mean that although all users are entitled to receive their packets at a certain speed, some users become more equal than others.

Impacts:

- Right to freedom of expression
- Right to non-discrimination
- Right to equal protection

##### Security
Question(s):
Did you have a look at Guidelines for Writing RFC Text on Security Considerations {{BCP72}}? Have you found any attacks that are out of scope for your protocol? Would these attacks be pertinent to the human rights enabling features of the Internet (as descibred throughout this document)?

Explanation:
Most people speak of security as if it were a single monolithic property of a protocol or system, however, upon reflection; one realizes that it is clearly not true. Rather, security is a series of related but somewhat independent properties. Not all of these properties are required for every application. Since communications are carried out by systems and access to systems is through communications channels, these goals obviously interlock, but they can also be independently provided {{BCP72}}.

Example:
See {{BCP72}}.

Impacts:

- Right to freedom of expression
- Right to freedom of assembly and association
- Right to non discrimination

##### Internationalization
Question(s):
Does your protocol have text strings that have to be understood or entered by humans? Does your protocol allow Unicode encoded in UTF-8 only? If other character sets or encodings are allowed, does your protocol mandate a proper tagging of the charset? Did you have a look at {{RFC6365}}?

Explanation:
Internationalization refers to the practice of making protocols, standards, and implementations usable in different languages and scripts.  (see Localization). In the IETF, internationalization means to add or improve the handling of non-ASCII text in a protocol. {{RFC6365}} A different perspective, more appropriate to protocols that are designed for global use from the beginning, is the definition used by W3C:

         "Internationalization is the design and development of a
         product, application or document content that enables easy
         localization for target audiences that vary in culture, region,
         or language."  {{W3Ci18nDef}}

Many protocols that handle text only handle one charset (US-ASCII), or leave the question of what CCS and encoding are used up to local guesswork (which leads, of course, to interoperability problems).  If multiple charsets are permitted, they must be explicitly identified {{RFC2277}}.  Adding non-ASCII text to a protocol allows the protocol to handle more scripts, hopefully representing users across the world.  In today's world, that is normally best accomplished by allowing Unicode encoded in UTF-8 only.

Example:
See localization
Impacts:

- Right to freedom of expression
- Right to political participation
- Right to participate in cultural life, arts and science
- Right to political participation

##### Censorship resistance
Question(s):
Does this protocol introduce new identifiers or reuse existing identifiers (e.g. MAC addresses) that might be associated with persons or content? Does your protocol make it apparent or transparent when filtering happens? Can your protocol contribute to filtering in a way it could be implemented to censor data or services? Could this be designed to ensure this doesn't happen?

Explanation:
Censorship resistance refers to the methods and measures to prevent Internet censorship.

Example:
Identifiers of content exposed within a protocol might be used to facilitate censorship, as in the case of IP based censorship, which affects protocols like HTTP. Filtering can be made apparent by the use of status code 451 - which allows server operators to operate with greater transparency in circumstances where issues of law or public policy affect their operation {{Bray}}.

Impacts:

- Right to freedom of expression
- Right to political participation
- Right to participate in cultural life, arts and science
- Right to freedom of assembly and association

##### Open Standards
Question(s):
Is your protocol fully documented in a way that it could be easily implemented, improved, build upon and/or further developed? Do you depend on proprietary code for the implementation, running or further development of your protocol? Does your protocol favor a particular proprietary specification over technically equivalent and competing specification(s), for instance by making any incorporated vendor specification  "required" or "recommended" {{RFC2026}}? Do you normatively reference another standard that is not available without cost? Are you aware of any patents that would prevent your standard from being fully implemented {{RFC3979}} {{RFC6701}}?

Explanation:
The Internet was able to developed into the global network of networks because of the existence of open, non-proprietary standards {{Zittrain}}. They are crucial for enabling interoperability. Yet, open standards are not explicitly defined within the IETF. On the subject, {{RFC2606}} states: Various national and international standards bodies, such as ANSI, ISO, IEEE, and ITU-T, develop a variety of protocol and service specifications that are similar to Technical Specifications defined at the IETF.  National and international groups also publish "implementors' agreements" that are analogous to Applicability Statements, capturing a body of implementation-specific detail concerned with the practical application of their standards.  All of these are considered to be "open external standards" for the purposes of the Internet Standards Process. 
Similarly, {{RFC3935}} does not define open standards but does emphasize the importance of ‘open process’: any interested person can participate in the work, know what is being decided, and make his or her voice heard on the issue. Part of this principle is the IETF’s commitment to making its documents, WG mailing lists, attendance lists, and meeting minutes publicly available on the Internet.

Open standards are important as they allow for permissionless innovation, which is important to maintain the freedom and ability to freely create and deploy new protocols on top of the communications constructs that currently exist. It is at the heart of the Internet as we know it, and to maintain its fundamentally open nature, we need to be mindful of the need for developing open standards.

All standards that need to be normatively implemented should be freely available and with reasonable protection for patent infringement claims, so it can also be implemented in open source or free software. Patents have often held back open standardization or been used against those deploying open stadards, particularly in the domain of cryptography {{newegg}}.
Patents in open standards or in normative references to other standards should have a patent disclosure {{notewell}}, royalty-free licensing {{patentpolicy}}, or some other form of reasonable protection. Reasonable patent protection should includes but is not limited to cryptographic primitives.

Example:
{{RFC6108}} describes a system for providing critical end-user notifications to web browsers, which has been deployed by Comcast, an Internet Service Provider (ISP).  Such a notification system is being used to provide near-immediate notifications to customers, such as to warn them that their traffic exhibits patterns that are indicative of malware or virus infection. There are other proprietary systems that can perform such notifications, but those systems utilize Deep Packet Inspection (DPI) technology.  In contrast to DPI, this document describes a system that does not rely upon DPI, and is instead based in open IETF standards and open source applications.

Impacts:

- Right to freedom of expression
- Right to participate in cultural life, arts and science

##### Heterogeneity Support
Question(s):
Does your protocol support heterogeneity by design? Does your protocol allow for multiple types of hardware? Does your protocol allow for multiple types of application protocols? Is your protocol liberal in what it receives and handles? Will it remain usable and open if the context changes? Does your protocol allow there to be well-defined extension points? Do these extension points to allow open innovation possibly have security and privacy ramifications, and if so,how can these be dealt with?

Explanation:
The Internet is characterized by heterogeneity on many levels: devices and nodes, router scheduling algorithms and queue management mechanisms, routing protocols, levels of multiplexing, protocol versions and implementations, underlying link layers (e.g., point-to-point, multi-access links, wireless, FDDI, etc.), in the traffic mix and in the levels of congestion at different times and places. Moreover, as the Internet is composed of autonomous organizations and Internet service providers, each with their own separate policy concerns, there is a large heterogeneity of administrative domains and pricing structures. As a result, the heterogeneity principle proposed in {{RFC1958}} needs to be supported by design {{FIArch}}.

Example:
Heterogeneity is inevitable and needs be supported by design. Multiple types of hardware must be allowed for, e.g. transmission speeds differing by at least 7 orders of magnitude, various computer word lengths, and hosts ranging from memory-starved microprocessors up to massively parallel supercomputers. Multiple types of    application protocol must be allowed for, ranging from the simplest such as remote login up to the most complex such as distributed databases {{RFC1958}}.

Impacts:

- Right to freedom of expression
- Right to security

##### Anonymity
Question(s):
Did you have a look at the Privacy Considerations for Internet Protocols {{RFC6973}}, especially section 6.1.1 ?

Explanation:
Anonymity refers to the condition of an identity being unknown or concealed {{RFC4949}}. It is an important feature for many end-users, as it allows them different degrees of privacy online.

Example:
Often standards expose private information, it is important to consider ways to mitigate the obvious privacy impacts. For instance, a feature which uses deep packet inspection or geolocation data could refuse to open this data to third parties, that might be able to connect the data to a physical person.

Impacts:

- Right to non-discrimination
- Right to political participation
- Right to freedom of assembly and association
- Right to security

##### Pseudonymity
Question(s):
Have you considered the Privacy Considerations for Internet Protocols {{RFC6973}}, especially section 6.1.2 ? Does this specification collect personally derived data?  Does the protocol generates or processes anything that can be, or be tightly correlated with, personally identifiable information? Does the standard utilize data that is personally-derived, i.e. derived from the interaction of a single person, or their device or address? Does this specification generate personally derived data, and if so how will that data be handled?

Explanation:
Pseudonymity - the ability to disguise one's identity online - is an important feature for many end-users, as it allows them different degrees of disguised identity and privacy online.

Example:
Designing a standard that exposes private information, it is important to consider ways to mitigate the obvious impacts. For instance, a feature which uses deep packet inspection or geolocation data could refuse to open this data to third parties, that might be able to connect the data to a physical person.

Impacts:

- Right to non-discrimination
- Right to freedom of assembly and association

##### Accessibility

Question(s):
Is your protocol designed to provide an enabling environment for people who are not able-bodied? Have you looked at the W3C Web Accessibility Initiative for examples and guidance? Is your protocol optimized for low bandwidth and high latency connections? Could your protocol also be developed in a stateless manner?

Explanation:
The Internet is fundamentally designed to work for all people, whatever their hardware, software, language, culture, location, or physical or mental ability. When the Internet meets this goal, it is accessible to people with a diverse range of hearing, movement, sight, and cognitive ability {{W3CAccessibility}}. Sometimes in the design of protocols, websites, web technologies, or web tools, barriers are created that exclude people from using the Web.

Example:
The HTML protocol as defined in {{HTML5}} specifically requires that every image must have an alt attribute (with a few exceptions) to ensure images are accessible for people that cannot themselves decipher non-text content in web pages.

Impacts:

- Right to non-discrimination
- Right to freedom of assembly and association
- Right to education
- Right to political participation

##### Localization

Question(s):
Does your protocol uphold the standards of internationalization? Have made any concrete  steps towards localizing your protocol for relevant audiences?

Explanation:
Localization refers to the adaptation of a product, application or document content to meet the language, cultural and other requirements of a specific target market (a locale) {{W3Ci18nDef}}. It is also described as the practice of translating an implementation to make it functional in a specific language or for users in a specific locale (see Internationalization).

Example:
The Internet is a global medium, but many of its protocols and products are developed with a certain audience in mind, that often share particular characteristics like knowing how to read and write in ASCII and knowing English. This limits the ability of a large part of the world's online population from using the Internet in a way that is culturally and linguistically accessible. An example of a protocol that has taken into account the view that individuals like to have access to data in their native language can be found in {{RFC1766}}. This protocol labels the information content with an identifier for the language in which it is written. And this allows information to be presented in more than one language.

Impacts:

- Right to non-discrimination
- Right to participate in cultural life, arts and science
- Right to Freedom of Expression



##### Decentralization
Question(s):
Can your protocol be implemented without one single point of control? If applicable, can your protocol be deployed in a federated manner? What is the potential for discrimination against users of your protocol? How can the use of your protocol be used to implicate users? Does your protocol create additional centralized points of control?

Explanation:
Decentralization is one of the central technical concepts of the architecture, and embraced as such by the IETF {{RFC3935}}. It refers to the absence or minimization of centralized points of control; a feature that is assumed to make it easy for new users to join and new uses to unfold {{Brown}}. It also reduces issues surrounding single points of failure, and distributes the network such that it continues to function if one or several nodes are disabled. With the commercialization of the Internet in the early 1990's there has been a slow move to move away from decentralization, to the detriment of the technical benefits of having a decentralized Internet.

Example:
The bits traveling the Internet are increasingly susceptible to monitoring and censorship, from both governments and Internet service providers, as well as third (malicious) parties. The ability to monitor and censor is further enabled by the increased centralization of the network that creates central infrastructure points that can be tapped in to. The creation of peer-to-peer networks and the development of voice-over-IP protocols using peer-to-peer technology in combination with distributed hash table (DHT) for scalability are examples of how protocols can preserve decentralization {{Pouwelse}}.

Impacts:

- Right to freedom of assembly and association

##### Reliability

Question(s):
Is your protocol fault tolerant? Does it degrade gracefully? Do you have a documented way to announce degradation? Do you have measures in place for recovery or partial healing from failure? Can your protocol maintain dependability and performance in the face of unanticipated changes or circumstances?

Explanation:
Reliability ensures that a protocol will execute its function consistently and error resistant as described, and function without unexpected result. A system that is reliable degenerates gracefully and will have a documented way to announce degradation.  It also has mechanisms to recover from failure gracefully, and if applicable, allow for partial healing. As with confidentiality, the growth of the Internet and fostering innovation in services depends on users having confidence and trust {{RFC3724}} in the network. For reliability it is necessary that services notify the users if a delivery fails. In the case of real-time systems in addition to the reliable delivery the protocol needs to safeguard timeliness.

Example:
In the modern IP stack structure, a reliable transport layer requires an indication that transport processing has successfully completed, such as given by TCP's ACK message {{RFC0793}}, and not simply an indication from the IP layer that the packet arrived.  Similarly, an application layer protocol may require an application-specific acknowledgement that contains, among other things, a status code indicating the disposition of the request (See {{RFC3724}}).

Impacts:

- Right to security

##### Confidentiality

Question(s):
Does this protocol expose information related to identifiers or data? If so, does it do so to each other protocol entity (i.e., recipients, intermediaries, and enablers) {{RFC6973}}? What options exist for protocol implementers to choose to limit the information shared with each entity? What operational controls are available to limit the information shared with each entity?

What controls or consent mechanisms does the protocol define or require before personal data or identifiers are shared or exposed via the protocol?  If no such mechanisms or controls are specified, is it expected that control and consent will be handled outside of the protocol?

Does the protocol provide ways for initiators to share different pieces of information with different recipients?  If not, are there mechanisms that exist outside of the protocol to provide initiators with such control?

Does the protocol provide ways for initiators to limit which information is shared with intermediaries?  If not, are there mechanisms that exist outside of the protocol to provide users with such control?  Is it expected that users will have relationships that govern the use of the information (contractual or otherwise) with those who operate these intermediaries? Does the protocol prefer encryption over clear text operation?

Does the protocol provide ways for initiators to express individuals' preferences to recipients or intermediaries with regard to the collection, use, or disclosure of their personal data?

Explanation:
Confidentiality refers to keeping your data secret from unintended listeners {{BCP72}}. The growth of the Internet depends on users having confidence that the network protects their private information {{RFC1984}}.

Example:
Protocols that do not encrypt their payload make the entire content of the communication available to the idealized attacker along their path. Following the advice in {{RFC3365}}, most such protocols have a secure variant that encrypts the payload for confidentiality, and these secure variants are seeing ever-wider deployment. A noteworthy exception is DNS {{RFC1035}}, as DNSSEC {{RFC4033}}does not have confidentiality as a requirement.  This implies that, in the absence of changes to the protocol as presently under development in the IETF's DNS Private Exchange   (DPRIVE) working group, all DNS queries and answers generated by the activities of any protocol are available to the attacker.  When store-and-forward protocols are used (e.g., SMTP {{RFC5321}}), intermediaries leave this data subject to observation by an attacker that has compromised these intermediaries, unless the data is    encrypted end-to-end by the application-layer protocol or the implementation uses an encrypted store for this data {{RFC7624}}.


Impacts:

- Right to security

##### Integrity
Question(s):
Does your protocol maintain and assure the accuracy of data? Does your protocol maintain and assure the consistency of data? Does your protocol in any way allow for the data to be (intentionally or unintentionally) altered?

Explanation:
Integrity refers to the maintenance and assurance of the accuracy and consistency of data to ensure it has not been (intentionally or unintentionally) altered.

Example:
See authenticity

Impacts:

- Right to security

##### Authenticity
Question(s):
Do you have sufficient measures to confirm the truth of an attribute of a single piece of data or entity? Can the attributes get garbled along the way (see security)? If relevant have you implemented IPsec, DNSsec, HTTPS and other Standard Security Best Practices?

Explanation:
Authenticity ensures that data does indeed come from the source it claims to come from. This is important to prevent attacks or unauthorized access and use of data.

Example:
Authentication of data is important to prevent vulnerabilities and attacks, like man-in-the-middle-attacks. These attacks happen when a third party (often for malicious reasons) intercepts a communication between two parties, inserting themselves in the middle and posing as both parties. In practice this looks as follows:

Alice wants to communicate with Bob.  
Alice sends data to Bob.  
Corinne intercepts the data sent to Bob.  
Corinne reads and alters the message to Bob.  
Bob cannot see the data did not come from Alice but from Corinne.  
Corinne intercepts and alters the communication as it is sent between Alice and Bob.  
Corinne knows all.

Impacts:

- Right to security

##### Adaptability
Question(s):
Is your protocol written in such a way that is would be easy for other protocols to be developed on top of it, or to interact with it? Does your protocol impact permissionless innovation? See 'Connectivity' above.

Explanation:
Adaptability is closely interrelated permissionless innovation, both maintain the freedom and ability to freely create and deploy new protocols on top of the communications constructs that currently exist. It is at the heart of the Internet as we know it, and to maintain its fundamentally open nature, we need to be mindful of the impact of protocols on maintaining or reducing permissionless innovation to ensure the Internet can continue to develop.

Example:
WebRTC generates audio and/or video data. In order to ensure that WebRTC can be used in different locations by different parties it is important that standard Javascript APIs are developed to support applications from different voice service providers. Multiple parties will have similar capabilities, in order to ensure that all parties can build upon existing standards these need to be adaptable, and allow for permissionless innovation.

Impacts:

- Right to education
- Freedom of expression
- Freedom of assembly and association


Acknowledgements
================
A special thanks to all members of the hrpc RG who contributed to this draft. The following deserve a special mention:

- Joana Varon for helping draft the first iteration of the methodology, previous drafts and the direction of the film Net of Rights and working on the interviews at IETF92 in Dallas.

- Daniel Kahn Gillmor (dkg) for helping with the first iteration of the glossary as well as a lot of technical guidance, support and language suggestions.

- Claudio Guarnieri for writing the first iterations of the case studies on VPN, HTTP, and Peer to Peer.

- Will Scott for writing the first iterations of the case studies on DNS, IP, XMPP.

- Avri Doria for proposing writing a glossary in the first place, help writing the initial proposals and Internet Drafts and contributing to the glossary.

and Stephane Bortzmeyer, John Curran, Barry Shein, Joe Hall, Joss Wright, Harry Halpin, and Tim Sammut who made a lot of excellent suggestions, many of which found their way directly into the text. We want to thank Stephane Bortzemeyer, Shane Kerr, Giovane Moura, James Gannon, and Scott Craig for their reviews and testing the HRPC guidelines in the wild.
We would also like to thank Molly Sauter, Arturo Filasto, Nathalie Marechal, Eleanor Saitta and all others who provided input on the draft or the conceptualization of the idea.

Security Considerations
=======================
As this document concerns a research document, there are no security considerations.

IANA Considerations
===================
This document has no actions for IANA.

Research Group Information
==========================
The discussion list for the IRTF Human Rights Protocol Considerations proposed working group is located at the e-mail address <hrpc@ietf.org>. Information on the group and information on how to subscribe to the list is at
<https://www.irtf.org/mailman/listinfo/hrpc>

Archives of the list can be found at:
<https://www.irtf.org/mail-archive/web/hrpc/current/index.html>

