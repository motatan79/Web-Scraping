import pytest

from pytestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("data_load")
class TestExample2(BaseClass):

    def test_editProfile(self, data_load):
        log = self.getLogger()
        log.info(data_load[0])
        log.info(data_load[2])
        # print(data_load[0])
        print(data_load[2])