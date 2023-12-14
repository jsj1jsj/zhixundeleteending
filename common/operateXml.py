from common.utilTool import UtilTool
class OperateXml(object):
    def __init__(self,filename=None):
        if filename:
            self.filename = filename
        else:
            self.filename = UtilTool().get_file_dirname('dataCase/jsonParams','alitrip.xml')

    def get_xml_data(self):
        with open(self.filename,'r',encoding='utf-8') as fn:
            data = fn.read()
            return data
class OperateXml1(object):
    def __init__(self,filename=None):
        if filename:
            self.filename = filename
        else:
            self.filename = UtilTool().get_file_dirname('dataCase/jsonParams','1.xml')

    def get_xml_data(self):
        with open(self.filename,'r',encoding='utf-8') as fn:
            data = fn.read()
            return data
class OperateXml2(object):
    def __init__(self,filename=None):
        if filename:
            self.filename = filename
        else:
            self.filename = UtilTool().get_file_dirname('dataCase/jsonParams','el.xml')

    def get_xml_data(self):
        with open(self.filename,'r',encoding='utf-8') as fn:
            data = fn.read()
            return data
if __name__ == '__main__':
    ox = OperateXml()
    print(ox.filename)
    data = ox.get_xml_data()
    print(type(data))

