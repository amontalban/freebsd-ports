# Created by: trasz <trasz@pin.if.uz.zgora.pl>
# $FreeBSD$

PORTNAME=	encfs
PORTVERSION=	1.7.4
PORTREVISION=	5
CATEGORIES=	sysutils
MASTER_SITES=	${MASTER_SITE_GOOGLE_CODE}
PKGNAMEPREFIX=	fusefs-
EXTRACT_SUFX=	.tgz

MAINTAINER=	ports@FreeBSD.org
COMMENT=	An encrypted pass-through FUSE filesystem

LIB_DEPENDS=	librlog.so:${PORTSDIR}/devel/rlog \
		libboost_serialization.so:${PORTSDIR}/devel/boost-libs

WRKSRC=		${WRKDIR}/encfs-${PORTVERSION}

GNU_CONFIGURE=	yes
CONFIGURE_ARGS=	--with-boost-serialization=boost_serialization \
		--with-boost-system=boost_system \
		--with-boost-filesystem=boost_filesystem
CPPFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-L${LOCALBASE}/lib
USES=		fuse gmake libtool:keepla pkgconfig
USE_LDCONFIG=	yes
USE_OPENSSL=	yes

OPTIONS_DEFINE=	NLS
OPTIONS_SUB=	yes
NLS_USES=	gettext
NLS_CONFIGURE_ENABLE=	nls

post-patch:
	@${FIND} ${WRKSRC}/encfs -type f | ${XARGS} ${REINPLACE_CMD} -E \
		's/(^|[[:space:]])(shared_ptr)/\1boost::\2/g'

.include <bsd.port.mk>
