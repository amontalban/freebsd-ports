# Created by: snb@threerings.net
# $FreeBSD$

PORTNAME=	osslsigncode
PORTVERSION=	1.3
PORTREVISION=	3
CATEGORIES=	security devel
MASTER_SITES=	SF/${PORTNAME}/${PORTNAME}/${PORTNAME}%20${PORTVERSION}

MAINTAINER=	snb@FreeBSD.org
COMMENT=	OpenSSL-based signcode utility

PLIST_FILES=	bin/osslsigncode

CPPFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-L${LOCALBASE}/lib
GNU_CONFIGURE=	yes
USE_GMAKE=	yes
USE_OPENSSL=	yes

.if !defined(WITHOUT_CURL)
LIB_DEPENDS+=	curl:${PORTSDIR}/ftp/curl
.endif

NO_STAGE=	yes
.include <bsd.port.mk>
