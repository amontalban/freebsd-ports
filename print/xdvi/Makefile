# Created by: Jean-Marc Zucconi <jmz@FreeBSD.org>
# $FreeBSD$

PORTNAME=	xdvi
PORTVERSION=	pl20
PORTREVISION=	4
CATEGORIES=	print
MASTER_SITES=	${MASTER_SITE_XCONTRIB}
MASTER_SITE_SUBDIR=	applications
DISTNAME=	${PORTNAME}-20
EXTRACT_SUFX=	.tar.Z
DIST_SUBDIR=	${PORTNAME}

MAINTAINER=	ports@FreeBSD.org
COMMENT=	DVI previewer for the X Window System

CONFLICTS=	teTeX-*

USES=		gmake imake:notall
USE_XORG=	ice sm x11 xaw xext xmu xt xpm
PKGINSTALL=	${WRKDIR}/pkg-install
PKGDEINSTALL=	${WRKDIR}/pkg-deinstall
PLIST_SUB=	LOCALBASE=${LOCALBASE}
.if defined(PACKAGE_BUILDING)
SCRIPTS_ENV=	PACKAGE_BUILDING=${PACKAGE_BUILDING}
.else
IS_INTERACTIVE=	yes
.endif

MAN1=		xdvi.1

NO_STAGE=	yes
post-configure:
	@${REINPLACE_CMD} -e "s=distclean::=distclean:=g" ${WRKSRC}/Makefile
.for F in pkg-install pkg-deinstall
	${SED}	-e "s=%%PREFIX%%=${PREFIX}=" \
		-e "s=%%LOCALBASE%%=${LOCALBASE}=" \
		< ${PKGDIR}/${F} > ${WRKDIR}/${F}
.endfor

do-install:
	@(cd ${WRKSRC}; ${GMAKE} install.man \
		MANDIR=${PREFIX}/man/man1 MANSUFFIX=1)
	@(cd ${WRKSRC}; ${GMAKE} ${MAKE_FLAGS} ${MAKEFILE} xdvi.man)
	@(cd ${WRKSRC}; ${GMAKE} -f Makefile install BINDIR=${PREFIX}/bin)
	@(cd ${WRKSRC}; ${INSTALL_SCRIPT} MakeTeXPK ${PREFIX}/bin)

post-install:
	@if [ -f ${WRKDIR}/post-install ]; then ${SH} ${WRKDIR}/post-install; fi

.include <bsd.port.mk>
