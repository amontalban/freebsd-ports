# Created by: Nikos Ntarmos <ntarmos@ceid.upatras.gr>
# $FreeBSD$

PORTNAME=	shell-fm
PORTVERSION=	0.7
PORTEPOCH=	2
CATEGORIES=	multimedia
MASTER_SITES=	http://nex.scrapping.cc/shell-fm/releases/

MAINTAINER=	ntarmos@cs.uoi.gr
COMMENT=	A command-line client for Last.FM

LIB_DEPENDS=	ao:${PORTSDIR}/audio/libao \
		mad:${PORTSDIR}/audio/libmad

USES=		gmake pkgconfig
USE_BZIP2=	true
LDFLAGS+=	-L${LOCALBASE}/lib
CFLAGS+=	-I${LOCALBASE}/include

DEPRECATED=	Unusable, subscription radio streaming service will come to an end
EXPIRATION_DATE=2014-06-02

MAN1=		shell-fm.1
MANCOMPRESSED=	yes
PLIST_FILES=	bin/shell-fm
PORTDOCS=	AUTHORS RELEASE INSTALL
PORTEXAMPLES=	shell-colors.sh shell-fm-tune.sh \
		unix.pl zcontrol

NO_STAGE=	yes
pre-build:
	@${REINPLACE_CMD} \
		-e 's/^PREFIX.*$$/\PREFIX := $$(LOCALBASE)/g' \
		${WRKSRC}/Makefile

post-install:
.if !defined(NOPORTDOCS)
	@${ECHO_MSG} "installing additional documentation to ${DOCSDIR}"
	@${MKDIR} ${DOCSDIR}
. for doc in ${PORTDOCS}
	@${INSTALL_DATA} ${WRKSRC}/${doc} ${DOCSDIR}
. endfor
.endif
.if !defined(NOPORTEXAMPLES)
	@${MKDIR} ${EXAMPLESDIR}
	@${ECHO_MSG} "installing examples to ${EXAMPLESDIR}"
. for example in ${PORTEXAMPLES}
	@${INSTALL_DATA} ${WRKSRC}/scripts/${example} ${EXAMPLESDIR}
. endfor
.endif

.include <bsd.port.mk>
