# Created by: Baptiste Grenier <gwarf@gwarf.org>
# $FreeBSD$

PORTNAME=	pydf
PORTVERSION=	10
CATEGORIES=	sysutils
MASTER_SITES=	http://kassiopeia.juls.savba.sk/~garabik/software/pydf/
DISTNAME=	${PORTNAME}_${PORTVERSION}

MAINTAINER=	baptiste@bapt.name
COMMENT=	A python implementation of df

LICENSE=	unknown
LICENSE_NAME=	Public Domain
LICENSE_FILE=	${WRKSRC}/COPYING
LICENSE_PERMS=	dist-mirror dist-sell pkg-mirror pkg-sell auto-accept

SUB_FILES=	pkg-message

USES=		shebangfix
USE_PYTHON=	yes
NO_BUILD=	yes

SHEBANG_FILES=	pydf
PLIST_FILES=	bin/pydf etc/pydfrc.sample man/man1/pydf.1.gz

WRKSRC=		${WRKDIR}/${PORTNAME}-${PORTVERSION}

post-patch:
	@${REINPLACE_CMD} -e 's|%%PYTHON_CMD%%|${PYTHON_CMD}| ; \
		s|%%PREFIX%%|${PREFIX}|' ${WRKSRC}/pydf

do-install:
	${INSTALL_SCRIPT} ${WRKSRC}/pydf ${STAGEDIR}${PREFIX}/bin
	${INSTALL_DATA} ${WRKSRC}/pydfrc ${STAGEDIR}${PREFIX}/etc/pydfrc.sample
	${INSTALL_MAN} ${WRKSRC}/pydf.1 ${STAGEDIR}${MANPREFIX}/man/man1

.include <bsd.port.mk>
