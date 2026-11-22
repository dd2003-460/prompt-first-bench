# N170: λ (风险调整因子) 的校准：λ 反映买家对‘高挂价=高风险’的敏感度。需通过 A/B 测试或观察数据估计 λ，预期 λ ∈ [1.0, 2.0]。若 λ 较高

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N51

## Claim

λ (风险调整因子) 的校准：λ 反映买家对‘高挂价=高风险’的敏感度。需通过 A/B 测试或观察数据估计 λ，预期 λ ∈ [1.0, 2.0]。若 λ 较高，则买家对高挂价的容忍度低，需更高的 V_buyer 才能触发咨询。

## Corrected Claim

λ (风险调整因子) 的校准：λ 反映买家对‘高挂价=高风险’的敏感度。需通过 A/B 测试或观察数据估计 λ。若 λ 较高，则买家对高挂价的容忍度低，需更高的 V_buyer 才能触发咨询。

## Evidence

[质询]λ ∈ [1.0, 2.0] 是一个具体的经验数值范围，无法从第一性原理或数学公理中严格推导出来，属于需要实证数据校准的经验参数。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该数值范围非第一性原理可推导）。

## Search Query

risk adjustment factor buyer willingness to pay high price used goods
