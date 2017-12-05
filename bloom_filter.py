#!/usr/bin/env python
class BloomFilter(object):

    #constructor
    def __init__(self,size):
        self.size = size
        self.values = [False]*size 

    #might contains
    def contains(self,value):
        index = self.hash_value(value)
        return self.values[index]

    #add 
    def add_value(self, value):
        index = self.hash_value(value)
        self.values[index] = True

    #hash value 
    def hash_value(self, value):
        return hash(value)%self.size

    #print 
    def print_content(self):
        print self.values


if __name__ == '__main__':
    print 'Bloom Filter'
    bf = BloomFilter(10)
    bf.add_value('fish')
    bf.print_content()
    bf.add_value('dog')
    bf.print_content()
    bf.add_value('cat')
    bf.print_content()
    bf.add_value('duck')
    bf.print_content()
