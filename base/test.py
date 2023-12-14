import urllib.request
import requests
import re
if __name__ == '__main__':
    ssxml = '<?xml version="1.0" encoding="utf-8" standalone="no"?><OTA_HotelResRQ EchoToken="56f9821b-7672-47a4-8262-b66b355e29e9" Password="qinghotel" PrimaryLangID="en-us" TimeStamp="2022-03-01 16:00:21" UserName="qinghotel" Version="1.000"><POS><Source><RequestorID ID="elong" Type="2"/></Source></POS><HotelReservations><HotelReservation><UniqueID ID="000701412" Type="14"/><RoomStays><RoomStay><RoomTypes><RoomType RoomTypeCode="50058544"/></RoomTypes><RatePlans><RatePlan RatePlanCode="0000000000846000"/></RatePlans><RoomRates><RoomRate RatePlanCode="0000000000846000" RoomTypeCode="50058544"><Rates><Rate><Base EffectDate="2022-03-29" SaleAmountOriginal="123" CurrencyCode="RMB"/><Total SaleAmountOriginal="123.00" CurrencyCode="RMB"/></Rate></Rates></RoomRate></RoomRates><GuestCounts><GuestCount AgeQualifyingCode="10" Count="1"/></GuestCounts><BasicPropertyInfo HotelCode="10030921"/></RoomStay></RoomStays><ResGuests><ResGuest><Profiles><ProfileInfo><Profile><Customer><PersonName><RoomGuest><GivenName/><MiddleName>TONG CHENG</MiddleName><Surname>\xe5\x90\x8c\xe7\xa8\x8b</Surname></RoomGuest></PersonName></Customer></Profile></ProfileInfo></Profiles></ResGuest></ResGuests><ResGlobalInfo><RoomNum>1</RoomNum><TimeSpan End="2022-03-30" Start="2022-03-29"/><EarliestCheckInTime>"2022-03-29 11:33:55"</EarliestCheckInTime><LatestCheckInTime>"2022-03-29 13:33:55"</LatestCheckInTime><Remark>*\xe5\xa6\x82\xe5\xae\xa2\xe4\xba\xba\xe7\xb4\xa2\xe5\x8f\x96\xe5\x8f\x91\xe7\xa5\xa8\xef\xbc\x8c\xe8\xaf\xb7\xe8\xb4\xb5\xe9\x85\x92\xe5\xba\x97\xe5\xbc\x80\xe5\x85\xb7\xef\xbc\x8c\xe9\x87\x91\xe9\xa2\x9d115.00\xe5\x85\x83*\xef\xbc\x9b\xe9\xa2\x84\xe4\xbb\x98\xe8\xae\xa2\xe5\x8d\x95 \xef\xbc\x9b\xe4\xbb\xb7\xe6\xa0\xbc\xef\xbc\x9a3.1/115;;ResID:491799404</Remark><Guarantee GuaranteeType="FP"/></ResGlobalInfo></HotelReservation></HotelReservations><RatePlanPolicy><CanBeCanceled>false</CanBeCanceled><CancelBeforeDays>0</CancelBeforeDays><CancelBeforeTime>0</CancelBeforeTime><CashScaleType>0</CashScaleType></RatePlanPolicy><ElongInventoryType>OnRequest</ElongInventoryType></OTA_HotelResRQ>'
    ssxml = ssxml.encode("utf-8")
    body_value = {"Message":ssxml}
    heead = {"Content-Type":"application/x-www-form-urlencoded"}
    url = 'https://t-channel.qinghotel.com/channel/tongCheng/order'
    html = requests.post(url,data=body_value,headers=heead)
    print(html.text) #cancel

    # ssxml = '<?xml version="1.0" encoding="utf-8" standalone="no"?><OTA_HotelResRQ EchoToken="56f9821b-7672-47a4-8262-b66b355e29e9" Password="qinghotel" PrimaryLangID="en-us" TimeStamp="2022-03-01 16:00:21" UserName="qinghotel" Version="1.000"><POS><Source><RequestorID ID="elong" Type="2"/></Source></POS><HotelReservations><HotelReservation><UniqueID ID="164862000713" Type="14"/><RoomStays><RoomStay><RoomTypes><RoomType RoomTypeCode="50058544"/></RoomTypes><RatePlans><RatePlan RatePlanCode="0000000000846000"/></RatePlans><RoomRates><RoomRate RatePlanCode="0000000000846000" RoomTypeCode="50058544"><Rates><Rate><Base EffectDate="2022-03-30" SaleAmountOriginal="123" CurrencyCode="RMB"/><Total SaleAmountOriginal="123.00" CurrencyCode="RMB"/></Rate></Rates></RoomRate></RoomRates><GuestCounts><GuestCount AgeQualifyingCode="10" Count="1"/></GuestCounts><BasicPropertyInfo HotelCode="10030921"/></RoomStay></RoomStays><ResGuests><ResGuest><Profiles><ProfileInfo><Profile><Customer><PersonName><RoomGuest><GivenName/><MiddleName>TONG CHENG</MiddleName><Surname>同程</Surname></RoomGuest></PersonName></Customer></Profile></ProfileInfo></Profiles></ResGuest></ResGuests><ResGlobalInfo><RoomNum>1</RoomNum><TimeSpan End="2022-03-31" Start="2022-03-30"/><EarliestCheckInTime>2022-03-30 15:24:54</EarliestCheckInTime><LatestCheckInTime>2022-03-31 15:24:54</LatestCheckInTime><Remark>*如客人索取发票，请贵酒店开具，金额115.00元*；预付订单 ；价格：3.1/115;;ResID:491799404</Remark><Guarantee GuaranteeType="FP"/></ResGlobalInfo></HotelReservation></HotelReservations><RatePlanPolicy><CanBeCanceled>false</CanBeCanceled><CancelBeforeDays>0</CancelBeforeDays><CancelBeforeTime>0</CancelBeforeTime><CashScaleType>0</CashScaleType></RatePlanPolicy><ElongInventoryType>OnRequest</ElongInventoryType></OTA_HotelResRQ>'
    # ssxml = ssxml.encode("utf-8")
    # body_value = {"Message":ssxml}
    # heead = {"Content-Type":"application/x-www-form-urlencoded"}
    # url = 'https://t-channel.qinghotel.com/channel/tongCheng/order'
    # html = requests.post(url,data=body_value,headers=heead)
    # print(html.text)
    # print('1')
    # print(html.text[346:365])
    # print(html.text[254:266])
    # print(re.findall(r'ID="(.*)">',html.text))
    # if '(.*)' in 'ID="(.*)">':
    #     try:
    #         relyValue = re.findall('"10" ID="(.*)">', html.text)
    #         print("22")
    #         print("".join(relyValue))
    #         print("22")
    #     except:
    #         relyValue = ''
    #     print('1')
    # else:
    #     print('2')