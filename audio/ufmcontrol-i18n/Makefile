# Created by: Nicola Vitale <nivit@users.sourceforge.net>
# $FreeBSD$

PORTNAME=		ufmcontrol-i18n
PORTVERSION=		0.3.1
CATEGORIES=		audio
MASTER_SITES=		SF/ufmcontrol/${PORTNAME}/${PORTVERSION}

MAINTAINER=		nivit@FreeBSD.org
COMMENT=		USB radio control utility

RUN_DEPENDS=		snack>=2.2.10_4:${PORTSDIR}/audio/snack

USES=			tcl
USE_LDCONFIG=		yes
MAKE_ENV=		NO_PROFILE=yes

pre-install:
	@${MKDIR} ${STAGEDIR}${MAN1PREFIX}/man/it.ISO8859-1/man1
	@${MKDIR} ${STAGEDIR}${DOCSDIR}

.include <bsd.port.mk>
