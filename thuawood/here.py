import sys
_before = sys.path[:]
import site, os.path as op
ROOT = op.abspath(op.dirname(__file__))
path = lambda *a: op.join(ROOT, *a)
site.addsitedir(path('vendor'))
_after = sys.path
for each in _after:
    if each not in _before:
        _after.remove(each)
        sys.path.insert(0, each)
