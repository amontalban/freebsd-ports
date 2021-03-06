# Created by: Steve Wills <swills@FreeBSD.org>
# $FreeBSD$

PORTNAME=		rubyrep
PORTVERSION=		1.2.0
CATEGORIES=		databases rubygems
MASTER_SITES=		RG

MAINTAINER=		ltning@anduin.net
COMMENT=		Multi-master replication and sync for MySQL and PostgreSQL

BUILD_DEPENDS=	rubygem-activesupport>=${PORTVERSION}:${PORTSDIR}/devel/rubygem-activesupport \
		rubygem-activerecord>=${PORTVERSION}:${PORTSDIR}/databases/rubygem-activerecord
RUN_DEPENDS+=	flog>=0:${PORTSDIR}/sysutils/flog \
		rubygem-activesupport>=${PORTVERSION}:${PORTSDIR}/devel/rubygem-activesupport \
		rubygem-activerecord>=${PORTVERSION}:${PORTSDIR}/databases/rubygem-activerecord

USE_RUBY=		yes
USE_RUBYGEMS=		yes
RUBYGEM_AUTOPLIST=	yes

USE_RC_SUBR=	rubyrep

OPTIONS_DEFINE=	MYSQL PGSQL
OPTIONS_DEFAULT=	PGSQL

PLIST_FILES=	bin/rubyrep

.include <bsd.port.options.mk>

.if ${PORT_OPTIONS:MPGSQL}
RUN_DEPENDS+=	rubygem-pg>=0:${PORTSDIR}/databases/rubygem-pg
.endif

.if ${PORT_OPTIONS:MMYSQL}
RUN_DEPENDS+=	ruby-mysql>=0:${PORTSDIR}/databases/ruby-mysql
.endif

.include <bsd.port.mk>
