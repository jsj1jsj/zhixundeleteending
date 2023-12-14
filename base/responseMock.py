from unittest import mock


# mock的结果
def mock_data(responseData):
    mockRes = mock.Mock(return_value=responseData)
    return mockRes

# mock统一的方法
def mock_test(runMethod,url,method,requestData,responseData):
    """
    :param runMethod: 接口测试定义的方法，需要mock的request方法
    :param url: request方法请求的接口地址
    :param method: request方法请求的接口类型post/get
    :param requestData: request方法请求的接口请求参数
    :param responseData: 需要mock的返回数据（结果）
    :return:
    """
    runMethod = mock.Mock(return_value=responseData,side_effect=runMethod)
    result = runMethod(url,method,requestData)
    return result
