# N125: FP8 量化在极端长上下文 (≥32K) 下的累积误差边界：虽然单 token PPL 增加 <1%，但在 32K 上下文的自回归生成中，误差可能累积导致 'L

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

FP8 量化在极端长上下文 (≥32K) 下的累积误差边界：虽然单 token PPL 增加 <1%，但在 32K 上下文的自回归生成中，误差可能累积导致 'Lost in the Middle' 现象加剧，需验证 FP8 模型在 32K 上下文下的 RULER 或 LongBench 得分是否低于 BF16 模型 >2%。

## Corrected Claim

FP8 量化在极端长上下文 (≥32K) 下可能存在累积误差，需验证其对 'Lost in the Middle' 现象及长上下文基准测试（如 RULER/LongBench）性能的具体影响，具体误差边界需通过实验确定。

## Evidence

[质询]该陈述包含具体的经验性阈值（如'PPL增加<1%'、'得分低于BF16 >2%'）和特定现象的因果关联（FP8导致Lost in the Middle加剧），这些属于经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

FP8 quantization long context 32k token cumulative error RULER LongBench performance degradation
