# Created by: Pete Fritchman <petef@databits.net>
# $FreeBSD$

PORTNAME=	devtodo
PORTVERSION=	0.1.20
PORTREVISION=	1
CATEGORIES=	devel
MASTER_SITES=	http://swapoff.org/files/devtodo/

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Tool to effectively maintain todo lists aimed at developers

CONFLICTS=	tdl-[0-9]* todo-[0-9]*

GNU_CONFIGURE=	yes

OPTIONS_DEFINE=	EXAMPLES

# Note: without this define util/regex.c doesn't compile due to redeclaration
# of malloc and realloc functions. Adding this define was the simplest
# (although not elegant) solution.
CFLAGS+=	-DSTDC_HEADERS

post-patch:
	@${REINPLACE_CMD} -e 's/^\ttest -f.*todorc.*\n//' ${WRKSRC}/doc/Makefile.in

post-install:
	@${MKDIR} ${STAGEDIR}${EXAMPLESDIR}
.for file in scripts.sh scripts.tcsh todorc.example
	${INSTALL_DATA} ${WRKSRC}/doc/${file} ${STAGEDIR}${EXAMPLESDIR}
.endfor
	${INSTALL_DATA} ${WRKSRC}/doc/todorc.example ${STAGEDIR}${PREFIX}/etc/todorc.sample

.include <bsd.port.mk>
