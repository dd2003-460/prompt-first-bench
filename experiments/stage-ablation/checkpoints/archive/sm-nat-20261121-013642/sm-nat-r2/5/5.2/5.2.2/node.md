# N72: 工作点2（热度分布）：Pareto(β=0.9) 的归一化常数 Z_freq 使得 Σr_i = 50,000,000/天，最小请求率 r_min=0.1/天，

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

工作点2（热度分布）：Pareto(β=0.9) 的归一化常数 Z_freq 使得 Σr_i = 50,000,000/天，最小请求率 r_min=0.1/天，第 k 热对象的请求频率 r_k = r_min * (N/k)^β，需验证长尾收敛性

## Corrected Claim

工作点2（热度分布）：Pareto(β=0.9) 的归一化常数 Z_freq 使得 Σr_i = 50,000,000/天，最小请求率 r_min=0.1/天，第 k 热对象的请求频率 r_k = r_min * (N/k)^β，需验证长尾收敛性

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布（Zipf-like）在β>0时具有收敛性，归一化常数Z_freq的存在性由积分收敛性保证，数学定义自洽。
