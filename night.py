import time
import datetime
import json
import requests


# 健康打卡的URL地址
check_url = "https://reportedh5.17wanxiao.com/sass/api/epmpics"

text = input()
deptId = eval(input())
address = input()
addtext = input()
code = input()
stuNum = input()
userName = input()
phoneNum = input()
userId = input()
emergency = input()
emergencyPhone = input()
sckey = input()


area = {'address': address, 'text': addtext, 'code': code}

areaStr = json.dumps(area, ensure_ascii=False)

# POST提交的json字段，根据自己的修改
jsons ={"businessType":"epmpics","method":"submitUpInfoSchool","jsonData":{"deptStr":{"deptid":72102,"text":"粮油食品学院-粮食工程-粮工1803"},"areaStr":"{\"streetNumber\":\"\",\"street\":\"长椿路辅路\",\"district\":\"中原区\",\"city\":\"郑州市\",\"province\":\"河南省\",\"town\":\"\",\"pois\":\"河南工业大学(莲花街校区)\",\"lng\":113.55057699999924,\"lat\":34.83918796232838,\"address\":\"中原区长椿路辅路河南工业大学(莲花街校区)\",\"text\":\"河南省-郑州市\",\"code\":\"\"}","reportdate":1601125933196,"customerid":43,"deptid":72102,"source":"app","templateid":"clockSign3","stuNo":"201811020308","username":"和嘉晖","userid":9564950,"updatainfo":[{"propertyname":"temperature","value":"36.4"},{"propertyname":"symptom","value":"无症状"}],"customerAppTypeRuleId":148,"clockState":0},"token":"1b18056c-8bff-40fa-84eb-c1262d3d6fef"}


response = requests.post(check_url, json=jsons)
# 以json格式打印json字符串
res = json.dumps(response.json(), sort_keys=True, indent=4, ensure_ascii=False)
print(res)


SCKEY = SCU115521Tcc18c0c55b554ad33d48b2d534891e0a5f6f5143e22a2

now_time = datetime.datetime.now()
bj_time = now_time + datetime.timedelta(hours=8)

test_day = datetime.datetime.strptime('2020-12-19 00:00:00','%Y-%m-%d %H:%M:%S')
date = (test_day - bj_time).days
desp = f"""
------
### 现在时间：
```
{bj_time.strftime("%Y-%m-%d %H:%M:%S %p")}
```
### 打卡信息：
```
{res}
```
> 关于打卡信息
>
> 1、成功则打卡成功
>
> 2、系统异常则是打卡频繁
### ⚡考研倒计时:
```
{date}天
```
>
> [GitHub项目地址](https://github.com/ReaJason/17wanxiaoCheckin-Actions) 
>
>期待你给项目的star✨
"""

headers = {
    "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
}

send_url = f"https://sc.ftqq.com/{SCKEY}.send"

params = {
    "text": f"完美校园健康打卡---{bj_time.strftime('%H:%M:%S')}",
    "desp": desp
}
    
# 发送消息
response = requests.post(send_url, data=params, headers=headers)
if response.json()["errmsg"] == 'success':
        print("Server酱推送服务成功")
else:
        print("Something Wrong")
