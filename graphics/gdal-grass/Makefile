# Created by: Laurent Courty
# $FreeBSD$

PORTNAME=	gdal-grass
PORTVERSION=	1.4.3
PORTREVISION=	13
CATEGORIES=	graphics
MASTER_SITES=	http://download.osgeo.org/gdal/

MAINTAINER=	ports@FreeBSD.org
COMMENT=	GDAL drivers for GRASS raster and vector files

BROKEN=		Fails to configure

BUILD_DEPENDS=	grass>6:${PORTSDIR}/databases/grass
LIB_DEPENDS=	libgdal.so:${PORTSDIR}/graphics/gdal
RUN_DEPENDS=	grass>6:${PORTSDIR}/databases/grass

GRASS_INST_DIR=	grass-6.4.2
WRKSRC=		${WRKDIR}/${PORTNAME}-${PORTVERSION}
USES=		gmake
GNU_CONFIGURE=	yes
CONFIGURE_ARGS=	--with-gdal=${LOCALBASE}/bin/gdal-config \
		--with-grass=${LOCALBASE}/${GRASS_INST_DIR} \
		--with-autoload=${GDAL_AUTOLOAD_DIR}
ALL_TARGET=
NO_STAGE=	yes

.include <bsd.port.pre.mk>

pre-install:
	${MKDIR} ${PREFIX}/share/gdal

.if !defined(GDAL_AUTOLOAD_DIR)
GDAL_AUTOLOAD_DIR=${PREFIX}/lib/gdalplugins
.endif

.if !defined (GRASS_INST_DIR)
GRASS_INST_DIR=	grass
.endif

.include <bsd.port.post.mk>
