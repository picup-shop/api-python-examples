import requests
import base64, json
import config
import time
import urllib.parse

print(config.API_BASE_URL)


# 模式一： 返回二进制图片文件
def matting(matting_type):
  url_params = {
    "mattingType":matting_type, #抠图类型， 1：人像，2：物体，3：头像，4：一键美化，6：通用抠图, 11：卡通化。
  }
  query_str = urllib.parse.urlencode(url_params)
  url = config.API_BASE_URL + '/api/v1/matting?'+query_str

  apikey = config.API_KEY
  response = requests.post(
      url,
      files={'file': open('input/idphoto.jpg', 'rb')},
      headers={'APIKEY': apikey},
  )
  file_name = './output/matting1-'+time.strftime("%Y.%m.%d.%H.%M.%S", time.localtime())+".jpg"
  with open(file_name, 'wb') as out:
      out.write(response.content)

#模式二： 返回json格式数据，图片数据为base64编码字符串
def matting2(matting_type):
  url_params = {
    "mattingType": matting_type,  # 抠图类型， 1：人像，2：物体，3：头像，4：一键美化，6：通用抠图, 11：卡通化。
  }
  query_str = urllib.parse.urlencode(url_params)
  url = config.API_BASE_URL + '/api/v1/matting2?' + query_str
  apikey = config.API_KEY
  response = requests.post(
      url,
      files={'file': open('input/idphoto.jpg', 'rb')},
      headers={'APIKEY': apikey},
  )

  content = response.content.decode(encoding = "utf-8")
  print(content)
  json_result = json.loads(content)
  if json_result["code"] == 0:
    image_base64 = json_result["data"]["imageBase64"]
    base64_binary = base64.b64decode(image_base64)
    file_name = './output/matting2-'+time.strftime("%Y.%m.%d.%H.%M.%S", time.localtime())+".png"
    with open(file_name, 'wb') as out:
        out.write(base64_binary)

#模式二： 通过图片url地址作为参数，返回json格式数据，图片数据为base64编码字符串
def mattingByUrl(matting_type):
  url = config.API_BASE_URL + '/api/v1/mattingByUrl'
  test_image_url = "http://deeplor.oss-cn-hangzhou.aliyuncs.com/upload/image/20200903/1705c25fa2884cb282ef2be77ec516ef.jpg"
  url_params = {
    "mattingType": matting_type,  # 抠图类型， 1：人像，2：物体，3：头像，4：一键美化，6：通用抠图, 11：卡通化。
    "url": test_image_url #图片url地址
  }
  url = config.API_BASE_URL + '/api/v1/mattingByUrl'
  apikey = config.API_KEY
  response = requests.get(
    url,
    params=url_params,
    headers={'APIKEY': apikey},
  )

  content = response.content.decode(encoding="utf-8")
  print(content)
  json_result = json.loads(content)
  if json_result["code"] == 0:
    image_base64 = json_result["data"]["imageBase64"]
    base64_binary = base64.b64decode(image_base64)
    file_name = './output/mattingByUrl-' + time.strftime("%Y.%m.%d.%H.%M.%S", time.localtime()) + ".png"
    with open(file_name, 'wb') as out:
      out.write(base64_binary)
if __name__ == '__main__':
  matting(matting_type=11)
  matting2(matting_type=11)
  mattingByUrl(matting_type=11)
