# Created by: Heiner <h.eichmann@gmx.de>
# $FreeBSD$

PORTNAME=	krusader
DISTVERSION=	2.4.0-beta3
PORTREVISION=	1
CATEGORIES=	x11-fm kde
MASTER_SITES=	SF/${PORTNAME}/${PORTNAME}/${DISTVERSION}/

MAINTAINER=	fluffy@FreeBSD.org
COMMENT=	Twin panel file manager for KDE, like midnight or norton commander

USE_BZIP2=	yes
USES=		cmake:outsource gettext
USE_KDE4=	kdelibs kdeprefix kdehier automoc4
USE_QT4=	moc_build qmake_build rcc_build uic_build

.include <bsd.port.mk>
