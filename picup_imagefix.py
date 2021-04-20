import requests
import base64, json
import config
import time
import utils

print(config.API_BASE_URL)


# 模式一： 返回二进制图片文件
def image_fix():
  url = config.API_BASE_URL+'/api/v1/imageFix'
  apikey = config.API_KEY
  headers = {'APIKEY': apikey, "Content-type": "application/json"}

  input_file = "input/imagefix1.jpg"
  mask_file = "input/imagefix1_mask.jpg"

  contentBase64 = None
  maskBase64 = None
  with open(input_file, mode='rb') as f:
    # base64的二进制
    base64_binary = base64.b64encode(f.read())
    # 使用utf-8编码将二进制转为字符串
    contentBase64 = base64_binary.decode(encoding="utf-8")
  with open(mask_file, mode='rb') as f:
    # base64的二进制
    base64_binary = base64.b64encode(f.read())
    # 使用utf-8编码将二进制转为字符串
    maskBase64 = base64_binary.decode(encoding="utf-8")
  data = {
    "base64": contentBase64,
    "maskBase64": maskBase64
  }
  response = requests.post(url=url, headers=headers, json=data)
  print(response.content)
  json_result = json.loads(response.content)
  if json_result["code"] == 0:
    image_url = json_result["data"]["imageUrl"]
    file_name = './output/image_fix'+time.strftime("%Y.%m.%d.%H.%M.%S", time.localtime())+".jpg"
    utils.download_img(image_url,file_name)

if __name__ == '__main__':
  image_fix()
