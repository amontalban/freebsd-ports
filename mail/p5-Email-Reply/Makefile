# Created by: Kay Abendroth <kay.abendroth@raxion.net>
# $FreeBSD$

PORTNAME=	Email-Reply
PORTVERSION=	1.203
CATEGORIES=	mail perl5
MASTER_SITES=	CPAN
PKGNAMEPREFIX=	p5-

MAINTAINER=	5u623l20@gmail.com
COMMENT=	Email::Reply - Reply to a Message

LICENSE=	ART10 GPLv1
LICENSE_COMB=	dual

BUILD_DEPENDS=	p5-Email-Abstract>=2.01:${PORTSDIR}/mail/p5-Email-Abstract \
		p5-Email-Address>=1.80:${PORTSDIR}/mail/p5-Email-Address \
		p5-Email-MIME>=1.82:${PORTSDIR}/mail/p5-Email-MIME
RUN_DEPENDS:=	${BUILD_DEPENDS}
TEST_DEPENDS=	p5-Capture-Tiny>=0:${PORTSDIR}/devel/p5-Capture-Tiny

USES=		perl5
USE_PERL5=	configure

.include <bsd.port.mk>
