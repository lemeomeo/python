'''
Given two binary strings, return their sum (also a binary string).
For example,
a = "11"
b = "1"
Return "100".
'''
class Solution(object):
    def addBinary(self, a, b):
        if max(a.len(), b.len()) == a.len():
            b.zfill(a.len())
        else:
            a.zfill(b.len())
        length = a.len()  # length of the binary strings
        index = a.len() - 1  # the last index of the binary strings
        '''
        There should be X cases:
        carry=0, a=1, b=0 --> 1
        '''
        for index in length:
            carry = "0"
            if a[index] == "0" and b[index] == "1" and carry=="0":
                index = index - 1
            elif a[index]=="1" and b[index]=="1":
                index = 0

            # TODO: adding two binary from right to left