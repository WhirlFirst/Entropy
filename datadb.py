import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "entropy.settings")

import django

django.setup()


def main():
    from date.models import Date
    filepath="H:\EntropyProject\后台数据"
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s' % (allDir))
        child1 = child.split('.')
        f = open("H:\EntropyProject\后台数据\\" + child, 'r')
        sum = []
        i = 1
        for line in f:
            sd = line.split('\t')
            if len(sd) <= 1:
                continue
            else:
                s = ''.join(sd[1])
                s = s.split('，', 1)
                p = ''.join(s[1])
                p ="\t" + p
                p = p.split('\n')
                sum.append(p[0])
                i = i + 1
        sum = ''.join(sum)
        Date.objects.get_or_create(day=child1[0],show=sum)
        f.close()


if __name__ == "__main__":
    main()
    print('Done!')