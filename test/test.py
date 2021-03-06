import pytest
from model.CovidRecordDTO import CovidRecord
import model.FileUtiles
import controller.Main


# from model.FileUtiles import FileUtils


class TestApp:

    @pytest.fixture
    def __init__(self, mocker):
        cov = []
        self.rec = CovidRecord('59', 'British Columbia', 'Colombie-Britannique', '1/31/2020', '1', '0', '0', '1', '1',
                               '1')
        cov.append(self.rec)
        cov.append(self.rec)

        # mocker.patch("model.FileUtiles.FileUtils._open_file", return_value=cov)

    # def test_get_file_content(self, init):
    #     f = model.FileUtiles.FileUtils()
    #     test = f.get_content(filename="test")
    #     assert len(test) == 2
    #     assert test[0] == self.rec
    #     assert test[1] == self.rec

    def test_loading_on_different_thread(self):
        f = model.FileUtiles.FileUtils()
        covidRecord = f.get_content("../../data/covid19-download.csv")

        assert len(covidRecord) > 0
