duration = int(input('Please enter your value here please\n'))
intervals = (
    (' дн', 86400),    # 60 * 60 * 24
    (' час', 3600),    # 60 * 60
    (' мин', 60),
    (' сек', 1),
)
def convert_time(duration):
    result=[]
    for name, count in intervals:
        value = duration//count
        if value>0:
            duration=duration-(value*count)
            result.append("{}{}".format(value,name))
    return ' '.join(result)
print(convert_time(duration))
