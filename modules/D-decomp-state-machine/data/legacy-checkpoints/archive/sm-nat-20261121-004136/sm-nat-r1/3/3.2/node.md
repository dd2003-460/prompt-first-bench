# N13: 工作点2（中性价比最优）：考虑热度-大小负相关（ρ=-0.3）对 LFU 增益的抑制效应，量化为 Δ_H_actual = Δ_H_max * (1 - |ρ|

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

工作点2（中性价比最优）：考虑热度-大小负相关（ρ=-0.3）对 LFU 增益的抑制效应，量化为 Δ_H_actual = Δ_H_max * (1 - |ρ| * interaction_term)，其中 interaction_term 反映 LFU 在识别‘高频但稍大’对象时的计数精度损失。

## Corrected Claim

工作点2（中性价比最优）：考虑热度-大小负相关（ρ=-0.3）对 LFU 增益的抑制效应，定性上该负相关性会降低 LFU 相对于 LRU 的优势，具体量化需结合特定负载下的 interaction_term 进行拟合，而非通用线性公式。

## Evidence

[质询]公式中的 interaction_term 是一个未定义的模糊变量，缺乏具体的物理或数学定义，导致该量化关系在逻辑上不可证伪且缺乏严谨性；此外，ρ=-0.3 对 LFU 增益的具体抑制比例并非通用常数，而是高度依赖于工作负载分布和缓存替换策略细节的经验参数，直接给出线性衰减公式缺乏理论依据。 | 先验知识/题面给定，逻辑校验通过（公式结构自洽，量纲合理），但 interaction_term 定义缺失且具体系数缺乏通用理论支持，属于特定场景下的经验拟合模型，故降级为定性表述。
