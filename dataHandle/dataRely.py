import ast
import re
from dataHandle.getData import GetData
import json
from jsonpath_rw import jsonpath, parse
from common.operateDB import OperateMysql
from common.readConfigInfo import ReadConfigInfo
from dataHandle.especialData import EspecialData
from common.log import Log

logger = Log().get_logger()


class DataRely(object):
    def __init__(self, filename=None):
        self.ed = EspecialData()
        self.data = GetData(filename)
        self.readCon = ReadConfigInfo()
        # self.db = OperateMysql()

    # 初始化依赖的数据（非接口获取的值）
    def get_init_rely_data(self, start=0, end=1):
        hotelCode = self.readCon.get_config_value('hotelInfo', 'hotelCode')
        vipUser = self.readCon.get_config_value('hotelInfo', 'vipUser')
        vipUserTel = self.readCon.get_config_value('hotelInfo', 'vipUserTel')
        vipCompany = self.readCon.get_config_value('hotelInfo', 'vipCompany')
        vipComTel = self.readCon.get_config_value('hotelInfo', 'vipComTel')
        hotelName = self.readCon.get_config_value('hotelInfo', 'hotelName')
        openid = self.readCon.get_config_value('hotelInfo', 'openid')
        startDate = self.ed.get_target_date(start)
        endDate = self.ed.get_target_date(end)

        QNcheckInDate = self.ed.get_UTC_time(start)
        QNcheckOutDate = self.ed.get_UTC_time(end)
        QNorderDate = self.ed.get_order_time()


        newStartDate = self.ed.get_target_date(start - 1)
        newEndDate = self.ed.get_target_date(end + 1)
        twoBeforeDate = self.ed.get_target_date(start - 2)
        twoBeforeTime = self.ed.get_target_time(start - 2)
        startTime = self.ed.get_target_time(start)
        xcxhour = self.readCon.get_config_value('xiaochengxuOrder', 'xcxhour')
        xcxhourendTime = self.ed.get_target_datetime(int(xcxhour))
        endTime = self.ed.get_target_time(end)
        arriveTime = self.ed.get_time_stamp13(startTime)
        leaveTime = self.ed.get_time_stamp13(endTime)
        newStartTime = self.ed.get_target_time(start - 1)
        newEndTime = self.ed.get_target_time(end + 1)
        newArriveTime = self.ed.get_time_stamp13(newStartTime)
        newLeaveTime = self.ed.get_time_stamp13(newEndTime)

        zxordersn = self.readCon.get_config_value('xiaochengxuOrder', 'zxordersn')

        xcxhotelName = self.readCon.get_config_value('xiaochengxuOrder', 'xcxhotelName')
        xcxvipUserTel = self.readCon.get_config_value('xiaochengxuOrder', 'xcxvipUserTel')
        xcxopenId = self.readCon.get_config_value('xiaochengxuOrder', 'xcxopenId')
        xcxroomTypeCode = self.readCon.get_config_value('xiaochengxuOrder', 'xcxroomTypeCode')
        xcxroomTypeName = self.readCon.get_config_value('xiaochengxuOrder', 'xcxroomTypeName')
        xcxgoodsCode = self.readCon.get_config_value('xiaochengxuOrder', 'xcxgoodsCode')
        xcxhourGoodsCode = self.readCon.get_config_value('xiaochengxuOrder', 'xcxhourGoodsCode')
        xcxroomNum = self.readCon.get_config_value('xiaochengxuOrder', 'xcxroomNum')
        xcxsalePrice = self.readCon.get_config_value('xiaochengxuOrder', 'xcxsalePrice')
        xcxvip1Price = self.readCon.get_config_value('xiaochengxuOrder', 'xcxvip1Price')
        xcxvip2Price = self.readCon.get_config_value('xiaochengxuOrder', 'xcxvip2Price')
        xcxvip3Price = self.readCon.get_config_value('xiaochengxuOrder', 'xcxvip3Price')
        xcxvip3Price2 = self.readCon.get_config_value('xiaochengxuOrder', 'xcxvip3Price2')
        xcxvip4Price = self.readCon.get_config_value('xiaochengxuOrder', 'xcxvip4Price')
        xcxpromotionDiscount = self.readCon.get_config_value('xiaochengxuOrder', 'xcxpromotionDiscount')

        xcxvip1PriceD = self.readCon.get_config_value('xiaochengxuOrder', 'xcxvip1PriceD')
        xcxvip2PriceD = self.readCon.get_config_value('xiaochengxuOrder', 'xcxvip2PriceD')
        xcxvip3PriceD = self.readCon.get_config_value('xiaochengxuOrder', 'xcxvip3PriceD')
        xcxvip3Price2D = self.readCon.get_config_value('xiaochengxuOrder', 'xcxvip3Price2D')
        xcxvip4PriceD = self.readCon.get_config_value('xiaochengxuOrder', 'xcxvip4PriceD')

        xcxvip1PriceZ = self.readCon.get_config_value('xiaochengxuOrder', 'xcxvip1PriceZ')
        xcxvip2PriceZ = self.readCon.get_config_value('xiaochengxuOrder', 'xcxvip2PriceZ')
        xcxvip3PriceZ = self.readCon.get_config_value('xiaochengxuOrder', 'xcxvip3PriceZ')
        xcxvip3Price2Z = self.readCon.get_config_value('xiaochengxuOrder', 'xcxvip3Price2Z')
        xcxvip4PriceZ = self.readCon.get_config_value('xiaochengxuOrder', 'xcxvip4PriceZ')

        xcxpromotionId = self.readCon.get_config_value('xiaochengxuOrder', 'xcxpromotionId')
        xcxnoproGoodsCode = self.readCon.get_config_value('xiaochengxuOrder', 'xcxnoproGoodsCode')
        xcxnoproroomTypeCode = self.readCon.get_config_value('xiaochengxuOrder', 'xcxnoproroomTypeCode')
        xcxnoproroomTypeName = self.readCon.get_config_value('xiaochengxuOrder', 'xcxnoproroomTypeName')
        xcxoGoodsCode93 = self.readCon.get_config_value('xiaochengxuOrder', 'xcxoGoodsCode93')
        xcxpromotionId93 = self.readCon.get_config_value('xiaochengxuOrder', 'xcxpromotionId93')

        mtOrderId = self.readCon.get_config_value('meituanOrder', 'mtOrderId')
        poiId = self.readCon.get_config_value('meituanOrder', 'poiId')
        salePrice = self.readCon.get_config_value('meituanOrder', 'salePrice')
        vip1Price = self.readCon.get_config_value('meituanOrder', 'vip1Price')
        vip2Price = self.readCon.get_config_value('meituanOrder', 'vip2Price')
        vip3Price = self.readCon.get_config_value('meituanOrder', 'vip3Price')
        vip3Price2 = self.readCon.get_config_value('meituanOrder', 'vip3Price2')
        vip4Price = self.readCon.get_config_value('meituanOrder', 'vip4Price')
        roomType = self.readCon.get_config_value('meituanOrder', 'roomType')
        roomTypeQx = self.readCon.get_config_value('meituanOrder', 'roomTypeQx')
        activeId = self.readCon.get_config_value('meituanOrder', 'activeId')
        activePrice = self.readCon.get_config_value('meituanOrder', 'activePrice')
        goodsId = self.readCon.get_config_value('meituanOrder', 'goodsId')
        activeGroupId95 = self.readCon.get_config_value('meituanOrder', 'activeGroupId95')
        activeGroupIdlj10 = self.readCon.get_config_value('meituanOrder', 'activeGroupIdlj10')
        activeCode0 = self.readCon.get_config_value('meituanOrder', 'activeCode0')
        activeCode1 = self.readCon.get_config_value('meituanOrder', 'activeCode1')
        activeCode2 = self.readCon.get_config_value('meituanOrder', 'activeCode2')
        activeCode3 = self.readCon.get_config_value('meituanOrder', 'activeCode3')
        activeCode4 = self.readCon.get_config_value('meituanOrder', 'activeCode4')
        activeCode5 = self.readCon.get_config_value('meituanOrder', 'activeCode5')
        activeCode6 = self.readCon.get_config_value('meituanOrder', 'activeCode6')
        activeCode7 = self.readCon.get_config_value('meituanOrder', 'activeCode7')
        activeCode8 = self.readCon.get_config_value('meituanOrder', 'activeCode8')
        activeCode9 = self.readCon.get_config_value('meituanOrder', 'activeCode9')
        activeCode10 = self.readCon.get_config_value('meituanOrder', 'activeCode10')
        activeCode11 = self.readCon.get_config_value('meituanOrder', 'activeCode11')
        activeCode12 = self.readCon.get_config_value('meituanOrder', 'activeCode12')
        activeCode13 = self.readCon.get_config_value('meituanOrder', 'activeCode13')
        roomTypeCode = self.readCon.get_config_value('hotelInfo', 'roomTypeCode')
        roomId = self.readCon.get_config_value('hotelInfo', 'roomId')
        roomTypeName = self.readCon.get_config_value('hotelInfo', 'roomTypeName')
        goodsCode = self.readCon.get_config_value('hotelInfo', 'goodsCode')
        roomNum = self.readCon.get_config_value('hotelInfo', 'roomNum')
        price = self.readCon.get_config_value('hotelInfo', 'price')
        discount = self.readCon.get_config_value('hotelInfo', 'discount')
        newPrice = self.readCon.get_config_value('hotelInfo', 'newPrice')
        vipNo = self.readCon.get_config_value('hotelInfo', 'vipNo')
        vipComId = self.readCon.get_config_value('hotelInfo', 'vipComId')
        hourGoodsCode = self.readCon.get_config_value('hotelInfo', 'hourGoodsCode')
        appletGoodsCode = self.readCon.get_config_value('meituanOrder', 'appletGoodsCode')

        batterysn1 = self.readCon.get_config_value('newBattery', 'batterysn1')
        batterysn2 = self.readCon.get_config_value('newBattery', 'batterysn2')
        battery_id = self.readCon.get_config_value('newBattery', 'battery_id')
        data = self.readCon.get_config_value('login', 'data')
        user_id = self.readCon.get_config_value('newBattery', 'user_id')

        opL1Price = self.readCon.get_config_value('opOrder', 'opL1Price')
        opL2Price = self.readCon.get_config_value('opOrder', 'opL2Price')
        opL3Price = self.readCon.get_config_value('opOrder', 'opL3Price')
        opL4Price = self.readCon.get_config_value('opOrder', 'opL4Price')
        oproomType = self.readCon.get_config_value('opOrder', 'oproomType')
        opactiveId = self.readCon.get_config_value('opOrder', 'opactiveId')
        oporiginPrice = self.readCon.get_config_value('opOrder', 'oporiginPrice')
        opweChatPrice = self.readCon.get_config_value('opOrder', 'opweChatPrice')
        opgoodsIdz95 = self.readCon.get_config_value('opOrder', 'opgoodsIdz95')
        opgoodsIdz30 = self.readCon.get_config_value('opOrder', 'opgoodsIdz30')
        opgoodsIdz70 = self.readCon.get_config_value('opOrder', 'opgoodsIdz70')
        opgoodsIdlj5 = self.readCon.get_config_value('opOrder', 'opgoodsIdlj5')
        opgoodsIdlj439 = self.readCon.get_config_value('opOrder', 'opgoodsIdlj439')
        opgoodsIdlj50 = self.readCon.get_config_value('opOrder', 'opgoodsIdlj50')
        ophourGoodsCode = self.readCon.get_config_value('opOrder', 'ophourGoodsCode')
        opappIdBMy0z051 = self.readCon.get_config_value('opOrder', 'opappIdBMy0z051')
        opappIdBMy1z0922 = self.readCon.get_config_value('opOrder', 'opappIdBMy1z0922')
        opappIdBMy6z0663 = self.readCon.get_config_value('opOrder', 'opappIdBMy6z0663')
        opappIdBMy99z14 = self.readCon.get_config_value('opOrder', 'opappIdBMy99z14')
        opappIdBDy0z051 = self.readCon.get_config_value('opOrder', 'opappIdBDy0z051')
        opappIdBDy1z0922 = self.readCon.get_config_value('opOrder', 'opappIdBDy1z0922')
        opappIdBDy6z0663 = self.readCon.get_config_value('opOrder', 'opappIdBDy6z0663')
        opappIdBDy99z14 = self.readCon.get_config_value('opOrder', 'opappIdBDy99z14')
        opappIdCMy15z08514 = self.readCon.get_config_value('opOrder', 'opappIdCMy15z08514')
        opappIdCMy0z0515 = self.readCon.get_config_value('opOrder', 'opappIdCMy0z0515')
        opappIdCMy11z07516 = self.readCon.get_config_value('opOrder', 'opappIdCMy11z07516')
        opappIdCMy99z117 = self.readCon.get_config_value('opOrder', 'opappIdCMy99z117')
        opappIdCMy0z0518 = self.readCon.get_config_value('opOrder', 'opappIdCMy0z0518')
        opappIdCMy11z119 = self.readCon.get_config_value('opOrder', 'opappIdCMy11z119')
        opappIdCMy99z07520 = self.readCon.get_config_value('opOrder', 'opappIdCMy99z07520')
        opappIdCMy0z0521 = self.readCon.get_config_value('opOrder', 'opappIdCMy0z0521')
        opappIdCMy11z07522 = self.readCon.get_config_value('opOrder', 'opappIdCMy11z07522')
        opappIdCMy99z123 = self.readCon.get_config_value('opOrder', 'opappIdCMy99z123')
        opappIdCDy15z08514 = self.readCon.get_config_value('opOrder', 'opappIdCDy15z08514')
        opappIdCDy0z0515 = self.readCon.get_config_value('opOrder', 'opappIdCDy0z0515')
        opappIdCDy11z07516 = self.readCon.get_config_value('opOrder', 'opappIdCDy11z07516')
        opappIdCDy99z117 = self.readCon.get_config_value('opOrder', 'opappIdCDy99z117')
        opappIdCDy0z0518 = self.readCon.get_config_value('opOrder', 'opappIdCDy0z0518')
        opappIdCDy11z119 = self.readCon.get_config_value('opOrder', 'opappIdCDy11z119')
        opappIdCDy99z07520 = self.readCon.get_config_value('opOrder', 'opappIdCDy99z07520')
        opappIdCDy0z0521 = self.readCon.get_config_value('opOrder', 'opappIdCDy0z0521')
        opappIdCDy11z07522 = self.readCon.get_config_value('opOrder', 'opappIdCDy11z07522')
        opappIdCDy99z123 = self.readCon.get_config_value('opOrder', 'opappIdCDy99z123')
        opqingMemberLevel1 = self.readCon.get_config_value('opOrder', 'opqingMemberLevel1')
        opqingMemberNo1 = self.readCon.get_config_value('opOrder', 'opqingMemberNo1')
        opqingMemberLevel2 = self.readCon.get_config_value('opOrder', 'opqingMemberLevel2')
        opqingMemberNo2 = self.readCon.get_config_value('opOrder', 'opqingMemberNo2')
        opqingMemberLevel3 = self.readCon.get_config_value('opOrder', 'opqingMemberLevel3')
        opqingMemberNo3 = self.readCon.get_config_value('opOrder', 'opqingMemberNo3')
        opqingMemberLevel4 = self.readCon.get_config_value('opOrder', 'opqingMemberLevel4')
        opqingMemberNo4 = self.readCon.get_config_value('opOrder', 'opqingMemberNo4')

        XCIp = self.readCon.get_config_value('XCOrder', 'XCIp')
        XCOrderId = self.readCon.get_config_value('XCOrder', 'XCOrderId')
        XChotelCode = self.readCon.get_config_value('XCOrder', 'XChotelCode')
        XCsalePrice = self.readCon.get_config_value('XCOrder', 'XCsalePrice')
        XCroomType = self.readCon.get_config_value('XCOrder', 'XCroomType')
        XCratePlanCode = self.readCon.get_config_value('XCOrder', 'XCratePlanCode')

        QNorderNum = self.readCon.get_config_value('QNOrder', 'QNorderNum')
        QNhotelId = self.readCon.get_config_value('QNOrder', 'QNhotelId')
        QNhotelName = self.readCon.get_config_value('QNOrder', 'QNhotelName')
        QNroomName = self.readCon.get_config_value('QNOrder', 'QNroomName')
        QNroomId = self.readCon.get_config_value('QNOrder', 'QNroomId')
        QNroomNum = self.readCon.get_config_value('QNOrder', 'QNroomNum')
        QNsalePrice = self.readCon.get_config_value('QNOrder', 'QNsalePrice')
        QNbasePrice = self.readCon.get_config_value('QNOrder', 'QNbasePrice')
        QNroomType = self.readCon.get_config_value('QNOrder', 'QNroomType')

        TCOrderId = self.readCon.get_config_value('TCOrder', 'TCOrderId')
        TCHotelCode = self.readCon.get_config_value('TCOrder', 'TCHotelCode')
        TCRoomTypeCode = self.readCon.get_config_value('TCOrder', 'TCRoomTypeCode')
        TCRatePlanCode = self.readCon.get_config_value('TCOrder', 'TCRatePlanCode')
        TCSaleAmountOriginal = self.readCon.get_config_value('TCOrder', 'TCSaleAmountOriginal')
        TCSaleAmountOriginal2 = self.readCon.get_config_value('TCOrder', 'TCSaleAmountOriginal2')
        TCUniqueID14 = self.readCon.get_config_value('TCOrder', 'TCUniqueID14')
        TCUniqueID10 = self.readCon.get_config_value('TCOrder', 'TCUniqueID10')


        relyData = {
            'hotelCode': hotelCode,
            'startDate': startDate,
            'endDate': endDate,

            'QNorderDate': QNorderDate,
            'QNcheckInDate': QNcheckInDate,
            'QNcheckOutDate': QNcheckOutDate,

            'arriveTime': arriveTime,
            'leaveTime': leaveTime,
            'startTime': startTime,
            'xcxhour': xcxhour,
            'xcxhourendTime': xcxhourendTime,
            'endTime': endTime,
            'vipUser': vipUser,
            'vipUserTel': vipUserTel,
            'vipCompany': vipCompany,
            'vipComTel': vipComTel,
            'hotelName': hotelName,
            'openid': openid,

            'zxordersn':  zxordersn,

            'xcxhotelName': xcxhotelName,
            'xcxvipUserTel': xcxvipUserTel,
            'xcxopenId': xcxopenId,
            'xcxroomTypeCode': xcxroomTypeCode,
            'xcxroomTypeName': xcxroomTypeName,
            'xcxgoodsCode': xcxgoodsCode,
            'xcxhourGoodsCode': xcxhourGoodsCode,
            'xcxroomNum':  xcxroomNum,
            'xcxsalePrice':  xcxsalePrice,
            'xcxvip1Price': xcxvip1Price,
            'xcxvip2Price': xcxvip2Price,
            'xcxvip3Price': xcxvip3Price,
            'xcxvip3Price2': xcxvip3Price2,
            'xcxvip4Price': xcxvip4Price,
            'xcxpromotionDiscount': xcxpromotionDiscount,
            'xcxvip1PriceD': xcxvip1PriceD,
            'xcxvip2PriceD': xcxvip2PriceD,
            'xcxvip3PriceD': xcxvip3PriceD,
            'xcxvip3Price2D': xcxvip3Price2D,
            'xcxvip4PriceD': xcxvip4PriceD,

            'xcxvip1PriceZ': xcxvip1PriceZ,
            'xcxvip2PriceZ': xcxvip2PriceZ,
            'xcxvip3PriceZ': xcxvip3PriceZ,
            'xcxvip3Price2Z': xcxvip3Price2Z,
            'xcxvip4PriceZ': xcxvip4PriceZ,

            'xcxpromotionId': xcxpromotionId,
            'xcxnoproGoodsCode': xcxnoproGoodsCode,
            'xcxnoproroomTypeCode': xcxnoproroomTypeCode,
            'xcxnoproroomTypeName': xcxnoproroomTypeName,
            'xcxoGoodsCode93': xcxoGoodsCode93,
            'xcxpromotionId93': xcxpromotionId93,

            'mtOrderId': mtOrderId,
            'poiId': poiId,
            'salePrice': salePrice,
            'vip1Price': vip1Price,
            'vip2Price': vip2Price,
            'vip3Price': vip3Price,
            'vip3Price2': vip3Price2,
            'vip4Price': vip4Price,
            'roomType': roomType,
            'roomTypeQx': roomTypeQx,
            'activeId': activeId,
            'activePrice': activePrice,
            'goodsId': goodsId,
            'activeGroupId95': activeGroupId95,
            'activeGroupIdlj10': activeGroupIdlj10,
            'activeCode0': activeCode0,
            'activeCode1': activeCode1,
            'activeCode2': activeCode2,
            'activeCode3': activeCode3,
            'activeCode4': activeCode4,
            'activeCode5': activeCode5,
            'activeCode6': activeCode6,
            'activeCode7': activeCode7,
            'activeCode8': activeCode8,
            'activeCode9': activeCode9,
            'activeCode10': activeCode10,
            'activeCode11': activeCode11,
            'activeCode12': activeCode12,
            'activeCode13': activeCode13,
            'roomTypeCode': roomTypeCode,
            'roomId': roomId,
            'roomTypeName': roomTypeName,
            'goodsCode': goodsCode,
            'roomNum': roomNum,
            'price': price,
            'discount': discount,
            'newPrice': newPrice,
            'vipNo': vipNo,
            'vipComId': vipComId,
            'hourGoodsCode': hourGoodsCode,
            'newStartDate': newStartDate,
            'newEndDate': newEndDate,
            'newEndTime': newEndTime,
            'newArriveTime': newArriveTime,
            'newLeaveTime': newLeaveTime,
            'appletGoodsCode': appletGoodsCode,

            'batterysn1': batterysn1,
            'batterysn2': batterysn2,

            'battery_id': battery_id,
            'twoBeforeDate': twoBeforeDate,
            'twoBeforeTime': twoBeforeTime,
            'data': data,
            'user_id': user_id,

            'opL1Price': opL1Price,
            'opL2Price': opL2Price,
            'opL3Price': opL3Price,
            'opL4Price': opL4Price,
            'oproomType': oproomType,
            'opactiveId': opactiveId,
            'oporiginPrice': oporiginPrice,
            'opweChatPrice': opweChatPrice,
            'opgoodsIdz95': opgoodsIdz95,
            'opgoodsIdz30': opgoodsIdz30,
            'opgoodsIdz70': opgoodsIdz70,
            'opgoodsIdlj5': opgoodsIdlj5,
            'opgoodsIdlj439': opgoodsIdlj439,
            'opgoodsIdlj50': opgoodsIdlj50,
            'ophourGoodsCode': ophourGoodsCode,
            'opappIdBMy0z051': opappIdBMy0z051,
            'opappIdBMy1z0922': opappIdBMy1z0922,
            'opappIdBMy6z0663': opappIdBMy6z0663,
            'opappIdBMy99z14': opappIdBMy99z14,
            'opappIdBDy0z051': opappIdBDy0z051,
            'opappIdBDy1z0922': opappIdBDy1z0922,
            'opappIdBDy6z0663': opappIdBDy6z0663,
            'opappIdBDy99z14': opappIdBDy99z14,
            'opappIdCMy15z08514': opappIdCMy15z08514,
            'opappIdCMy0z0515': opappIdCMy0z0515,
            'opappIdCMy11z07516': opappIdCMy11z07516,
            'opappIdCMy99z117': opappIdCMy99z117,
            'opappIdCMy0z0518': opappIdCMy0z0518,
            'opappIdCMy11z119': opappIdCMy11z119,
            'opappIdCMy99z07520': opappIdCMy99z07520,
            'opappIdCMy0z0521': opappIdCMy0z0521,
            'opappIdCMy11z07522': opappIdCMy11z07522,
            'opappIdCMy99z123': opappIdCMy99z123,
            'opappIdCDy15z08514': opappIdCDy15z08514,
            'opappIdCDy0z0515': opappIdCDy0z0515,
            'opappIdCDy11z07516': opappIdCDy11z07516,
            'opappIdCDy99z117': opappIdCDy99z117,
            'opappIdCDy0z0518': opappIdCDy0z0518,
            'opappIdCDy11z119': opappIdCDy11z119,
            'opappIdCDy99z07520': opappIdCDy99z07520,
            'opappIdCDy0z0521': opappIdCDy0z0521,
            'opappIdCDy11z07522': opappIdCDy11z07522,
            'opappIdCDy99z123': opappIdCDy99z123,
            'opqingMemberLevel1': opqingMemberLevel1,
            'opqingMemberNo1': opqingMemberNo1,
            'opqingMemberLevel2': opqingMemberLevel2,
            'opqingMemberNo2': opqingMemberNo2,
            'opqingMemberLevel3': opqingMemberLevel3,
            'opqingMemberNo3': opqingMemberNo3,
            'opqingMemberLevel4': opqingMemberLevel4,
            'opqingMemberNo4': opqingMemberNo4,

            'XCIp': XCIp,
            'XCOrderId': XCOrderId,
            'XChotelCode': XChotelCode,
            'XCsalePrice': XCsalePrice,
            'XCratePlanCode': XCratePlanCode,
            'XCroomType': XCroomType,

            'QNorderNum': QNorderNum,
            'QNhotelId': QNhotelId,
            'QNhotelName': QNhotelName,
            'QNroomName': QNroomName,
            'QNroomId': QNroomId,
            'QNroomNum': QNroomNum,
            'QNsalePrice': QNsalePrice,
            'QNbasePrice': QNbasePrice,
            'QNroomType': QNroomType,

            'TCOrderId': TCOrderId,
            'TCHotelCode': TCHotelCode,
            'TCRoomTypeCode': TCRoomTypeCode,
            'TCRatePlanCode': TCRatePlanCode,
            'TCSaleAmountOriginal': TCSaleAmountOriginal,
            'TCSaleAmountOriginal2': TCSaleAmountOriginal2,
            'TCUniqueID14': TCUniqueID14,
            'TCUniqueID10': TCUniqueID10
        }
        return relyData

    # 根据dataRely和接口返回数据获取依赖的值
    def get_rely_response_value(self, dataRely, response):
        if dataRely == 'all':
            return response
        if '(.*)' in dataRely:
            try:
                relyValue = "".join(re.findall(dataRely, response))
            except:
                relyValue = ''
            return relyValue
        if '(.+?)' in dataRely:
            try:
                relyValue = re.findall(dataRely, response)[0]
            except:
                relyValue = ''
            return relyValue
        if not isinstance(response, dict):
            responseData = json.loads(response)
        else:
            responseData = response
        jsonExe = parse(dataRely)
        male = jsonExe.find(responseData)
        try:
            relyValue = [math.value for math in male][0]
            logger.info(f'通过依赖的数据路径:{dataRely},成功获取到依赖的值:{relyValue}')
        except Exception as msg:
            relyValue = ''
            logger.error(f'没有获取到依赖的字段{dataRely}对应的值，给默认值空字符串,原因:{msg}')
        return relyValue

    # 将依赖的值写入到全局变量中
    def save_rely_value(self, case, response, relyData):
        dataRely = self.data.get_data_rely(case)
        fieldRely = self.data.get_field_rely(case)
        if dataRely:
            for i in range(len(dataRely)):
                relyValue = self.get_rely_response_value(dataRely[i],response)
                relyData[fieldRely[i]] = relyValue
        logger.info(f'成功将所有依赖的数据写入全局变量testData中:{relyData}')

    # # 从全局变量中获取本接口依赖的字段
    # def get_rely_value(self, case, relyData):
    #     paramsRely = self.data.get_params_rely(case)
    #     relyValue = relyData[paramsRely]
    #     logger.info(f'成功全局变量中获取本接口依赖的字段{paramsRely}的值为:{relyData}')
    #     return relyValue

    # 从请求数据中，替换掉依赖的参数值
    def replace_params(self, paramsRely, relyValue, requestStr):
        """
        替换请求参数中依赖的值
        @param paramsRely: 需替换的变量名称
        @param relyValue: 需要替换的依赖变量对应的值（有些值从接口数据获取后需要特殊处理）
        @param requestStr: 获取到的请求参数（包括参数化的变量）
        """
        # requestStr = json.dumps(requestData)
        if '$' + paramsRely + '$' in requestStr:
            requestStr = requestStr.replace('$' + paramsRely + '$', relyValue)
            logger.info(f'成功从请求数据中，将依赖的参数值${paramsRely}$替换为具体值:{relyValue}')
        # requestDict = json.loads(requestStr)
        return requestStr

    # 替换所有的参数
    def replace_all_params(self, paramsList, relyData, requestData):
        requestStr = requestData
        if paramsList:
            for params in paramsList:
                try:
                    if params == 'randomNum' or params == 'mtOrderId':
                        relyValue = self.ed.get_random_num()
                    else:
                        relyValue = relyData[params]
                    if isinstance(relyValue, (int, float)):
                        relyValue = str(relyValue)
                    logger.info(f'成功获取到依赖参数{params}的值为{relyValue}')
                except Exception as msg:
                    relyValue = ''
                    logger.error(f'获取依赖的值{params}失败,默认赋值为空，失败原因：{msg},全局变量参数:{relyData}')
                # finally:
                #     self.replace_params(params,relyValue,requestStr)
                requestStr = self.replace_params(params, relyValue, requestStr)
            return requestStr
        else:
            return None

    # 重新组装请求参数
    def regroup_request_data(self, case, relyData):
        requestData = self.data.get_request_data(case)
        paramsList = self.data.get_params_rely(case)
        # 请求参数为json格式时替换参数
        if isinstance(requestData, dict):
            requestStr = json.dumps(requestData)
            requestStr = self.replace_all_params(paramsList, relyData, requestStr)
            requestDict = json.loads(requestStr)
            # 将时间戳由str型转化为int型
            try:
                if 'arrivelHotelTime' in requestDict.keys() and '-' not in requestDict['arrivelHotelTime']:
                    requestDict['arrivelHotelTime'] = int(requestDict['arrivelHotelTime'])
                if 'departureHotelTime' in requestDict.keys() and '-' not in requestDict['departureHotelTime']:
                    requestDict['departureHotelTime'] = int(requestDict['departureHotelTime'])
                logger.info('本接口所有依赖的数据全部替换完成')
                # if 'protocolDiscount' in requestDict.keys():
                #     requestDict['protocolDiscount'] = int(requestDict['protocolDiscount'])
            except Exception as msg:
                logger.warning(f'时间戳转换失败:{msg}')
            return requestDict
        # 非json格式的请求参数的参数化值的处理（字符串/xml格式等）
        elif isinstance(requestData, str):
            requestData = self.replace_all_params(paramsList, relyData, requestData)
            # 需要转码为utf-8格式
            return requestData.encode('utf-8')
        elif isinstance(requestData, list):
            requestStr = str(requestData)
            requestData = self.replace_all_params(paramsList, relyData, requestStr)
            requestData = ast.literal_eval(requestData)
            return requestData
        else:
            logger.error(f'非json/text等格式，无法转换，给默认值None')
            return None

    # 处理后置sql语句
    def get_execute_sql(self, case, relyDate):
        sqlParams = self.data.get_rely_sql_params(case)
        if sqlParams:
            sql = self.data.get_sql(case)
            for params in sqlParams:
                value = relyDate[params]
                sql = self.replace_params(params, value, sql)
            sqlList = sql.split(';')
        else:
            sqlList = None
        return sqlList

    # 执行sql语句
    def execute_sql_sentence(self, case, relyData):
        sqlList = self.get_execute_sql(case, relyData)
        if sqlList:
            db = OperateMysql()
            for sql in sqlList:
                db.execute_sql(sql)
            db.close_connect()

    # 从请求的参数中获取需要参数化的变量名
    def get_rely_params_by_str(self,requestData):
        paramsList = []
        if requestData and isinstance(requestData, str) and '$' in requestData:
            paramsList = re.findall('\$(.+?)\$', requestData)
            # paramsList = re.findall('\${(.+?)}', requestData)
        return paramsList

    # 对单个预期的值参数值进行替换或运算
    def replace_expect_value(self, expectValue,relyData):
        if expectValue and '$' in expectValue:
            # 获取依赖参数字符串表达式
            index = expectValue.find('$')
            # value1 = expectValue
            if expectValue[-1] in ["'", '"']:
                value1 = expectValue[index:-1]
            else:
                value1 = expectValue[index:]
            # 替换表达式内的参数
            relyParams = self.get_rely_params_by_str(value1)[0]
            relyValue = self.get_rely_data_value(relyData,relyParams)
            value2 = self.replace_params(relyParams,relyValue,value1)
            # 计算结果
            value3 = eval(value2)
            # 替换整个依赖的参数表达式
            newExpectValue = expectValue.replace(value1, str(value3))
            return newExpectValue
        else:
            return expectValue

    # 获取全部替换后的预期值
    def get_all_expect_value(self,case,relyData):
        expectValueList = self.data.get_expect_value(case)
        newExpectValueList = []
        if expectValueList:
            for expectValue in expectValueList:
                newExpectValue = self.replace_expect_value(expectValue,relyData)
                newExpectValueList.append(newExpectValue)
            return newExpectValueList
        else:
            return expectValueList

    # 读取全局变量中的值
    def get_rely_data_value(self,relyData,key):
        try:
            relyValue = relyData[key]
        except:
            relyValue = ''
        return relyValue


'''
   对于依赖数据的处理
   1，定义一个全局变量，用于存储依赖的数据
   2，获取依赖的所有的接口返回的字段responseRely（全路径字段），转化为list
   3，获取依赖的所有的请求的参数的变量名fieldRely（全路径字段），转化为list
   4，根据请求返回的结果获取依赖的值，并把值存放到字典中dataRely
   5，根据接口所依赖的字段，在全局变量中获取对应的值keyRely
   6，根据获取到的依赖的值和请求参数的变量拼接参数（最好实现的方式就是使用字符串替换的方法，拼接完再转为字典）
   (进行拼接前还需要判断是否需要特殊处理：如日期实时获取，某个价格需要打折)

'''

if __name__ == '__main__':
    # dr = DataRely()
    # case = {'dataRely': 'data.info.name,data.info.age', 'fieldRely': 'name,age', 'paramsRely': 'name,age,id',
    #         'especialRely': '', 'requestKey': 'order001', 'jsonPath': '../dataCase/order.json'}
    # requestData = dr.data.get_request_data(case)
    # response = {'code': 200, 'msg': '成功', 'data': {'id': 1, 'info': {'name': 'zenghao', 'age': 21}}}
    # print('requestData', requestData)
    da = 'we'
    st = json.dumps(da)
    di = json.loads(st)
    print(EspecialData().get_random_num())
