# Created by: Jonathan Hanna
# $FreeBSD$

PORTNAME=	edict
PORTVERSION=	19990714
PORTREVISION=	5
CATEGORIES=	japanese
MASTER_SITES=	\
		http://japanology.arts.kuleuven.ac.be/mirrors/monash/ \
		http://www.bcit-broadcast.com/monash/ \
		ftp://ftp.mirrorservice.org/sites/ftp.cc.monash.edu.au/pub/nihongo/ \
		ftp://ftp.edrdg.org/pub/Nihongo/ \
		ftp://ftp.u-aizu.ac.jp/pub/SciEng/nihongo/ftp.cc.monash.edu.au/ \
		ftp://ftp.funet.fi/pub/culture/japan/mirrors/monash/pub/nihongo/ \
		ftp://ftp.uni-duisburg.de/Mirrors/ftp.monash.edu.au/pub/nihongo/ \
		ftp://ftp.monash.edu.au/pub/nihongo/
EXTRACT_SUFX=
DISTFILES=	${DICTFILES} ${SRCFILES} ${DOCFILES}

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Japanese-English dictionaries with access and maintenance utilities

BUILD_DEPENDS=	${UNZIP_CMD}:${PORTSDIR}/archivers/unzip

DIST_SUBDIR=	edict

DICTFILES=	edict.gz edicth enamdict.gz compdic.gz \
		j_places.gz ediclsd3.zip \
		kanjidic.gz kanjd212.gz lawgledt.zip \
		lingdic.zip geodic.gz pandpdic.zip \
		aviation.zip findic.zip mktdic.zip \
		4jword3_edict.zip concrete.zip

SRCFILES=	xjdic23.tgz

DOCFILES=	edict_doc.html edicth.doc \
		enamdict_doc.txt enamdict_doc.html \
		j_places.inf kanjidic.doc kanjd212.doc ediclsd3.rme \
		lawgldoc.new lingdic.txt geodic.doc aviation.txt \
		findic.doc mktdic.doc 4jword3_inf.txt \
		concrete.doc

#
# These change too often and are not made into executables.
#
IGNOREFILES=	${DICTFILES} ${DOCFILES}

BINFILES=	exjdxgen xjdic_cl xjdic_sa xjdserver xjdxgen

# Where to install the data files
DATADIR=	${PREFIX}/share/dict/edict
DOCSDIR=	${PREFIX}/share/doc/xjdic

NO_WRKSUBDIR=	yes

sparc64_BROKEN=	Fails to install on sparc64 with error 2

OPTIONS_DEFINE=	DOCS

post-patch:
	@${GREP} -l '^main' ${WRKSRC}/*.c | ${XARGS} ${REINPLACE_CMD} \
		-e '/argv/s/unsigned//'

do-extract:
	@${RM} -rf ${WRKDIR}
	@${MKDIR} ${WRKDIR}
.for file in ${SRCFILES}
	(cd ${WRKDIR} && ${EXTRACT_CMD} ${EXTRACT_BEFORE_ARGS} \
		${_DISTDIR}/${file} ${EXTRACT_AFTER_ARGS})
.endfor

do-install:
	(cd ${WRKDIR} && ${INSTALL_PROGRAM} ${BINFILES} ${STAGEDIR}${PREFIX}/bin)
	@${MKDIR} ${STAGEDIR}${DATADIR}
	${CP} ${_DISTDIR}/edicth ${STAGEDIR}${DATADIR}
.for file in edict enamdict compdic j_places kanjidic kanjd212 geodic
	${GZIP_CMD} -cd ${_DISTDIR}/${file}.gz > ${STAGEDIR}${DATADIR}/${file}
.endfor
.for file in ediclsd3 lawgledt lingdic pandpdic aviation findic mktdic \
	4jword3_edict concrete
	${UNZIP_CMD} -o ${_DISTDIR}/${file}.zip ${file:S|edict|edict.euc|} \
		-d ${STAGEDIR}${DATADIR}
.endfor
.for dict in ${DICTFILES:S|_edict|_edict.euc|}
	(cd ${STAGEDIR}${DATADIR} && ${STAGEDIR}${PREFIX}/bin/xjdxgen ${dict:R})
	(cd ${STAGEDIR}${DATADIR} && ${CHMOD} ${SHAREMODE} \
		${dict:R} ${dict:R}.xjdx)
.endfor
	${RM} -f ${STAGEDIR}${PREFIX}/bin/xjdic
	${LN} -s ${PREFIX}/bin/xjdic_sa ${STAGEDIR}${PREFIX}/bin/xjdic
	(cd ${WRKDIR} && ${INSTALL_DATA} radicals.tm radkfile kanjstroke \
		romkana.cnv vconj ${STAGEDIR}${DATADIR})
	#
	# Only 9 dictionaries can be enabled
	#
	@${ECHO_CMD} dicdir ${DATADIR} > ${STAGEDIR}${DATADIR}/.xjdicrc
	@${ECHO_CMD} dicfile edict >> ${STAGEDIR}${DATADIR}/.xjdicrc
	@${ECHO_CMD} dicfile enamdict >> ${STAGEDIR}${DATADIR}/.xjdicrc
	@${ECHO_CMD} dicfile compdic >> ${STAGEDIR}${DATADIR}/.xjdicrc
	@${ECHO_CMD} dicfile ediclsd3 >> ${STAGEDIR}${DATADIR}/.xjdicrc
	@${ECHO_CMD} dicfile j_places >> ${STAGEDIR}${DATADIR}/.xjdicrc
	# @${ECHO_CMD} dicfile lawgledt >> ${DATADIR}/.xjdicrc
	@${ECHO_CMD} dicfile geodic >> ${STAGEDIR}${DATADIR}/.xjdicrc
	# @${ECHO_CMD} dicfile pandpdic >> ${DATADIR}/.xjdicrc
	@${ECHO_CMD} dicfile aviation >> ${STAGEDIR}${DATADIR}/.xjdicrc
	# @${ECHO_CMD} dicfile findic >> ${DATADIR}/.xjdicrc
	# @${ECHO_CMD} dicfile mktdic >> ${DATADIR}/.xjdicrc
	@${ECHO_CMD} dicfile 4jword3_edict.euc >> ${STAGEDIR}${DATADIR}/.xjdicrc
	# @${ECHO_CMD} dicfile concrete.doc >> ${DATADIR}/.xjdicrc
	# @${ECHO_CMD} dicfile lingdic >> ${DATADIR}/.xjdicrc
	@${CHMOD} ${SHAREMODE} ${STAGEDIR}${DATADIR}/.xjdicrc
	${INSTALL_MAN} ${WRKSRC}/xjdic.1 ${STAGEDIR}${PREFIX}/man/man1
	@${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${WRKSRC}/xjdic23.inf ${STAGEDIR}${DOCSDIR}
	(cd ${_DISTDIR} && ${INSTALL_DATA} ${DOCFILES} ${STAGEDIR}${DOCSDIR})

.include <bsd.port.mk>
