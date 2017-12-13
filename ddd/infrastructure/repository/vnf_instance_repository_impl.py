# coding=utf-8

from domain.repository.vnf_instance_repository import VnfInstanceRepository


class VnfInstanceRepositoryImpl(VnfInstanceRepository):
    def __init__(self):
        self._repo = {}

    def add(self):
        print "add vnf instance"

    def save(self):
        print "save vnf instance"

    def update(self):
        print "update vnf instance"

    def delete(self):
        print "delete vnf instance"

    def find_by_id(self, id):
        print "find vnf instance"

    def _has_key(self):
        print "check vnf instance"


if __name__ == '__main__':
    from domain.base.repository import Repository
    print('Subclass:', issubclass(VnfInstanceRepositoryImpl, Repository))
    print('Instance:', isinstance(VnfInstanceRepositoryImpl(), Repository))
