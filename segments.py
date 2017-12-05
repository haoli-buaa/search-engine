#!/usr/bin/env python

def segments(s):
    result = set()
    for major in major_segment(s):
        for minor in minor_segment(major):
            result.add(minor)
    return result;


def major_segment(s):
    last = -1
    segment_word = ' '
    result = set()

    for idx,ch in enumerate(s):
        if ch in segment_word:
            segment = s[last+1:idx]
            #print segment
            result.add(segment)
            #print result
            last = idx
            #print last

    result.add(s[last+1:])
    
    return result

def minor_segment(s):
    last = -1
    segment_word = '._'
    result = set()

    for idx,ch in enumerate(s):
        if ch in segment_word:
            segment = s[last+1:idx]
            result.add(segment)
            segment = s[:idx]
            result.add(segment)
            last = idx

    result.add(s[last+1:])
    result.add(s)

    return result


if __name__ == '__main__':
   s = 'hello world'
   result  = major_segment(s)
   print result   
   ip_addr = '1.2.3.4'
   result = minor_segment(ip_addr)
   print result 
   s = 'src_ip = 1.2.3.4'
   result = segments(s)
   print result
