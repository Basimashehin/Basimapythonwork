f=open("abc.txt","w")
# lines=list(f)
# out=[lines.rstrip("\n") for lines in f]
# print(out)
company_name="luminar\n"
f.write(company_name)
# print(list(f))

lst=["python","javascript","c#"]
for l in lst:
    l+="\n"
    f.write(l)

