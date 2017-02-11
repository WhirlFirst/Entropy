import os
import xlrd
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "entropy.settings")

import django

django.setup()

def main():
    from date.models import Processing
    data = xlrd.open_workbook('H:\EntropyProject\processingFinal.xls')
    table = data.sheets()[0]
    nrows = table.nrows
    for i in range(nrows):  # 循环逐行打印
        if i == 0:  # 跳过第一行
            continue
        f = table.row_values(i)
        URL1 = str(f[0])
        name1 = str(f[1])
        Processing.objects.get_or_create(name=name1,iframe=URL1)


if __name__ == "__main__":
    main()
    print('Done!')
