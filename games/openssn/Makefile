# Created by: Jesse Smith <jessefrgsmith@yahoo.ca>
# $FreeBSD$

PORTNAME=	openssn
PORTVERSION=	1.4
PORTREVISION=	2
CATEGORIES=	games
MASTER_SITES=	SF/${PORTNAME}/${PORTNAME}-${PORTVERSION}

MAINTAINER=	jessefrgsmith@yahoo.ca
COMMENT=	Modern submarine simulator

LICENSE=	GPLv2

USE_SDL=	sdl gfx image mixer
USE_XORG=	x11 xau xdmcp xext xmu xpm xxf86vm
WRKSRC=		${WRKDIR}/${PORTNAME}

post-patch:
	@${REINPLACE_CMD} -E \
		-e '/cp|mkdir/s,\$$\(PREFIX\)|\$$\(DATADIR\),$$(DESTDIR)&,' \
		-e 's,share/man/man6,man/man6,' ${WRKSRC}/Makefile

.include <bsd.port.mk>
