# Created by: Dmitry Marakasov <amdmi3@FreeBSD.org>
# $FreeBSD$

PORTNAME=	chroma
PORTVERSION=	1.08
PORTREVISION=	5
CATEGORIES=	games
MASTER_SITES=	http://www.level7.org.uk/chroma/download/ \
		http://mirror.amdmi3.ru/distfiles/

MAINTAINER=	amdmi3@FreeBSD.org
COMMENT=	Abstract puzzle game

USES=		tar:bzip2 gettext
GNU_CONFIGURE=	yes
CONFIGURE_ENV=	LIBS="-lintl"
CPPFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-L${LOCALBASE}/lib

PORTDOCS=	*
PORTDATA=	*

OPTIONS_DEFINE=	DOCS
OPTIONS_MULTI=	INTERFACES
OPTIONS_MULTI_INTERFACES=SDL CURSES
OPTIONS_DEFAULT=SDL CURSES

SDL_DESC=	Enable SDL interface
CURSES_DESC=	Enable curses interface

OPTIONS_SUB=		yes
CURSES_USES=		ncurses
CURSES_CONFIGURE_ENABLE=curses
CURSES_PLIST_FILES=	bin/${PORTNAME}-curses
SDL_CONFIGURE_ENABLE=	sdl
SDL_LIB_DEPENDS=	libfreetype.so:${PORTSDIR}/print/freetype2
SDL_USE=		SDL=sdl,image
SDL_PLIST_FILES=	bin/${PORTNAME}

post-install:
	${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${WRKSRC}/README ${STAGEDIR}${DOCSDIR}/

.include <bsd.port.mk>
