# Created by: Romain Tartiere <romain@blogreen.org>
# $FreeBSD$

PORTNAME=	mono-basic
PORTVERSION=	2.10
CATEGORIES=	lang
MASTER_SITES=	http://ftp.novell.com/pub/mono/sources/${PORTNAME}/

MAINTAINER=	mono@FreeBSD.org
COMMENT=	VisualBasic.NET support for Mono

BUILD_DEPENDS=	mono:${PORTSDIR}/lang/mono
RUN_DEPENDS=	mono:${PORTSDIR}/lang/mono

USE_BZIP2=	yes
HAS_CONFIGURE=	yes
CONFIGURE_ARGS=	--prefix=${PREFIX}
USES=		gmake

tests: build
	@${ECHO_MSG} "===> Running ${PORTNAME} regression tests"
	@(cd ${WRKSRC} && ${SETENV} ${MAKE_ENV} ${GMAKE} \
		${MAKE_FLAGS} Makefile ${MAKE_ARGS} test)

.include <bsd.port.mk>
