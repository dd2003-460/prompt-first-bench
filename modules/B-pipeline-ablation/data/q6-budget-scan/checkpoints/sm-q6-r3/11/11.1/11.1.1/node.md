# N381: 边缘节点处理延迟 $L_{processing}$ 的量化估算：包括 DNS 解析、TLS 握手、HTTP 请求处理及缓存查找；典型值为 $5-10 \text

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N143

## Claim

边缘节点处理延迟 $L_{processing}$ 的量化估算：包括 DNS 解析、TLS 握手、HTTP 请求处理及缓存查找；典型值为 $5-10 \text{ ms}$，其中 TLS 握手占 $3-5 \text{ ms}$（若启用会话复用则降至 $1-2 \text{ ms}$），缓存查找占 $1-2 \text{ ms}$，HTTP 处理占 $1-2 \text{ ms}$。

## Corrected Claim

边缘节点处理延迟 $L_{processing}$ 的量化估算：包括 DNS 解析、TLS 握手、HTTP 请求处理及缓存查找；典型值为 $5-10 \text{ ms}$，其中 TLS 握手占 $3-5 \text{ ms}$（若启用会话复用则降至 $1-2 \text{ ms}$），缓存查找占 $1-2 \text{ ms}$，HTTP 处理占 $1-2 \text{ ms}$。

## Evidence

先验知识/题面给定，逻辑校验通过
