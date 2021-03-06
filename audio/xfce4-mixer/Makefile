# Created by: James Earl <jdearl@telus.net>
# $FreeBSD$

PORTNAME=	xfce4-mixer
PORTVERSION=	4.10.0
PORTREVISION=	5
CATEGORIES=	audio xfce
MASTER_SITES=	${MASTER_SITE_XFCE}
MASTER_SITE_SUBDIR=	src/apps/${PORTNAME}/${PORTVERSION:R}
DIST_SUBDIR=	xfce4

MAINTAINER=	xfce@FreeBSD.org
COMMENT=	Volume control for the Xfce desktop

LIB_DEPENDS=	libdbus-glib-1.so:${PORTSDIR}/devel/dbus-glib \
		libunique-1.0.so:${PORTSDIR}/x11-toolkits/unique

GNU_CONFIGURE=	yes
INSTALLS_ICONS= yes
USES=		gettext gmake libtool pathfix pkgconfig tar:bzip2
USE_GNOME=	glib20 gtk20 intltool intlhack
USE_XFCE=	configenv libmenu libutil panel xfconf
USE_GSTREAMER=	good

MAKE_JOBS_UNSAFE=	yes

OPTIONS_DEFINE=	KEYBIND

KEYBIND_DESC=	Multimedia keyboard shortcuts

.include <bsd.port.options.mk>

.if ${PORT_OPTIONS:MKEYBIND}
LIB_DEPENDS+=	libkeybinder.so:${PORTSDIR}/x11/keybinder
CONFIGURE_ARGS+=--enable-keybinder
.else
CONFIGURE_ARGS+=--disable-keybinder
.endif

post-patch:
	@${FIND} ${WRKSRC} -name 'Makefile.in' -or -name 'xfce-mixer-track.c' \
		-type f | ${XARGS} ${REINPLACE_CMD} -e \
		's|(pkgdatadir)/icons|(datadir)/icons| ; \
		s|pixmaps/xfce4-mixer|pixmaps|'

.include <bsd.port.mk>
