# Created by: Christopher Preston <rbg@gayteenresource.org>
# $FreeBSD$

PORTNAME=	nettoe
PORTVERSION=	1.5
CATEGORIES=	games
MASTER_SITES=	http://www.c-s.li/ports/ \
		SF

MAINTAINER=	cs@FreeBSD.org
COMMENT=	Tic tac toe game playable over the network

LICENSE=	GPLv2

PLIST_FILES=	bin/nettoe man/man6/nettoe.6.gz

USES=		gmake
GNU_CONFIGURE=	yes
PORTDOCS=	AUTHORS BUGS ChangeLog NEWS README TO-DO

OPTIONS_DEFINE=	DOCS

.include <bsd.port.options.mk>

post-install:
.if ${PORT_OPTIONS:MDOCS}
	${MKDIR} ${STAGEDIR}${DOCSDIR}
.for I in ${PORTDOCS}
	${INSTALL_DATA} ${WRKSRC}/$I ${STAGEDIR}${DOCSDIR}/
.endfor
.endif

.include <bsd.port.mk>
