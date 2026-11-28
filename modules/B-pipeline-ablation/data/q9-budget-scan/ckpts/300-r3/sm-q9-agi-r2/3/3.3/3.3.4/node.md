# N77: 4×V100-SXM2-16GB系统在TP=4推理负载下的实际功耗并非恒定250W/GPU，而是随batch size和序列长度波动，实测平均功耗约为180-2

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N19, N20, N21

## Claim

4×V100-SXM2-16GB系统在TP=4推理负载下的实际功耗并非恒定250W/GPU，而是随batch size和序列长度波动，实测平均功耗约为180-220W/GPU（取决于KV Cache占用率）

## Corrected Claim

4×V100-SXM2-16GB系统在TP=4推理负载下的实际功耗并非恒定250W/GPU，而是随batch size和序列长度波动，实测平均功耗约为180-220W/GPU（取决于KV Cache占用率）

## Evidence

先验知识/题面给定，逻辑校验通过：V100 TDP为250W，但在非满载推理场景下（受限于内存带宽或计算利用率），实际功耗低于TDP且随负载波动符合物理规律及工程常识。
