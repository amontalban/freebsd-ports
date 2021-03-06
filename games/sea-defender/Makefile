# Created by: Dmitry Marakasov <amdmi3@FreeBSD.org>
# $FreeBSD$

PORTNAME=	sea-defender
PORTVERSION=	0.9
PORTREVISION=	1
CATEGORIES=	games
MASTER_SITES=	http://mirror.amdmi3.ru/distfiles/:DEFAULT,icon \
		SF/nemysisfreebsdp/:icon
DISTFILES=	${DISTNAME}${EXTRACT_SUFX} \
		${PORTNAME}.png:icon
EXTRACT_ONLY=	${DISTNAME}${EXTRACT_SUFX}

MAINTAINER=	amdmi3@FreeBSD.org
COMMENT=	Simple missile command clone

LICENSE=	MIT

BUILD_DEPENDS=	${LOCALBASE}/lib/libglfw.a:${PORTSDIR}/graphics/glfw2

USE_GITHUB=	yes
GH_ACCOUNT=	snoutmate
GH_PROJECT=	Sea-Defender
GH_TAGNAME=	${GH_COMMIT}
GH_COMMIT=	d628051

USES=		gmake
USE_SDL=	sdl mixer image ttf
USE_GL=		gl glu
USE_XORG=	x11 xrandr

SUB_FILES=	${PORTNAME}.sh
PLIST_FILES=	bin/${PORTNAME} \
		libexec/${PORTNAME} \
		share/pixmaps/${PORTNAME}.png

PORTDOCS=	*

DESKTOP_ENTRIES="Sea Defender" \
		"${COMMENT}" \
		"${PORTNAME}" \
		"${PORTNAME}" \
		"Game;ArcadeGame;" \
		""

OPTIONS_DEFINE=	DOCS

.include <bsd.port.options.mk>

.if defined(WITH_NEW_XORG)
EXTRA_PATCHES+=	${FILESDIR}/extra-snoutlib_gldefs.h
.endif

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/sea ${STAGEDIR}${PREFIX}/libexec/${PORTNAME}
	${INSTALL_SCRIPT} ${WRKDIR}/${PORTNAME}.sh ${STAGEDIR}${PREFIX}/bin/${PORTNAME}
	${INSTALL_DATA} ${_DISTDIR}/${PORTNAME}.png ${STAGEDIR}${PREFIX}/share/pixmaps/
	${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${WRKSRC}/README ${STAGEDIR}${DOCSDIR}/

.include <bsd.port.mk>
