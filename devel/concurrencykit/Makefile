# Created by: Kubilay Kocak <koobs@FreeBSD.org>
# $FreeBSD$

PORTNAME=	concurrencykit
PORTVERSION=	0.4.1
CATEGORIES=	devel
MASTER_SITES=	http://concurrencykit.org/releases/ \
		http://repnop.org/releases/
DISTNAME=	ck-${PORTVERSION}

MAINTAINER=	koobs@FreeBSD.org
COMMENT=	Lock-free data structures for high performance concurrent systems

LICENSE=	BSD2CLAUSE

OPTIONS_DEFINE=	RTM VMAPACK
OPTIONS_DEFAULT=RTM VMAPACK

RTM_DESC=	Restricted Transactional Memory (x86_64 only)
VMAPACK_DESC=	Enable pointer packing

RTM_CONFIGURE_ON=	--enable-rtm
VMAPACK_CONFIGURE_ON=	--enable-pointer-packing

USES=		pkgconfig
USE_LDCONFIG=	yes
HAS_CONFIGURE=	yes

CONFIGURE_ARGS+=	--mandir=${PREFIX}/man

PLIST_SUB+=	VERSION=${PORTVERSION}

post-extract:
	${REINPLACE_CMD} -e 's|PKGCONFIG_DATA=@LIBRARY@|PKGCONFIG_DATA=${PREFIX}/libdata/|g' \
	${WRKSRC}/Makefile.in

regression-test: build
	@cd ${WRKSRC} && ${MAKE} check

.include <bsd.port.mk>
