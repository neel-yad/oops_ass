def filtering_article(article,keyword):
    print("The article having '%s' keyword are:-" %keyword)
    for name in article:
        name_lower=name.lower()
        name_split=name_lower.split()
        keyword=keyword.lower()
        for word in name_split:
            if((word==keyword) or (word==(keyword+'.')) or (word==(keyword+',')) ):
                print(name)
Article=["Hello Dude Myself Neel","neel is a good boy","neel is studying in IIIT Dwd","I live in jaunpur","I am CSE students","neel. will also be included"]
filtering_article(Article,"neel")                        