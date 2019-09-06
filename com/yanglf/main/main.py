import pywifi

AKMS = {
    0: 'AKM_TYPE_NONE',
    1: 'AKM_TYPE_WPA',
    2: 'AKM_TYPE_WPAPKS',
    3: 'AKM_TYPE_WPA2',
    4: 'AKM_TYPE_WPA2PSK',
    5: 'AKM_TYPE_UNKNOWN'
}


def get_status():
    # 创建无线 WiFi 对象
    wifi = pywifi.PyWiFi()
    # 获取第一个无线网卡
    interface = wifi.interfaces()[0]
    status = interface.status()
    if status == 4:
        print('电脑已经连接网络')
    else:
        print('电脑未连接网络')


def get_wireless():
    wifi = pywifi.PyWiFi()
    interface = wifi.interfaces()[0]
    wireless = interface.scan_results()
    for data in wireless:
        # wifi 名称
        print(data.ssid)
        # wifi 加密方式
        print(AKMS[data.akm[0]])


def test_connect(self, find_str):
    # 创建 WiFi配置文件
    profile = pywifi.Profile()
    # 设置 WiFi名称
    profile.ssid = self.wifi_name
    # 设置 加密方式
    profile.akm.append(self.akm)
    # 设置加密单元
    profile.cipher = ''
    # 设置 密码
    profile.key =find_str





get_wireless()
