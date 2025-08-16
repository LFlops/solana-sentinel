# ---- Builder Stage ----
# 使用官方 Rust 镜像作为构建环境
FROM rust:1-slim as builder

WORKDIR /usr/app

# 复制 Cargo 配置文件并仅安装依赖，以利用 Docker 的层缓存
COPY ./listener/Cargo.toml ./listener/Cargo.lock ./
RUN mkdir ./src && \
    echo "fn main() {}" >./src/main.rs && \
    cargo build --release && \
    rm -rf./src

# 复制完整的源代码并构建应用
COPY ./listener/src ./src
RUN cargo build --release

# ---- Final Stage ----
# 使用一个非常小的基础镜像
FROM debian:12-slim

# 从构建阶段复制编译好的二进制文件
COPY --from=builder /usr/app/target/release/listener /usr/local/bin/listener

# 设置启动命令
CMD ["listener"]