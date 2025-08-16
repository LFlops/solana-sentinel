# --- 第一阶段：构建器 (Builder) ---
# 这个阶段负责编译和安装所有依赖
FROM python:3.11-slim AS builder

# 1. 安装 uv
RUN pip install uv

# 2. 创建并指定一个虚拟环境
# 这是在容器内管理依赖的最佳方式
ENV VENV_PATH=/opt/venv
RUN python -m venv $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"

# 3. 拷贝依赖文件并安装
WORKDIR /app
COPY pyproject.toml .
# --system 指示 uv 安装到当前激活的虚拟环境中
RUN uv pip install --system --no-cache .


# --- 第二阶段：最终镜像 (Final Image) ---
# 这个阶段只包含运行应用所需的东西
FROM python:3.11-slim

# 创建一个非 root 用户来运行应用，更安全
RUN adduser --disabled-password --gecos '' api
USER api

WORKDIR /app

# 从构建器阶段拷贝已经安装好依赖的虚拟环境
# 这是多阶段构建最核心的步骤！
COPY --from=builder /opt/venv /opt/venv

# 拷贝你的应用代码，并设置正确的用户权限
COPY --chown=api:api . .

# 让 shell 可以找到虚拟环境中的可执行文件
ENV PATH="/opt/venv/bin:$PATH"

# 暴露端口
EXPOSE 8000

# 容器启动时运行的命令
MD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000", "main:app"]