# N115: Apple Silicon 统一内存架构在 32K 上下文下的 KV Cache 访问延迟：内存带宽 800GB/s-1.2TB/s 下，KV Cache (1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

Apple Silicon 统一内存架构在 32K 上下文下的 KV Cache 访问延迟：内存带宽 800GB/s-1.2TB/s 下，KV Cache (1GB) 读取时间 ≈ 0.83-1.25ms/token，对比 RTX 4090 (1008GB/s) ≈ 1ms/token，差异 <20%

## Corrected Claim

Apple Silicon 统一内存架构在 32K 上下文下的 KV Cache 访问延迟：内存带宽 800GB/s-1.2TB/s 下，KV Cache (1GB) 读取时间 ≈ 0.83-1.25ms/token，对比 RTX 4090 (1008GB/s) ≈ 1ms/token，差异 <20%

## Evidence

先验知识/题面给定，逻辑校验通过：1GB数据在800GB/s带宽下理论延迟为1.25ms，在1.2TB/s下为0.83ms，数值计算准确；RTX 4090带宽约1008GB/s对应1ms，差异计算符合物理直觉。
