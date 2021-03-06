# Created by: Meno Abels <meno.abels@adviser.com>
# $FreeBSD$

PORTNAME=	crm114
PORTVERSION=	20100106
PORTREVISION=	1
# WARNING change versionname in CRM114RELEASENAME too.
# portlint didn't like this variable at this place.
# So I have to put it down in this file.
CATEGORIES=	mail
MASTER_SITES=	http://crm114.sourceforge.net/tarballs/
# Oliver Eikemeier recommended the following construction
# to avoid the reduncany of the CRM114RELEASENAME and .src and
# .css extention.
DISTNAME=	${PORTNAME}-${PORTVERSION}-${CRM114RELEASENAME}.src

MAINTAINER=	chalpin@cs.wisc.edu
COMMENT=	A Markov based SpamFilter

LIB_DEPENDS=	tre.5:${PORTSDIR}/textproc/libtre

CRM114RELEASENAME=BlameMichelson

USES=		gettext iconv

MAKE_ARGS=	CC="${CC}" prefix="${PREFIX}" \
		LIBS="${LIBS}" \
		INSTALL_PROGRAM="${INSTALL_PROGRAM}"

CFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-L${LOCALBASE}/lib
LIBS+=		-L${LOCALBASE}/lib ${ICONV_LIB} -lintl

CFLAGS+=	-DVERSION='\"${PORTVERSION}-${CRM114RELEASENAME}\"'
CFLAGS+=	-DNO_LOGL

INSTALL_TARGET=	install_binary_only

CRM_FILES=	mailfilter.crm mailfilter.cf mailreaver.crm mailtrainer.crm \
		maillib.crm shuffle.crm rewriteutil.crm rewrites.mfp \
		whitelist.mfp blacklist.mfp priolist.mfp priolist.mfp.example \
		blacklist.mfp.example whitelist.mfp.example crm114-mode.el \
		reto_procmailrc.recipe

OPTIONS_DEFINE=	PGO

NO_STAGE=	yes
.include <bsd.port.options.mk>

.if ${PORT_OPTIONS:MPGO}
MAKE_ARGS+=	CFLAGS="${CFLAGS} -fprofile-use" \
		LDFLAGS="${LDFLAGS} -fprofile-use"
.else
MAKE_ARGS+=	CFLAGS="${CFLAGS}" \
		LDFLAGS="${LDFLAGS}"
.endif

post-patch:
	@${REINPLACE_CMD} -Ee \
	  's,^((LD|C)FLAGS),#\1,;;s,^(prefix=),#\1,;;s,^(.*-install),#\1,' \
	  ${WRKSRC}/Makefile

.if ${PORT_OPTIONS:MPGO}
.if target(pre-build)
.error Makefile error since pre-build target has already been defined
.endif
pre-build: pgo
.endif

# Peter Jeremy recommended the use of b64decode and md5 20040302
post-install:
	@${REINPLACE_CMD} -Ee 's|^(.*/openssl base64 -d/)|#\1|' \
		-e 's|/mewdecode/|/b64decode -pr/|' ${WRKSRC}/mailfilter.cf
	@${REINPLACE_CMD} -e 's|/md5sum/|/md5 -r/|' \
		-e 's|#!.*/usr/bin/crm.*|#!${PREFIX}/bin/crm|' \
		${WRKSRC}/mailfilter.crm ${WRKSRC}/mailtrainer.crm \
		${WRKSRC}/rewriteutil.crm \
		${WRKSRC}/mailreaver.crm ${WRKSRC}/shuffle.crm
	@for i in priolist.mfp whitelist.mfp; do \
		${CP} ${WRKSRC}/$${i}.example ${WRKSRC}/$${i}; \
	done
.if ${PORT_OPTIONS:MNORMALIZEMIME}
	@${REINPLACE_CMD} -Ee 's|^#(.*/normalizemime/)|\1|' \
	  ${WRKSRC}/mailfilter.cf
.else
	@${REINPLACE_CMD} -Ee 's|^#(.*/b64decode -pr/)|\1|' \
	  ${WRKSRC}/mailfilter.cf
.endif
	@${MKDIR} ${EXAMPLESDIR}
	for i in ${CRM_FILES}; do \
		${INSTALL_DATA} ${WRKSRC}/$${i} ${EXAMPLESDIR}; \
	done
.ifndef(NOPORTDOCS)
	@${MKDIR} ${DOCSDIR}
	@for i in ${WRKSRC}/[^G]*.txt ${WRKSRC}/README; do \
		${INSTALL_DATA} $${i} ${DOCSDIR}; \
	done
.endif

.if ${PORT_OPTIONS:MPGO}
pgo: pgo-build pgo-run pgo-clean

pgo-build:
	@(cd ${BUILD_WRKSRC}; ${SETENV} ${MAKE_ENV} ${MAKE} ${MAKE_FLAGS} ${MAKEFILE} ${MAKE_ARGS} CFLAGS="${CFLAGS} -fprofile-generate" LDFLAGS="${LDFLAGS} -fprofile-generate" ${ALL_TARGET})

pgo-run:
# Check everything to generate profiling information.
# We will ignore any errors.
	@-(cd ${BUILD_WRKSRC}; ${MAKE} megatest)

pgo-clean:
	@(cd ${BUILD_WRKSRC}; ${MAKE} clean)
.endif # if ${PORT_OPTIONS:MPGO}

.include <bsd.port.mk>
