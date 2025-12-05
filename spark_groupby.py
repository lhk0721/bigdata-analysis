myRdd2_group = myRdd2.groupBy(lambda x: '아파치' in x)
for k,v in myRdd2_group.collect():
    for eachvalue in v:
        print(f'{k}: {v}')
    print('-----')
