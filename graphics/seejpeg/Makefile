# Created by: Donn Miller <dmmiller@cvzoom.net>
# $FreeBSD$

PORTNAME=	seejpeg
PORTVERSION=	1.10
PORTREVISION=	4
CATEGORIES=	graphics
MASTER_SITES=	${MASTER_SITE_SUNSITE}
MASTER_SITE_SUBDIR=	apps/graphics/viewers/svga
EXTRACT_SUFX=	.tgz

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Console graphics viewer using the svga console graphics library

LIB_DEPENDS=	libvga.so:${PORTSDIR}/graphics/svgalib \
		libjpeg.so:${PORTSDIR}/graphics/jpeg

USES=		gmake
ALL_TARGET=	seejpeg
CPPFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-L${LOCALBASE}/lib

PLIST_FILES=	bin/seejpeg man/man1/seejpeg.1.gz

post-extract:
	${CHMOD} 0644 ${WRKSRC}/Makefile

post-patch:
	${MV}	${WRKSRC}/Makefile ${WRKSRC}/Makefile.prev
	${SED}	"s|-O3|${CFLAGS}|g" ${WRKSRC}/Makefile.prev >  ${WRKSRC}/Makefile

.include <bsd.port.mk>
