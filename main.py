if __name__ =="__main__":
    import Purchase_detail,excel,time

    purchase=[
        "1016249358111511",
        "1016249358110712",
        "1016248793157240",
        "1016248793202042",
        "1016248793228844",
        "1016249358157617",
        "1016249358200222",
        "1016249358252824",
        "1016249376002834",
        "1016249376001235",
        "1016251061517514",
        "1016252205967201",
        "1016252206064807",
        "1016252206459224",
        ]

    xiekeyun=Purchase_detail.xiekeyun()
    time.sleep(2)
    for i in purchase:
        
        detail=xiekeyun.purchase_detail(purchase=i)
        time.sleep(1)
        excel.excel(detail)
        time.sleep(1)
    xiekeyun.close()
