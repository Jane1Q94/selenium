from selenium import webdriver
import time
cookie = [
{
    "domain": ".huazhu.com",
    "expirationDate": 1606207444,
    "hostOnly": 'false',
    "httpOnly": 'false',
    "name": "__utma",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'false',
    "storeId": "0",
    "value": "107792157.1109483102.1543134949.1543134949.1543134949.1",
    "id": 1
},
{
    "domain": ".huazhu.com",
    "expirationDate": 1543137244,
    "hostOnly": 'false',
    "httpOnly": 'false',
    "name": "__utmb",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'false',
    "storeId": "0",
    "value": "107792157.17.8.1543135443557",
    "id": 2
},
{
    "domain": ".huazhu.com",
    "hostOnly": 'false',
    "httpOnly": 'false',
    "name": "__utmc",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'true',
    "storeId": "0",
    "value": "107792157",
    "id": 3
},
{
    "domain": ".huazhu.com",
    "expirationDate": 1558903444,
    "hostOnly": 'false',
    "httpOnly": 'false',
    "name": "__utmz",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'false',
    "storeId": "0",
    "value": "107792157.1543134949.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)",
    "id": 4
},
{
    "domain": ".huazhu.com",
    "expirationDate": 1543139040.229657,
    "hostOnly": 'false',
    "httpOnly": 'true',
    "name": "_HZ_SessionId",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'false',
    "storeId": "0",
    "value": "9tB/9ZnWlYtLyJethpggPOTc46jMFowbBxDetJmW7YY=",
    "id": 5
},
{
    "domain": ".huazhu.com",
    "expirationDate": 1543136748,
    "hostOnly": 'false',
    "httpOnly": 'false',
    "name": "gr_session_id_8f6e3e7f89d647cab9784afa81ea87bd",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'false',
    "storeId": "0",
    "value": "1d1f7ae4-6271-4490-afd9-1eca4288c788",
    "id": 6
},
{
    "domain": ".huazhu.com",
    "expirationDate": 1543136748,
    "hostOnly": 'false',
    "httpOnly": 'false',
    "name": "gr_session_id_8f6e3e7f89d647cab9784afa81ea87bd_1d1f7ae4-6271-4490-afd9-1eca4288c788",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'false',
    "storeId": "0",
    "value": "'true'",
    "id": 7
},
{
    "domain": ".huazhu.com",
    "expirationDate": 1858495443,
    "hostOnly": 'false',
    "httpOnly": 'false',
    "name": "gr_user_id",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'false',
    "storeId": "0",
    "value": "e0d18278-ebf5-4559-9b6f-0f097ee3bb02",
    "id": 8
},
{
    "domain": ".huazhu.com",
    "hostOnly": 'false',
    "httpOnly": 'false',
    "name": "Hm_lpvt_e5770a47472445b3f839a58a32b8abe5",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'true',
    "storeId": "0",
    "value": "1543135444",
    "id": 9
},
{
    "domain": ".huazhu.com",
    "expirationDate": 1574671443,
    "hostOnly": 'false',
    "httpOnly": 'false',
    "name": "Hm_lvt_e5770a47472445b3f839a58a32b8abe5",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'false',
    "storeId": "0",
    "value": "1543134949",
    "id": 10
},
{
    "domain": ".huazhu.com",
    "hostOnly": 'false',
    "httpOnly": 'false',
    "name": "MemberLevelID",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'true',
    "storeId": "0",
    "value": "A",
    "id": 11
},
{
    "domain": ".huazhu.com",
    "expirationDate": 1543142267.956681,
    "hostOnly": 'false',
    "httpOnly": 'true',
    "name": "p_t",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'false',
    "storeId": "0",
    "value": "55Y2JX2KgQ7iXaNC0Cp1No3q0FfTigWH/L3Mc3P40PycY8Td5dKw8g==",
    "id": 12
},
{
    "domain": ".huazhu.com",
    "expirationDate": 1543142267.956769,
    "hostOnly": 'false',
    "httpOnly": 'false',
    "name": "unick",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'false',
    "storeId": "0",
    "value": "%e6%9d%a8%e5%9f%ba%e5%bb%ba",
    "id": 13
},
{
    "domain": "www.huazhu.com",
    "hostOnly": 'true',
    "httpOnly": 'true',
    "name": "__RequestVerificationToken",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'true',
    "storeId": "0",
    "value": "MzTPPdoq0p7teDENvdnhDvoBSNiAEMED2wbFJGPgZrs8lj11-ZGQFuGiSVQbeQPrdPnn5EfaGOIDHQ-tusp6G6YgSImB1j3YYgQdtiy_WS7-NOqf3MpfYHf0xCuj5-Yjs4vBXBfD3LQIyGDPmn3bMQ2",
    "id": 14
},
{
    "domain": "www.huazhu.com",
    "expirationDate": 1543136267.956726,
    "hostOnly": 'true',
    "httpOnly": 'true',
    "name": ".ASPXAUTH",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'false',
    "storeId": "0",
    "value": "9444EA0017C82F713497459E0F7307E88544AFB89772D8ACB4EA225CCEC705925195856718F1C5C495C81AD09D0BEBFB17A12BE2A7B6620BBB76DE39D096F4DD7807886AC74492B24BCB15A91DFD9CAF15005248E82A328F7CD193288BB27B98691FDF62B94D9D2A854CEC26246BF736AD2737388DEBFC115AF3D653E08C6A4ACDF3C28C07F469D69477129E81878DED8A9C0ED2524C92E9C3F28E10E46F9212786F7AD192B7814D75C18221828C59E29D68D6E17DB061BA27715C252702EC4F350849079E4E7C6BEBB6CFA29B5C9FD66D57FDEB95DC71B4680520D720CCD05D5C1B85EDC846D25A4ECD76B872E3041AF2BE9FE80567762093B34549AF518BF309FE9990C229B54A566AC0819B1D374C5250A4E7837636E3BBBEBAC0D10A8B8E05613A45BB5834729D830AF8DB379C14B4DEDDD4422958E02888C322EAB89B5B2F7CF01EA950BE05D2C4069F68F995C9B51F0C5AD09D190E193F5D4EAE887D31E14E4D4BC61597B54AEC73604F06A590AAA3626DF38A38AEA1E76EBF7ABC784C50D74C11F71C2205AC441F5E25FA2624",
    "id": 15
},
{
    "domain": "www.huazhu.com",
    "expirationDate": 1574671443,
    "hostOnly": 'true',
    "httpOnly": 'false',
    "name": "ADHOC_MEMBERSHIP_CLIENT_ID1.0",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'false',
    "storeId": "0",
    "value": "3f72aeea-b3d8-efc7-75ea-5d62c92749c2",
    "id": 16
},
{
    "domain": "www.huazhu.com",
    "hostOnly": 'true',
    "httpOnly": 'true',
    "name": "ASP.NET_SessionId",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'true',
    "storeId": "0",
    "value": "b5lsminme13xqx2xi2zyuq14",
    "id": 17
},
{
    "domain": "www.huazhu.com",
    "expirationDate": 1858494945.673823,
    "hostOnly": 'true',
    "httpOnly": 'false',
    "name": "YIF+pxrGp0isUkYUsAWxn3rQH6pBrNY@",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'false',
    "session": 'false',
    "storeId": "0",
    "value": "v19RovgwSDkJW",
    "id": 18
}
]
driver = webdriver.Chrome()

driver.get("http://www.huazhu.com/")

print("done")

for c in cookie:
    driver.add_cookie(c)


driver.refresh()

time.sleep(4)

element_get = driver.find_element_by_xpath("//*[@id='loginAfter']/div/a[2]")

element_get.click()

time.sleep(4)


time.sleep(4)
