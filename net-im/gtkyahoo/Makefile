# Created by: dannyman@dannyland.org
# $FreeBSD$

PORTNAME=	gtkyahoo
PORTVERSION=	0.18.3
PORTREVISION=	4
CATEGORIES=	net-im
MASTER_SITES=	SF

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Yahoo Messenger Client using GTK

USE_GNOME=	gtk12
USES=		bison
GNU_CONFIGURE=	yes
USE_LDCONFIG=	yes
ONLY_FOR_ARCHS=	i386

NO_STAGE=	yes
post-patch:
	@${REINPLACE_CMD} -e '/@INSTALL@/s/$$INSTALL/${INSTALL}/; \
		s/echo aout/echo elf/' \
		${WRKSRC}/libyahoo/configure

.include <bsd.port.mk>
