# N77: W4量化下的KV Cache精度策略：若KV Cache保持FP16，则占用10.7GB；若KV Cache量化为INT8，则占用5.35GB，总显存需求在FP

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

W4量化下的KV Cache精度策略：若KV Cache保持FP16，则占用10.7GB；若KV Cache量化为INT8，则占用5.35GB，总显存需求在FP16 KV下为28.2GB（13.5+10.7+4.0），在INT8 KV下为22.85GB（13.5+5.35+4.0）

## Corrected Claim

W4量化下的KV Cache精度策略：若KV Cache保持FP16，则占用10.7GB；若KV Cache量化为INT8，则占用5.35GB，总显存需求在FP16 KV下为28.2GB（13.5+10.7+4.0），在INT8 KV下为22.85GB（13.5+5.35+4.0）

## Evidence

父节点级核验未通过：有冗余（子节点分别描述了FP16和INT8两种KV Cache量化配置下的显存占用及可行性，二者互斥且无重叠（正交）；覆盖了父节点中提到的两种主要量化策略及其对应的总显存需求（完备）。然而，两个子节点的结构高度相似，仅数值不同，且都包含‘可行性分析’这一相同逻辑分支，属于同一参数（KV量化位宽）的不同取值，存在结构性冗余。）
