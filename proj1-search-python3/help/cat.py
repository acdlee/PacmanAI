from util import Stack as s, Queue as q

st = s()
qu = q()

st.push(8)
st.push(10)

qu.push(8)
qu.push(10)

print("This is st: " + str(st))
print("This is qu: " + str(qu))

print("st.pop(): " + str(st.pop()))
print("qu.pop(): " + str(qu.pop()))
