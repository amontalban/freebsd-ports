# $FreeBSD$

PORTNAME=	libarchive
PORTVERSION=	3.1.2
PORTREVISION=	1
PORTEPOCH=	1
CATEGORIES=	archivers
MASTER_SITES=	http://libarchive.org/downloads/

MAINTAINER=	glewis@FreeBSD.org
COMMENT=	Library to create and read several streaming archive formats

OPTIONS_DEFINE=	LIBXML2 LZO NETTLE
OPTIONS_DEFAULT=LIBXML2 LZO

LIBXML2_DESC=	Support writing xar via libxml2
LZO_DESC=	Support lzo compression via liblzo2
NETTLE_DESC=	Use Nettle instead of OpenSSL

USES=		pathfix
GNU_CONFIGURE=	yes
USE_LDCONFIG=	yes
PATCH_STRIP=	-p1

CONFIGURE_ARGS+=	--without-expat

PLIST_FILES=	bin/bsdcpio \
		bin/bsdtar \
		include/archive.h \
		include/archive_entry.h \
		lib/libarchive.a \
		lib/libarchive.la \
		lib/libarchive.so \
		lib/libarchive.so.14 \
		libdata/pkgconfig/libarchive.pc \
		man/man1/bsdcpio.1.gz \
		man/man1/bsdtar.1.gz \
		man/man3/archive_entry.3.gz \
		man/man3/archive_entry_acl.3.gz \
		man/man3/archive_entry_linkify.3.gz \
		man/man3/archive_entry_paths.3.gz \
		man/man3/archive_entry_perms.3.gz \
		man/man3/archive_entry_stat.3.gz \
		man/man3/archive_entry_time.3.gz \
		man/man3/archive_read.3.gz \
		man/man3/archive_read_data.3.gz \
		man/man3/archive_read_disk.3.gz \
		man/man3/archive_read_extract.3.gz \
		man/man3/archive_read_filter.3.gz \
		man/man3/archive_read_format.3.gz \
		man/man3/archive_read_free.3.gz \
		man/man3/archive_read_header.3.gz \
		man/man3/archive_read_new.3.gz \
		man/man3/archive_read_open.3.gz \
		man/man3/archive_read_set_options.3.gz \
		man/man3/archive_util.3.gz \
		man/man3/archive_write.3.gz \
		man/man3/archive_write_blocksize.3.gz \
		man/man3/archive_write_data.3.gz \
		man/man3/archive_write_disk.3.gz \
		man/man3/archive_write_filter.3.gz \
		man/man3/archive_write_finish_entry.3.gz \
		man/man3/archive_write_format.3.gz \
		man/man3/archive_write_free.3.gz \
		man/man3/archive_write_header.3.gz \
		man/man3/archive_write_new.3.gz \
		man/man3/archive_write_open.3.gz \
		man/man3/archive_write_set_options.3.gz \
		man/man3/libarchive.3.gz \
		man/man3/libarchive_changes.3.gz \
		man/man3/libarchive_internals.3.gz \
		man/man5/cpio.5.gz \
		man/man5/libarchive-formats.5.gz \
		man/man5/mtree.5.gz \
		man/man5/tar.5.gz

CFLAGS+=	"-I${LOCALBASE}/include"
CPPFLAGS+=	"-I${LOCALBASE}/include"
LDFLAGS+=	"-L${LOCALBASE}/lib"

.include <bsd.port.options.mk>

.if ${PORT_OPTIONS:MLIBXML2}
USE_GNOME+=	libxml2
CONFIGURE_ARGS+=	--with-xml2
.else
CFLAGS+=	-DHAVE_BSDXML_H=1
LDFLAGS+=	-lbsdxml
CONFIGURE_ARGS+=	--without-xml2
.endif

.if ${PORT_OPTIONS:MLZO}
LIB_DEPENDS=	liblzo2.so:${PORTSDIR}/archivers/lzo2
CONFIGURE_ARGS+=	--with-lzo2
.else
CONFIGURE_ARGS+=	--without-lzo2
.endif

.if ${PORT_OPTIONS:MNETTLE}
LIB_DEPENDS+=	nettle:${PORTSDIR}/security/nettle
CONFIGURE_ARGS+=	--without-openssl --with-nettle
.else
USE_OPENSSL=	yes
CONFIGURE_ARGS+=	--with-openssl --without-nettle
.endif

check:
	(cd ${WRKSRC}; ${SETENV} ${MAKE_ENV} ${MAKE} check)

.include <bsd.port.mk>
