import requests, socket

# 在下方输入你的账号
UserName = ""
# 在下方输入你的密码
Pwd = ""
# 在下方选择你的运营商 删除＃以启用 校园网为空
# ISP = "telecom"
# ISP = "yidong"
# ISP = "unicom"
# ISP = ""


# 测试是否已经联网
def Check_connected():
    s = socket.socket()
    s.settimeout(2)
    status = s.connect_ex(('103.235.46.39', 443))
    return status

def connect_net(UserName,Pwd,ISP,Post_addr):

    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    post_str = "DDDDD=%2C0%2C"+UserName+"%40"+ISP+"&upass="+Pwd+"&R1=0&R2=0" \
              "&R6=0&para=00&0MKKey=123456&buttonClicked=&redirect_url=&err_fl" \
              "ag=&username=&password=&user=&cmd=&Login="
    post_login = "http://"+Post_addr+":801/eportal/?c=ACSetting&a=Login&protoco" \
                 "l=http:&hostname="+Post_addr+"&iTermType=1&mac=000000000000&" \
                 "ip="+ip+"&enAdvert=0&loginMethod=1"
    post_lenth = len(post_str)
    post_header ={
        'Host': ''+Post_addr+':801',
        'Connection': 'keep-alive',
        'Content-Length': str(post_lenth),
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'http://'+Post_addr+'',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://'+Post_addr+'/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'program=aygxy; vlan=0; ip='+ip+'; areaID=mac%3D000000000000; is_login=1'
    }
    post_data = {
        'DDDDD':',0,'+UserName+'@'+ISP,
        'upass':Pwd,
        'R1': '',
        'R2': '',
        'R6': '',
        'para': '00',
        '0MKKey': '123456',
        'buttonClicked': '',
        'redirect_url': '',
        'err_flag': '',
        'username': '',
        'password': '',
        'user': '',
        'cmd': '',
        'Login': ''
    }

    requests.post(post_login, data=post_data, headers=post_header)

def main():
    connected = Check_connected()
    if connected == 0:
        print("network is already connected")
        pass
    else:
        if ISP == "":
            Post_addr = "172.168.254.4"
        else:
            Post_addr = "172.168.254.6"
        connect_net(UserName, Pwd, ISP, Post_addr)

if __name__ == '__main__':
    main()