from postgres_util import writeToPostgresFromCsvFile
from download_transform import getDownloadedFile
import arrow

def upload_nse(dateToDownload):
    months = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
    # dateToDownload = "270520"
    format_str = 'DDMMYY' # The format
    date_obj = arrow.get(dateToDownload, format_str)
    # cm01JUN2020bhav.csv
    dateOfMonth = str(date_obj.day) if len(str(date_obj.day)) == 2 else "0"+str(date_obj.day)
    csvFileToExtract = "cm" +  dateOfMonth + months[date_obj.month-1] + str(date_obj.year) + "bhav.csv"
    # cm01JUN2020bhav.csv.zip
    zipFileToDownload = csvFileToExtract + ".zip"
    newCsvFileName = "NSE_" + csvFileToExtract
    # https://www1.nseindia.com/content/historical/EQUITIES/2020/MAY/cm27MAY2020bhav.csv.zip
    # https://www1.nseindia.com/content/historical/EQUITIES/2020/JUN/cm01JUN2020bhav.csv.zip
    urlToDowndoad = "https://www1.nseindia.com/content/historical/EQUITIES/" + str(date_obj.year) + "/" + months[date_obj.month-1]+ "/" +zipFileToDownload
    folderToWriteTo = "./nse/" 
    zipFileToWriteTo = folderToWriteTo + zipFileToDownload
    extractedcsvFileCompletePath = folderToWriteTo + csvFileToExtract
    newFileCompletePath = folderToWriteTo + newCsvFileName 

    metaDataToDownloadFile = {
        'urlToDowndoad': urlToDowndoad,
        'completZipFilePathToDownload': zipFileToWriteTo, 
        'csvFileToExtract': csvFileToExtract,
        'folderToExtract': folderToWriteTo,
        'completeCsvFilePathToExtract': extractedcsvFileCompletePath,
        'newCompleteCsvFilePathToRename': newFileCompletePath,
        'type': "NSE",
        'existingHeader': "SYMBOL,SERIES,OPEN,HIGH,LOW,CLOSE,LAST,PREVCLOSE,TOTTRDQTY,TOTTRDVAL,TIMESTAMP,TOTALTRADES,ISIN,",
        'newHeader': "security_id,equity_group,open,high,low,close,last,prev_close,no_of_shares,net_turnover,trading_date,no_trades,isin_no"
    }
    fileToUpload = getDownloadedFile(metaDataToDownloadFile)
    writeToPostgresFromCsvFile(fileToUpload, "nse_daily_trade")