# coding=utf-8
from domain.provider.res_calc_provider import ResCalcProvider


class ResCalcProviderImpl(ResCalcProvider):

    def calc(self, package_id, inputs):
        print('resource calc')


if __name__ == '__main__':
    from domain.base import Provider
    provider = ResCalcProviderImpl()
    print('Subclass:', issubclass(ResCalcProviderImpl, Provider))
    print('Instance:', isinstance(provider, Provider))
    provider.calc(None, None)
