try:
    import unittest2 as unittest
except ImportError:
    import unittest

import datetime
import jdcal
    
import thepyutils.datemanip.mjd as tdm


class MJD2000Test(unittest.TestCase):

    def test_mjd2000_to_date(self):
        self.assertIsInstance(tdm.mjd2000_to_date(6393.499178),
                              datetime.datetime)

    def test_mjd2000_to_ISO_rettype(self):
        self.assertIsInstance(tdm.mjd2000_to_ISO(3456.92),
                              str)
        
    def test_mjd2000_to_ISO(self):
        self.assertEqual(tdm.mjd2000_to_ISO(6393.499178),
                         '2017-07-03T23:58:48.979200')

    def test_mjd2000_strftime(self):
        self.assertEqual(tdm.mjd2000_strftime(6393.499178, "%FT%T"),
                         '2017-07-03T23:58:48')

        
    # def test_mjd_fraction_to_timedelta(self):
    #     self.assertIsInstance(tdm.__mjd2000_fraction_to_timedelta(
    #         jdcal.jd2gcal(jdcal.MJD_0 + jdcal.MJD_JD2000, mjd)[3]),
    #                           datetime.timedelta)
                              

def main():
    unittest.main()


if __name__ == "__main__":
    main()
