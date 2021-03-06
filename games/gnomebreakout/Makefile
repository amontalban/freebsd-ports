# Created by: Kris Kennaway <kris@FreeBSD.org>
# $FreeBSD$

PORTNAME=	gnomebreakout
PORTVERSION=	0.5.3
PORTREVISION=	12
CATEGORIES=	games gnome
MASTER_SITES=	SF/${PORTNAME:S/eb/e-b/}/${PORTNAME:S/eb/e-b/}/${PORTVERSION}/ \
		http://www.users.on.net/~mipearson/
DISTNAME=	gnome-breakout-${PORTVERSION}

MAINTAINER=	games@FreeBSD.org
COMMENT=	GNOME version of the classic breakout game

USES=		pathfix pkgconfig
USE_GNOME=	gnomeprefix libgnomeui
GNU_CONFIGURE=	yes
USE_GCC=	yes

CPPFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-L${LOCALBASE}/lib -lm

PORTDOCS=	AUTHORS ChangeLog NEWS README

OPTIONS_DEFINE=	DOCS NLS
OPTIONS_SUB=	yes

NLS_USES=	gettext:run

.include <bsd.port.options.mk>

post-patch:
	@${REINPLACE_CMD} -e 's|-Werror||' ${WRKSRC}/src/Makefile.in
	@${REINPLACE_CMD} -e \
		's|@GETTEXT_PACKAGE@|@PACKAGE@|' ${WRKSRC}/po/Makefile.in.in
	@${FIND} ${WRKSRC} -name Makefile.in | ${XARGS} ${REINPLACE_CMD} -e \
		's|-DGNOME_DISABLE_DEPRECATED||; s|-DGTK_DISABLE_DEPRECATED||; \
		 s|-DGDK_PIXBUF_DISABLE_DEPRECATED||; s|-DG_DISABLE_DEPRECATED||'

.if ! ${PORT_OPTIONS:MNLS}
	@${REINPLACE_CMD} -e 's|po src|src|' \
		${WRKSRC}/Makefile.in
.endif

post-install:
	@${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${PORTDOCS:S|^|${WRKSRC}/|} ${STAGEDIR}${DOCSDIR}

.include <bsd.port.mk>
