query="""
    SELECT NAME,
           ID,
           DEPT,
    FROM FUNC
    WHERE SAL > 10;
"""
q2='''
    SELECT NAME,
           ID,
           DEPT
    FROM FUNC
    WHERE SAL > 20;
'''

h1="""
<li name='item'>{}</li>
""".format(200).upper()

print(query, type(query))
print(q2, type(q2))
print(h1)