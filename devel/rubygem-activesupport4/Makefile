# Created by: Jonathan Weiss (<jw@innerewut.de>)
# $FreeBSD$

PORTNAME=	activesupport
PORTVERSION=	4.0.2
CATEGORIES=	devel rubygems
MASTER_SITES=	RG
PKGNAMESUFFIX=	4

MAINTAINER=	ruby@FreeBSD.org
COMMENT=	Utility classes and extension that are required by Rails MVC Framework

LICENSE=	MIT

RUN_DEPENDS=	rubygem-i18n>=0.6.4:${PORTSDIR}/devel/rubygem-i18n \
		rubygem-minitest4>=4.2:${PORTSDIR}/devel/rubygem-minitest4 \
		rubygem-multi_json>=1.3:${PORTSDIR}/devel/rubygem-multi_json \
		rubygem-thread_safe>=0.1:${PORTSDIR}/devel/rubygem-thread_safe \
		rubygem-tzinfo>=0.3.37:${PORTSDIR}/devel/rubygem-tzinfo

USE_RUBY=	yes
USE_RUBYGEMS=	yes
USE_RUBY_FEATURES=	iconv
RUBYGEM_AUTOPLIST=	yes

NOPORTDOCS=	yes

.include <bsd.port.mk>
