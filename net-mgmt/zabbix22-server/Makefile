# Created by: Pakhom Golynga <pakhom706@gmail.com>
# $FreeBSD$

PORTNAME=	zabbix22
PORTVERSION=	2.2.2
PORTREVISION?=	1
CATEGORIES=	net-mgmt
MASTER_SITES=	SF/zabbix/ZABBIX%20Latest%20Stable/${PORTVERSION}
PKGNAMESUFFIX?=	-server
DISTNAME=	zabbix-${PORTVERSION}

MAINTAINER=	pakhom706@gmail.com
COMMENT=	Enterprise-class open source distributed monitoring (${PKGNAMESUFFIX:S/^-//})

LICENSE=	GPLv2

CONFLICTS=	${PKGBASE}-1.[0-8]*

IGNORE_WITH_PHP=	52
IGNORE_WITH_MYSQL=	41

.if ${PKGNAMESUFFIX} != "-agent"
CONFLICTS+=	${PORTNAME}-1.[0-8]*
.endif

ZABBIX_BUILD=	${PKGNAMESUFFIX:S/^-//}

.if ${ZABBIX_BUILD} != "frontend" # frontend only needs the version/distribution settings
.if ${ZABBIX_BUILD} != "agent"
USE_RC_SUBR=	zabbix_${ZABBIX_BUILD}
.else
USE_RC_SUBR=	zabbix_${ZABBIX_BUILD}d
.endif

USES=		pkgconfig iconv

USERS=		zabbix
GROUPS=		zabbix

.if ${ZABBIX_BUILD} != "proxy"
PLIST_SUB=	PROXY="@comment "
.else
PLIST_SUB=	PROXY=""
.endif

.if ${ZABBIX_BUILD} == "server"
PLIST_SUB+=	SERVER=""
.else
PLIST_SUB+=	SERVER="@comment "
.endif

PLIST_SUB+=	ZABBIX_BUILD=${ZABBIX_BUILD} PORTVERSION=${PORTVERSION}
SUB_LIST=	ZABBIX_BUILD=${ZABBIX_BUILD} ZABBIX_REQUIRE=${ZABBIX_REQUIRE}

MAKE_ARGS+=	ARCH=freebsd
GNU_CONFIGURE=	yes
CONFIGURE_ARGS+=	--enable-${ZABBIX_BUILD} \
			--sysconfdir=${ETCDIR} \
			--datadir=${ETCDIR} \
			--with-iconv=${ICONV_PREFIX}

.if ${ZABBIX_BUILD} != "agent"
LIB_DEPENDS=	libnetsnmp.so:${PORTSDIR}/net-mgmt/net-snmp \
		libexecinfo.so:${PORTSDIR}/devel/libexecinfo

SUB_FILES=	pkg-message

CONFIGURE_ARGS+=	--with-net-snmp

OPTIONSFILE=	${PORT_DBDIR}/${PORTNAME}${PKGNAMESUFFIX}/options

OPTIONS_DEFINE=	IPV6 FPING JABBER CURL LDAP IPMI SSH NMAP JAVAGW LIBXML2
OPTIONS_DEFAULT=	MYSQL IPV6 FPING JABBER CURL

CURL_DESC=	Support for web monitoring
FPING_DESC=	Build/install fping for ping checks
IPMI_DESC=	Support for IPMI checks
JABBER_DESC=	Support for Jabber media type
LDAP_DESC=	Support for LDAP server checks
NMAP_DESC=	Build/install nmap for o/s detection
SSH_DESC=	Support for SSH-based checks
ODBC_DESC=	Support for database checks via ODBC
JAVAGW_DESC=	Support for Java gateway
LIBXML2_DESC=	Support for libxml2 (required by monitoring VMware)

OPTIONS_SINGLE=	DB
OPTIONS_SINGLE_DB=	MYSQL PGSQL SQLITE ORACLE ODBC

.include <bsd.port.options.mk>

.if ${PORT_OPTIONS:MMYSQL}
ZABBIX_REQUIRE=	" mysql"
USE_MYSQL=	yes
CONFIGURE_ARGS+=	--with-mysql
.endif

.if ${PORT_OPTIONS:MPGSQL}
ZABBIX_REQUIRE=	" postgresql"
USE_PGSQL=	yes
CONFIGURE_ARGS+=	--with-postgresql
.endif

.if ${PORT_OPTIONS:MSQLITE}
ZABBIX_REQUIRE=	" sqlite"
USE_SQLITE=	3
CONFIGURE_ARGS+=	--with-sqlite3
.endif

.if ${PORT_OPTIONS:MORACLE}
ZABBIX_REQUIRE=
CONFIGURE_ARGS+=	--with-oracle
.endif

.if ${PORT_OPTIONS:MCURL}
LIB_DEPENDS+=	libcurl.so:${PORTSDIR}/ftp/curl
CONFIGURE_ARGS+=	--with-libcurl
.endif

.if ${PORT_OPTIONS:MLDAP}
USE_OPENLDAP=	yes
CONFIGURE_ARGS+=	--with-ldap
.endif

.if ${PORT_OPTIONS:MIPMI}
LIB_DEPENDS+=	libOpenIPMI.so:${PORTSDIR}/sysutils/openipmi
CONFIGURE_ARGS+=	--with-openipmi
.endif

.if ${PORT_OPTIONS:MJABBER}
LIB_DEPENDS+=	libiksemel.so:${PORTSDIR}/textproc/iksemel
CONFIGURE_ARGS+=	--with-jabber
.endif

.if ${PORT_OPTIONS:MFPING}
RUN_DEPENDS+=	fping:${PORTSDIR}/net/fping
.endif

.if ${PORT_OPTIONS:MSSH}
LIB_DEPENDS+=	libssh2.so:${PORTSDIR}/security/libssh2
CONFIGURE_ARGS+=	--with-ssh2
.endif

.if ${PORT_OPTIONS:MODBC}
LIB_DEPENDS+=	libodbc.so:${PORTSDIR}/databases/unixODBC
CONFIGURE_ARGS+=	--with-unixodbc
.endif
.endif # if ${ZABBIX_BUILD} != "agent"

.if ${PORT_OPTIONS:MIPV6}
CONFIGURE_ARGS+=	--enable-ipv6
.endif

.if ${PORT_OPTIONS:MNMAP}
RUN_DEPENDS+=	nmap:${PORTSDIR}/security/nmap \
		sudo:${PORTSDIR}/security/sudo
.endif

.if ${PORT_OPTIONS:MJAVAGW}
USE_JAVA=	yes
CONFIGURE_ARGS+=	--enable-java
PLIST_SUB+=	ZABBIX_JAVA="sbin/zabbix_java"
PLIST_SUB+=	JAVAGW=""
.else
PLIST_SUB+=	JAVAGW="@comment "
.endif

.if ${PORT_OPTIONS:MLIBXML2}
LIB_DEPENDS+=	libxml2.so:${PORTSDIR}/textproc/libxml2
CONFIGURE_ARGS+=	--with-libxml2
.endif

post-patch:
	@${GREP} -rl "/etc/zabbix" ${WRKSRC} \
	  | ${XARGS} ${REINPLACE_CMD} -e 's#/etc/zabbix#${ETCDIR}#g'
	@${REINPLACE_CMD} -e 's#/usr/sbin/fping#${LOCALBASE}/sbin/fping#g' ${WRKSRC}/conf/zabbix_*.conf

.if ${ZABBIX_BUILD} != "agent"
.if empty(PORT_OPTIONS:MFPING)
.endif
.for d in mysql oracle postgresql sqlite3
	@${REINPLACE_CMD} -e 's|/bin/ping|/sbin/ping|g; \
	                      s|/usr/bin/traceroute|/usr/sbin/traceroute|g; \
	                      s|sudo /usr/bin/nmap|sudo ${LOCALBASE}/bin/nmap|g;' \
	                      ${WRKSRC}/database/${d}/data.sql
.endfor
.endif
	@${REINPLACE_CMD} -Ee 's|(@sysconfdir@/(\$$\([A-Z]*_CONFIG\)))" ([|][|] cp "../../conf/\$$\([A-Z]*_CONFIG\)" "\$$\(DESTDIR\)@sysconfdir@)"|\1.sample" \3/\2.sample"|;' \
		${WRKSRC}/src/zabbix_${ZABBIX_BUILD}/Makefile.in
	@${FIND} ${WRKSRC} -type f \( -name '*.bak' -or -name '*.orig' \) -exec ${RM} -f {} +

post-install:

.if defined(WITH_JAVAGW)
	@${MV} ${STAGEDIR}${PREFIX}/sbin/zabbix_java/settings.sh ${STAGEDIR}${PREFIX}/sbin/zabbix_java/settings.sh.sample
.endif

.if ${ZABBIX_BUILD} != "agent"
	@${MKDIR} "${STAGEDIR}${DATADIR}/${ZABBIX_BUILD}/database"
	@cd ${WRKSRC}/upgrades/ && ${COPYTREE_SHARE} dbpatches ${STAGEDIR}${DATADIR}/${ZABBIX_BUILD}/upgrades/
	@cd ${WRKSRC}/database/ && ${COPYTREE_SHARE} "ibm_db2 mysql oracle postgresql sqlite3" ${STAGEDIR}${DATADIR}/${ZABBIX_BUILD}/database/
.endif
.endif # if ${ZABBIX_BUILD} != "frontend"

.include <bsd.port.mk>
