# Created by: Pedro Giffuni
# $FreeBSD$

PORTNAME=	pdfbox
PORTVERSION=	1.8.5
CATEGORIES=	print textproc java
MASTER_SITES=	${MASTER_SITE_APACHE:S,%SUBDIR%,pdfbox/${PORTVERSION},}
MASTER_SITE_SUBDIR=	${PORTNAME}
DISTFILES=	${JAR_NAMES:S/$/-${PORTVERSION}.jar/}

MAINTAINER=	ale@FreeBSD.org
COMMENT=	Java tool for working with PDF documents

LICENSE=	APACHE20

RUN_DEPENDS=	${JAVAJARDIR}/bcmail.jar:${PORTSDIR}/java/bouncycastle	\
		${JAVALIBDIR}/commons-logging.jar:${PORTSDIR}/java/jakarta-commons-logging

JAR_NAMES=	pdfbox fontbox jempbox preflight xmpbox

USE_JAVA=	yes
NO_EXTRACT=	yes
NO_BUILD=	yes

PLIST_FILES=	${JAR_NAMES:S/^/%%JAVAJARDIR%%\//:S/$/.jar/}

do-install:
	@${ECHO_MSG} -n ">> Installing JAR files in ${JAVAJARDIR}..."
	@${MKDIR} ${STAGEDIR}${JAVAJARDIR}
.for f in ${JAR_NAMES}
	${INSTALL_DATA} ${DISTDIR}/${f}-${PORTVERSION}.jar \
		${STAGEDIR}${JAVAJARDIR}/${f}.jar
.endfor
	@${ECHO_MSG} " [ DONE ]"

.include <bsd.port.mk>
