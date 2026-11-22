# N39: N10 中的公式 H_req = Σ_{i=1}^{K} R_i / 5×10^7 计算的是请求命中率（Request Hit Ratio），而非题目要求的字节

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

N10 中的公式 H_req = Σ_{i=1}^{K} R_i / 5×10^7 计算的是请求命中率（Request Hit Ratio），而非题目要求的字节命中率（Byte Hit Ratio），需修正为 H_byte = Σ_{i=1}^{K} (R_i * S_i) / (Σ_{j=1}^{N} R_j * S_j)。

## Corrected Claim

N10 中的公式 H_req = Σ_{i=1}^{K} R_i / 5×10^7 计算的是请求命中率（Request Hit Ratio），而非题目要求的字节命中率（Byte Hit Ratio），需修正为 H_byte = Σ_{i=1}^{K} (R_i * S_i) / (Σ_{j=1}^{N} R_j * S_j)。

## Evidence

先验知识/题面给定，逻辑校验通过：请求命中率（Request Hit Ratio）定义为命中请求数除以总请求数，而字节命中率（Byte Hit Ratio）定义为命中字节数除以总字节数。原公式 H_req = Σ R_i / 5×10^7 若 R_i 为请求数，则计算的是请求维度的比率；修正后的公式 H_byte = Σ (R_i * S_i) / (Σ R_j * S_j) 正确地将权重从请求数转换为字节数（请求数×平均大小），符合字节命中率的定义。
