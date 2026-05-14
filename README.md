# LangBot Weather Plugin

LangBot 天气查询工具插件，支持查询任意城市的实时天气信息。

## 功能

- 输入城市名称，返回实时天气状况
- 输出温度、湿度、风速、日出/日落时间

## 技术栈

- Python / LangBot Plugin SDK
- wttr.in 公开天气 API
- httpx 异步 HTTP 客户端

## 安装

将插件目录放入 LangBot 的插件路径下，重启即可。

## 使用

在对话中向 Bot 发送城市名称，插件会自动调用天气查询工具。

## 项目结构

```
├── main.py                          # 插件入口
├── manifest.yaml                    # 插件元数据
├── components/
│   └── tools/
│       ├── get_weather.py           # 天气查询工具实现
│       └── get_weather.yaml         # 工具参数定义
└── requirements.txt                 # 依赖
```
