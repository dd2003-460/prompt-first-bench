# N387: 核心区域回源路径的协议栈开销 $L_{protocol}$ 包括 TCP 握手、TLS 握手及 HTTP 头处理，若启用 HTTP/2 多路复用且连接复用，$L

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N144

## Claim

核心区域回源路径的协议栈开销 $L_{protocol}$ 包括 TCP 握手、TLS 握手及 HTTP 头处理，若启用 HTTP/2 多路复用且连接复用，$L_{protocol} \approx 1-3$ms；若每次新建连接，$L_{protocol} \approx 10-20$ms

## Corrected Claim

核心区域回源路径的协议栈开销 $L_{protocol}$ 包括 TCP 握手、TLS 握手及 HTTP 头处理，若启用 HTTP/2 多路复用且连接复用，$L_{protocol} \approx 1-3$ms；若每次新建连接，$L_{protocol} \approx 10-20$ms

## Evidence

先验知识/题面给定，逻辑校验通过
