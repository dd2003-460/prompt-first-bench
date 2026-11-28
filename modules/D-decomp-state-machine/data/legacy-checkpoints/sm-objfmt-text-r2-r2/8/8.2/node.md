# N110: ROCm 环境下 Qwen3-27B 的算子效率因子 η_ops 实测值约为 0.65，定义为实际观测吞吐量与基于硬件峰值和模型算术强度计算的理论上界之比，该系

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

ROCm 环境下 Qwen3-27B 的算子效率因子 η_ops 实测值约为 0.65，定义为实际观测吞吐量与基于硬件峰值和模型算术强度计算的理论上界之比，该系数涵盖了 Flash Attention 和 PagedAttention 的未优化损耗。

## Corrected Claim

ROCm 环境下 Qwen3-27B 的算子效率因子 η_ops 存在未优化损耗，具体实测值需参考详细性能基准测试报告。

## Evidence

[质询]参考来源仅提及部署环境和验证层级，未提供具体的算子效率因子（η_ops）数值或吞吐量对比数据，无法证实0.65这一具体经验参数。 | 经验事实，逻辑自洽但缺来源支持（来源[1]仅确认ROCm环境部署，未包含具体性能指标数值）。

## Search Query

ROCm Qwen 27B inference efficiency factor vs CUDA

## Retrieval Sources

- {'url': 'https://github.com/zhangsongyang/Qwen3.8-27B-ROCm&rut=c511df7f42e751cb871647a74806f8ad55e8ab8682657401941a99ea150548d4', 'type': 'ddg', 'title': 'GitHub - zhangsongyang/Qwen3.8-27B-ROCm'}
