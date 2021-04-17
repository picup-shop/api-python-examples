import requests
import base64, json
import config
import time
import utils
print(config.API_BASE_URL)

url = config.API_BASE_URL + '/api/v1/idphoto/printLayout'
apikey = config.API_KEY
headers={'APIKEY': apikey, "Content-type": "application/json"}
file = "input/idphoto.jpg"
with open(file, mode='rb') as f:
  #base64的二进制
  base64_binary = base64.b64encode(f.read())
  #使用utf-8编码将二进制转为字符串
  base64_str = base64_binary.decode(encoding = "utf-8")
  # print(base64Str)
  data = {
    "base64": base64_str, #人像图片文件的base64
    "bgColor": "438EDB",#证件照背景色，格式为十六进制RGB， 如：3557FF
    "dpi": 300, #证件照打印dpi, 一般为300
    "mmHeight": 35, #证件照物理高度，单位为毫米
    "mmWidth": 25, #证件照物理宽度，单位为毫米
    "printBgColor": "FFFFFF", #排版背景色，格式为十六进制RGB， 如：FFFCF9
    "printMmHeight": 152, #打印的排版尺寸，单位为毫米, 如果为0或小于证件照尺寸则不会进行打印排版，输出单张证件照
    "printMmWidth": 102, #打印的排版尺寸，单位为毫米, 如果为0或小于证件照尺寸则不会进行打印排版，输出单张证件照
    "dress": "man8", #换装参数，非必填项，无参数时不换装，为类型+换装编号格式，比如 man1 男士第一个换装图， woman3 女士第三个换装，child5 儿童第五个换装。换装需额外扣除一个点点数
    "printMarginMm":5 #打印的排版的外部预留空间尺寸，非必填项
  }
  response = requests.post(url=url, headers=headers, json=data)
  content = response.content.decode(encoding = "utf-8")
  print(content)
  json_result = json.loads(content)
  if json_result["code"] == 0:
    image_url = json_result["data"]["idPhotoImage"]
    file_name = './output/idphoto'+time.strftime("%Y.%m.%d.%H.%M.%S", time.localtime())+".jpg"
    utils.download_img(image_url,file_name)
