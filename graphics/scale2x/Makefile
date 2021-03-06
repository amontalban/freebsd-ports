# Created by: chinsan
# $FreeBSD$

PORTNAME=	scale2x
PORTVERSION=	3.0
CATEGORIES=	graphics
MASTER_SITES=	SF

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Real-time graphics effect able to increase the size of small bitmaps

LICENSE=	GPLv2 # (or later)

LIB_DEPENDS=	libpng15.so:${PORTSDIR}/graphics/png

GNU_CONFIGURE=	yes

CPPFLAGS+=	$$(libpng15-config --I_opts)
LDFLAGS+=	$$(libpng15-config --L_opts)

PORTDOCS=	*
PORTEXAMPLES=	*
PLIST_FILES=	bin/scalex bin/scalerx man/man1/scalex.1.gz \
		man/man1/scalerx.1.gz

OPTIONS_DEFINE=	DOCS EXAMPLES
OPTIONS_DEFINE_i386=	MMX

MMX_CPPFLAGS+=	-DHAVE_MMX

post-patch:
	@${REINPLACE_CMD} -e \
		'/<malloc.h>/d ; \
		 s|__i386__|HAVE_MMX| ; \
		 s|__x86_64__|__amd64__|' ${WRKSRC}/*.[ch]

post-install:
	@${MKDIR} ${STAGEDIR}${DOCSDIR}
	(cd ${WRKSRC}/doc && ${INSTALL_DATA} *.html ${STAGEDIR}${DOCSDIR})
	@${MKDIR} ${STAGEDIR}${EXAMPLESDIR}
	(cd ${WRKSRC}/example && ${INSTALL_DATA} *.png ${STAGEDIR}${EXAMPLESDIR})

.include <bsd.port.mk>
