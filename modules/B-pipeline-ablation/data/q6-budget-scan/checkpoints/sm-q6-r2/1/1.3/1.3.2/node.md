# N44: 单边缘节点服务速率 μ 的估算：基于标准 10Gbps 上行带宽和平均对象大小 1MB，理论最大吞吐量 μ_max ≈ 10Gbps / (1MB × 8) ≈

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N8

## Claim

单边缘节点服务速率 μ 的估算：基于标准 10Gbps 上行带宽和平均对象大小 1MB，理论最大吞吐量 μ_max ≈ 10Gbps / (1MB × 8) ≈ 1250 req/s；考虑 CPU 处理开销和并发连接限制，实际 μ ≈ 500-800 req/s/节点，需根据硬件规格（如 CPU 核心数、内存）进一步修正。

## Corrected Claim

单边缘节点服务速率 μ 的估算：基于标准 10Gbps 上行带宽和平均对象大小 1MB，理论最大吞吐量 μ_max ≈ 10Gbps / (1MB × 8) ≈ 1250 req/s；考虑 CPU 处理开销和并发连接限制，实际 μ ≈ 500-800 req/s/节点，需根据硬件规格（如 CPU 核心数、内存）进一步修正。

## Evidence

先验知识/题面给定，逻辑校验通过：10Gbps带宽除以8bit/Byte和1MB/对象，理论上限确为1250 req/s，考虑系统开销后500-800 req/s符合工程直觉。
