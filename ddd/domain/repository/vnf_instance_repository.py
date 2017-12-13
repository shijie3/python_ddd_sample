# coding=utf-8

from domain.base.repository import Repository


class VnfInstanceRepository(object):
    def __init__(self):
        pass

    def add(self):
        pass

    def save(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def find_by_id(self, id):
        pass

    def _has_key(self):
        pass

Repository.register(VnfInstanceRepository)

if __name__ == '__main__':

    print('Subclass:', issubclass(VnfInstanceRepository, Repository))
    print('Instance:', isinstance(VnfInstanceRepository(), Repository))
