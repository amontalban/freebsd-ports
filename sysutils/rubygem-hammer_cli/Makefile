# Created by: Michael Moll <kvedulv@kvedulv.de>
# $FreeBSD$

PORTNAME=	hammer_cli
PORTVERSION=	0.1.0
CATEGORIES=	sysutils ruby
MASTER_SITES=	RG

MAINTAINER=	kvedulv@kvedulv.de
COMMENT=	Provides CLI interfaces for Ruby apps

LICENSE=	GPLv3

RUN_DEPENDS=	rubygem-apipie-bindings>=0.0.6:${PORTSDIR}/devel/rubygem-apipie-bindings \
		rubygem-awesome_print>=1.1.0:${PORTSDIR}/devel/rubygem-awesome_print \
		rubygem-clamp>=0.6.3:${PORTSDIR}/devel/rubygem-clamp \
		rubygem-fastercsv>=1.5.5:${PORTSDIR}/devel/rubygem-fastercsv \
		rubygem-fast_gettext>=0.8.1:${PORTSDIR}/devel/rubygem-fast_gettext \
		rubygem-highline>=1.6.20:${PORTSDIR}/devel/rubygem-highline \
		rubygem-json>=1.8.1:${PORTSDIR}/devel/rubygem-json \
		rubygem-locale=2.0.8:${PORTSDIR}/devel/rubygem-locale \
		rubygem-logging>=1.8.1:${PORTSDIR}/devel/rubygem-logging \
		rubygem-mime-types>=1.0:${PORTSDIR}/misc/rubygem-mime-types \
		rubygem-rest-client>=1.6.7:${PORTSDIR}/www/rubygem-rest-client \
		rubygem-table_print>=1.5.1:${PORTSDIR}/devel/rubygem-table_print

USE_RUBY=	yes
USE_RUBYGEMS=	yes
RUBYGEM_AUTOPLIST=	yes

.include <bsd.port.pre.mk>

post-install:
		${MKDIR} ${STAGEDIR}${PREFIX}/etc/hammer
		${MKDIR} ${STAGEDIR}${PREFIX}/etc/hammer/cli.modules.d
		${INSTALL_DATA} ${FILESDIR}/cli_config.yml.sample ${STAGEDIR}${PREFIX}/etc/hammer/cli_config.yml.sample

.include <bsd.port.post.mk>
