s1 = "Maria".upper()
s2 = "José".lower()
s3 = "😃🐻🍔🍔" #UTF-8 - UNICODE
s4 = "यह कोड एक गड़बड़ है" # Hindi
s5 = "ఈ కోడ్ గందరగోళంగా ఉంది" # Telugo

print(s1, len(s1), s1.encode(), len(s1.encode()), type(s1))
print(s2, len(s2), s2.encode(), len(s1.encode()), type(s2))
print(s3, len(s3), s3.encode(), len(s3.encode()), type(s3))
print(s4, len(s4), s4.encode(), len(s4.encode()), type(s4))
print(s5, len(s5), s5.encode(), len(s5.encode()), type(s5))