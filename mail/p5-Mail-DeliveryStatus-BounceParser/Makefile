# Created by: Alexander Zhuravlev <zaa@zaa.pp.ru>
# $FreeBSD$

PORTNAME=	Mail-DeliveryStatus-BounceParser
PORTVERSION=	1.5.34
CATEGORIES=	mail perl5
MASTER_SITES=	CPAN
PKGNAMEPREFIX=	p5-
DISTNAME=	${PORTNAME}-${PORTVERSION:R}${PORTVERSION:E}

MAINTAINER=	chifeng@gmail.com
COMMENT=	Perl extension to analyze bounce messages

RUN_DEPENDS=	p5-MIME-Tools>=5.418:${PORTSDIR}/mail/p5-MIME-Tools \
		p5-Mail-Tools>=2.04:${PORTSDIR}/mail/p5-Mail-Tools
BUILD_DEPENDS:=	${RUN_DEPENDS}

USES=		perl5
USE_PERL5=	configure

.include <bsd.port.mk>
