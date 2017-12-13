# coding=utf-8

from domain.base.provider import Provider


class ResGrantProvider(object):

    def grant(self, res_model_json):
        pass


Provider.register(ResGrantProvider)

if __name__ == '__main__':
    provider = ResGrantProvider()
    print('Subclass:', issubclass(ResGrantProvider, Provider))
    print('Instance:', isinstance(provider, Provider))
    provider.grant(None)
