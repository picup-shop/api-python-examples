import urllib.request

def download_img(img_url, file_name):
    try:
        request = urllib.request.Request(img_url)
        response = urllib.request.urlopen(request)
        if (response.getcode() == 200):
            with open(file_name, "wb") as f:
                f.write(response.read()) # 将内容写入图片
            return file_name
    except:
        return "failed"