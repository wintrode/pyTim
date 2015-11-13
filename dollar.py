# cost of a string

def cost(str) :
    val = 0
    str = str.lower()
    for c in str:
        val += ord(c) - ord('a') + 1

    return val

def find_dollars(file) :

    count = 0
    for l in open(file, 'r') :
        words = l.strip().split();
        for w in words :
            v = cost(w);
            if (v == 100) :
                print "Found a $1 word: %s" % (w)
                count += 1
    print "Found %d $1 words" % (count)




