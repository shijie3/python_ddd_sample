# coding=utf-8

from domain.provider.catalog_provider import CatalogProvider


class CatalogProviderImpl(CatalogProvider):

    def check_status(self, package):
        print('check package status')


if __name__ == '__main__':
    from domain.base import Provider
    provider = CatalogProviderImpl()
    print('Subclass:', issubclass(CatalogProviderImpl, Provider))
    print('Instance:', isinstance(provider, Provider))
    provider.check_status(None)
