myfilehandle = open("jenkins.csv", 'r')

# get the order name
raw_ordername = myfilehandle.name
ordername = (raw_ordername.split('.csv'))

# get order name from the file
raw_orderkey = ordername[0]
orderkey = raw_orderkey
# print('orderkey: ', orderkey)


# get the order value
myorder = myfilehandle.readlines()
newlist = []
for value in myorder:
    value = value.split(",")
    newlist.extend(value)

people_num = newlist[0]
avg_slices = newlist[1]
