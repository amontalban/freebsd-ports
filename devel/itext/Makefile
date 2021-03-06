# Created by: Ying-Chieh Liao <ijliao@FreeBSD.org>
# $FreeBSD$

PORTNAME=	itext
PORTVERSION=	4.2.0
PORTREVISION=	4
PORTEPOCH=	1
CATEGORIES=	devel java
MASTER_SITES=	${MASTER_SITE_LOCAL}
MASTER_SITE_SUBDIR=	ale

MAINTAINER=	ale@FreeBSD.org
COMMENT=	A Java-PDF Library

LICENSE=	MPL LGPL20
LICENSE_COMB=	dual

BUILD_DEPENDS=	${JAVAJARDIR}/bcmail.jar:${PORTSDIR}/java/bouncycastle \
		${JAVAJARDIR}/dom4j.jar:${PORTSDIR}/textproc/dom4j \
		${JAVAJARDIR}/pdf-renderer.jar:${PORTSDIR}/print/pdf-renderer
RUN_DEPENDS=	${JAVAJARDIR}/bcmail.jar:${PORTSDIR}/java/bouncycastle \
		${JAVAJARDIR}/dom4j.jar:${PORTSDIR}/textproc/dom4j \
		${JAVAJARDIR}/pdf-renderer.jar:${PORTSDIR}/print/pdf-renderer

OPTIONS=	DOCS

USES=		tar:bzip2
USE_JAVA=	yes
JAVA_VERSION=	1.6+
USE_ANT=	yes
ALL_TARGET=	jar jar.rtf jar.rups
MAKE_ENV=	ANT_INCLUDE_SHARED_JARS=YES

PLIST_FILES=	%%JAVAJARDIR%%/${PORTNAME}.jar \
		%%JAVAJARDIR%%/${PORTNAME}-rtf.jar \
		%%JAVAJARDIR%%/${PORTNAME}-rups.jar \
		bin/${PORTNAME}-rups

PORTDOCS=	*

.include <bsd.port.options.mk>

.if ${PORT_OPTIONS:MDOCS}
ALL_TARGET+=	javadoc
.endif

do-install:
	@${INSTALL_DATA} ${WRKDIR}/lib/iText.jar \
		${STAGEDIR}${JAVAJARDIR}/${PORTNAME}.jar
	@${INSTALL_DATA} ${WRKDIR}/lib/iText-rtf.jar \
		${STAGEDIR}${JAVAJARDIR}/${PORTNAME}-rtf.jar
	@${INSTALL_DATA} ${WRKDIR}/lib/iText-rups.jar \
		${STAGEDIR}${JAVAJARDIR}/${PORTNAME}-rups.jar
	@${INSTALL_SCRIPT} ${FILESDIR}/${PORTNAME}-rups \
		${STAGEDIR}${PREFIX}/bin/
.if ${PORT_OPTIONS:MDOCS}
	@${MKDIR} ${STAGEDIR}${DOCSDIR}/apidocs
	@${CP} -R ${WRKDIR}/build/docs/* ${STAGEDIR}${DOCSDIR}/apidocs
	@${CHOWN} -h -R ${SHAREOWN}:${SHAREGRP} ${STAGEDIR}${DOCSDIR}/apidocs
.endif

.include <bsd.port.mk>
