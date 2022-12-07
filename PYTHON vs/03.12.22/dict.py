#dict1={"one":1,"two":2,"three":3}
#dict2={"four":4,"five":5,"six":6}
#MERGE THE DICTIONARY IN ONE
#| IS USED TO MERGE TWO DICTIONARY
#print(dict1|dict2)
#.COPY IS USED TO MERGE TWO DICTIONARY
#dict3=dict1.copy()
#dict3.update(dict2)
#print(dict3)

dict1={
    "class":{
        "student":{
            "name":"XYZ",
            "marks":{
                "python":100,
                "web":90
            }
        }
    }
}

print(dict1["class"]["student"]["marks"]["web"])
