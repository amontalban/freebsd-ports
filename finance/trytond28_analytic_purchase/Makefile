# Created by: Matthias Petermann <matthias@petermann-it.de>
# $FreeBSD$

PORTNAME=	trytond28_analytic_purchase
PORTVERSION=	2.8.0
PORTREVISION=	1
CATEGORIES=	finance python
MASTER_SITES=	https://pypi.python.org/packages/source/t/trytond_analytic_purchase/ \
		http://downloads.tryton.org/${PORTVERSION:R}/
DISTNAME=	trytond_analytic_purchase-${PORTVERSION}

MAINTAINER=	matthias@petermann-it.de
COMMENT=	Tryton Application Platform (Analytic Purchase Module)

LICENSE=	GPLv3

RUN_DEPENDS=	trytond28_analytic_account>=2.8.0:${PORTSDIR}/finance/trytond28_analytic_account \
		trytond28_analytic_invoice>=2.8.0:${PORTSDIR}/finance/trytond28_analytic_invoice \
		trytond28_purchase>=2.8.0:${PORTSDIR}/finance/trytond28_purchase

CONFLICTS=	trytond_analytic_purchase-2.[46].*

USE_PYTHON=	yes
USE_PYDISTUTILS=	yes
PYDISTUTILS_AUTOPLIST=	yes
PYEASYINSTALL_EGG=${DISTNAME}-py${PYTHON_VER}${PYEASYINSTALL_OSARCH}.egg

.include <bsd.port.mk>
