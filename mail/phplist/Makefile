# Created by: Nick Hilliard <nick@foobar.org>
# $FreeBSD$

PORTNAME=	phplist
PORTVERSION=	3.0.5
PORTREVISION=	1
CATEGORIES=	mail www
MASTER_SITES=	SF
EXTRACT_SUFX=	.tgz

MAINTAINER=	ports@bsdserwis.com
COMMENT=	A full-featured open-source newsletter manager

RUN_DEPENDS=	${PEARDIR}/HTTP/Request.php:${PORTSDIR}/www/pear-HTTP_Request

USE_PHP=	hash iconv imap mysql pcre session xml zlib
NO_BUILD=	yes
PEARDIR?=	${LOCALBASE}/share/pear

PORTDOCS=	BUGS INSTALL NEWS PEOPLE README README.batches \
		README.bounces README.commandline README.passwords \
		README.repetition README.rssfeeds README.security \
		README.usertables README.utf8 TODO UPGRADE VERSION \
		phplist.sql

SUB_FILES=	phplist pkg-message

.include <bsd.port.options.mk>

post-extract:
	@${MV} ${WRKSRC}/public_html/lists/config/config.php ${WRKSRC}/public_html/lists/config/config.php-dist

do-install:
	@cd ${WRKSRC}/public_html/&&${COPYTREE_SHARE} . ${STAGEDIR}${WWWDIR}/
	${INSTALL_SCRIPT} ${WRKDIR}/phplist ${STAGEDIR}${PREFIX}/bin
.if ${PORT_OPTIONS:MDOCS}
	${MKDIR} ${STAGEDIR}${DOCSDIR}
	@cd ${WRKSRC} && ${INSTALL_DATA} ${PORTDOCS} ${STAGEDIR}${DOCSDIR}
.endif
	@${CAT} ${PKGMESSAGE}

.include <bsd.port.mk>
