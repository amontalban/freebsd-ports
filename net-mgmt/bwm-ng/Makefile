# Created by: Tim Bishop <tdb@FreeBSD.org>
# $FreeBSD$

PORTNAME=	bwm-ng
PORTVERSION=	0.6
PORTREVISION=	1
CATEGORIES=	net-mgmt
MASTER_SITES=	http://www.gropp.org/bwm-ng/

MAINTAINER=	tdb@FreeBSD.org
COMMENT=	A small and simple bandwidth monitor

LIB_DEPENDS=	libstatgrab.so:${PORTSDIR}/devel/libstatgrab

GNU_CONFIGURE=	yes
USES=		pkgconfig
PLIST_FILES=	bin/bwm-ng man/man1/bwm-ng.1.gz

CONFIGURE_ENV=	CPPFLAGS="-std=gnu89 `pkg-config --cflags libstatgrab`" \
		LIBS="`pkg-config --libs libstatgrab`"
CONFIGURE_ARGS=	--with-libstatgrab

.include <bsd.port.mk>
