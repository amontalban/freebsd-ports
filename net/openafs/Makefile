# $FreeBSD$

PORTNAME=	openafs
DISTVERSION=	${AFS_DISTVERSION}.${DBVERSION:S/-//g}
CATEGORIES=	net
MASTER_SITES=	http://dl.central.org/dl/openafs/${AFS_DISTVERSION}/:openafs \
		http://dl.openafs.org/dl/openafs/${AFS_DISTVERSION}/:openafs \
		http://dl.central.org/dl/cellservdb/:gco \
		http://grand.central.org/dl/cellservdb/:gco
DISTFILES=	${PORTNAME}-${AFS_DISTVERSION}-src.tar.bz2:openafs \
		${PORTNAME}-${AFS_DISTVERSION}-doc.tar.bz2:openafs \
		CellServDB.${DBVERSION}:gco
EXTRACT_ONLY=	${PORTNAME}-${AFS_DISTVERSION}-src.tar.bz2 \
		${PORTNAME}-${AFS_DISTVERSION}-doc.tar.bz2

MAINTAINER=	bjk@FreeBSD.org
COMMENT=	AFS implementation from openafs.org

LICENSE=	IPLv1
LICENSE_NAME=	IBM Public License Version 1.0
LICENSE_FILE=	${WRKSRC}/doc/LICENSE
LICENSE_PERMS=	auto-accept

AFS_DISTVERSION=1.6.7
DBVERSION=	2013-01-28

USES=		kmod
USE_LDCONFIG=	yes
PATCH_STRIP=	-p1
USE_BZIP2=	yes
HAS_CONFIGURE=	yes
CONFIGURE_ARGS=	--prefix=${PREFIX} \
		--localstatedir=/var \
		--mandir=${MANPREFIX}/man \
		--with-bsd-kernel-headers=${SRC_BASE}/sys \
		--with-bsd-kernel-build=${WRKDIR}/conf \
		--enable-debug \
		--enable-debug-kernel \
		--enable-debug-lwp \
		--includedir=${PREFIX}/include/openafs \
		${CONFIGURE_TARGET}
WRKSRC=		${WRKDIR}/${PORTNAME}-${AFS_DISTVERSION}
USE_RC_SUBR=	afsd afsserver

CONFLICTS=	coda-server-6.[0-9]* heimdal-[0-9]*
ONLY_FOR_ARCHS=	i386 amd64

AFSMNTDIR?=	/afs
AFSSTATEDIR?=	/var/${PORTNAME}
AFSCACHEDIR?=	${AFSSTATEDIR}/cache
PLIST_SUB+=	AFSMNTDIR=${AFSMNTDIR:C,^/,,} \
		AFSSTATEDIR=${AFSSTATEDIR:C,^/,,} \
		AFSCACHEDIR=${AFSCACHEDIR:C,^/,,}

# clang (the base system compiler in __FreeBSD_version 1000024 and later)
# is pickier about stack alignment than gcc; OpenAFS uses its own
# lightweight process "threading" library which will produce a misaligned
# stack under clang; we need to pass -mstackrealign to avoid SIGBUS at
# runtime.  gcc does not understand this flag, so we use compiler.mk to
# figure out what type of compiler is in use.
USES+=		compiler

OPTIONS_DEFINE=	FUSE
FUSE_USES=	fuse
OPTIONS_SUB=	yes
FUSE_CONFIGURE_OFF=	--disable-fuse-client

.include <bsd.port.pre.mk>

KERNCONF?=	GENERIC
KERNCONFDIR?=	${SRC_BASE}/sys/${ARCH}/conf

# Use the first component of ${KERNCONF}.
.for K in ${KERNCONF}
_KERNCONF?=$K
.endfor

.if !exists(${KERNCONFDIR}/${_KERNCONF})
IGNORE=	requires kernel configuration file ${_KERNCONF} to build
.endif

.if ${OSVERSION} < 800000
IGNORE=	supports FreeBSD 8.0 and later
.endif

# Do not show users the reminder about cleandepend and depend
post-extract:
	${MKDIR} ${WRKDIR}/conf
	cd ${KERNCONFDIR} && \
	    /usr/sbin/config -d ${WRKDIR}/conf ${_KERNCONF} >/dev/null

post-patch:
.if ${COMPILER_TYPE} == clang
	${REINPLACE_CMD} -e 's/XCFLAGS="-O2 -pipe -fPIC"/XCFLAGS="${CFLAGS} -fPIC -mstackrealign"/' ${WRKSRC}/configure
	${REINPLACE_CMD} -e 's/-mno-align-long-strings//' ${WRKSRC}/src/libafs/MakefileProto.FBSD.in
.endif

create-sample-files:
	@${ECHO_CMD} openafs.org > ${WRKDIR}/ThisCell
	@${ECHO_CMD} "${AFSMNTDIR}:${AFSCACHEDIR}:150000" > ${WRKDIR}/cacheinfo
	@${INSTALL_DATA} ${DISTDIR}/CellServDB.${DBVERSION} ${WRKDIR}/CellServDB

post-install: create-sample-files
	@${MKDIR} ${STAGEDIR}${ETCDIR}
.for F in CellServDB ThisCell cacheinfo
	@${INSTALL_DATA} ${WRKDIR}/${F} ${STAGEDIR}${ETCDIR}/${F}.sample
.endfor
	@${INSTALL_KLD} ${STAGEDIR}${PREFIX}/lib/openafs/libafs.ko \
	    ${STAGEDIR}${KMODDIR}
	@${RM} ${STAGEDIR}${PREFIX}/lib/openafs/libafs.ko
	@${RMDIR} ${STAGEDIR}${PREFIX}/lib/openafs
	${MKDIR} ${STAGEDIR}${AFSMNTDIR} \
	    ${STAGEDIR}${AFSSTATEDIR} ${STAGEDIR}${AFSCACHEDIR}

.include <bsd.port.post.mk>
