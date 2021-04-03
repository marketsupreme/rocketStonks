from requests import get
import json
import time as t

#use text file to create list used to parse through easily in the scrape() fucntion
def create_list():
    with open('stockList.txt', 'r') as sl:
        ticker_list = []
        for line in sl:
            if line == 'end':
                return(ticker_list)
            new = line.replace('\n','')
            ticker_list.append(str(new))
    sl.close()

#use text file with tickers and categories to create an empty dictionary with zeros as placeholders
def create_dict():
    with open('stockList.txt', 'r') as sl:
        ticker_dict = {'Technology': 0, 'Biomedical': 0, 'Industry': 0, 'Cryptocurrency': 0, 'Penny Stocks': 0}
        temp_dict = {}
        sl.readline()
        for line in sl:
            if line == 'Industry\n':
                ticker_dict['Technology'] = temp_dict
                temp_dict = {}
                continue
            if line == 'Biomedical\n':
                ticker_dict['Industry'] = temp_dict
                temp_dict = {}
                continue
            if line == 'end':
                ticker_dict['Biomedical'] = temp_dict
                temp_dict = {}
                continue

            new = line.replace('\n','')
            temp_dict[str(new)]=0

    sl.close()
    return ticker_dict

#scraping AlphaVantage in increments of 1 minute so as to not overuse credits
def scrape():

    ticker_dict = create_dict()
    ticker_list = create_list()
    cat_list = ['Technology','Biomedical', 'Industry', 'Cryptocurrency' 'Penny Stocks']
    # ticker_list = ['Technology','Jim','Biomedical', 'Industry']
    # cat_list = ['Technology','Biomedical', 'Industry', 'Bill']

    main_key2 = '10SVU9Y1PENCIBZN'
    main_key1 = '1TOJZH2ZKESRFYVI'
    main_key = main_key1
    counter = 0

    for ticker in ticker_list:
        if ticker in cat_list:
            cat = ticker
            continue
        
        print(f'beginning {ticker}')

        '''ALPHA VANTAGE API CALLS'''
        #OVERVIEW
        overview = get(f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&apikey={main_key}")
        OVERVIEW_JSON = overview.json()

        # #GLOBAL_QUOTE
        global_quote = get(f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={main_key}&datatype=json")
        GLOBAL_QUOTE_JSON = global_quote.json()
        
        # #TIME_SERIES_DAILY
        time_series_daily = get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={main_key}&datatype=json")
        TIME_SERIES_DAILY_JSON = time_series_daily.json()
        
        # #TIME_SERIES_INTRADAY
        time_series_intraday = get(f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=15min&apikey={main_key}&datatype=json")
        TIME_SERIES_INTRADAY_JSON = time_series_intraday.json()

        #change key if number of calls is too high
        counter+=4
        if counter >300:
            main_key = main_key2
            print('key changed')
        
        ticker_dict[cat][ticker] = {'OVERVIEW': OVERVIEW_JSON, 'GLOBAL_QUOTE': GLOBAL_QUOTE_JSON, 'TIME_SERIES_DAILY': TIME_SERIES_DAILY_JSON, 'TIME_SERIES_INTRADAY': TIME_SERIES_INTRADAY_JSON}

        with open('stocks.json', 'w') as fp:
            json.dump(ticker_dict, fp, indent=4)
        fp.close()

        print(f'done with {ticker}')
        print('Waiting...')
        t.sleep(65)
        
    with open('stocks.json', 'w') as fp:
        json.dump(ticker_dict, fp, indent=4)
    fp.close()
        

scrape()
