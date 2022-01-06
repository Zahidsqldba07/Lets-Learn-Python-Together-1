x={1,2,3,4,9,6,7,8,5,9}
y={10,11,15,13,14,12,16,17,18,19,19}
z={20,21,22,23,27,25,26,24,28,29,22}

unionize=x.union(y).union(z)

convert=list(unionize)

a=slice(20)

print(convert[a])

'''----------------------------------------------------------------'''

x={1,2,3,4,9,6,7,8,5,9}
y={10,11,15,13,14,12,16,17,18,19,19}
z={20,21,22,23,27,25,26,24,28,29,22}

unionize=x.union(y,z)

convert=list(unionize)

a=slice(20)

print(convert[a])

'''----------------------------------------------------------------'''

a=list()
for i in range(10):
    a.append(i)

b=set()
for i in range(10):
    b.add(i)

print(a)
print(b)

'''----------------------------------------------------------------'''

nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1 | nums2) # Union

print(nums1.union(nums2)) # Union

nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1 & nums2) # Intersection

print(nums1.intersection(nums2)) # Intersection

nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1 - nums2) # Difference

print(nums1.difference(nums2)) # Difference

nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1.symmetric_difference(nums2)) # Symmetric Difference

print(nums1 ^ nums2) # Symmetric Difference

'''----------------------------------------------------------------'''

nums1={0,1,2,3,1,3,4,10,5,6,6,7,8,9,10,23}
nums2={1,2,7,1,3,4,10,5,6,6,7,8,9,10,11,22}

print(nums1 | nums2) # Union
print(nums1 & nums2) # Intersection
print(nums1 - nums2) # Difference
print(nums1 ^ nums2) # Symmetric Difference

nums1=[1,2,3,1,3,4,10,5,6,6,7,8,9,10]
nums2=[1,2,3,1,3,4,10,5,6,6,7,8,9,10]

uniques1=set(nums1)
uniques2=set(nums2)

print(uniques1 | uniques2)
