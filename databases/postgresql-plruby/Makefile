# Created by: Akinori MUSHA aka knu <knu@idaemons.org>
# $FreeBSD$

PORTNAME=	postgresql-plruby
PORTVERSION=	0.5.4
PORTREVISION=	2
CATEGORIES=	databases ruby
DIST_SUBDIR=	ruby

MAINTAINER=	knu@FreeBSD.org
COMMENT=	PL/Ruby procedural language for the PostgreSQL database system

USE_GITHUB=	yes
GH_ACCOUNT=	CraigCottingham
GH_TAGNAME=	${GH_COMMIT}
GH_COMMIT=	f8d9ced

USES=	uidfix
USE_BZIP2=	yes
USE_PGSQL=	server
USE_RUBY=	yes
USE_RUBY_EXTCONF=	yes
USE_RUBY_RDOC=		yes
NEED_ROOT=	yes

POSTGRESQL_PORT?=	databases/postgresql${PGSQL_VER}-server
PGSQL_PORTDIR?=		${PORTSDIR}/${POSTGRESQL_PORT}
PGSQL_WRKSRC_CMD=	cd ${PGSQL_PORTDIR} && ${MAKE} -V WRKSRC

CONFIGURE_ARGS=		--with-pg-config="${LOCALBASE}/bin/pg_config" \
			--with-pgsql-srcinc="`${PGSQL_WRKSRC_CMD}`/src/include"
#CONFIGURE_ARGS+=	--with-safe-level=0
#CONFIGURE_ARGS+=	--with-main-safe-level=0
#CONFIGURE_ARGS+=	--with-timeout=30
INSTALL_TARGET=	site-install

DOCS=		Changes plruby.html plruby.rd

PKGMESSAGE=	${WRKDIR}/createlang.sql

post-fetch:
	cd ${PGSQL_PORTDIR} && ${MAKE} -DBATCH patch

post-build:
	${SED} 's,!!PLRUBY_SO!!,${RUBY_SITEARCHLIBDIR}/plruby.so,' \
		${FILESDIR}/createlang.sql > ${WRKDIR}/createlang.sql
.if !defined(NOPORTDOCS)
	cd ${BUILD_WRKSRC}; ${SETENV} ${MAKE_ENV} ${MAKE} ${MAKE_FLAGS} ${MAKEFILE} ${MAKE_ARGS} rdoc
.endif

.include <bsd.port.pre.mk>

post-install:
	@${MKDIR} ${STAGEDIR}${RUBY_MODEXAMPLESDIR}/
	${INSTALL_DATA} ${WRKDIR}/createlang.sql ${STAGEDIR}${RUBY_MODEXAMPLESDIR}/
.if !defined(NOPORTDOCS)
	@${MKDIR} ${STAGEDIR}${RUBY_MODDOCDIR}
	cd ${WRKSRC}/ && ${COPYTREE_SHARE} docs/doc ${STAGEDIR}${RUBY_MODDOCDIR}/ README.markdown && ${INSTALL_DATA} ${DOCS} ${STAGEDIR}${RUBY_MODDOCDIR}/
	${FIND} -ds ${STAGEDIR}${RUBY_MODDOCDIR} -type f -print | ${SED} -E -e \
		's,^${STAGEDIR}${PREFIX}/?,,' >> ${TMPPLIST}
	${FIND} -ds ${STAGEDIR}${RUBY_MODDOCDIR} -type d -print | ${SED} -E -e \
		's,^${STAGEDIR}${PREFIX}/?,@dirrm ,' >> ${TMPPLIST}
	${ECHO_CMD} "@unexec rmdir %D/share/doc/ruby19/ 2>/dev/null || true" \
		>> ${TMPPLIST}
.endif

.include <bsd.port.post.mk>
