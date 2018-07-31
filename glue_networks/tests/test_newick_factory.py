import os
import glob
import shutil

from ..newick_factory import is_newick, newick_reader

DATA = os.path.join(os.path.dirname(__file__), 'data')


def test_dicom(tmpdir):

    # empty_dir = tmpdir.strpath
    data = newick_reader(os.path.join(DATA, 'newick0.nwk'))
    assert list(data['parent']) == [-1, 0, 0, 0, 3, 3]
    assert list(data['size']) == [0, 0.1, 0.2, 0.5, 0.3, 0.4]

    data = newick_reader(os.path.join(DATA, 'newick1.nwk'))
    assert list(data['parent']) == [-1, 0, 0, 2, 2]
    assert list(data['size']) == [50.0, 20.0, 20.0, 30.0, 60.0]

    data = newick_reader(os.path.join(DATA, 'newick2.nwk'))
    assert list(data['parent']) == [-1, 0, 0, 2, 2, 4, 4, 6, 6, 8, 8, 0]
    assert list(data['size']) == [1.0, 0.69395, 0.54939, 0.36079, 0.15057, 0.33636, 0.06124, 0.17147, 0.08386, 0.19268, 0.11927, 1.2146]
