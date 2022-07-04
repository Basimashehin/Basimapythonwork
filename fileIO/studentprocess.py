# f=open("students.txt")
# f1=open("failed.txt")
# f2=open("passed.txt","w")
# st=[st.rstrip("\n") for st in f]
# fail=[fl.rstrip("\n")for fl in f1]
# print(st)
# print(fail)
# passed=set(st)-set(fail)
# # passed=[s for s in st if s not in fail]
# for l in passed:
#     l+="\n"
#     f2.write(l)


fp=open("passed.txt","a")
name="sooraj"
fp.write(name)