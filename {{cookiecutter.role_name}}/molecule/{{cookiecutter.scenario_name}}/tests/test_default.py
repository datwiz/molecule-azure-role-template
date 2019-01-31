import pytest

@pytest.mark.parametrize('file', [
    ('/etc/hosts'),
    ('/etc/resolv.conf'),
])
def test_files(host, file):
    f = host.file(file)
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
