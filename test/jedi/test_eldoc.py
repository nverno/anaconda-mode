from test.helpers import send


def test_eldoc_signature():
    rv = send('''
              def f(obj, fp, skipkeys=False, ensure_ascii=True,
                    check_circular=True, allow_nan=True, cls=None,
                    indent=None, separators=None, default=None,
                    sort_keys=False, **kw):
                  pass

              f(_|_
              ''', 'eldoc')

    assert rv == ('f(obj, fp, skipkeys = False, ensure_ascii = True,'
                  ' check_circular = True, allow_nan = True, cls = None,'
                  ' indent = None, separators = None, default = None,'
                  ' sort_keys = False, **kw)')


def test_eldoc_unknown_fn():
    rv = send('''
              unknown_fn(_|_
              ''', 'eldoc')
    assert rv == ''
