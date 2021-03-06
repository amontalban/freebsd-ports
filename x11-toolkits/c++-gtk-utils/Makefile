# Created by: Pawel Pekala <pawel@FreeBSD.org>
# $FreeBSD$

PORTNAME=	c++-gtk-utils
PORTVERSION=	2.2.6
CATEGORIES=	x11-toolkits
MASTER_SITES=	SF/cxx-gtk-utils/cxx-gtk-utils/${PORTVERSION}/
DISTNAME=	c%2B%2B-gtk-utils-${PORTVERSION}

MAINTAINER=	pawel@FreeBSD.org
COMMENT=	Lightweight library for programming GTK+ programs

LICENSE=	LGPL21

GNU_CONFIGURE=	yes
USES=		compiler:c++11-lib pathfix pkgconfig
USE_GNOME=	gtk20
USE_LDCONFIG=	yes

CONFIGURE_SCRIPT=	configure-gtk2
CONFIGURE_ARGS+=	--docdir=${DOCSDIR}

WRKSRC=		${WRKDIR}/${PORTNAME}-${PORTVERSION}
PORTDOCS=	*

OPTIONS_DEFINE=	DEBUG DOCS

DEBUG_CONFIGURE_ON=	--enable-debug

.include <bsd.port.options.mk>

post-configure:
	@${REINPLACE_CMD} '/^SUBDIRS/ s|tests||' ${WRKSRC}/Makefile

post-install:
.if ! ${PORT_OPTIONS:MDEBUG}
	@${STRIP_CMD} ${STAGEDIR}${PREFIX}/lib/libcxx-gtk-utils-2-2.2.so.1
.endif

.include <bsd.port.mk>
