# $FreeBSD$

PORTNAME=	clisp-hyperspec
PORTVERSION=	7.0
CATEGORIES=	devel lisp
MASTER_SITES=	ftp://ftp.lispworks.com/pub/software_tools/reference/
DISTNAME=	HyperSpec-7-0

MAINTAINER=	olgeni@FreeBSD.org
COMMENT=	A Common Lisp reference in HTML format, from LispWorks Ltd

NO_CDROM=	Commercial redistribution prohibited

WRKSRC=		${WRKDIR}
NO_BUILD=	yes

do-install:
	@${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${WRKSRC}/HyperSpec-Legalese.text ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${WRKSRC}/HyperSpec-README.text ${STAGEDIR}${DOCSDIR}
	${CP} -r ${WRKSRC}/HyperSpec ${STAGEDIR}${DOCSDIR}

.include <bsd.port.mk>
