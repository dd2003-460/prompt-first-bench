# N383: Apple M2 Ultra 的 INT8 推理软件栈成熟度：MLX 框架对 M2 Ultra 的 INT8 推理支持尚不完善，实际吞吐量可能低于理论值的 85

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N146, N147, N149

## Claim

Apple M2 Ultra 的 INT8 推理软件栈成熟度：MLX 框架对 M2 Ultra 的 INT8 推理支持尚不完善，实际吞吐量可能低于理论值的 85%。实测数据表明，M2 Ultra 在 INT8 下 Decode 吞吐量约为 20-25 tokens/s（[待核验]），低于理论计算的 25.2 tokens/s，主要瓶颈在于内存控制器调度和指令集优化不足。

## Corrected Claim

Apple M2 Ultra 的 INT8 推理软件栈（如 MLX）成熟度仍在提升中，实际吞吐量通常低于理论峰值，具体数值受模型规模及软件优化程度影响较大。

## Evidence

[质询]具体数值（20-25 tokens/s）和性能损耗比例（85%）属于特定硬件与软件版本的经验性实测数据，无法从第一性原理推导，且缺乏来源支持，存在因测试环境、模型大小不同导致数值偏差的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Apple M2 Ultra MLX INT8 inference benchmark tokens per second
