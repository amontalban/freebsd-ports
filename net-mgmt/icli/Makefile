# $FreeBSD$

PORTNAME=	icli
DISTVERSION=	0.46
PORTREVISION=	1
CATEGORIES=	net-mgmt perl5
MASTER_SITES=	http://finalrewind.org/projects/icli/

MAINTAINER=	lme@FreeBSD.org
COMMENT=	Command line interface to Icinga

LICENSE=	ICLI
LICENSE_NAME=	ICLI license
LICENSE_FILE=	${WRKSRC}/COPYING
LICENSE_PERMS=	dist-mirror dist-sell pkg-mirror pkg-sell auto-accept

RUN_DEPENDS=	p5-List-MoreUtils>=0:${PORTSDIR}/lang/p5-List-MoreUtils \
		p5-Term-Size>=0:${PORTSDIR}/devel/p5-Term-Size \
		icinga:${PORTSDIR}/net-mgmt/icinga

CONFIGURE_ARGS+=	--destdir ${STAGEDIR}

USES=		perl5
USE_PERL5=	modbuild

PLIST_FILES=	bin/${PORTNAME} man/man1/${PORTNAME}.1.gz

post-patch:
		@${REINPLACE_CMD} -i '' 's|/var/[^/]*/icinga|/var/spool/icinga|' \
			${WRKSRC}/bin/${PORTNAME}

.include <bsd.port.mk>
