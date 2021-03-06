# Created by: thierry@pompo.net
# $FreeBSD$

PORTNAME=		xvidcap
PORTVERSION=		1.1.7
PORTEPOCH=		1
CATEGORIES=		sysutils multimedia
MASTER_SITES=		SF/${PORTNAME}/${PORTNAME}/${PORTVERSION}

MAINTAINER=		thierry@FreeBSD.org
COMMENT=		Capture your X display to individual frames or MPEG video

LICENSE=		GPLv3

BUILD_DEPENDS=		xml2po:${PORTSDIR}/textproc/gnome-doc-utils	\
			scrollkeeper-config:${PORTSDIR}/textproc/scrollkeeper
LIB_DEPENDS=		libswscale.so:${PORTSDIR}/multimedia/ffmpeg	\
			libdbus-glib-1.so:${PORTSDIR}/devel/dbus-glib	\
			libmp3lame.so:${PORTSDIR}/audio/lame
RUN_DEPENDS=		animate:${PORTSDIR}/graphics/ImageMagick	\
			gimp:${PORTSDIR}/graphics/gimp-app

GNU_CONFIGURE=		yes
CPPFLAGS+=		-I${LOCALBASE}/include
# --export-dynamic fixes libglade problems
LDFLAGS+=		-L${LOCALBASE}/lib -Wl,--export-dynamic

USE_GNOME=		glib20 libglade2
USES=			gettext gmake pkgconfig
USE_XORG=		x11 xmu ice xfixes xdamage
INSTALLS_OMF=		yes
MANLANG=		"" de es it

.if !defined(CFLAGS) || ${CFLAGS:M-fno-strict-aliasing*} == ""
CFLAGS+=	-O2 -fno-strict-aliasing
.endif

PORTDOCS=		AUTHORS ChangeLog README
NULLDOCS=		COPYING

pre-configure:
.if defined(NOPORTDOCS)
	${REINPLACE_CMD} -e 's|pkgdataDATA install-xvidcapdocDATA|pkgdataDATA|'	\
		${WRKSRC}/Makefile.in
.endif
	${REINPLACE_CMD} -e 's|/bin/bash | /bin/sh|' ${WRKSRC}/ppm2mpeg.sh

post-install:
.if !defined(NOPORTDOCS)
	${RM} -f ${NULLDOCS:S|^|${STAGEDIR}${DOCSDIR}/|}
.endif

.include <bsd.port.mk>
