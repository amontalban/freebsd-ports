# Created by: roam@FreeBSD.org
# $FreeBSD$

PORTNAME=	c-ares
PORTVERSION=	1.10.0
CATEGORIES=	dns
MASTER_SITES=	http://c-ares.haxx.se/download/ \
		http://obsd.isc.org/pub/OpenBSD/distfiles/ \
		http://mirrors.rit.edu/zi/

MAINTAINER=	zi@FreeBSD.org
COMMENT=	An asynchronous DNS resolver library

LICENSE=	MIT

SSP_UNSAFE=	Refuses -l in LDFLAGS

OPTIONS_DEFINE=		CONFIG_INFO DEBUG HIDE_SYMBOLS OPTIMIZED_CFLAGS
OPTIONS_DEFAULT=	CONFIG_INFO HIDE_SYMBOLS

CONFIG_INFO_DESC=	Add the ares_config_info patch
HIDE_SYMBOLS_DESC=	Hide internal library symbols
OPTIMIZED_CFLAGS_DESC=	Build with compiler optimizations

CONFLICTS=		ares-1.*

MAKE_JOBS_UNSAFE=	yes

.include <bsd.port.pre.mk>

.if ${PORT_OPTIONS:MCONFIG_INFO}
EXTRA_PATCHES+=	${FILESDIR}/ares-config-info.patch
PKGNAMESUFFIX=	-config
.endif

.if ${PORT_OPTIONS:MDEBUG}
CONFIGURE_ARGS+=--enable-debug
.else
CONFIGURE_ARGS+=--disable-debug
.endif

.if ${PORT_OPTIONS:MHIDE_SYMBOLS}
CONFIGURE_ARGS+=--enable-symbol-hiding
.else
CONFIGURE_ARGS+=--disable-symbol-hiding
.endif

.if ${PORT_OPTIONS:MOPTIMIZED_CFLAGS}
CONFIGURE_ARGS+=--enable-optimize
.else
CONFIGURE_ARGS+=--disable-optimize
.endif

USE_LDCONFIG=	yes
SHLIB_VER=	3

MAKE_ENV=	SHLIB_VER="${SHLIB_VER}"
PLIST_SUB=	SHLIB_VER="${SHLIB_VER}"

GNU_CONFIGURE=	yes
CONFIGURE_ARGS+=--enable-shared --disable-werror

PROGRAMS=	acountry adig ahost

post-install:
	${INSTALL_PROGRAM} ${PROGRAMS:S@^@${WRKSRC}/.libs/@} ${STAGEDIR}${PREFIX}/bin/

.include <bsd.port.post.mk>
