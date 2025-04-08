from django.urls import path, include

app_configs = [
	{ 'app_name': 'finance.purchases', 'url': 'finance/purchases/', 'namespace': 'purchases' },

	{ 'app_name': 'people.customers', 'url': 'people/customers/', 'namespace': 'customers' },

	{ 'app_name': 'inventory.suppliers', 'url': 'inventory/suppliers/', 'namespace': 'suppliers' },

	{ 'app_name': 'inventory.stock', 'url': 'inventory/stock/', 'namespace': 'stock' },

	{ 'app_name': 'finance.payments', 'url': 'finance/payments/', 'namespace': 'payments' },

	{ 'app_name': 'finance.sales', 'url': 'finance/sales/', 'namespace': 'sales' },

	{ 'app_name': 'accounts', 'url': 'accounts/', 'namespace': 'accounts' },

	{ 'app_name': 'misc.pages', 'url': '', 'namespace': 'pages' },

	{ 'app_name': 'inventory.parts', 'url': 'inventory/parts/', 'namespace': 'parts' },

    # { "app_name": "finances.payments", "url": "finances/payments", "namespace": "payments" },
]

def getAppUrls():
    urlpatterns = []
    for config in app_configs:
        urlpatterns.append(
            path(f"{config['url']}", include(f"{config['app_name']}.urls", namespace=config['namespace']))
        )
    return urlpatterns

def getAppNames():
    return [config['app_name'] for config in app_configs]
