# Created by: Piotr Smyrak <smyru@heron.pl> and
# $FreeBSD$

PORTNAME=	libtlen
PORTVERSION=	20041113
CATEGORIES=	polish net
MASTER_SITES=	SF/${PORTNAME}/${PORTNAME}/${PORTNAME}-${PORTVERSION}

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Backend for interoperability with Tlen.pl, Polish IM network

GNU_CONFIGURE=	yes
USE_LDCONFIG=	yes
NO_STAGE=	yes

.if !defined(NOPORTDOCS)
post-install:
	@${MKDIR} ${DOCSDIR}
.for f in libtlen.html libtlen.css AUTHORS TODO
	@${INSTALL_DATA} ${WRKSRC}/docs/${f} ${DOCSDIR}
.endfor
.endif

.include <bsd.port.mk>
