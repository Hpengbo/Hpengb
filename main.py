"""
调用风险处置列表接口
接口: http://192.10.91.36:8081/fxfk/api/v1/fxcz/fxczlb
"""

import requests
import json


# input_token = input("输入 token: ")
input_token = ('111')
# 接口URL
API_URL = "http://192.10.91.36:8081/fxfk/api/v1/fxcz/fxczlb"

# 请求头
HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Referer": "http://babg-appweb-pre.oss-cn-hangzhou-yzwsouth-d01-a.res.zgf.yzwsouth.com/fxfkxt/homepage.html?yzw_theme=blueTheme&yzw_font=large&",
    "Origin": "http://babg-appweb-pre.oss-cn-hangzhou-yzwsouth-d01-a.res.zgf.yzwsouth.com",
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
    # "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl9JZCI6IjE0NDk2NTNmODM0OGE1MWUzYTI2NTcxYzVkZjQ2MDljIiwiZXhwIjoxNzc2NTg0NDMwLCJuYmYiOjE3NzY0OTgwMzAsImlhdCI6MTc3NjQ5ODAzMH0.poTpdPNX9JNw03uStdT5lLoYOhNq7TksUkoBZ1ixlE4",
    "token": input_token,
    "routerId": "4"
}
# print(HEADERS)
# 请求体
PAYLOAD = {
    "limit": 15,
    "offset": 0,
    "warningLevel": [],
    "sujectMc": "",
    "cbrMc": "",
    "sjyMc": "",
    "modelMc": "",
    "notice": "",
    "czzt": "2"
}


def call_fxczlb_api():
    """
    调用风险处置列表接口
    """
    print("=" * 80)
    print("调用风险处置列表接口")
    print("=" * 80)
    print(f"接口URL: {API_URL}")
    print("=" * 80)

    try:
        # 发送POST请求
        response = requests.post(
            API_URL,
            headers=HEADERS,
            json=PAYLOAD,
            timeout=30
        )

        # 检查响应状态码
        if response.status_code == 200:
            # 解析响应数据
            data = response.json()
            print("[SUCCESS] 接口调用成功!")
            print(f"[INFO] 响应状态码: {response.status_code}")
            print(f"[INFO] 响应数据: {json.dumps(data, ensure_ascii=False, indent=2)}")

            # 保存响应数据到文件
            with open("fxczlb_response.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print("[INFO] 响应数据已保存到: fxczlb_response.json")

            return data
        else:
            print(f"[ERROR] 接口调用失败，状态码: {response.status_code}")
            print(f"[ERROR] 响应内容: {response.text}")
            return None

    except Exception as e:
        print(f"[ERROR] 调用接口时发生错误: {e}")
        return None


def main():
    """
    主函数
    """
    call_fxczlb_api()


if __name__ == "__main__":
    main()
