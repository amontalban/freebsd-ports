# Created by: Stefan 'Steve' Tell <stefan.tell@crashmail.de>
# $FreeBSD$

PORTNAME=	bsdgroup-firefox-searchplugin
PORTVERSION=	0.2
PORTREVISION=	9
CATEGORIES=	german www
MASTER_SITES=	http://www.crashmail.de/files/ \
		http://people.bsdgroup.de/~steve/files/
DISTFILES=	bsdgroup.src bsdgroup.png bsdgroup-wiki.src bsdgroup-wiki.png
EXTRACT_ONLY=	yes

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Firefox search plugins for the www.BSDGroup.de board

USES=		gecko:firefox

NO_BUILD=	yes

NO_STAGE=	yes

DEPRECATED=	bsdgroup.de no longer seems to exist
EXPIRATION_DATE=2014-05-31

do-extract:
	@${MKDIR} ${WRKSRC}
	@${CP} ${DISTDIR}/${DIST_SUBDIR}/bsdgroup.src ${WRKSRC}
	@${CP} ${DISTDIR}/${DIST_SUBDIR}/bsdgroup.png ${WRKSRC}
	@${CP} ${DISTDIR}/${DIST_SUBDIR}/bsdgroup-wiki.src ${WRKSRC}
	@${CP} ${DISTDIR}/${DIST_SUBDIR}/bsdgroup-wiki.png ${WRKSRC}

do-install:
	@${MKDIR} ${PREFIX}/lib/firefox/searchplugins
	${INSTALL_DATA} ${WRKSRC}/bsdgroup.src ${PREFIX}/lib/firefox/searchplugins
	${INSTALL_DATA} ${WRKSRC}/bsdgroup.png ${PREFIX}/lib/firefox/searchplugins
	${INSTALL_DATA} ${WRKSRC}/bsdgroup-wiki.src ${PREFIX}/lib/firefox/searchplugins
	${INSTALL_DATA} ${WRKSRC}/bsdgroup-wiki.png ${PREFIX}/lib/firefox/searchplugins

.include <bsd.port.mk>
