# Created by: rmallory@csusb.edu
# $FreeBSD$

PORTNAME=	rplay
PORTVERSION=	3.3.2
PORTREVISION=	3
CATEGORIES=	audio
MASTER_SITES=	http://rplay.doit.org/dist/

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Network audio player

LIB_DEPENDS=	libgsm.so:${PORTSDIR}/audio/gsm

USE_LDCONFIG=	yes
GNU_CONFIGURE=	yes
CONFIGURE_ENV=	LIBS="-L${LOCALBASE}/lib"
CPPFLAGS+=	-I${LOCALBASE}/include

INFO=		RPLAY RPTP librplay rplayd

.include <bsd.port.pre.mk>

USE_RC_SUBR=	rplayd

.if ${ARCH} == "amd64"
# pr ports/166658 mentions a problem with amd64. if it happens on i386, you can delete this conditional
# and rename to patch-ao
EXTRA_PATCHES=	${FILESDIR}/extra-patch-ao
.endif

post-extract:
	@${CP} ${WRKSRC}/doc/rplay.texi ${WRKSRC}/doc/rplayd.texi

post-patch:
	@${REINPLACE_CMD} -E \
		's,(bin|include|info|lib|man|sbin)dir),DESTDIR)$$(&,' \
		${WRKSRC}/include/Makefile.in \
		${WRKSRC}/librplay/Makefile.in \
		${WRKSRC}/rplayd/Makefile.in \
		${WRKSRC}/rplay/Makefile.in \
		${WRKSRC}/rptp/Makefile.in \
		${WRKSRC}/doc/Makefile.in

post-install:
.for file in rplay.conf rplay.helpers rplay.servers rplay.hosts
	${CP} ${WRKSRC}/etc/${file} ${STAGEDIR}${PREFIX}/etc/${file}.sample
.endfor
	@${ECHO_CMD} localhost > ${STAGEDIR}${PREFIX}/etc/rplay.hosts.sample

.include <bsd.port.post.mk>
