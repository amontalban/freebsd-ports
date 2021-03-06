# Created by: Joe Marcus Clarke <marcus@FreeBSD.org>
# $FreeBSD$
#   $MCom: ports/devel/libgconf-java/Makefile,v 1.9 2005/10/29 22:06:05 marcus Exp $

PORTNAME=	libgconf-java
PORTVERSION=	2.12.6
PORTREVISION=	6
CATEGORIES=	devel java
MASTER_SITES=	GNOME
DIST_SUBDIR=	gnome2

MAINTAINER=	gnome@FreeBSD.org
COMMENT=	Java wrapper for GConf

DEPRECATED=	Unmaintained, outdated not depend on
EXPIRATION_DATE=	2014-05-25

BUILD_DEPENDS=	${JAVALIBDIR}/gtk${GTK_API_VERSION}.jar:${PORTSDIR}/x11-toolkits/libgtk-java
RUN_DEPENDS=	${JAVALIBDIR}/gtk${GTK_API_VERSION}.jar:${PORTSDIR}/x11-toolkits/libgtk-java

USES=		gmake libtool pathfix pkgconfig tar:bzip2
USE_LDCONFIG=	yes
GNU_CONFIGURE=	yes
USE_JAVA=	yes
JAVA_VERSION=	1.6+
JAVA_OS=	native
USE_GNOME=	gconf2
CONFIGURE_ARGS=	--without-gcj-compile --with-jardir=${JAVAJARDIR}
CPPFLAGS+=	-I${JAVA_HOME}/include -I${JAVA_HOME}/include/freebsd

GCONF_API_VERSION=	2.12
GTK_API_VERSION=	2.10
PLIST_SUB=		GCONF_API_VERSION=${GCONF_API_VERSION} \
			PORTNAME=${PORTNAME}

PKGMESSAGE=		${WRKDIR}/pkg-message

NO_STAGE=	yes
post-patch:
	@${REINPLACE_CMD} -e 's|echo aout|echo elf|g' \
		${WRKSRC}/configure

do-install:
	${INSTALL_DATA} ${WRKSRC}/.libs/libgconfjni-${GCONF_API_VERSION}.so \
		${PREFIX}/lib/libgconfjni-${GCONF_API_VERSION}.so.1
	${LN} -sf ${PREFIX}/lib/libgconfjni-${GCONF_API_VERSION}.so.1 \
		${PREFIX}/lib/libgconfjni-${GCONF_API_VERSION}.so
	${MKDIR} ${PREFIX}/libdata/pkgconfig
	${INSTALL_DATA} ${WRKSRC}/gconf-java.pc	${PREFIX}/libdata/pkgconfig
	${MKDIR} ${JAVAJARDIR}
	${INSTALL_DATA} ${WRKSRC}/gconf${GCONF_API_VERSION}.jar ${JAVAJARDIR}

post-install:
.if !defined(NOPORTDOCS)
	${MKDIR} ${DOCSDIR}
	${INSTALL_DATA} ${WRKSRC}/AUTHORS ${DOCSDIR}
	${INSTALL_DATA} ${WRKSRC}/COPYING ${DOCSDIR}
	${INSTALL_DATA} ${WRKSRC}/NEWS ${DOCSDIR}
	${INSTALL_DATA} ${WRKSRC}/README ${DOCSDIR}
	${MKDIR} ${DOCSDIR}/api
	cd ${WRKSRC}/doc/api && ${FIND} . | ${CPIO} -pdmu ${DOCSDIR}/api
	${TOUCH} ${DOCSDIR}/api/packages.html
	${MKDIR} ${DOCSDIR}/examples
	cd ${WRKSRC}/doc/examples && ${FIND} . \
		| ${CPIO} -pdmu ${DOCSDIR}/examples
.endif
	@${SED} -e 's|%%JAVAJARDIR%%|${JAVAJARDIR}|g ; \
		s|%%PREFIX%%|${PREFIX}|g ; \
		s|%%GCONF_API_VERSION%%|${GCONF_API_VERSION}|g' \
		 < ${PKGDIR}/pkg-message > ${PKGMESSAGE}
	@${CAT} ${PKGMESSAGE}

.include <bsd.port.mk>
