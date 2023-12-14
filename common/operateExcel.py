from datetime import date
import xlrd
from xlutils.copy import copy
from common.utilTool import UtilTool
from common.log import Log
from configFile import confPath

logger = Log().get_logger()


class OperateExcel(object):
    def __init__(self,filename=None):
        if filename:
            self.filename = filename
        else:
            # self.filename = UtilTool().get_file_dirname('dataCase','meizhuPMSApi.xls')
            self.filename = confPath.TEST_CASE_PATH
        self.workbook = xlrd.open_workbook(self.filename)

    # 初始化对象，读取全部sheets对象
    def get_all_sheets(self):
        sheets = self.workbook.sheets()
        # logger.info(f'成功读取Excel文件全部sheet对象，sheet对象:{sheets}')
        return sheets

    # 查询全部sheets数量
    def get_sheet_counts(self):
        sheetSum = self.workbook.nsheets
        # logger.info(f'成功获取到全部业务模块的数量为：{sheetSum}个')
        return sheetSum

    # 查询全部sheet页的名字
    def get_sheet_names(self):
        sheetNames = self.workbook.sheet_names()
        # logger.info(f'成功获取到全部业务模块：{sheetNames}')
        return sheetNames

    # 通过索引获取单个sheet页的内容
    def get_data_by_id(self,sheetId):
        data = self.workbook.sheet_by_index(sheetId)
        # logger.info(f'成功获取到sheet内容为：{data}')
        return data

    # 通过sheet名获取单个sheet页的内容
    def get_data_by_name(self,sheetName):
        data = self.workbook.sheet_by_name(sheetName)
        # logger.info(f'成功获取到业务模块[{sheetName}]的全部内容')
        return data

    # 获取sheet页单元格总行数
    def get_lines(self,data):
        """
        :param data: 单个sheet对象
        :return: 单元格行数
        """
        rowSum = data.nrows
        # logger.info(f'成功获取到单个sheet页总行数为：{rowSum}')
        return rowSum

    # 获取sheet页单元格总列数
    def get_columns(self,data):
        colSum = data.ncols
        # logger.info(f'成功获取到单个sheet页总行数为：{colSum}')
        return colSum

    # 获取某一行的数据
    def get_row_values(self,data,row):
        rowData = data.row_values(row)
        # logger.info(f'成功获取到第{row}行的数据为：{rowData}')
        return rowData

    # 获取某一列的数据
    def get_col_values(self,data,col=None):
        if not col:
            col = 0
        colData = data.col_values(col)
        # logger.info(f'成功获取到第{col}列的数据为：{colData}')
        return colData

    # 获取某个单元格的数据类型
    def get_cell_type(self,data,row,col):
        cellType = data.cell(row,col).ctype
        # logger.info(f'成功获取到单元格({row},{col})的数据类型为：{cellType}')
        return cellType

    # 获取单元格的数据
    def get_cell_value(self,data,row,col):
        # 读取日期格式时的特殊处理
        if self.get_cell_type(data,row,col) == 3:
            dateValue = xlrd.xldate_as_tuple(data.cell_value(row, col), self.workbook.datemode)
            getValue = date(*dateValue[:3]).strftime('%Y/%m/%d')
        else:
            getValue = data.cell_value(row,col)
        # logger.info(f'成功获取到第{row}行第{col}列的值为：{getValue}')
        return getValue

    # 写入数据--通过sheetId或者sheetName都可以
    def write_value(self, sheetX, row, col, value):
        # 复制文件(需要新建一个打开文件的实例对象)
        # writeData = copy(self.workbook)
        writeData = copy(xlrd.open_workbook(self.filename))
        # 读取sheet页
        # sheetData = writeData.sheet_by_index(sheetId)
        sheetData = writeData.get_sheet(sheetX)
        sheetData.write(row, col, value)
        writeData.save(self.filename)
        # logger.info(f'成功写入测试/查询结果：{value}')



    # 根据caseId获取依赖的用例所在的列的行号
    def get_row_num(self,data,caseId):
        num = 0
        colValues = self.get_col_values(data)
        for data in colValues:
            if data == caseId:
                return num
            num += 1

    # 根据依赖用例的行号获取行的内容
    def get_row_data(self,data,caseId):
        num = self.get_row_num(data,caseId)
        rowValues = self.get_row_values(data,num)
        return rowValues






if __name__ == '__main__':

    filename= 'C:\\Users\\admin\\Desktop\\fz.xlsx'
    op = OperateExcel(filename)
    print(op.filename)



