# N361: Intel Gaudi 3 在 FP8 精度下运行 Qwen3-27B 的实际 TPOT 需考虑 MoE 稀疏激活优化：理论 TPOT 为 7.3ms/toke

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N137

## Claim

Intel Gaudi 3 在 FP8 精度下运行 Qwen3-27B 的实际 TPOT 需考虑 MoE 稀疏激活优化：理论 TPOT 为 7.3ms/token (27.18GB / 3.7TB/s)，但 MoE 架构仅激活 3.3B 参数，实际计算量降至 3.3GB，理论 TPOT 可降至 0.89ms/token [待核验]；实际部署需验证 Intel 推理框架 (如 OpenVINO) 是否有效利用 MoE 稀疏性，否则实际 TPOT 将接近理论全参数值 7.3ms/token。

## Corrected Claim

Intel Gaudi 3 在 FP8 精度下运行 Qwen3-27B 的 TPOT 受 MoE 稀疏激活影响。若假设内存带宽为 3.7TB/s 且 MoE 稀疏性可完全转化为内存读取量的线性减少（仅读取激活的 3.3B 参数），理论 TPOT 可从全参数加载的约 7.3ms/token 降至约 0.89ms/token。但实际部署中，TPOT 取决于 Intel 推理框架对 MoE 稀疏性的优化程度及实际内存访问模式，需实测验证。

## Evidence

[质询]该陈述包含具体的硬件性能参数（Gaudi 3 带宽 3.7TB/s）和特定模型（Qwen3-27B）的推理延迟数据，属于经验事实。检索无可用来源，无法验证这些具体数值（如 3.7TB/s 是否为 Gaudi 3 的真实 HBM 带宽，以及 7.3ms 和 0.89ms 的计算是否基于正确的内存访问模式）的准确性。此外，MoE 稀疏激活在推理中的实际加速效果受限于内存带宽瓶颈而非计算量，仅激活 3.3B 参数并不必然意味着内存读取量线性降至 3.3GB（取决于专家路由和缓存策略），因此 0.89ms 的理论值存在逻辑简化风险。 | 经验事实，逻辑自洽但缺来源支持。虽然数学推导（27.18GB/3.7TB/s ≈ 7.3ms）在给定参数下成立，但 Gaudi 3 的具体带宽参数及 Qwen3-27B 的 MoE 推理实际表现无法通过第一性原理严格推出，且无外部来源佐证，故降级。

## Search Query

Intel Gaudi 3 MoE sparse activation inference Qwen3-27B FP8 TPOT benchmark
