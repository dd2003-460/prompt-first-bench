# N268: AMD Radeon PRO W7900 在 ROCm 6.x 环境下运行 Qwen3-27B BF16 的实测吞吐量下限（tokens/s），需修正 N104

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N104

## Claim

AMD Radeon PRO W7900 在 ROCm 6.x 环境下运行 Qwen3-27B BF16 的实测吞吐量下限（tokens/s），需修正 N104 中 '8-12 tokens/s' 的估算；由于 ROCm 对 Qwen3 新架构（如 GQA 优化）的支持滞后，实际性能可能低于理论值，需查找针对 W7900 的 Qwen3-27B 具体基准测试数据，若缺失则标记为 [待核验] 并采用保守值 5 tokens/s 进行 TCO 计算。

## Corrected Claim

AMD Radeon PRO W7900 在 ROCm 6.x 环境下运行 Qwen3-27B BF16 的实测吞吐量具体数值待核验；基于现有部署验证（来源[1]）及保守估计，TCO 计算中暂采用 5 tokens/s 作为下限参考值。

## Evidence

[质询]参考来源[1]仅提供了部署验证和可复现性说明，未包含具体的吞吐量数值（tokens/s），无法直接证实或证伪'5 tokens/s'这一保守下限值；且来源标题提及'Qwen3.8-27B'，与节点中的'Qwen3-27B'存在版本命名差异，需确认是否为同一模型架构。 | 来源[1]确认了AMD Radeon Pro W7900D在ROCm环境下部署Qwen3系列27B模型（BF16）的可行性，但缺乏具体性能基准数据，属于间接支持；经验事实（具体吞吐量）缺直接来源支持，故降级。

## Search Query

AMD Radeon PRO W7900 ROCm Qwen3-27B BF16 inference throughput tokens/s benchmark

## Retrieval Sources

- {'url': 'https://github.com/zhangsongyang/Qwen3.8-27B-ROCm&rut=5ca42f084d924a2c6ed34808a4e37fe8151ced164ab3123f3a66dbe660a1abfe', 'type': 'ddg', 'title': 'GitHub - zhangsongyang/Qwen3.8-27B-ROCm'}
