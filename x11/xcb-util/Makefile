# Created by: Nikos Ntarmos <ntarmos@ceid.upatras.gr>
# $FreeBSD$

PORTNAME=	xcb-util
PORTVERSION=	0.3.9
PORTREVISION=	3
PORTEPOCH=	1
CATEGORIES=	x11
MASTER_SITES=	http://xcb.freedesktop.org/dist/

MAINTAINER=	garga@FreeBSD.org
COMMENT=	A module with libxcb/libX11 extension/replacement libraries

XORG_CAT=	lib
USE_BZIP2=	yes
USES=		gmake
USE_XORG=	xau xcb xdmcp

post-patch:
	@${REINPLACE_CMD} -e \
		's|$${libdir}/pkgconfig|$${prefix}/libdata/pkgconfig|' \
		${WRKSRC}/configure

.include <bsd.port.mk>
