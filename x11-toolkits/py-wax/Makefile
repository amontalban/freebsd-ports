# Created by: Nicola Vitale	<nivit@email.it>
# $FreeBSD$

PORTNAME=	wax
PORTVERSION=	0.3.33
PORTREVISION=	6
CATEGORIES=	x11-toolkits devel python
MASTER_SITES=	SF/${PORTNAME}gui/${PORTNAME}gui/${PORTNAME}-${PORTVERSION}
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	nivit@FreeBSD.org
COMMENT=	A user-friendly layer on top of wxPython

NO_BUILD=	yes
USE_PYTHON=	yes
USE_WX=		2.8
WX_UNICODE=	yes
WX_COMPS=	python:run

DATADIR=	${PYTHON_SITELIBDIR}

FIND_DIRS=	-type d \! -empty
FIND_DATA=	-type f
FIND_DELETE=	\( -name "*.txt" -and -maxdepth 2 \)

.if !defined(WITH_EXAMPLES)
PLIST_SUB=	PORTEXAMPLES="@comment "
.else
PLIST_SUB=	PORTEXAMPLES=""
.endif

NO_STAGE=	yes
do-install:
	@cd ${WRKSRC} && ${FIND} . ${FIND_DIRS} -exec ${MKDIR} ${DATADIR}/{} \;
	@cd ${WRKSRC} && ${FIND} . ${FIND_DELETE} -delete
	@cd ${WRKSRC} && ${FIND} . ${FIND_DATA} -exec ${INSTALL_DATA} {} ${DATADIR}/{} \;
.if !defined(WITH_EXAMPLES)
	${RM} -r ${DATADIR}/${PORTNAME}/examples
.else
	${MV} ${DATADIR}/${PORTNAME}/examples ${EXAMPLESDIR}
.endif

.include <bsd.port.mk>
