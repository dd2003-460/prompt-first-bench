# N192: T_acc 阈值 0.85 的统计依据：假设任务成功概率 p 服从 Beta 分布，0.85 对应 95% 置信区间下界；若需将假阳性率（误判为高置信度）控制在

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N68

## Claim

T_acc 阈值 0.85 的统计依据：假设任务成功概率 p 服从 Beta 分布，0.85 对应 95% 置信区间下界；若需将假阳性率（误判为高置信度）控制在 5% 以内，需基于历史任务成功率 S_hist 校准，公式为 Threshold = S_hist * (1 + Z_alpha * StdErr)，其中 Z_alpha=1.645。

## Corrected Claim

T_acc 阈值 0.85 的设定通常基于历史任务成功率的统计校准，例如采用均值加上一定倍数标准误的形式（如 Threshold = S_hist + k * StdErr），具体系数 k 和阈值需根据实际数据分布确定，而非固定由 Beta 分布 95% 下界唯一决定。

## Evidence

[质询]该陈述包含具体的经验参数（阈值0.85、Z_alpha=1.645）和特定的校准公式，属于经验事实而非第一性原理可推导内容；且参考来源仅讨论自一致性校准，未提供该特定Beta分布假设下的阈值推导或公式支持。 | 逻辑自洽（Z_alpha=1.645对应单侧95%置信度，公式结构符合均值加标准误的常见校准形式），但参考来源[1]主题相关却未直接支持该具体公式和数值，属经验事实缺来源直接支持。

## Search Query

self-consistency threshold calibration beta distribution LLM confidence

## Retrieval Sources

- {'url': 'https://arxiv.org/abs/2403.09849&rut=110a96fafa03584ca47247149a452532417183119cf0ff4dc6d346b9c23ba8a9', 'type': 'ddg', 'title': 'Self-Consistency Boosts Calibration for Math Reasoning'}
