# Created by: "Waitman Gobble" <uzimac@da3m0n8t3r.com>
# $FreeBSD$

PORTNAME=	chucky
PORTVERSION=	1.0
CATEGORIES=	ports-mgmt
MASTER_SITES=	GH
DISTNAME=	${GH_ACCOUNT}-${GH_PROJECT}-${PORTVERSION}-0-g${GH_COMMIT}

MAINTAINER=	waitman@waitman.net
COMMENT=	Port installed version check/report with shar archival

LICENSE=	CHUCKY
LICENSE_NAME=	CHUCKY BSD LICENSE
LICENSE_FILE=	${WRKSRC}/LICENSE
LICENSE_PERMS=	${_LICENSE_PERMS_DEFAULT}

LIB_DEPENDS=	libpkg.so:${PORTSDIR}/ports-mgmt/pkg \
		libsqlite3.so:${PORTSDIR}/databases/sqlite3

USE_GITHUB=	yes
GH_ACCOUNT=	waitman
GH_PROJECT=	chucky
GH_TAGNAME=	075defe
GH_COMMIT=	${GH_TAGNAME}

SUB_FILES=	pkg-message
SUB_LIST=	MAN7PREFIX="${MAN7PREFIX}"
PORTDOCS=	*

OPTIONS_DEFINE=	DOCS

.include <bsd.port.options.mk>

post-install:
	@${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${WRKSRC}/README ${STAGEDIR}${DOCSDIR}

.include <bsd.port.mk>
