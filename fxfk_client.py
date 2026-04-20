"""
风险处置系统API客户端
包含两个接口：
1. fxczlb - 风险处置列表
2. save - 风险处置保存
"""

import requests
import json


imput_token = input("请输入token: ")

# 基础配置
BASE_URL = "http://192.10.91.36:8081"

# 请求头
HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Referer": "http://babg-appweb-pre.oss-cn-hangzhou-yzwsouth-d01-a.res.zgf.yzwsouth.com/fxfkxt/homepage.html?yzw_theme=blueTheme&yzw_font=large&",
    "Origin": "http://babg-appweb-pre.oss-cn-hangzhou-yzwsouth-d01-a.res.zgf.yzwsouth.com",
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
    "token": imput_token,
    "routerId": "4"
}


class FxfkApiClient:
    """风险处置系统API客户端"""
    
    def __init__(self):
        """初始化客户端"""
        self.base_url = BASE_URL
        self.headers = HEADERS
    
    def call_fxczlb(self, limit=15, offset=0, warning_level=None, suject_mc="", 
                    cbr_mc="", sjy_mc="", model_mc="", notice="", czzt="2"):
        """
        调用风险处置列表接口
        
        Args:
            limit: 每页数量
            offset: 偏移量
            warning_level: 预警级别
            suject_mc: 主体名称
            cbr_mc: 承办人名称
            sjy_mc: 审计员名称
            model_mc: 模型名称
            notice: 通知
            czzt: 处置状态
        
        Returns:
            响应数据
        """
        url = f"{self.base_url}/fxfk/api/v1/fxcz/fxczlb"
        
        payload = {
            "limit": limit,
            "offset": offset,
            "warningLevel": warning_level or [],
            "sujectMc": suject_mc,
            "cbrMc": cbr_mc,
            "sjyMc": sjy_mc,
            "modelMc": model_mc,
            "notice": notice,
            "czzt": czzt
        }
        
        print("=" * 80)
        print("调用风险处置列表接口")
        print("=" * 80)
        print(f"接口URL: {url}")
        print(f"请求参数: {json.dumps(payload, ensure_ascii=False, indent=2)}")
        print("=" * 80)
        
        try:
            # 发送POST请求
            response = requests.post(
                url,
                headers=self.headers,
                json=payload,
                timeout=30,
                proxies={}  # 禁用代理
            )
            
            # 检查响应状态码
            if response.status_code == 200:
                # 解析响应数据
                data = response.json()
                print("[SUCCESS] 接口调用成功!")
                print(f"[INFO] 响应状态码: {response.status_code}")
                print(f"[INFO] 响应数据: {json.dumps(data, ensure_ascii=False, indent=2)}")
                
                return data
            else:
                print(f"[ERROR] 接口调用失败，状态码: {response.status_code}")
                print(f"[ERROR] 响应内容: {response.text}")
                return None
                
        except Exception as e:
            print(f"[ERROR] 调用接口时发生错误: {e}")
            print(f"[ERROR] 错误类型: {type(e).__name__}")
            return None
    
    def call_save(self, subject_bh, dispose_json):
        """
        调用风险处置保存接口
        
        Args:
            subject_bh: 主体编号
            dispose_json: 处置JSON
        
        Returns:
            响应数据
        """
        url = f"{self.base_url}/fxfk/api/v1/fxcz/ save"
        
        payload = {
            "subjectBh": subject_bh,
            "disposeJson": dispose_json
        }
        
        print("=" * 80)
        print("调用风险处置保存接口")
        print("=" * 80)
        print(f"接口URL: {url}")
        print(f"请求参数: {json.dumps(payload, ensure_ascii=False, indent=2)}")
        print("=" * 80)
        
        try:
            # 发送POST请求
            response = requests.post(
                url,
                headers=self.headers,
                json=payload,
                timeout=30,
                proxies={}  # 禁用代理
            )
            
            # 检查响应状态码
            if response.status_code == 200:
                # 解析响应数据
                data = response.json()
                print("[SUCCESS] 接口调用成功!")
                print(f"[INFO] 响应状态码: {response.status_code}")
                print(f"[INFO] 响应数据: {json.dumps(data, ensure_ascii=False, indent=2)}")
                
                return data
            else:
                print(f"[ERROR] 接口调用失败，状态码: {response.status_code}")
                print(f"[ERROR] 响应内容: {response.text}")
                return None
                
        except Exception as e:
            print(f"[ERROR] 调用接口时发生错误: {e}")
            print(f"[ERROR] 错误类型: {type(e).__name__}")
            return None


def main():
    """
    主函数
    """
    # 创建API客户端
    client = FxfkApiClient()
    
    print("=" * 80)
    print("风险处置系统API客户端")
    print("=" * 80)
    
    # 自动测试两个接口
    print("1. 测试风险处置列表接口")
    fxczlbList = client.call_fxczlb()['data']
    print(f"风险处置列表数量: {len(fxczlbList)}")
    

    print("\n2. 测试风险处置保存接口")
    for fxcz in fxczlbList:
        subject_bh = fxcz['subjectBh']
        dispose_json = fxcz['disposeJson']
        client.call_save(subject_bh, dispose_json)
    
    print("\n" + "=" * 80)
    print("测试完成")
    print("=" * 80)


if __name__ == "__main__":
    main()
