import dateparser

def timeToStr(time):
    dt = dateparser.parse(time)
    return dt.strftime('%Y-%m-%d %H:%M:%S')