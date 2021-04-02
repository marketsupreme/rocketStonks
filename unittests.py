import os
import unittest
import sys

from models import app,db,Stock

class Tests(unittest.TestCase):

    def test_1(self):
        a = Stock(id='', title= '')
        db.session.add(a)
        db.session.commit()

        b = db.session.query(Stock).filter_by(id = '').one()
        self.assertEqual(str(b.id), '')

        db.session.query(Stock).filter_by(id = '').delete()
        db.session.commit()

if __name__ == "__main__":
    unittest.main()