# Created by: Martin Dieringer <martin.dieringer@gmx.de>
# $FreeBSD$

PORTNAME=	rtf2latex2e
PORTVERSION=	2.2.2
CATEGORIES=	print
MASTER_SITES=	SF/${PORTNAME}/${PORTNAME}-unix/2-2
DISTNAME=	${PORTNAME}-${PORTVERSION:C|\.|-|g}

MAINTAINER=	martin.dieringer@gmx.de
COMMENT=	Newer filter that converts RTF (MS Rich Text Format) into LaTeX

LICENSE=	GPLv2

USES=		gmake
MAKE_ARGS=	CC=${CC} \
		mandir=${MAN1PREFIX}/man/

.include <bsd.port.mk>
