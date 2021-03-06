# Created by: Peter Hawkins <thepish@FreeBSD.org>
# $FreeBSD$

PORTNAME=	XmHTML
PORTVERSION=	1.1.9
CATEGORIES=	x11-toolkits www
MASTER_SITES=	SF/${PORTNAME:tl}
EXTRACT_SUFX=	.tgz

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Motif widget set for displaying HTML 3.2 documents

LICENSE=	LGPL20 # (or later)

LIB_DEPENDS=	libjpeg.so:${PORTSDIR}/graphics/jpeg \
		libpng15.so:${PORTSDIR}/graphics/png

USES=		gmake motif pkgconfig
USE_XORG=	xft xmu xpm xt
USE_AUTOTOOLS=	libtool:env
USE_LDCONFIG=	yes

do-install:
	(cd ${WRKSRC}/lib && ${LIBTOOL} --mode=install ${INSTALL_DATA} \
		libXmHTML.la ${STAGEDIR}${PREFIX}/lib)
	@${MKDIR} ${STAGEDIR}${PREFIX}/include/XmHTML
	(cd ${WRKSRC}/include/XmHTML && ${INSTALL_DATA} *.h \
		${STAGEDIR}${PREFIX}/include/XmHTML)
	@${MKDIR} ${STAGEDIR}${DOCSDIR}
	@(cd ${WRKSRC}/html && ${FIND} . ! -name "*Makefile*" | \
		${CPIO} --quiet -dump -R ${SHAREOWN}:${SHAREGRP} \
		${STAGEDIR}${DOCSDIR})
	@${MKDIR} ${STAGEDIR}${EXAMPLESDIR}
.for i in book contrib examples
	@(cd ${WRKSRC} && ${FIND} ${i} ! -name "*Makefile*" | \
		${CPIO} --quiet -dump -R ${SHAREOWN}:${SHAREGRP} \
		${STAGEDIR}${EXAMPLESDIR})
.endfor

.include <bsd.port.mk>
