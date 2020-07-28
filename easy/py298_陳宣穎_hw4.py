zipcode = {"台北市":{"中正區": 100, "大同區": 103, "中山區": 104, "松山區": 105, 
                  "大安區": 106, "萬華區": 108, "信義區": 110, "士林區": 111,
                  "北投區": 112, "內湖區": 114, "南港區": 115, "文山區": 116}, 
           "基隆市":{"仁愛區": 200, "信義區": 201, "中正區": 202, "中山區": 203, 
                  "安樂區": 204, "暖暖區": 205, "七堵區": 206},
           "新北市": {"萬里區": 207, "金山區": 208, "板橋區": 220, "汐止區": 221,
                   "深坑區": 222, "石碇區": 223, "瑞芳區": 224, "平溪區": 226, 
                   "雙溪區": 227, "貢寮區": 228, "新店區": 231, "坪林區": 232, 
                   "烏來區": 233, "永和區": 234, "中和區": 235, "土城區": 236, 
                   "三峽區": 237, "樹林區": 238, "鶯歌區": 239, "三重區": 241, 
                   "新莊區": 242, "泰山區": 243, "林口區": 244, "蘆洲區": 247, 
                   "五股區": 248, "八里區": 249, "淡水區": 251, "三芝區": 252, 
                   "石門區": 253}}

def list_zip(city):
    n = zipcode.get(city)
    for (area, codes) in n.items():
        print(area, codes)

list_zip('台北市')

def area_to_zip(a):
    for (city, zipcodes) in zipcode.items():
        for (area, codes) in zipcodes.items():
            if a in zipcodes:
                return city, zipcodes[a]

a = input('請輸入一個區域名稱:')
print(area_to_zip(a))

def zip_to_area(zips):
    for (city, zipcodes) in zipcode.items():
        for (area, codes) in zipcodes.items():
            if zips == codes: 
                return area

z = int(input('請輸入郵遞區號:'))
print(zip_to_area(z))

    

