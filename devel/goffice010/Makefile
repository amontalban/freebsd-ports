# Created by: Joe Marcus Clarke <marcus@FreeBSD.org>
# $FreeBSD$
#   $MCom: ports/trunk/devel/goffice/Makefile 18385 2013-04-22 12:56:25Z kwm $

PORTNAME=	goffice
PORTVERSION=	0.10.11
PORTREVISION=	1
CATEGORIES=	devel gnome
MASTER_SITES=	GNOME
PKGNAMESUFFIX=	010

MAINTAINER=	gnome@FreeBSD.org
COMMENT=	GLib/GTK+ set of document centric objects and utilities

LICENSE=	GPLv2
LICENSE_FILE=	${WRKSRC}/COPYING

USE_XZ=		yes
USE_GNOME=	gnomeprefix gtk30 intlhack libgsf librsvg2
USES=		gettext gmake libtool:keepla pathfix pkgconfig
GNU_CONFIGURE=	yes
USE_LDCONFIG=	yes
CPPFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-L${LOCALBASE}/lib
INSTALL_TARGET=	install-strip
CONFIGURE_ARGS=	--with-lasem=no --with-config-backend=gsettings
CONFIGURE_ARGS+=--enable-compile-warnings=no

PLIST_SUB=	VERSION=${PORTVERSION} SHORT_VER=${SHORT_VER} \
		LIBVERSION=10.0.11
SHORT_VER=	0.10

post-install:
	@${MKDIR} ${STAGEDIR}${PREFIX}/lib/goffice/${SHORT_VER}/plugins

.include <bsd.port.mk>
