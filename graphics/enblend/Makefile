# Created by: cartola@openit.com.br
# $FreeBSD$

PORTNAME=	enblend
PORTVERSION=	4.1.1
PORTREVISION=	8
CATEGORIES=	graphics
MASTER_SITES=	SF/enblend/enblend-enfuse/enblend-enfuse-${PORTVERSION:R}
DISTNAME=	enblend-enfuse-${PORTVERSION}

MAINTAINER=	grog@FreeBSD.org
COMMENT=	Tool for image blending with multiresolution splines

BUILD_DEPENDS=	${LOCALBASE}/bin/makeinfo:${PORTSDIR}/print/texinfo \
		OpenEXR>=1.0:${PORTSDIR}/graphics/OpenEXR
LIB_DEPENDS=	libjpeg.so:${PORTSDIR}/graphics/jpeg \
		liblcms2.so:${PORTSDIR}/graphics/lcms2 \
		libxmi.so:${PORTSDIR}/graphics/plotutils \
		libtiff.so:${PORTSDIR}/graphics/tiff \
		libboost_filesystem.so:${PORTSDIR}/devel/boost-libs \
		libvigraimpex.so:${PORTSDIR}/graphics/vigra \
		libgsl.so:${PORTSDIR}/math/gsl
RUN_DEPENDS=	OpenEXR>=1.0:${PORTSDIR}/graphics/OpenEXR

USE_AUTOTOOLS=	automake:env autoconf:env
USES=		gmake compiler:features 
# We need a newer version of makeinfo for this.
# Remove this line when we remove texinfo from the base system.
CONFIGURE_ARGS=	MAKEINFO="${LOCALBASE}/bin/makeinfo"

USE_GL=		glew glut
GNU_CONFIGURE=	yes
CONFIGURE_ENV+=	"LIBS=-lboost_system"
CONFIGURE_ARGS+=	--with-boost-filesystem
CPPFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-L${LOCALBASE}/lib

.include <bsd.port.pre.mk>

.if ${COMPILER_TYPE} == gcc
# GCC 4.2 has some problems, see
# http://groups.google.com/group/hugin-ptx/browse_thread/thread/725b1581c9889e37/50abe3387d61541a#50abe3387d61541a
# Clang, on 10.0-RELEASE is fine.
USE_GCC=	yes
.else
CXXFLAGS+=	-Wno-c++11-extensions
.endif

INFO=		enfuse enblend
PLIST_FILES=	bin/enblend bin/enfuse man/man1/enblend.1.gz man/man1/enfuse.1.gz

post-install:
		${INSTALL_DATA} ${WRKSRC}/doc/*.info ${STAGEDIR}${PREFIX}/${INFO_PATH}

.include <bsd.port.post.mk>
