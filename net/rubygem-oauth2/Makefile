# Created by: Sunpoet Po-Chuan Hsieh <sunpoet@FreeBSD.org>
# $FreeBSD$

PORTNAME=	oauth2
PORTVERSION=	0.9.3
CATEGORIES=	net rubygems
MASTER_SITES=	RG

MAINTAINER=	sunpoet@FreeBSD.org
COMMENT=	Ruby wrapper for the OAuth 2.0 protocol

LICENSE=	MIT

RUN_DEPENDS=	rubygem-faraday>=0.8:${PORTSDIR}/www/rubygem-faraday \
		rubygem-jwt>=0.1.8:${PORTSDIR}/www/rubygem-jwt \
		rubygem-multi_json>=1.3:${PORTSDIR}/devel/rubygem-multi_json \
		rubygem-multi_xml>=0.5:${PORTSDIR}/textproc/rubygem-multi_xml \
		rubygem-rack>=1.2:${PORTSDIR}/www/rubygem-rack

USE_RUBY=	yes
USE_RUBYGEMS=	yes
RUBYGEM_AUTOPLIST=	yes

.include <bsd.port.mk>
