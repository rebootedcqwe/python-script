import re,string
f = open("sd.txt","r")
text = f.read()
#text = " Hello, world! 这，是：我;第!一个程序\?()（）<>《》 "
punc = '~`!#$%^&*()_+-=|\;":/.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》《{}'
print(re.sub(r"[%s]+" %punc, " ",text))
f.close()                                         
