import xlwt  
 
def txt_xls(filename, xlsname):
    try:
        f = open(filename, 'r', encoding='utf-8')
        xls = xlwt.Workbook()
        sheet = xls.add_sheet('单词', cell_overwrite_ok=True)
        x = 0
        while True:
            # 按行循环，读取文本文件
            line = f.readline()
            if not line:
                break
            for i in range(len(line.split('\t'))):
                item = line.split('\t')[i]
                sheet.write(x, i, item)
            x += 1
        f.close()
        xls.save(xlsname)  # 保存xls文件
    except:
        raise
 
if __name__ == "__main__":
    filename = "/root/test_003"   #vvv
    xlsname = "/root/aaa.xlsx"     #保存及命名
    txt_xls(filename, xlsname)
