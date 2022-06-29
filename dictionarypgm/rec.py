# print(dir(dict))
word_count={"a":2,"b":5,"c":2,"d":4,"e":2}
#
#
#
# print(word_count)
print(word_count.items())
for k,v in word_count.items():
    print(k,v)



# wc_list = word_count.items()
# print(sorted(wc_list,key=lambda item:item[1],reverse=True))
#
# print(max(wc_list,key=lambda l:l[1]))
print(max(word_count.items(),key=lambda i:i[1]))

print(min(word_count.items(),key=lambda i:i[1]))