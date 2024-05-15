# Python 环境配置

当前项目使用的 Python 版本是 3.9, 因为原项目中使用的 `matplotlib` 版本低于3.5, 所以使用了 3.9 版本.

## Poetry

```bash
# 修改清华源, 仅对当前目录有效?
poetry source add tsinghua https://pypi.tuna.tsinghua.edu.cn/simple

rm poetry.lock  # 删除 lock 文件
poetry install  # 安装依赖
```

## Pyenv

```bash
# 安装 python, pyenv 配置有些复杂, 使用 brew 安装
# eg.
brew install python@3.10
```

