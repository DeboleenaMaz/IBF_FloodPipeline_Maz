#API_SERVICE_URL = 'https://ibf-test.510.global/api/'
#IBF_API_URL = 'https://ibf-test.510.global/api/'
#API_LOGIN_URL = IBF_API_URL+'user/login'
#API_SERVICE_URL = IBF_API_URL
#ADMIN_LOGIN = 'dunant@redcross.nl'
#ADMIN_PASSWORD = 'password'
#API_SERVICE_URL = 'https://ibf-ethiopia.510.global/api/'
#IBF_API_URL = 'https://ibf-ethiopia.510.global/api/'
#API_LOGIN_URL =API_LOGIN_URL# 'https://ibf-ethiopia.510.global/api/user/login'
ADMIN_LOGIN = 'dunant@redcross.nl'
#ADMIN_PASSWORD = 'sLuE6V6ExyqEppZw'
ADMIN_PASSWORD = 'password'
GLOFAS_API_KEY='67259:2636f069-273b-4e2a-858e-70d67c629c0c'
GLOFAS_API_URL='https://cds.climate.copernicus.eu/api/v2'
GLOFAS_USER='safer'
GLOFAS_PW = 'neo2008'
GLOFAS_FTP = 'data-portal.ecmwf.int/ZambiaRedcross_glofas_point/'
DATALAKE_STORAGE_ACCOUNT_NAME = '510datalakestorage'
DATALAKE_STORAGE_ACCOUNT_KEY = 'RnPSnWqM6sDvTMxMyYVu9cKhqN1yJ6Q5PcqC6WEIzXBtyLOojaoLt71e4VhMfohDTE2NMZ2fwJ6hxT69JD6Fig=='
DATALAKE_API_VERSION = '2018-11-09'
GOOGLE_DRIVE_DATA_URL='https://drive.google.com/file/d/1vptMfC_IVm4EwEC67G1Q_KoapxeQCiCc/view?usp=sharing'


# COUNTRY SETTINGS
SETTINGS_SECRET = {
    "ZMB": {
        "IBF_API_URL":'https://ibf-test.510.global/api/',
        "mock": True,
        "if_mock_trigger": True,
        "notify_email": False
    },
    "UGA": {
        "IBF_API_URL":'https://ibf-test.510.global/api/',
        "mock": True,
        "if_mock_trigger": True,
        "notify_email": False
    },
    "KEN": {
        "IBF_API_URL":'https://ibf-test.510.global/api/',
        "mock": True,
        "if_mock_trigger": False,
        "notify_email": False,
        
    },
    "ETH": {
        "IBF_API_URL":'https://ibf-test.510.global/api/',
        "mock": False,
        "if_mock_trigger": False,
        "notify_email": False
    }
}