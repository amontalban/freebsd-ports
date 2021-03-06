# Created by: Andreas Fehlner (fehlner@gmx.de)
# $FreeBSD$

PORTNAME=	userneu
PORTVERSION=	1.43
PORTREVISION=	2
CATEGORIES=	sysutils
MASTER_SITES=	http://btw23.de/johannes/files/userneu/\
		http://home.arcor.de/fehlner/fbsd_ports/\
		http://home.arcor.de/teambushido/fbsd_ports/
PKGNAMESUFFIX=	-devel
DISTNAME=	${PORTNAME}-${PORTVERSION}b

MAINTAINER=	fehlner@gmx.de
COMMENT=	Account management and creation tool

RUN_DEPENDS=	\
    p5-Crypt-PasswdMD5>=0:${PORTSDIR}/security/p5-Crypt-PasswdMD5 \
    p5-Crypt-RandPasswd>=0:${PORTSDIR}/security/p5-Crypt-RandPasswd

USES=		perl5
USE_PERL5=	run
NO_BUILD=	yes

CONFLICTS=	userneu-1.*

SCRIPTS=	userneu.pl smbrepair.pl
MAN5=		userneu.conf.5
MAN8=		userneu.8
LDOCS1=		BUGS CHANGES CREDITS REQUIREMENTS TODO
LDOCS2=		README INSTALL userneu.pod userneu.conf.pod
PORTDOCS=	${LDOCS1} ${LDOCS2}
EXAMPLES=	userlist userneu.conf.example

NO_STAGE=	yes
.include <bsd.port.pre.mk>

do-install:
	cd ${WRKSRC}/doc && ${INSTALL_MAN} ${MAN8} ${MANPREFIX}/man/man8
	cd ${WRKSRC}/doc && ${INSTALL_MAN} ${MAN5} ${MANPREFIX}/man/man5
	cd ${WRKSRC} && ${INSTALL_SCRIPT} ${SCRIPTS} ${PREFIX}/sbin
	${LN} ${PREFIX}/sbin/userneu.pl ${PREFIX}/sbin/userquick
	@${MKDIR} ${EXAMPLESDIR}
	cd ${WRKSRC} && ${INSTALL_DATA} ${EXAMPLES} ${EXAMPLESDIR}
.if !defined(NOPORTDOCS)
	@${MKDIR} ${DOCSDIR}
	cd ${WRKSRC} && ${INSTALL_DATA} ${LDOCS1} ${DOCSDIR}
	cd ${WRKSRC}/doc && ${INSTALL_DATA} ${LDOCS2} ${DOCSDIR}
.endif

.include <bsd.port.post.mk>
