# Created by: Gerrit Beine <tux@pinguru.net>
# $FreeBSD$

PORTNAME=	typo3
PORTVERSION=	6.1.8
CATEGORIES=	www
MASTER_SITES=	SF/${PORTNAME}/TYPO3%20Source%20and%20Dummy/TYPO3%20${PORTVERSION}

MAINTAINER=	freebsd-ports@charlieroot.de
COMMENT=	The typo3 content management system

LICENSE=	GPLv2

PORTSCOUT=	limit:^6\.1\.

NO_BUILD=	yes
USE_PHP=	ctype filter json mysqli pcre session xml
WANT_PHP_WEB=	yes

TYPO3WWW=	www
TYPO3RELEASE=
TYPO3SITE=	${TYPO3WWW}/${PORTNAME}
TYPO3PKG=	${PORTNAME}-${PORTVERSION}
TYPO3SRC=	${PORTNAME}_src-${PORTVERSION}
TYPO3DUMMY=	dummy-${PORTVERSION}

USERS=		${WWWOWN}
GROUPS=		${WWWGRP}

PLIST_SUB+=	PORTVERSION="${PORTVERSION}" \
		WWWOWN=${WWWOWN} WWWGRP=${WWWGRP}

DISTFILES+=	${TYPO3SRC}${EXTRACT_SUFX} ${TYPO3DUMMY}${EXTRACT_SUFX}

OPTIONS_DEFINE=	APC CURL GD IMAGICK MBSTRING MYSQL ZLIB
APC_DESC=	Alternative PHP Cache
GD_DESC=	GDlib/freetype support
IMAGICK_DESC=	${IMAGEMAGICK_DESC}
MBSTRING_DESC=	${MULTIBYTE_DESC}
MYSQL_DESC=	Install MySQL Server

APC_USE=	PHP=apc
CURL_USE=	PHP=curl
GD_USE=		PHP=gd
MBSTRING_USE=	PHP=mbstring
MYSQL_USE=	MYSQL=server
ZLIB_USE=	PHP=zlib

.include <bsd.port.options.mk>

.if ${PORT_OPTIONS:MIMAGICK}
.if ${PORT_OPTIONS:MX11}
RUN_DEPENDS+=	convert:${PORTSDIR}/graphics/ImageMagick
.else
RUN_DEPENDS+=	convert:${PORTSDIR}/graphics/ImageMagick-nox11
.endif
.endif

pre-install:
	@if [ -f ${WRKDIR}/${TYPO3DUMMY}/typo3conf/LocalConfiguration.php ]; then \
		${MV} ${WRKDIR}/${TYPO3DUMMY}/typo3conf/LocalConfiguration.php \
			${WRKDIR}/${TYPO3DUMMY}/typo3conf/LocalConfiguration.php.dist; \
	fi

do-install:
	${CP} -R ${WRKDIR}/${TYPO3DUMMY}/ ${STAGEDIR}${PREFIX}/${TYPO3SITE}
	${CP} -R ${WRKDIR}/${TYPO3SRC} ${STAGEDIR}${PREFIX}/${TYPO3WWW}
	${RM} ${STAGEDIR}${PREFIX}/${TYPO3SITE}/typo3_src && \
		${LN} -s ../${TYPO3SRC} ${STAGEDIR}${PREFIX}/${TYPO3SITE}/typo3_src

.include <bsd.port.mk>
