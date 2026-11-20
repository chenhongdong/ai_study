# 安装快捷镜像
## Windows系统，在CMD运行如下命令：
```
setx UV_DEFAULT_INDEX "https://pypi.tuna.tsinghua.edu.cn/simple"
```
### macOs或Linux系统：
```
echo 'export UV_DEFAULT_INDEX=https://pypi.tuna.tsinghua.edu.cn/simple' >> ~/.zshrc && source ~/.zshrc
```



# 命令行启动python项目
`uv run python -m app.main`