# frp_ngrok

使用 “ngrok” 实现内网穿透

## 注册

通过[ngrok设置与安装](https://dashboard.ngrok.com/get-started/setup)注册ngrok账号，不能使用QQ邮箱

按照界面指示安装ngrok，并配置环境

## 使用

配置完**ngrok.yml**[配置文件](https://ngrok.com/docs/agent/config/)后可以直接在命令行使用

```bash
ngrok <proto> <addr>
```

proto：tcp或者http

addr：[host][:[port]]/[url]可以只输入host，如果是https，port默认443；如果是http，port默认80；也可以只输入port
