# coding=utf-8
from domain.base.provider import Provider


class CatalogProvider(object):

    def check_status(self, package):
        pass

Provider.register(CatalogProvider)

if __name__ == '__main__':
    provider = CatalogProvider()
    print('Subclass:', issubclass(CatalogProvider, Provider))
    print('Instance:', isinstance(provider, Provider))
    provider.check_status(None)
