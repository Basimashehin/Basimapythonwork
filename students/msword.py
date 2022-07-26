master_word="abbcceddffggt"
chk_word="cat"


cur_char_count=0
flag=0
mw_dic={}


for char in master_word:
    if char in mw_dic:
        mw_dic[char]+=1
    else:
        mw_dic[char]=1
print(mw_dic)


for char in chk_word:
    if char in mw_dic:
        cur_char_count=mw_dic.get(char)
        if cur_char_count>0:
            mw_dic[char]-=1
        elif cur_char_count==0:
            flag=1
            break
    else:
        flag=1
        break

if flag==1:
    print("false")
else:
    print("true")
