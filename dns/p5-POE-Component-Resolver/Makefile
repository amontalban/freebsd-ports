# Created by: Jase Thew <freebsd@beardz.net>
# $FreeBSD$

PORTNAME=	POE-Component-Resolver
PORTVERSION=	0.921
CATEGORIES=	dns devel perl5
MASTER_SITES=	CPAN
MASTER_SITE_SUBDIR=	CPAN:RCAPUTO
PKGNAMEPREFIX=	p5-

MAINTAINER=	jase@FreeBSD.org
COMMENT=	A non-blocking getaddrinfo() resolver

LICENSE=	ART10 GPLv1
LICENSE_COMB=	dual

BUILD_DEPENDS=	p5-POE>=1.311:${PORTSDIR}/devel/p5-POE \
		p5-Socket>=2.001:${PORTSDIR}/net/p5-Socket
RUN_DEPENDS:=	${BUILD_DEPENDS}

USES=		perl5
USE_PERL5=	configure

.include <bsd.port.mk>
