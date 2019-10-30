import sys 
for line in sys.stdin: 
    # remove leading and trailing whitespace 
    line = line.strip() 
    # split the line into words 
    numb = line.split() 
    # increase counters 
    for num in numb: 
        print('%s\t%s' % (num,1))
