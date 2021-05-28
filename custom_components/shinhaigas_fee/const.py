"""Constants of the ShinHai Gas Fee component."""

DEFAULT_NAME = "ShinHai Gas Fee"
DOMAIN = "shinhaigas_fee"
DOMAINS = ["sensor"]
DATA_KEY = "sensor.shinhaigas_fee"

ATTR_BILLING_DATE = "billing_date"
ATTR_CURRENT_GASMETER = "current_gasmeter"
ATTR_PAYMENT = "gas_payment"
ATTR_GAS_CONSUMPTION = "gas_consumption"
ATTR_CURRENT_STATUS = "current_status"
ATTR_BILL_AMOUNT = "billing_amount"
ATTR_HTTPS_RESULT = "https_result"
ATTR_LIST = [
    ATTR_BILLING_DATE,
    ATTR_CURRENT_GASMETER,
    ATTR_PAYMENT,
    ATTR_GAS_CONSUMPTION,
    ATTR_CURRENT_STATUS,
    ATTR_BILL_AMOUNT,
    ATTR_HTTPS_RESULT
]

CONF_GASID = "gasid"
ATTRIBUTION = "Powered by ShinHai Gas Data"

HA_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 OPR/38.0.2220.41"
BASE_URL = 'http://www.shinhaigas.com.tw/billquery.php'

REQUEST_TIMEOUT = 10  # seconds
