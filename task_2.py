text="Advertising companies say advertising is necessary and important. It informs people about new products. Advertising hoardings in the street make our environment colorful. And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next program in the mini-drama. Advertising can educate, too. Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. Without advertising, life is boring and colorless.But some consumers argue that advertising is a bad thing. They say that advertising is bad for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers know we love our children and want to give them everything. So they use children’s ‘pester power’ to sell their products. Finally, consumers say, if there is advertising there must be rules. Some adverts advertise unhealthy things like cigarettes and make people waste their money."
text_2=text.lower()
s_count=0
t_count=0
advert_count=0

for elem in text_2:
    if elem =='t':
        t_count +=1
    if elem =='s':
        s_count +=1


splitted_text=text_2.split()
new_text=""
for elem in splitted_text:
    if "advert" in elem:
        splitted_text_2=text_2.replace("advert","ADVERT")
        advert_count +=1
        new_text=(" "+elem)
    else :
        pass

text=new_text
print(splitted_text_2)
print(f"S:{s_count}")
print(f'T:{t_count}')
print(f'words with "advert":{advert_count}')