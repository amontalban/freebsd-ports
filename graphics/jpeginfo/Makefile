# Created by: ache
# $FreeBSD$

PORTNAME=	jpeginfo
PORTVERSION=	1.6.1
PORTREVISION=	1
CATEGORIES=	graphics
MASTER_SITES=	http://www.kokkonen.net/tjko/src/

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Generate listing and MD5, check jpegs for error, delete broken ones

LIB_DEPENDS=	libjpeg.so:${PORTSDIR}/graphics/jpeg

GNU_CONFIGURE=	yes
CONFIGURE_ENV=	LIBS="-L${LOCALBASE}/lib"
CPPFLAGS+=	-I${LOCALBASE}/include
MAKE_ARGS=	mandir=${MANPREFIX}/man INSTALL_ROOT=${STAGEDIR}

PLIST_FILES=	bin/jpeginfo man/man1/jpeginfo.1.gz

.include <bsd.port.mk>
