import requests,json,time

session=requests.session()
class xiekeyun():
    def __init__(self) -> None:
        self.headers={"content-type":"application/json"}
        self.token=self.login()
        pass

    def login(self):
        url="https://console.xiekeyun.com/api/user/_sysUser_login"

        data=json.dumps({
            "apiPath":"/sysUser/login",
            "email":None,
            "mobile":"13713088931",
            "mobileArea":"+86",
            "operateWay":1,
            "password":"GAOliu19780825",
            "screen":{
                "height":1080,
                "innerHeight":937,
                "innerWidth":1920,
                "outerHeight":1040,
                "outerWidth":1920,
                "width":1920,
            },
        })

        r=session.post(url=url,data=data,headers=self.headers)
        print("登陆成功！")
        return dict(r.cookies)["XSRF-TOKEN"]

    def get_modelNum(self,model1,model2):
        r=model2.find(model1)
        return model2[r:]

    def purchase_detail(self,purchase):
        url="https://console.xiekeyun.com/api/cloudCenter/_customerPurchase_detail"

        data=json.dumps({
            "apiPath":"/customerPurchase/detail",
            "companyCode":"74980966",
            "poXkNo":str(purchase),  #平台单号
        })
        
        headers=self.headers
        headers["company-code"]="74980966"
        headers["visit-source"]="1001"
        headers["user-agent"]="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64"
        headers["x-xsrf-token"]=self.token

        detail={}   #定义一个空字典
        result=session.post(url=url,data=data,headers=headers).json()["data"]

        detail["客户名称"]=result["extendN02"]
        detail["订单号码"]=result["poErpNo"]

        productCode=[] #模号
        productName=[] #物料名称
        productScale=[]    #规格
        purchaseQty=[]      #数量        
        for i in range(len(result["lineList"])):
            productName.append(result["lineList"][i]["productName"])

            model1=result["lineList"][i]["extendN02"]
            model2=result["lineList"][i]["productCode"]
            productCode.append(self.get_modelNum(model1,model2))

            productScale.append(result["lineList"][i]["productScale"])
            purchaseQty.append(str(result["lineList"][i]["purchaseQty"])+str(result["lineList"][i]["purchaseUnitName"]))
        #从订单内取出所有采购项的所需信息，返回列表
        
        detail["模号"]=productCode
        detail["物料名称"]=productName
        detail["规格"]=productScale
        detail["数量"]=purchaseQty

        print(detail["订单号码"]+"爬取数据成功！")

        return detail

    def close(self):
        session.close()


if __name__ == "__main__":

    tp=xiekeyun("1016249358111511")
    time.sleep(2)
    detail=tp.purchase_detail()
    import excel
    print(detail)
    excel.excel(detail)

