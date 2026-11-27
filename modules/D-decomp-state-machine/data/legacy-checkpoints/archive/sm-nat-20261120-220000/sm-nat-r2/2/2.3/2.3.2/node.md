# N33: LFU的冷启动惩罚对综合命中率的影响量化为：新对象在最初n_warmup次请求内的命中率下降 P_cold = (n_warmup * f_new) / F_t

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

LFU的冷启动惩罚对综合命中率的影响量化为：新对象在最初n_warmup次请求内的命中率下降 P_cold = (n_warmup * f_new) / F_total，其中n_warmup ≈ 100，f_new为新对象总请求数（假设10%的请求为新对象，即500万次/天），则P_cold ≈ 0.5%，导致LFU的综合提升上限从理论值3.5%降至约3.0%

## Corrected Claim

LFU的冷启动惩罚对综合命中率的影响量化为：新对象在最初n_warmup次请求内的命中率下降 P_cold 取决于新对象在预热期内的未命中比例。若假设新对象在预热期内完全未命中，且新对象占总请求的10%，则理论最大惩罚上限为10%（而非0.5%）。具体数值需结合预热期内的实际访问分布计算，原公式 P_cold = (n_warmup * f_new) / F_total 量纲错误，无法得出0.5%的结论。

## Evidence

[质询]公式 P_cold = (n_warmup * f_new) / F_total 存在严重的量纲和逻辑错误。f_new 是总请求数（500万），n_warmup 是次数（100），分子是 5亿，分母是总请求数（5000万），结果 P_cold 将远大于 1（即 1000%），这与声称的 0.5% 完全矛盾。正确的冷启动惩罚计算通常涉及新对象在预热期内未被缓存命中的概率，而非简单的请求数乘积除以总请求数。 | 逻辑校验失败：公式推导出的数值量级与结论严重不符（计算结果应为1000%而非0.5%），且该公式不符合LFU冷启动惩罚的标准定义。
