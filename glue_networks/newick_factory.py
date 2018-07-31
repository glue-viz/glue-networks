from __future__ import absolute_import, division, print_function

import os
import glob
import re
import numpy as np

from glue.logger import logger
from glue.core.data import Data
from glue.config import data_factory

__all__ = ['is_newick', 'newick_reader']


def newick_label(filename):
    """
    This function just returns the name of the file without the .nwk extension
    if present. We don't strip off any other extensions in case they are part
    of the name and not actually an extension.
    """
    label = os.path.basename(os.path.normpath(filename))
    if label.endswith('.nwk'):
        label = label[:-4]
    return label


def is_newick(filename, **kwargs):
    """
    Determine if the file is of newick type
    """
    return filename.endswith('.nwk')

def parse(newick):
    tokens = re.findall(r"([^:;,()\s]*)(?:\s*:\s*([\d.]+)\s*)?([,);])|(\S)", newick+";")

    def recurse(nextid = 0, parentid = -1): # one node
        thisid = nextid;
        children = []
        name, length, delim, ch = tokens.pop(0)
        if ch == "(":
            while ch in "(,":
                node, ch, nextid = recurse(nextid+1, thisid)
                children.append(node)
            name, length, delim, ch = tokens.pop(0)

        return {"id": thisid, "name": name, "length": float(length) if length else None,
                "parentid": parentid, "children": children}, delim, nextid

    return recurse()[0]


def extract_arrays(tree_structure, names, parent, size):
    names.append(tree_structure['name'])
    parent.append(tree_structure['parentid'])
    size.append(tree_structure['length'])
    if tree_structure['children']:
        for sub_dicts in tree_structure['children']:
            extract_arrays(sub_dicts, names, parent, size)


@data_factory(
    label='Newick file or directory',
    identifier=is_newick,
    priority=99999,
)
def newick_reader(file_name):

    with open(file_name, 'r') as f:
        newick_tree = f.readline()

    # Open and parse newick file
    # convert newick file into parent array
    names = []
    size = []
    parent = []

    newick_in = parse(newick_tree)
    extract_arrays(newick_in, names, parent, size)

    if (size[0] == None):
        size[0] = 0

    data = Data(label='newick file')
    data['parent'] = parent
    data['names'] = names
    data['size'] = size

    return data
