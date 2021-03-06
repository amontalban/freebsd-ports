# Created by: Yinghong Liu <relaxbsd@gmail.com>
# $FreeBSD$

PORTNAME=	roxterm
PORTVERSION=	2.8.3
CATEGORIES=	x11
MASTER_SITES=	SF

MAINTAINER=	ports@FreeBSD.org
COMMENT=	GTK+ terminal emulator with tabs

LICENSE=	GPLv3

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}lockfile>0:${PORTSDIR}/devel/py-lockfile \
		docbook-xsl>0:${PORTSDIR}/textproc/docbook-xsl \
		xsltproc:${PORTSDIR}/textproc/libxslt
LIB_DEPENDS=	libdbus-glib-1.so:${PORTSDIR}/devel/dbus-glib
RUN_DEPENDS=	xdg-open:${PORTSDIR}/devel/xdg-utils

USE_BZIP2=	yes
USES=		gettext pkgconfig
USE_GNOME=	librsvg2
USE_PYTHON_BUILD=	yes
USE_AUTOTOOLS=	libtool:env
INSTALLS_ICONS=	yes

OPTIONS_DEFINE=		DOCS GTK3

MAITCHFLAGS=	DISABLE_GTK3=${DISABLE_GTK3};DISABLE_GIT=True;DISABLE_PO4A=True;
MAITCHFLAGS+=	CC=${CC};GCC=${CC};CPP=${CC};CFLAGS=${CFLAGS};
MAITCHFLAGS+=	PARALLEL=${MAKE_JOBS_NUMBER};PREFIX=${PREFIX};

.include <bsd.port.options.mk>

.if ${PORT_OPTIONS:MGTK3}
USE_GNOME+=	vte3
.else
USE_GNOME+=	vte
DISABLE_GTK3=	True
.endif

post-patch:
	@${REINPLACE_CMD} -e \
		's|/usr/local|${LOCALBASE}|' ${WRKSRC}/maitch.py
	@${REINPLACE_CMD} -e \
		's|x-www-browser|xdg-open|' ${WRKSRC}/src/uri.c

do-configure:
	@(cd ${WRKSRC} && ${SETENV} MAITCHFLAGS="${MAITCHFLAGS}" \
		${PYTHON_CMD} mscript.py configure)

do-build:
	@(cd ${WRKSRC} && ${PYTHON_CMD} mscript.py build)

do-install:
.for i in roxterm roxterm-config
	(cd ${WRKSRC}/build && ${INSTALL_PROGRAM} ${i} \
		${STAGEDIR}${PREFIX}/bin)
.endfor
	(cd ${WRKSRC}/build && ${INSTALL_MAN} *.1 \
		${STAGEDIR}${MANPREFIX}/man/man1)
	(cd ${WRKSRC} && ${INSTALL_DATA} roxterm.desktop \
		${STAGEDIR}${DESKTOPDIR})
	@${MKDIR} ${STAGEDIR}${PREFIX}/share/icons/hicolor/scalable/apps
	(cd ${WRKSRC} && ${INSTALL_DATA} roxterm.svg \
		${STAGEDIR}${PREFIX}/share/icons/hicolor/scalable/apps)
	@${MKDIR} ${STAGEDIR}${DATADIR}
	(cd ${WRKSRC}/src && ${INSTALL_DATA} roxterm-config.ui \
		${STAGEDIR}${DATADIR})
	@(cd ${WRKSRC} && ${COPYTREE_SHARE} Config ${STAGEDIR}${DATADIR})
.for i in es fr pt_BR ru uk
	@${MKDIR} ${STAGEDIR}${PREFIX}/share/locale/${i}/LC_MESSAGES
	(cd ${WRKSRC}/build/po && ${INSTALL_DATA} ${i}.mo \
		${STAGEDIR}${PREFIX}/share/locale/${i}/LC_MESSAGES/roxterm.mo)
.endfor
	@${MKDIR} ${STAGEDIR}${DOCSDIR}
.for i in AUTHORS ChangeLog README
	@(cd ${WRKSRC} && ${INSTALL_DATA} ${i} ${STAGEDIR}${DOCSDIR})
.endfor
	@${MKDIR} ${STAGEDIR}${DOCSDIR}/en
	@(cd ${WRKSRC}/Help/en && ${INSTALL_DATA} * ${STAGEDIR}${DOCSDIR}/en)
	@${MKDIR} ${STAGEDIR}${DOCSDIR}/lib
	@(cd ${WRKSRC}/Help/lib && ${INSTALL_DATA} * ${STAGEDIR}${DOCSDIR}/lib)

.include <bsd.port.mk>
