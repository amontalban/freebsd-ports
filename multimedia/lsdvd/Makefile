# Created by: michael johnson <ahze@ahze.net>
# $FreeBSD$

PORTNAME=	lsdvd
PORTVERSION=	0.16
PORTREVISION=	8
CATEGORIES=	multimedia
MASTER_SITES=	SF/${PORTNAME}/${PORTNAME}/${PORTVERSION}%20-%20I%20hate%20James%20Blunt

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Print information about the contents and structure of a DVD

LIB_DEPENDS=	libdvdread.so:${PORTSDIR}/multimedia/libdvdread

GNU_CONFIGURE=	yes
CPPFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-L${LOCALBASE}/lib

MAN1=		lsdvd.1
PLIST_FILES=	bin/lsdvd

WITH_DVD_DEVICE?=/dev/acd0

NO_STAGE=	yes
pre-everything::
	@${ECHO_MSG} "===> The default DVD device is ${WITH_DVD_DEVICE}"
	@${ECHO_MSG} "===> Define WITH_DVD_DEVICE if you want to change the default"
	@${ECHO_MSG} "===> For example, 'make WITH_DVD_DEVICE=\"/dev/somedevice\"'"
	@${ECHO_MSG} "===>"

post-patch:
	@${REINPLACE_CMD} -e 's|/dev/dvd|${WITH_DVD_DEVICE}|' \
		${WRKSRC}/lsdvd.c

.include <bsd.port.mk>
