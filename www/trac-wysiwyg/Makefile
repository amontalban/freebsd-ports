# Created by: Greg Larkin <glarkin@FreeBSD.org>
# $FreeBSD$

PORTNAME=	wysiwyg
DISTVERSION=	0.4.${SVN_REV}
PORTREVISION=	1
CATEGORIES=	www devel python
MASTER_SITES=	http://www.sourcehosting.net/freebsd/distfiles/ \
		LOCAL/brooks
PKGNAMEPREFIX=	trac-
DIST_SUBDIR=	trac

MAINTAINER=	ports@FreeBSD.org
COMMENT=	WYSIWYG editor for Trac wiki

RUN_DEPENDS+=	tracd:${PORTSDIR}/www/trac

USES=		tar:bzip2
USE_PYTHON=	2
USE_PYDISTUTILS=	yes
PYDISTUTILS_AUTOPLIST=	yes

.include <bsd.port.pre.mk>

.if !defined(SVN_REV)
.if defined(BOOTSTRAP)
SVN_URL=	http://trac-hacks.org/svn/tracwysiwygplugin/0.12/
LANG=		"C"
SVN_REV!=	svn info ${SVN_URL} | ${GREP} Revision | cut -d' ' -f2
.else
.include "Makefile.svn_rev"
.endif
.endif

.if defined(BOOTSTRAP) || defined(SVN_FETCH)
FETCH_DEPENDS+=	svn:${PORTSDIR}/devel/subversion

do-fetch:
	${MKDIR} ${WRKDIR}
	svn export -r ${SVN_REV} ${SVN_URL} ${WRKSRC}
	cd ${WRKDIR}; tar cvfy ${DISTDIR}/${DIST_SUBDIR}/${DISTNAME}.tar.bz2 ${DISTNAME}
	echo "SVN_REV=  ${SVN_REV}" > ${MASTERDIR}/Makefile.svn_rev
.endif

.include <bsd.port.post.mk>
