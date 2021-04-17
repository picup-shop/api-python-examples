import lib.utils



def test():
    url = 'http://deeplor.oss-cn-hangzhou.aliyuncs.com/upload/image/20200817/b261cffebe11499f8d283c18bbd3a544.png'
    file_name = 'out.jpg'
    lib.utils.download_img(url,file_name)