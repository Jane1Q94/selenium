from selenium import webdriver
import time
import collections
cookie = [
{
    "domain": ".alipay.com",
    "hostOnly": 'false',
    "httpOnly": 'true',
    "name": "ali_apache_tracktmp",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'true',
    "storeId": "0",
    "value": "\"uid=2088512309621063\"",
    "id": 1
},
{
    "domain": ".alipay.com",
    "expirationDate": 1543120460.966778,
    "hostOnly": 'false',
    "httpOnly": 'true',
    "name": "alipay",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'false',
    "storeId": "0",
    "value": "\"K1iSL1z1pqZ1OmQvJ1hdAsdOQ15vFvI5wKPmYcnx/G3DuOz5\"",
    "id": 2
},
{
    "domain": ".alipay.com",
    "hostOnly": 'false',
    "httpOnly": 'false',
    "name": "ALIPAYJSESSIONID",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'true',
    "storeId": "0",
    "value": "RZ19lSAmHIPYMarq5FHtHM3uSoaX7oauthRZ25GZ00",
    "id": 3
},
{
    "domain": ".alipay.com",
    "hostOnly": 'false',
    "httpOnly": 'true',
    "name": "CLUB_ALIPAY_COM",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'true',
    "storeId": "0",
    "value": "2088512309621063",
    "id": 4
},
{
    "domain": ".alipay.com",
    "expirationDate": 3626384463.144629,
    "hostOnly": 'false',
    "httpOnly": 'false',
    "name": "cna",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'false',
    "storeId": "0",
    "value": "wtDBE23y1kwCAdz4LD6GANQh",
    "id": 5
},
{
    "domain": ".alipay.com",
    "expirationDate": 1574604836,
    "hostOnly": 'false',
    "httpOnly": 'false',
    "name": "credibleMobileSendTime",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'false',
    "storeId": "0",
    "value": "-1",
    "id": 6
},
{
    "domain": ".alipay.com",
    "hostOnly": 'false',
    "httpOnly": 'false',
    "name": "ctoken",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'true',
    "storeId": "0",
    "value": "vWbJM8lMql0J7REt",
    "id": 7
},
{
    "domain": ".alipay.com",
    "expirationDate": 1574604836,
    "hostOnly": 'false',
    "httpOnly": 'false',
    "name": "ctuMobileSendTime",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'false',
    "storeId": "0",
    "value": "-1",
    "id": 8
},
{
    "domain": ".alipay.com",
    "expirationDate": 1543161860.966879,
    "hostOnly": 'false',
    "httpOnly": 'true',
    "name": "iw.userid",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'false',
    "storeId": "0",
    "value": "\"K1iSL1z1pqZ1OmQvJ1hdAg==\"",
    "id": 9
},
{
    "domain": ".alipay.com",
    "hostOnly": 'false',
    "httpOnly": 'true',
    "name": "LoginForm",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'true',
    "storeId": "0",
    "value": "alipay_login_home",
    "id": 10
},
{
    "domain": ".alipay.com",
    "expirationDate": 1574604836,
    "hostOnly": 'false',
    "httpOnly": 'false',
    "name": "mobileSendTime",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'false',
    "storeId": "0",
    "value": "-1",
    "id": 11
},
{
    "domain": ".alipay.com",
    "expirationDate": 1574604836,
    "hostOnly": 'false',
    "httpOnly": 'false',
    "name": "riskCredibleMobileSendTime",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'false',
    "storeId": "0",
    "value": "-1",
    "id": 12
},
{
    "domain": ".alipay.com",
    "expirationDate": 1574604836,
    "hostOnly": 'false',
    "httpOnly": 'false',
    "name": "riskMobileAccoutSendTime",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'false',
    "storeId": "0",
    "value": "-1",
    "id": 13
},
{
    "domain": ".alipay.com",
    "expirationDate": 1574604836,
    "hostOnly": 'false',
    "httpOnly": 'false',
    "name": "riskMobileBankSendTime",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'false',
    "storeId": "0",
    "value": "-1",
    "id": 14
},
{
    "domain": ".alipay.com",
    "expirationDate": 1574604836,
    "hostOnly": 'false',
    "httpOnly": 'false',
    "name": "riskMobileCreditSendTime",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'false',
    "storeId": "0",
    "value": "-1",
    "id": 15
},
{
    "domain": ".alipay.com",
    "expirationDate": 1574604836,
    "hostOnly": 'false',
    "httpOnly": 'false',
    "name": "riskOriginalAccountMobileSendTime",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'false',
    "storeId": "0",
    "value": "-1",
    "id": 16
},
{
    "domain": ".alipay.com",
    "expirationDate": 1574654662,
    "hostOnly": 'false',
    "httpOnly": 'false',
    "name": "rtk",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'false',
    "storeId": "0",
    "value": "IWrjlMcWmYGFztyAvWr8aYUF0NkqfVhWElrvKkbEAqtjPsauKdx",
    "id": 17
},
{
    "domain": ".alipay.com",
    "hostOnly": 'false',
    "httpOnly": 'false',
    "name": "session.cookieNameId",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'true',
    "storeId": "0",
    "value": "ALIPAYJSESSIONID",
    "id": 18
},
{
    "domain": ".alipay.com",
    "expirationDate": 1574683461.951822,
    "hostOnly": 'false',
    "httpOnly": 'true',
    "name": "unicard1.vm",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'true',
    "session": 'false',
    "storeId": "0",
    "value": "\"K1iSL1z1pqZ1OmQvJ1hdAg==\"",
    "id": 19
},
{
    "domain": ".alipay.com",
    "hostOnly": 'false',
    "httpOnly": 'false',
    "name": "zone",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'true',
    "storeId": "0",
    "value": "GZ00D",
    "id": 20
},
{
    "domain": "my.alipay.com",
    "expirationDate": 1543155243.219969,
    "hostOnly": 'true',
    "httpOnly": 'true',
    "name": "CHAIR_SESS",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'true',
    "session": 'false',
    "storeId": "0",
    "value": "K6iO619fGWnMOmQO_wFsrOC7EDTcDQys6FECFoD0f1E0-LcyaWvVerWWQg93dGOFWVbJdveS9bN3qncWn-iSoc017SzVvujxLzsHt_041oKkpJOutxv2lrKa9XsAKk9T4uORDQyAXnwVK4i8uqx42A==",
    "id": 21
},
{
    "domain": "my.alipay.com",
    "hostOnly": 'true',
    "httpOnly": 'false',
    "name": "spanner",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'true',
    "session": 'true',
    "storeId": "0",
    "value": "rZ5PwuzeViNk4x8DWBHriNUhsHdrCkRb",
    "id": 22
},
{
    "domain": "my.alipay.com",
    "hostOnly": 'true',
    "httpOnly": 'false',
    "name": "ssl_upgrade",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'true',
    "session": 'true',
    "storeId": "0",
    "value": "0",
    "id": 23
}
]
#cookie_washed = dict([c.split("=", 1) for c in cookie.split("; ")])




driver = webdriver.Chrome()
driver.get("https://my.alipay.com/portal/i.htm?referer=https%3A%2F%2Fauthsu121.alipay.com%2Flogin%2FhomeB.htm")


#cookie_washed_2 = {"name":"buvid3", "value":"61063DFE-9148-43A9-B91C-941EF6E04C65149011infoc"}

#driver.add_cookie(cookie_dict=cookie_washed_2)

for c in cookie:

    driver.add_cookie(cookie_dict=c)



driver.get("https://my.alipay.com/portal/i.htm?referer=https%3A%2F%2Fauthsu121.alipay.com%2Flogin%2FhomeB.htm")

print(driver.get_cookies())

time.sleep(4)
