import os

from pyngrok import ngrok
with open(f"{os.path.dirname(os.path.abspath(__file__))}/token", "r") as f:
    token = f.read()
ngrok.set_auth_token(token)
https_tunnel = ngrok.connect(addr=":80", proto="http", name="LanAn")
print("Public URL:", https_tunnel)

# 保持运行，直到手动终止
try:
    while True:
        pass
except KeyboardInterrupt:
    # 在 Ctrl+C 中断时断开隧道并停止 ngrok 进程
    ngrok.disconnect(str(https_tunnel))
    ngrok.kill()
