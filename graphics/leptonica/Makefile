# Created by: Hiroto Kagotani <hiroto.kagotani@gmail.com>
# $FreeBSD$

PORTNAME=	leptonica
PORTVERSION=	1.69
PORTREVISION=	2
CATEGORIES=	graphics
MASTER_SITES=	GOOGLE_CODE

MAINTAINER=	hiroto.kagotani@gmail.com
COMMENT=	C library for efficient image processing and image analysis operations

LIB_DEPENDS=	libgif.so:${PORTSDIR}/graphics/giflib \
		libjpeg.so:${PORTSDIR}/graphics/jpeg \
		libpng15.so:${PORTSDIR}/graphics/png \
		libtiff.so:${PORTSDIR}/graphics/tiff \
		libwebp.so:${PORTSDIR}/graphics/webp

CONFLICTS=	leptonlib-[0-9]*

GNU_CONFIGURE=	yes
USE_LDCONFIG=	yes
CPPFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-L${LOCALBASE}/lib

TESTS?=	generate compare
.if defined(MAINTAINER_MODE) || defined(PACKAGE_BUILDING)
BUILD_DEPENDS+=	${LOCALBASE}/bin/gnuplot:${PORTSDIR}/math/gnuplot
.endif
#the display portion of the regression tests is interactive,
#and requires the use of xv, xli or xzgv as an image viewer
.if defined(MAINTAINER_MODE) && !defined(BATCH)
TESTS+=	display
.endif

check regression-test test: build
.for c in ${TESTS}
	@cd ${WRKSRC}/prog; ${SETENV} \
	LD_LIBRARY_PATH="${WRKSRC}/src/.libs:${LOCALBASE}/lib" \
	${WRKSRC}/prog/alltests_reg ${c}
.endfor

.include <bsd.port.mk>
