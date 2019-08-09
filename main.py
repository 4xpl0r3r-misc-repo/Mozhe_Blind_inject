import sys,requests,logging
from class_iSpider import iSpider
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

def main():
    if len(sys.argv)<2:
        oriURL=input("请输入URL:")
        oriStr=input("请输入正确标志字符串(仅限英文,可为html代码):")
        table=input("请输入数据表")
    else:
        oriURL=sys.argv[1]
        oriStr=sys.argv[2]
        table=sys.argv[3]
    logging.info("初始化爬虫实例中...")
    mySpider=iSpider(oriURL,oriStr,table)
    logging.info("爬虫实例初始化完成!")
    logging.info("正在获取数据集...")
    mySpider.getResultList()
    logging.info("成功获取数据集!")
    logging.info("开始打印数据结果!")
    mySpider.printAllResult()


if __name__ == '__main__':
    main()