# N155: 综合 p_base 的加权计算公式为 p_base_weighted = Σ(w_i * p_base_i)，其中 w_i 为任务类型 i 在研究循环中的出现频

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N53

## Claim

综合 p_base 的加权计算公式为 p_base_weighted = Σ(w_i * p_base_i)，其中 w_i 为任务类型 i 在研究循环中的出现频率（需从日志统计，如数学 30%, 检索 50%, 创意 20%），若 w_i 未知，则采用均匀权重 1/3，计算得 p_base_weighted ≈ 0.567，该值用于代入 IR(K) 公式。

## Corrected Claim

综合 p_base 的加权计算公式为 p_base_weighted = Σ(w_i * p_base_i)，其中 w_i 为任务类型 i 在研究循环中的出现频率（需从日志统计，如数学 30%, 检索 50%, 创意 20%），若 w_i 未知，则采用均匀权重 1/3，计算得 p_base_weighted ≈ 0.567，该值用于代入 IR(K) 公式。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均公式定义正确，数值计算 (0.3*0.5 + 0.5*0.6 + 0.2*0.58 = 0.567) 符合算术逻辑，且作为模型内部参数推导过程自洽。
