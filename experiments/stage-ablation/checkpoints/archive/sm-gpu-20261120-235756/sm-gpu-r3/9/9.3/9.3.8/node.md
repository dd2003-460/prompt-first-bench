# N347: MI300X 在 BF16 下运行 Qwen3-27B 的内存带宽瓶颈分析：HBM3 带宽 5.3 TB/s 在 MoE 路由阶段需频繁加载非连续 Expert

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N129, N130, N131

## Claim

MI300X 在 BF16 下运行 Qwen3-27B 的内存带宽瓶颈分析：HBM3 带宽 5.3 TB/s 在 MoE 路由阶段需频繁加载非连续 Expert 权重，若未使用 L2 Cache 优化，有效带宽利用率仅 60-70%，导致实际 TPOT 比纯带宽理论值（10.23ms）增加 30-40%，即实际 TPOT 约为 13-14ms/token。

## Corrected Claim

MI300X 在 BF16 下运行 Qwen3-27B 时，HBM3 带宽（5.3 TB/s）在 MoE 路由阶段因需加载非连续 Expert 权重而成为瓶颈。若缺乏有效的 L2 Cache 或内存访问优化，有效带宽利用率会显著低于理论峰值，导致实际 TPOT 高于纯带宽理论值（10.23ms），具体增加幅度取决于优化策略，通常可能在 13-14ms/token 左右。

## Evidence

[质询]该陈述包含具体的经验性工程参数（如60-70%的有效带宽利用率、30-40%的TPOT增加幅度），这些数值并非MI300X或Qwen3-27B的固定物理常数，而是高度依赖于具体的MoE架构设计（如Expert数量、激活比例）、软件栈优化（如AllReduce实现、Kernel融合）以及硬件微架构细节。在没有具体基准测试数据支持的情况下，断言一个固定的百分比范围缺乏严谨性，且不同实现下波动可能很大。 | source=knowledge，逻辑自洽（带宽瓶颈导致延迟增加符合直觉），但具体数值（60-70%利用率等）属于经验事实，缺乏来源直接支持，依据经验事实排除条款降级。

## Search Query

MI300X HBM3 effective bandwidth utilization MoE inference
