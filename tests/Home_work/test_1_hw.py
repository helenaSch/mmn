def test_home_work():
    assert ('home', 'work') == ('home', 'work')


def test_qa_about():
    assert not 'QA' == 'QC'


def test_numbers():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)
