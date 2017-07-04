try:
    import unittest2 as unittest
except ImportError:
    import unittest



import thepyutils.str.str as tss


class TestStr(unittest.TestCase):


    def test_all_but_last(self):
        self.assertEqual(tss.all_but_last('This is a test string'),
                         'This is a test')

    def test_all_but_last_sep(self):
        self.assertEqual(tss.all_but_last('This:is:a:test:string', sep=':'),
                         'This:is:a:test')
                         
