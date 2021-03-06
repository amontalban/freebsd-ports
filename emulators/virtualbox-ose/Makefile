# Created by: Bernhard Froehlich <decke@bluelife.at>
# $FreeBSD$

PORTNAME=	virtualbox-ose
DISTVERSION=	4.3.10
PORTREVISION=	1
CATEGORIES=	emulators
MASTER_SITES=	http://download.virtualbox.org/virtualbox/${DISTVERSION}/ \
		http://tmp.chruetertee.ch/ \
		http://disasterarea.chruetertee.ch/ \
		http://download.virtualbox.org/virtualbox/${VBOX_GUEST_VER}/:guestadditions
DISTFILES=	VirtualBox-${DISTVERSION}${EXTRACT_SUFX} ${GADISTFILES}
EXTRACT_ONLY=	VirtualBox-${DISTVERSION}${EXTRACT_SUFX}

MAINTAINER=	vbox@FreeBSD.org
COMMENT=	A general-purpose full virtualizer for x86 hardware

LICENSE=	GPLv2
LICENSE_FILE=	${WRKSRC}/COPYING

BUILD_DEPENDS=	yasm:${PORTSDIR}/devel/yasm \
		xsltproc:${PORTSDIR}/textproc/libxslt \
		kmk:${PORTSDIR}/devel/kBuild \
		gtar:${PORTSDIR}/archivers/gtar \
		cdrecord:${PORTSDIR}/sysutils/cdrtools
LIB_DEPENDS=	libpng.so:${PORTSDIR}/graphics/png \
		libxslt.so:${PORTSDIR}/textproc/libxslt \
		libcurl.so:${PORTSDIR}/ftp/curl
RUN_DEPENDS=	${LOCALBASE}/etc/rc.d/vboxnet:${PORTSDIR}/emulators/virtualbox-ose-kmod \
		cdrecord:${PORTSDIR}/sysutils/cdrtools

WRKSRC=		${WRKDIR}/VirtualBox-${PORTVERSION}
ONLY_FOR_ARCHS=	i386 amd64
USES=		compiler iconv pkgconfig tar:bzip2
USE_GNOME=	libidl
USE_PYTHON_BUILD=	yes

HAS_CONFIGURE=	yes
CONFIGURE_ARGS+=--with-gcc="${CC}" --with-g++="${CXX}" --passive-mesa
USE_LDCONFIG=	${PREFIX}/lib/virtualbox

CONFLICTS_INSTALL=	virtualbox-ose-devel-4* virtualbox-ose-legacy-4* virtualbox-ose-additions-4* virtualbox-ose-additions-devel-4*

VBOXUSER?=	vboxusers
VBOXWSUSER?=	vboxusers
VBOXGROUP?=	vboxusers
USERS=		${VBOXUSER}
GROUPS=		${VBOXGROUP}
VBOX_FRONTENDS=	VBoxAutostart VBoxHeadless
VBOX_GUEST_VER=	${PORTVERSION}

OPTIONS_DEFINE=	DBUS DEBUG GUESTADDITIONS MANUAL NLS PULSEAUDIO PYTHON \
		QT4 UDPTUNNEL VDE VNC VPX WEBSERVICE X11
OPTIONS_DEFAULT=	DBUS PYTHON QT4 UDPTUNNEL VNC WEBSERVICE X11
OPTIONS_SUB=	yes
DEBUG_DESC=	Debug symbols, additional logs and assertions
MANUAL_DESC=	Build with user manual
QT4_DESC=	Build with QT4 Frontend
GUESTADDITIONS_DESC=	Build with Guest Additions
UDPTUNNEL_DESC=	Build with UDP tunnel support
VDE_DESC=	Build with VDE support
VNC_DESC=	Build with VNC support
WEBSERVICE_DESC=	Build Webservice
VPX_DESC=	Use vpx for video capturing

PULSEAUDIO_LIB_DEPENDS=	libpulse.so:${PORTSDIR}/audio/pulseaudio
PULSEAUDIO_CONFIGURE_OFF=	--disable-pulse

DBUS_LIB_DEPENDS=	libdbus-1.so:${PORTSDIR}/devel/dbus
DBUS_CONFIGURE_OFF=	--disable-dbus

MANUAL_CONFIGURE_OFF=	--disable-docs

VNC_LIB_DEPENDS=	libvncserver.so:${PORTSDIR}/net/libvncserver
VNC_CONFIGURE_ON=	--enable-vnc

VPX_LIB_DEPENDS=	libvpx.so:${PORTSDIR}/multimedia/libvpx
VPX_CONFIGURE_OFF=	--disable-libvpx

VDE_RUN_DEPENDS=	vde_switch:${PORTSDIR}/net/vde2
VDE_CONFIGURE_ON=	--enable-vde

# bmake doesn't know about unsetenv=true
.if defined(.PARSEDIR)
ENV=
.export ENV
.else
.SHELL:		path="/bin/sh" unsetenv=true
.endif

.include <bsd.port.options.mk>

PLIST_SUB+=	GUEST_VER=${VBOX_GUEST_VER} \
		PYTHON_VER=${PYTHON_VER} \
		PYTHON_VERU=${PYTHON_VER:S/./_/} \
		VBOXGROUP=${VBOXGROUP}

SUB_LIST+=	VBOXUSER=${VBOXUSER} \
		VBOXWSUSER=${VBOXWSUSER}
USE_RC_SUBR+=	vboxheadless vboxwatchdog

KMK_BUILDTYPE=	release
KMK_CONFIG=	VBOX_LIBPATH_X11=${LOCALBASE} VBOX_FREEBSD_SRC=${SRC_BASE}/sys
KMK_FLAGS=	-j${MAKE_JOBS_NUMBER}

.if empty(PORT_OPTIONS:MQT4) && !empty(PORT_OPTIONS:MNLS)
BROKEN=		NLS support requires QT4 frontend. Run 'make config' again!
.endif

.if empty(PORT_OPTIONS:MX11) && !empty(PORT_OPTIONS:MQT4)
BROKEN=		QT4 frontend requires X11 support. Run 'make config' again!
.endif

.if ${PORT_OPTIONS:MX11}
USE_SDL=	sdl
USE_XORG=	xcursor xmu inputproto xinerama
VBOX_FRONTENDS+=VBoxSDL
.else
CONFIGURE_ARGS+=--build-headless
.endif

.if ${PORT_OPTIONS:MQT4}
QT_NONSTANDARD=	yes
USE_QT4=	linguist_build moc_build rcc_build uic_build
USE_QT4+=	gui network opengl
INSTALLS_ICONS=	yes
VBOX_FRONTENDS+=VirtualBox VBoxTestOGL
.else
CONFIGURE_ARGS+=--disable-qt4
.endif

.if ${PORT_OPTIONS:MPYTHON}
USE_PYTHON=	2
USE_PYDISTUTILS=	yes
PYDISTUTILS_PKGNAME=	vboxapi
PYDISTUTILS_PKGVERSION=	1.0
PYDISTUTILS_NOEGGINFO=	yes
.else
CONFIGURE_ARGS+=--disable-python
.endif

.if ${PORT_OPTIONS:MGUESTADDITIONS}
GUESTADDITIONS=	VBoxGuestAdditions_${VBOX_GUEST_VER}.iso
GADISTFILES=	${GUESTADDITIONS}:guestadditions
RESTRICTED=	for personal use only
RESTRICTED_FILES=	${GUESTADDITIONS}
.endif

.if ${PORT_OPTIONS:MDEBUG}
KMK_BUILDTYPE=	debug
KMK_FLAGS+=	BUILD_TYPE=debug
.endif

.if ${PORT_OPTIONS:MMANUAL}
USE_TEX=	dvipsk:build formats:build texlive
.endif

.if ${PORT_OPTIONS:MWEBSERVICE}
BUILD_DEPENDS+=	soapcpp2:${PORTSDIR}/devel/gsoap
VBOX_WEB=	vboxwebsrv webtest
USE_RC_SUBR+=	vboxwebsrv
.endif

.if ${ARCH} == i386
KMK_ARCH=	freebsd.x86
PLIST_SUB+=	I386=""
.else
KMK_ARCH=	freebsd.${ARCH}
PLIST_SUB+=	I386="@comment "
.endif

PLIST_SUB+=	ARCH="${KMK_ARCH}"

.include <bsd.port.pre.mk>

.if ${OSVERSION} < 900000
EXTRA_PATCHES+=	${PATCHDIR}/extrapatch-src-VBox-Devices-PC-vbox.dsl \
		${PATCHDIR}/extrapatch-src-VBox-Main-src-server-generic-NetIf-generic.cpp
.endif

.if ${COMPILER_TYPE} == clang
PATCH_DEPENDS+=	${LOCALBASE}/share/kBuild/tools/GXX3.kmk:${PORTSDIR}/devel/kBuild
EXTRA_PATCHES+=	${PATCHDIR}/extrapatch-Config.kmk \
		${PATCHDIR}/extrapatch-src-VBox-Devices-PC-ipxe-Makefile.kmk \
		${PATCHDIR}/extrapatch-src-recompiler-Makefile.kmk
.endif

pre-everything::
.if ${ARCH} == "amd64"
.if !exists(/usr/lib32/libc.so)
	@${ECHO} 'Requires 32-bit libraries installed under /usr/lib32.'
	@${ECHO} 'Do: cd /usr/src; make build32 install32; /etc/rc.d/ldconfig restart'
	@${FALSE}
.endif
.endif

post-patch:
	@${ECHO} 'VBOX_PATH_APP_PRIVATE_ARCH = ${PREFIX}/lib/virtualbox' > ${WRKSRC}/LocalConfig.kmk
	@${ECHO} 'VBOX_PATH_SHARED_LIBS = ${PREFIX}/lib/virtualbox' >> ${WRKSRC}/LocalConfig.kmk
	@${ECHO} 'VBOX_WITH_RUNPATH = ${PREFIX}/lib/virtualbox' >> ${WRKSRC}/LocalConfig.kmk
	@${ECHO} 'VBOX_PATH_APP_PRIVATE = ${DATADIR}' >> ${WRKSRC}/LocalConfig.kmk
	@${ECHO} 'VBOX_PATH_APP_DOCS = ${DOCSDIR}' >> ${WRKSRC}/LocalConfig.kmk
	@${ECHO} 'VBOX_WITH_INSTALLER = 1' >> ${WRKSRC}/LocalConfig.kmk
	@${ECHO} 'VBOX_WITH_VBOXDRV =' >> ${WRKSRC}/LocalConfig.kmk
	@${ECHO} 'VBOX_WITH_TESTCASES =' >> ${WRKSRC}/LocalConfig.kmk
	@${ECHO} 'SDK_VBOX_LIBPNG_INCS = ${PREFIX}/include/libpng' >> ${WRKSRC}/LocalConfig.kmk
	@${ECHO} 'SDK_VBOX_LIBPNG_LIBS = png' >> ${WRKSRC}/LocalConfig.kmk
	@${ECHO} 'VBOX_WITH_ADDITIONS =' >> ${WRKSRC}/LocalConfig.kmk
	@${ECHO} 'VBOX_WITH_X11_ADDITIONS =' >> ${WRKSRC}/LocalConfig.kmk
.if ${PORT_OPTIONS:MUDPTUNNEL}
	@${ECHO} 'VBOX_WITH_UDPTUNNEL = 1' >> ${WRKSRC}/LocalConfig.kmk
.endif
.if ${PORT_OPTIONS:MVNC}
	@${ECHO} 'VBOX_WITH_EXTPACK_VNC = 1' >> ${WRKSRC}/LocalConfig.kmk
.endif
.if ${PORT_OPTIONS:MWEBSERVICE}
	@${ECHO} 'VBOX_WITH_WEBSERVICES = 1' >> ${WRKSRC}/LocalConfig.kmk
	@${ECHO} 'VBOX_GSOAP_INSTALLED = 1' >> ${WRKSRC}/LocalConfig.kmk
	@${ECHO} 'VBOX_PATH_GSOAP = ${PREFIX}/lib/gsoap' >> ${WRKSRC}/LocalConfig.kmk
	@${ECHO} 'VBOX_PATH_GSOAP_BIN = ${PREFIX}/bin' >> ${WRKSRC}/LocalConfig.kmk
	@${ECHO} 'VBOX_PATH_GSOAP_IMPORT = ${PREFIX}/share/gsoap/import' >> ${WRKSRC}/LocalConfig.kmk
	@${ECHO} 'VBOX_GCC_PEDANTIC_CXX = -Wshadow $(VBOX_GCC_WARN) -Wno-long-long' >> ${WRKSRC}/LocalConfig.kmk
.endif
.if empty(PORT_OPTIONS:MX11)
	@${ECHO} 'VBOX_WITH_VDMA =' >> ${WRKSRC}/LocalConfig.kmk
	@${ECHO} 'VBOX_WITH_WDDM =' >> ${WRKSRC}/LocalConfig.kmk
	@${ECHO} 'VBOX_WITH_WDDM_W8 =' >> ${WRKSRC}/LocalConfig.kmk
.endif
.if ${COMPILER_TYPE} == clang
	@${REINPLACE_CMD} -e 's| -finline-limit=8000||' \
	    -e 's| -mpreferred-stack-boundary=2||' ${WRKSRC}/Config.kmk
	@${REINPLACE_CMD} -e 's| -fpermissive||' ${WRKSRC}/Config.kmk ${WRKSRC}/src/VBox/Main/webservice/Makefile.kmk
	@${ECHO} 'VBOX_GCC_Wno-unused-parameter = -Wno-unused-parameter' >> ${WRKSRC}/LocalConfig.kmk
	@${ECHO} 'TOOL_VBoxGccFreeBSD_LD = ${CXX}' >> ${WRKSRC}/LocalConfig.kmk
	@${SED} -e 's|GXX3|VBoxGccFreeBSD|g' ${LOCALBASE}/share/kBuild/tools/GXX3.kmk > ${WRKSRC}/tools/kBuildTools/VBoxGccFreeBSD.kmk
.endif
	@${REINPLACE_CMD} -e 's|/usr/local|${LOCALBASE}|g' \
		${WRKSRC}/Config.kmk ${WRKSRC}/configure \
		${WRKSRC}/kBuild/units/qt3.kmk ${WRKSRC}/kBuild/units/qt4.kmk \
		${WRKSRC}/kBuild/sdks/LIBSDL.kmk \
		${WRKSRC}/src/libs/xpcom18a4/python/gen_python_deps.py
	@${REINPLACE_CMD} -e 's|\$$KBUILDDIR_BIN/kmk_sed|${LOCALBASE}/bin/kmk_sed|g' ${WRKSRC}/configure
.if empty(ICONV_LIB)
	@${REINPLACE_CMD} -e 's|iconv||' ${WRKSRC}/Config.kmk ${WRKSRC}/src/VBox/Runtime/Makefile.kmk
	@${ECHO} 'VBOX_ICONV_DEFS = LIBICONV_PLUG' >> ${WRKSRC}/LocalConfig.kmk
.endif

pre-build:
	@${REINPLACE_CMD} -e 's|/bin/bash|/bin/sh|' ${WRKSRC}/env.sh

do-build:
	cd ${WRKSRC} && ${SH} env.sh && \
	    ${KMK_CONFIG} ${LOCALBASE}/bin/kmk ${KMK_FLAGS}

do-install:
	${MKDIR} ${STAGEDIR}${DATADIR}
	cd ${WRKSRC}/out/${KMK_ARCH}/${KMK_BUILDTYPE}/bin/sdk/bindings/xpcom && ${COPYTREE_SHARE} "idl samples" ${STAGEDIR}${DATADIR}

	${MKDIR} ${STAGEDIR}${PREFIX}/include/virtualbox
	cd ${WRKSRC}/out/${KMK_ARCH}/${KMK_BUILDTYPE}/bin/sdk/bindings/xpcom/include && ${COPYTREE_SHARE} "*" ${STAGEDIR}${PREFIX}/include/virtualbox

	${MKDIR} ${STAGEDIR}${PREFIX}/lib/virtualbox
	cd ${WRKSRC}/out/${KMK_ARCH}/${KMK_BUILDTYPE}/bin && ${COPYTREE_SHARE} "*.so *.gc *.r0 *.fd components VBoxExtPackHelperApp" ${STAGEDIR}${PREFIX}/lib/virtualbox

.if ${PORT_OPTIONS:MMANUAL}
	${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${WRKSRC}/out/${KMK_ARCH}/${KMK_BUILDTYPE}/bin/UserManual*.pdf ${STAGEDIR}${DOCSDIR}
.endif

.if ${PORT_OPTIONS:MNLS}
	cd ${WRKSRC}/out/${KMK_ARCH}/${KMK_BUILDTYPE}/obj/VirtualBox/qtnls && ${COPYTREE_SHARE} "*.qm" ${STAGEDIR}${DATADIR}/nls
.endif

.for f in VBoxManage VBoxNetAdpCtl VBoxNetDHCP VBoxSVC VBoxXPCOMIPCD VBoxBalloonCtrl ${VBOX_FRONTENDS} ${VBOX_WEB}
	${INSTALL_PROGRAM} ${WRKSRC}/out/${KMK_ARCH}/${KMK_BUILDTYPE}/bin/${f} ${STAGEDIR}${PREFIX}/lib/virtualbox/
	${LN} -sf ${PREFIX}/lib/virtualbox/${f} ${STAGEDIR}${PREFIX}/bin/
.endfor

.if ${PORT_OPTIONS:MVNC}
	${MKDIR} ${STAGEDIR}${PREFIX}/lib/virtualbox/ExtensionPacks/VNC/${KMK_ARCH}
	${INSTALL_DATA} ${WRKSRC}/out/${KMK_ARCH}/${KMK_BUILDTYPE}/bin/ExtensionPacks/VNC/ExtPack* ${STAGEDIR}${PREFIX}/lib/virtualbox/ExtensionPacks/VNC/
	${INSTALL_LIB} ${WRKSRC}/out/${KMK_ARCH}/${KMK_BUILDTYPE}/bin/ExtensionPacks/VNC/${KMK_ARCH}/* ${STAGEDIR}${PREFIX}/lib/virtualbox/ExtensionPacks/VNC/${KMK_ARCH}/
.endif

.if ${PORT_OPTIONS:MWEBSERVICE}
	${MKDIR} ${STAGEDIR}${DATADIR}/sdk/bindings/webservice
.for f in vboxweb.wsdl
	${INSTALL_DATA} ${WRKSRC}/out/${KMK_ARCH}/${KMK_BUILDTYPE}/obj/webservice/${f} ${STAGEDIR}${DATADIR}/sdk/bindings/webservice/
.endfor
.endif

.if ${PORT_OPTIONS:MGUESTADDITIONS}
	${MKDIR} ${STAGEDIR}${PREFIX}/lib/virtualbox/additions
	${INSTALL_DATA} ${DISTDIR}/${GUESTADDITIONS} ${STAGEDIR}${PREFIX}/lib/virtualbox/additions/
	${LN} -sf ${PREFIX}/lib/virtualbox/additions/${GUESTADDITIONS} ${STAGEDIR}${PREFIX}/lib/virtualbox/additions/VBoxGuestAdditions.iso
.endif

.if ${PORT_OPTIONS:MPYTHON}
	cd ${WRKSRC}/out/${KMK_ARCH}/${KMK_BUILDTYPE}/bin/sdk/installer && \
	    ${SETENV} VBOX_INSTALL_PATH="${PREFIX}/lib/virtualbox" \
	    ${PYTHON_CMD} vboxapisetup.py install --root=${STAGEDIR}

	@${MKDIR} ${STAGEDIR}${PYTHON_SITELIBDIR}
	cd ${WRKSRC}/out/${KMK_ARCH}/${KMK_BUILDTYPE}/bin/sdk/bindings/xpcom/python && ${COPYTREE_SHARE} "*" ${STAGEDIR}${PYTHON_SITELIBDIR}
	${PYTHON_CMD} -mcompileall ${STAGEDIR}${PYTHON_SITELIBDIR}/xpcom/
.endif

.if ${PORT_OPTIONS:MQT4}
	${INSTALL_DATA} ${WRKSRC}/src/VBox/Frontends/VirtualBox/images/OSE/VirtualBox_48px.png ${STAGEDIR}${PREFIX}/share/pixmaps/VBox.png
	${INSTALL_DATA} ${WRKSRC}/src/VBox/Installer/freebsd/virtualbox.desktop ${STAGEDIR}${PREFIX}/share/applications/virtualbox.desktop
.endif

.include <bsd.port.post.mk>
