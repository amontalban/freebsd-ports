# Created by: Nicola Vitale <nivit@email.it>
# $FreeBSD$

PORTNAME=	wxMaxima
PORTVERSION=	13.04.2
PORTREVISION=	2
CATEGORIES=	math
MASTER_SITES=	SF
MASTER_SITE_SUBDIR=	${PORTNAME:tl}/${PORTNAME}/${PORTVERSION}
#MASTER_SITE_SUBDIR=	${PORTNAME:tl}/${PORTNAME}/${PORTVERSION}

MAINTAINER=	nivit@FreeBSD.org
COMMENT=	A wxWidgets GUI for the computer algebra system maxima

LICENSE=	GPLv2

RUN_DEPENDS=	maxima:${PORTSDIR}/math/maxima

USES=		gettext
USE_GNOME=	desktopfileutils libxml2
USE_WX=		2.8
WX_COMPS=	wx
WX_CONF_ARGS=	absolute
WANT_UNICODE=	yes
GNU_CONFIGURE=	yes
CONFIGURE_ARGS=	--program-prefix=

PLIST_SUB=	DESKTOPDIR=${DESKTOPDIR:S,${PREFIX}/,,}

NO_STAGE=	yes
post-install:
	@${LN} -s ${DATADIR}/wxmaxima.png ${PREFIX}/share/pixmaps/wxmaxima.png
	@${LOCALBASE}/bin/desktop-file-install \
		--mode=${SHAREMODE} --dir=${DESKTOPDIR} \
		--rebuild-mime-info-cache ${WRKSRC}/${PORTNAME:tl}.desktop
# 		--rebuild-mime-info-cache ${WRKSRC}/${PORTNAME:tl}.desktop
	@${CAT} ${PKGMESSAGE}

.include <bsd.port.mk>
