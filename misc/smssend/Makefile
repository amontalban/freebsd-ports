# Created by: Miklos Niedermayer <mico@bsd.hu>
# $FreeBSD$

PORTNAME=	smssend
PORTVERSION=	3.5
CATEGORIES=	misc
MASTER_SITES=	${MASTER_SITE_LOCAL}
MASTER_SITE_SUBDIR=	laszlof

MAINTAINER=	ports@FreeBSD.org
COMMENT=	A tool to send a SMS to any GSM

LIB_DEPENDS=	skyutils-2.9.9:${PORTSDIR}/misc/skyutils

WRKSRC=		${WRKDIR}/${PORTNAME}
MAN1=	smssend.1 smssend.scripting.1 email2smssend.1

MANLANG=	"" fr

GNU_CONFIGURE=	yes

NO_STAGE=	yes
post-install:
	${STRIP_CMD} ${PREFIX}/bin/smssend

.include <bsd.port.mk>
