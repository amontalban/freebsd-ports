# Created by: verm@drunkmonk.net
# $FreeBSD$

PORTNAME=	lbreakout2
PORTVERSION=	2.6
PORTREVISION=	4
CATEGORIES=	games
MASTER_SITES=	SF/lgames/${PORTNAME}/${PORTVERSION}

MAINTAINER=	mmendez@gmail.com
COMMENT=	The polished successor to LBreakout

LIB_DEPENDS=	png15:${PORTSDIR}/graphics/png

USE_SDL=	mixer net sdl
USE_GMAKE=	yes
GNU_CONFIGURE=	yes
CONFIGURE_ARGS=	--enable-sdl-net \
		--localstatedir=/var/games \
		--disable-nls

CPPFLAGS+=	-I${LOCALBASE}/include -I${LOCALBASE}/include/libpng15
LDFLAGS+=	-L${LOCALBASE}/lib

NO_STAGE=	yes
post-patch:
	@${REINPLACE_CMD} -e \
		's|== "-D|= "-D|g' ${WRKSRC}/configure
	@${REINPLACE_CMD} -e \
		's|client docs|client|g' ${WRKSRC}/Makefile.in
	@${REINPLACE_CMD} -e \
		's|: install-data-local|:|g' ${WRKSRC}/client/Makefile.in

post-install:
	${INSTALL_DATA} ${WRKSRC}/client/empty.hscr ${DATADIR}
	@${CHOWN} root:games ${PREFIX}/bin/lbreakout2
	@${CHMOD} g+s ${PREFIX}/bin/lbreakout2
.if !defined(NOPORTDOCS)
	@${MKDIR} ${DOCSDIR}
	${INSTALL_DATA} ${WRKSRC}/docs/*.html ${DOCSDIR}
	${INSTALL_DATA} ${WRKSRC}/docs/*.jpg ${DOCSDIR}
.endif
	@${SETENV} "PKG_PREFIX=${PREFIX}" \
		${SH} ${.CURDIR}/pkg-install ${PKGNAME} POST-INSTALL

.include <bsd.port.mk>
