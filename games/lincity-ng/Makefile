# Created by: Andrej Zverev
# $FreeBSD$

PORTNAME=	lincity-ng
PORTVERSION=	2.0
PORTREVISION=	9
CATEGORIES=	games
MASTER_SITES=	${MASTER_SITE_BERLIOS}
MASTER_SITE_SUBDIR=	${PORTNAME}

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Improved rich city simulation game for X

BUILD_DEPENDS=	jam:${PORTSDIR}/devel/jam
LIB_DEPENDS=	libphysfs.so:${PORTSDIR}/devel/physfs

USES=		pkgconfig
USE_BZIP2=	yes
USE_SDL=	sdl mixer image ttf gfx
USE_GL=		yes
USE_GNOME=	libxml2

GNU_CONFIGURE=	yes
CONFIGURE_ARGS=	--with-libphysfs=${PREFIX} \
		--x-libraries=${LOCALBASE}/lib --x-includes=${LOCALBASE}/include
CPPFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-L${LOCALBASE}/lib ${PTHREAD_LIBS}

post-patch:
	@${REINPLACE_CMD} -e 's| -O| -I${LOCALBASE}/include&|g' \
		${WRKSRC}/Jamrules
do-build:
	@(cd ${BUILD_WRKSRC}; ${SETENV} ${MAKE_ENV} jam -j${MAKE_JOBS_NUMBER})

do-install:
	@(cd ${INSTALL_WRKSRC} && ${SETENV} ${MAKE_ENV} jam -sprefix=${STAGEDIR}${PREFIX} ${INSTALL_TARGET})

.include <bsd.port.mk>
