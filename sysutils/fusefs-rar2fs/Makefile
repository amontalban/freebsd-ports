# Created by: Joris Vandalon
# $FreeBSD$

PORTNAME=	rar2fs
PORTVERSION=	1.15.1
PORTREVISION=	1
CATEGORIES=	sysutils
MASTER_SITES=	${MASTER_SITE_GOOGLE_CODE}:rar2fs http://www.rarlab.com/rar/:unrarsrc
PKGNAMEPREFIX=	fusefs-
DISTFILES=	rar2fs-1.15.1.tar.gz:rar2fs unrarsrc-4.2.4.tar.gz:unrarsrc

MAINTAINER=	joris@vandalon.nl
COMMENT=	Mount rar archives as filesystem

LICENSE=	GPLv3

LIB_DEPENDS=	libexecinfo.so:${PORTSDIR}/devel/libexecinfo \
		libunrar.so:${PORTSDIR}/archivers/libunrar4

GNU_CONFIGURE=	yes
CONFIGURE_ARGS=	--with-fuse-lib=${LOCALBASE}/lib \
	--with-fuse=${LOCALBASE}/include/fuse \
	--with-unrar=${WRKDIR}/unrar \
	--with-unrar-lib=${LOCALBASE}/lib

PLIST_FILES=	bin/${PORTNAME} man/man1/rar2fs.1.gz
USES=		fuse gmake

post-patch:
	@${REINPLACE_CMD} 's/-lstdc++/-lexecinfo/' ${WRKSRC}/Makefile.in

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/${PORTNAME} ${STAGEDIR}${PREFIX}/bin
	${INSTALL_MAN} ${WRKSRC}/rar2fs.1 ${STAGEDIR}${PREFIX}/man/man1

.include <bsd.port.mk>
