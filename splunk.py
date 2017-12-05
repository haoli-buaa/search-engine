from bloom_filter import BloomFilter
from segments import segments

BLOOM_FILTER_SIZE = 64

class Splunk(object):
    def __init__(self):
        self.bf = BloomFilter(BLOOM_FILTER_SIZE)
        self.terms = {}
        self.events = []

    def add_event(self,event):
        event_id = len(self.events)
        terms = segments(event)
        for term in terms:
            if term not in self.terms:
                self.terms[term] = set()
            self.terms[term].add(event_id)
            self.bf.add_value(term)
        self.events.append(event)

    def search(self, term):
        if not self.bf.contains(term):
            return []
        return self.terms[term]

    def print_event(self, event_ids):
        for event_id in event_ids:
            print self.events[event_id]

if __name__ == '__main__':
    splunk = Splunk()
    splunk.add_event('src_ip = 1.2.3.4')
    splunk.add_event('src_ip = 10.10.10.4')
    splunk.add_event('src_ip = 192.168.1.1')
    splunk.add_event('hello world')

    result = splunk.search('src_ip')
    print '***src_ip***'
    splunk.print_event(result)

    result = splunk.search('cat')
    print '***cat***'
    splunk.print_event(result)

    result = splunk.search('4')
    print '***4***'
    splunk.print_event(result)

    result = splunk.search('hello')
    print '***hello***'
    splunk.print_event(result)
