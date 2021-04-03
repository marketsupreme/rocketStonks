import os
import unittest
import sys

from models import app,db,Stock, StockIntraday, StockStats

class Tests(unittest.TestCase):

    def test_1(self):
        a = Stock(name='Bumble', ticker= '$BMBL', exchange= '1', price='2', change='3', 
                    changePercent='5', day='6', previousClose='7', marketCapitalization='8', 
                    open='9', beta='10', peRatio='11', eps='12', low='13', high='14', 
                    yearlyLow='15', yearlyHigh='16', dividend='17', 
                    dividendYield='18', volume='19', exDividend='20', category='21'  )
        db.session.add(a)
        db.session.commit()

        b = db.session.query(Stock).filter_by(name= 'Bumble').one()
        self.assertEqual(str(b.name), 'Bumble')

        db.session.query(Stock).filter_by(name= 'Bumble').delete()
        db.session.commit()
    
    def test_2(self):
        a = Stock(name='Nvidia', ticker= '$NVDA', exchange= '1', price='2', change='3', 
                    changePercent='5', day='6', previousClose='7', marketCapitalization='8', 
                    open='9', beta='10', peRatio='11', eps='12', low='13', high='14', 
                    yearlyLow='15', yearlyHigh='16', dividend='17', 
                    dividendYield='18', volume='19', exDividend='20', category='21'  )
        db.session.add(a)
        db.session.commit()

        b = db.session.query(Stock).filter_by(name= 'Nvidia').one()
        self.assertEqual(str(b.name), 'Nvidia')

        db.session.query(Stock).filter_by(name= 'Nvidia').delete()
        db.session.commit()
    
    def test_3(self):
        a = Stock(name='GameStop', ticker= '$GME', exchange= '1', price='2', change='3', 
                    changePercent='5', day='6', previousClose='7', marketCapitalization='8', 
                    open='9', beta='10', peRatio='11', eps='12', low='13', high='14', 
                    yearlyLow='15', yearlyHigh='16', dividend='17', 
                    dividendYield='18', volume='19', exDividend='20', category='21'  )
        db.session.add(a)
        db.session.commit()

        b = db.session.query(Stock).filter_by(name= 'GameStop').one()
        self.assertEqual(str(b.name), 'GameStop')

        db.session.query(Stock).filter_by(name= 'GameStop').delete()
        db.session.commit()
    
    def test_4(self):
        a = StockIntraday(date='1', price='2', ticker='3',open='4', high='5', volume='6', low='7')

        db.session.add(a)
        db.session.commit()

        b = db.session.query(StockIntraday).filter_by(date='1').one()
        self.assertEqual(str(b.date), '1')

        db.session.query(StockIntraday).filter_by(date='1').delete()
        db.session.commit()
    
    def test_5(self):
        a = StockStats(symbol='$GME', name='GameStop', description='a', currency='s', 
            country='d', MarketCapitalization='f', 
            EBITDA='g', PERatio='h', PEGRatio='k', BookValue='l', 
            DividendPerShare='1', DividendYield='2', EPS='3', 
            RevenuePerShareTTM='4', ProfitMargin='5', 
            OperatingMarginTTM='6', ReturnOnAssetsTTM='7',
            ReturnOnEquityTTM='8', RevenueTTM='9', 
            GrossProfitTTM='0', DilutedEPSTTM='10', 
            QuarterlyEarningsGrowthYOY='11', QuarterlyRevenueGrowthYOY='12', 
            AnalystTargetPrice='13', TrailingPE='14', 
            ForwardPE='15', PriceToSalesRatioTTM='16', 
            PriceToBookRatio='17', EVToRevenue='18', EVToEBITDA='19')
        
        db.session.add(a)
        db.session.commit()

        b = db.session.query(StockStats).filter_by(symbol='$GME').one()
        self.assertEqual(str(b.symbol), '$GME')

        db.session.query(StockStats).filter_by(symbol='$GME').delete()
        db.session.commit()
    

if __name__ == "__main__":
    unittest.main()