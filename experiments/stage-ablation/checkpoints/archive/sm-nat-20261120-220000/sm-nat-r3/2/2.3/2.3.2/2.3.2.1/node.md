# N95: LFU冷启动惩罚的精确公式修正：P_cold = (N_new * S_avg_new * f_miss_warmup) / B_total，其中N_new为日

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N33

## Claim

LFU冷启动惩罚的精确公式修正：P_cold = (N_new * S_avg_new * f_miss_warmup) / B_total，其中N_new为日均新对象数，f_miss_warmup为新对象在预热期(n_warmup=100次访问)内的未命中率，若假设新对象前100次访问中80%未命中，则P_cold ≈ 0.8 * (N_new * S_avg_new) / B_total。

## Corrected Claim

LFU冷启动惩罚的精确公式修正：P_cold = (N_new * S_avg_new * f_miss_warmup) / B_total，其中N_new为日均新对象数，f_miss_warmup为新对象在预热期(n_warmup=100次访问)内的未命中率，若假设新对象前100次访问中80%未命中，则P_cold ≈ 0.8 * (N_new * S_avg_new) / B_total。

## Evidence

先验知识/题面给定，逻辑校验通过
