# Created by: joseph@randomnetworks.com
# $FreeBSD$

PORTNAME=	adtool
PORTVERSION=	1.3.3
CATEGORIES=	sysutils
MASTER_SITES=	http://gp2x.org/adtool/

MAINTAINER=	joseph@randomnetworks.com
COMMENT=	Active Directory administration tool

USES=		gmake
USE_OPENLDAP=	yes
USE_AUTOTOOLS=	libtool

CONFIGURE_ARGS+=--with-ldap=${LOCALBASE}

PLIST_FILES=	bin/adtool \
		etc/adtool.cfg.dist \
		man/man1/adtool.1.gz

LICENSE=	GPLv2
LICENSE_FILE=	${WRKSRC}/COPYING

.include <bsd.port.mk>
