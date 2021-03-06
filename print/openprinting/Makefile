# Created by: Bruce M Simpson <bms@FreeBSD.org>
# $FreeBSD$

PORTNAME=	openprinting
PORTVERSION=	1.0
PORTREVISION=	3
CATEGORIES=	print net
MASTER_SITES=	${MASTER_SITE_SOURCEFORGE}
MASTER_SITE_SUBDIR=\
		openprinting/papi/1.0%20Beta
DISTNAME=	papi-${PORTVERSION}_beta
DIST_SUBDIR=	${PORTNAME}

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Sun's implementation of the OpenPrinting API (PAPI)

WRKSRC=		${WRKDIR}/papi-${PORTVERSION}_beta

USE_BZIP2=	yes
USES=		gettext iconv gmake

USE_LDCONFIG=	${PREFIX}/lib ${PREFIX}/libexec

GNU_CONFIGURE=	yes
MAKE_JOBS_UNSAFE=	yes

USE_AUTOTOOLS=	aclocal autoconf autoheader automake libtool
ACLOCAL_ARGS+=	-I ${LOCALBASE}/share/aclocal
AUTOMAKE_ARGS+=	-a -c

# Really disable building static libraries; the package does not use
# its own libtool, and we have to tell it to stop.
# Static libraries are not very useful in this package.
MAKE_ARGS=	LIBTOOL="${LIBTOOL} --tag=disable-static"

# TODO: Get mod_ipp to actually work; Sun's example seems to be broken
# under both Apache 1.3/2.0, this could be a papi issue; does not build
# w/Apache 2.2.
# TODO: Fix Apache module install target to instead use APXS
# from this file; it is intended only as an example.
# TODO: CUPS integration is broken in distfiles (missing papi_int.h).
#OPTIONS=\
#	MOD_IPP		"Build example mod_ipp.so for Apache" Off
#	PSM_CUPS	"Build psm_cups.so for printing to CUPS" Off

.include <bsd.port.options.mk>

# NOTE: hard dependency on gettext() in distfiles.
CONFIGURE_ARGS+=\
		LDFLAGS="-L${LOCALBASE}/lib" \
		CPPFLAGS="-I${LOCALBASE}/include" \
		LIBS="-lintl"

# NOTE: This has only been tested with www/apache20, with integrated APR.
.if defined(WITH_MOD_IPP)
IGNORE=	no supported apache versions available
#USE_APACHE=	20
#CONFIGURE_ARGS+=--with-apache=${LOCALBASE}
.else
CONFIGURE_ARGS+=--without-apache
.endif

.if defined(WITH_PSM_CUPS)
LIB_DEPENDS+=	cups.2:${PORTSDIR}/print/cups-client
CONFIGURE_ARGS+=--with-cups=${LOCALBASE}
.else
CONFIGURE_ARGS+=--without-cups
.endif


PLIST_DIRS+=	man/mani

PLIST_FILES+=\
	include/papi.h \
	include/ipp.h \
	include/debug.h \
	include/http.h \
	include/http-private.h \
	include/ipp-listener.h \
	lib/libpapi-common.so \
	lib/libpapi-common.so.0 \
	lib/libpapi-common.la \
	lib/libpapi.so \
	lib/libpapi.so.0 \
	lib/libpapi.la \
	lib/libipp-core.so \
	lib/libipp-core.so.0 \
	lib/libipp-core.la \
	lib/libipp-listener.so \
	lib/libipp-listener.so.0 \
	lib/libipp-listener.la \
	libexec/psm-lpd.so \
	libexec/psm-lpd.la \
	libexec/psm-ipp.so \
	libexec/psm-ipp.la \
	libexec/lpd-port \
	man/man5/psm-ipp.5.gz

.if defined(WITH_PSM_CUPS)
PLIST_FILES+=\
	libexec/psm-cups.so \
	libexec/psm-cups.la
.endif

.if defined(WITH_MOD_IPP)
PLIST_FILES+=\
	lib/mod_ipp.so \
	lib/mod_ipp.la
.endif

.include <bsd.port.pre.mk>

pre-configure:
	cd ${WRKSRC}; ./autogen.sh

.include <bsd.port.post.mk>
