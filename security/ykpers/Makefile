# $FreeBSD$

PORTNAME=	ykpers
PORTVERSION=	1.15.0
CATEGORIES=	security
MASTER_SITES=	http://opensource.yubico.com/yubikey-personalization/releases/

MAINTAINER=	matt@mjslabs.com
COMMENT=	Library and tool for personalization of Yubico's YubiKey

LICENSE=	BSD2CLAUSE

LIB_DEPENDS=	libyubikey.so:${PORTSDIR}/security/libyubikey

GNU_CONFIGURE=	yes
USE_LDCONFIG=	yes
USES=		pkgconfig

PLIST_FILES=	bin/ykchalresp \
		bin/ykinfo \
		bin/ykpersonalize \
		include/ykpers-1/ykcore.h \
		include/ykpers-1/ykdef.h \
		include/ykpers-1/ykpbkdf2.h \
		include/ykpers-1/ykpers.h \
		include/ykpers-1/ykpers-version.h \
		include/ykpers-1/ykstatus.h \
		lib/libykpers-1.la \
		lib/libykpers-1.so \
		lib/libykpers-1.so.16 \
		libdata/pkgconfig/ykpers-1.pc \
		man/man1/ykchalresp.1.gz \
		man/man1/ykinfo.1.gz \
		man/man1/ykpersonalize.1.gz
PLIST_DIRS=	include/ykpers-1

OPTIONS_DEFINE=	STATIC

STATIC_CONFIGURE_ENABLE=	static
STATIC_PLIST_FILES=		lib/libykpers-1.a

MAKE_JOBS_UNSAFE=	yes

LDFLAGS+=	-L/usr/lib

post-patch:
	@${REINPLACE_CMD} -e 's|^pkgconfigdir = .*|pkgconfigdir = /usr/local/libdata/pkgconfig|g' \
		${WRKSRC}/Makefile.in

regression-test: build
	@(cd ${WRKSRC}; ${MAKE} check)

.include <bsd.port.mk>
