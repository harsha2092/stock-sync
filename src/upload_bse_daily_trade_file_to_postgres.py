from postgres_util import writeToPostgresFromCsvFile
from download_transform import getDownloadedFile

def upload_bse(dateToDownload):
    # dateToDownload = "270520"
    zipFileToDownload = "EQ_ISINCODE_"+ dateToDownload + ".zip"
    csvFileToExtract = "EQ_ISINCODE_"+ dateToDownload + ".CSV"
    newCsvFileName = "BSE_EQ_ISINCODE_"+ dateToDownload + ".csv"
    urlToDowndoad = "https://www.bseindia.com/download/BhavCopy/Equity/" + zipFileToDownload
    # fileToUpload = "C:/personal/documents/finance/share market/BSE/BSE_EQ_ISINCODE_270520.csv"
    folderToWriteTo = "./bse/" 
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
        'type': "BSE",
        'existingHeader': "SC_CODE,SC_NAME,SC_GROUP,SC_TYPE,OPEN,HIGH,LOW,CLOSE,LAST,PREVCLOSE,NO_TRADES,NO_OF_SHRS,NET_TURNOV,TDCLOINDI,ISIN_CODE,TRADING_DATE,FILLER2,FILLER3",
        'newHeader': "security_code,security_id,equity_group,SC_TYPE,open,high,low,close,last,prev_close,no_trades,no_of_shares,net_turnover,tdcloindi,isin_no,trading_date,filler2,filler3"
    }
    fileToUpload = getDownloadedFile(metaDataToDownloadFile)
    writeToPostgresFromCsvFile(fileToUpload, "bse_daily_trade")