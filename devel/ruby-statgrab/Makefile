# Created by: Tim Bishop <tdb@FreeBSD.org>
# $FreeBSD$

PORTNAME=	statgrab
PORTVERSION=	0.1
PORTREVISION=	1
CATEGORIES=	devel ruby
MASTER_SITES=	RF
PKGNAMEPREFIX=	${RUBY_PKGNAMEPREFIX}
DIST_SUBDIR=	ruby

MAINTAINER=	tdb@FreeBSD.org
COMMENT=	A set of Ruby bindings for libstatgrab

LIB_DEPENDS=	libstatgrab0.so:${PORTSDIR}/devel/libstatgrab0

USE_RUBY=	yes
USE_RUBY_EXTCONF=	yes
USES=		pkgconfig

INSTALL_TARGET=	site-install

post-install:
	${MKDIR} ${STAGEDIR}${RUBY_MODDOCDIR}
	${INSTALL_DATA} ${WRKSRC}/README.mkdn ${STAGEDIR}${RUBY_MODDOCDIR}

.include <bsd.port.mk>
