# coding=utf-8

from domain.base.provider import Provider


class ResCalcProvider(object):

    def calc(self, package_id, inputs):
        pass


Provider.register(ResCalcProvider)

if __name__ == '__main__':
    provider = ResCalcProvider()
    print('Subclass:', issubclass(ResCalcProvider, Provider))
    print('Instance:', isinstance(provider, Provider))
    provider.calc(None, None)
