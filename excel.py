import xlwt,time

def excel(detail):
    
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet = workbook.add_sheet('Sheet1')

    worksheet.write(0,0,"客户名称")#行，列，数据
    for i in range(len(detail["模号"])):
        worksheet.write(i+1,0,detail["客户名称"])

    worksheet.write(0,1,"订单号码")
    for i in range(len(detail["模号"])):
        worksheet.write(i+1,1,detail["订单号码"])

    worksheet.write(0,2,"模号")
    if type(detail["模号"]) is list:
        for i in range(len(detail["模号"])):
            worksheet.write(i+1,2,detail["模号"][i])
    
    worksheet.write(0,3,"物料名称")
    if type(detail["物料名称"]) is list:
        for i in range(len(detail["物料名称"])):
            worksheet.write(i+1,3,detail["物料名称"][i])

    worksheet.write(0,4,"规格")
    if type(detail["规格"]) is list:
        for i in range(len(detail["规格"])):
            worksheet.write(i+1,4,detail["规格"][i])

    worksheet.write(0,5,"数量")
    if type(detail["数量"]) is list:
        for i in range(len(detail["数量"])):
            worksheet.write(i+1,5,detail["数量"][i])

    date=time.strftime("%Y.%m.%d")
    worksheet.write(0,6,"日期")#行，列，数据
    for i in range(len(detail["模号"])):
        worksheet.write(i+1,6,date)


    for i in range(0,7):
        worksheet.col(i).width = 6000
    workbook.save("./"+detail["订单号码"]+".xls")
    print(detail["订单号码"]+"写入xls成功！")

if __name__ == "__main__":
    detail={
        '客户名称': '货送百汇厂',
        '订单号码': 'SZTOL2101710',
        '模号': ['LEH21331A-0-210', 'LEH21331A-0-211', 'LEH21331A-0-212', 'LEH21331A-0-213', 'LEH21331A-0-214', 'LEH21331A-0-219', 'LEH21333A-0-201', 'LEH21333A-0-202', 'LEH21333A-0-206', 'LEH21333A-0-207', 'LEH21333A-0-211', 'LEH21333A-0-212', 'LEH21333A-0-213'],
        '物料名称': ['喉塞', 'O型密封圈', 'O型密封圈', 'O型密封圈', '铜水管', '快速喉咀', '喉塞', '快速喉咀', ' 铜水咀', 'O型密封圈', 'O型密封圈', '波子螺丝', '铜水管'],
        '规格': ['PT1/8', 'ORP8', 'ORP9', 'ORP12', '内外牙PT1/8*75', 'M-PC-8-01', 'PT1/8"', 'M-PC8-01', 'PT1/8*1”', 'ORP9', 'ORP10', 'BBSJ8', 'PT1/8-L75内外牙'],
        '数量': ['20个', '10个', '10个', '10个', '6条', '10个', '30个', '20个', '20个', '15个', '4个', '10支', '5支']
        }
    excel(detail)
    #print(type(detail["客户名称"])=)