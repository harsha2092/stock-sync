from upload_bse_daily_trade_file_to_postgres import upload_bse
from upload_nse_daily_trade_file_to_postgres import upload_nse

#ddmmyy
dateToGetData = "030720" 
upload_bse(dateToGetData)
upload_nse(dateToGetData)