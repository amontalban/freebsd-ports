# Created by: ijliao
# $FreeBSD$

PORTNAME=	libdvdcss
PORTVERSION=	1.2.12
PORTREVISION=	1
CATEGORIES=	multimedia
MASTER_SITES=	http://download.videolan.org/pub/%SUBDIR%/
MASTER_SITE_SUBDIR=	${PORTNAME}/${PORTVERSION}

MAINTAINER=	jpaetzel@FreeBSD.org
COMMENT=	Portable abstraction library for DVD decryption

RESTRICTED=	CSS code may violate the DMCA

GNU_CONFIGURE=	yes
INSTALL_TARGET=	install-strip
USES=		gmake libtool pathfix tar:bzip2
USE_LDCONFIG=	yes

OPTIONS_DEFINE=	DOXYGEN

.include <bsd.port.options.mk>

.if ${PORT_OPTIONS:MDOXYGEN}
BUILD_DEPENDS+=	doxygen:${PORTSDIR}/devel/doxygen
PORTDOCS=	*
.endif

post-patch:
.if ${PORT_OPTIONS:MDOXYGEN}
# we do not want the latex documents... too many dependencies just
# to get in ps what we already have in html
	@${REINPLACE_CMD} '/^all:/s/stamp-latex//' ${WRKSRC}/doc/Makefile.in
.else
	@${REINPLACE_CMD} '/^SUBDIRS =/s/doc//' ${WRKSRC}/Makefile.in
.endif

post-install:
.if ${PORT_OPTIONS:MDOXYGEN}
	${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${INSTALL_WRKSRC}/doc/html/* ${STAGEDIR}${DOCSDIR}
.endif

.include <bsd.port.mk>
