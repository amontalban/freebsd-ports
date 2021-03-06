# Created by: Ulrich Spoerlein <uspoerlein@gmail.com>
# $FreeBSD$

PORTNAME=	librcc
PORTVERSION=	0.2.12
PORTREVISION=	2
CATEGORIES=	devel
MASTER_SITES=	http://dside.dyndns.org/files/rusxmms/ \
		LOCAL/fluffy

MAINTAINER=	fluffy@FreeBSD.org
COMMENT=	Library used by rusxmms for language autodetection

LIB_DEPENDS=	librcd.so:${PORTSDIR}/devel/librcd \
		libenca.so:${PORTSDIR}/converters/enca \
		libaspell.so:${PORTSDIR}/textproc/aspell

USE_BZIP2=	yes
GNU_CONFIGURE=	yes
USE_GNOME=	libxml2
USES=		gmake iconv libtool:oldver pathfix pkgconfig
USE_LDCONFIG=	yes

CPPFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-L${LOCALBASE}/lib

OPTIONS_DEFINE=	BDB TRANSLATE TOOLS GTK1 GTK2 GTK3
OPTIONS_DEFAULT=TOOLS GTK2
OPTIONS_SUB=	yes

BDB_DESC=		Translation database support
BDB_CONFIGURE_ENABLE=	bdb
BDB_CPPFLAGS=		-I${BDB_INCLUDE_DIR}
BDB_LDFLAGS=		-L${BDB_LIB_DIR}
BDB_USE=		BDB=41+

TRANSLATE_DESC=			Online translation support
TRANSLATE_CONFIGURE_ENABLE=	libtranslate
TRANSLATE_LIB_DEPENDS=		libtranslate.so:${PORTSDIR}/textproc/libtranslate

TOOLS_DESC=		Recode configuration utility
TOOLS_EXTRA_PATCHES=	${FILESDIR}/extrapatch-rcc-config

GTK1_CONFIGURE_ENABLE=	gtk1
GTK1_USE=		GNOME=glib12,gtk12

GTK2_CONFIGURE_ENABLE=	gtk2
GTK2_USE=		GNOME=gtk20

GTK3_CONFIGURE_ENABLE=	gtk3
GTK3_USE=		GNOME=gtk30

.include <bsd.port.pre.mk>

.if empty(ICONV_LIB)
CONFIGURE_ARGS+=--enable-force-system-iconv
.endif

.if ${PORT_OPTIONS:MGTK2} || ${PORT_OPTIONS:MGTK3}
CONFIGURE_ARGS+=--enable-glib2
PLIST_SUB+=	WITH_GLIB2=""
.else
CONFIGURE_ARGS+=--disable-glib2
PLIST_SUB+=	WITH_GLIB2="@comment "
.endif

pre-everything::
.if ${ARCH} == "i386"
.if ${PORT_OPTIONS:MBDB} || ${PORT_OPTIONS:MTRANSLATE}
	@${ECHO} 'BDB/LibTranslate support may cause breakages in depended apps on ${ARCH}'
	@${ECHO} 'Use it with caution'
.endif
.endif

post-patch:
	@${REINPLACE_CMD} -e 's|glib/.*\.h>|glib.h>|g' \
		${WRKSRC}/external/rccexternal.c

.include <bsd.port.post.mk>
