# N106: NVIDIA A100 (80GB SXM) 在 LLM 推理负载下的典型整机功耗 P_avg 约为 650W (GPU TDP 400W + 系统开销 ~60

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

NVIDIA A100 (80GB SXM) 在 LLM 推理负载下的典型整机功耗 P_avg 约为 650W (GPU TDP 400W + 系统开销 ~60%)，需对比其 2039 GB/s 带宽带来的高能效优势

## Corrected Claim

NVIDIA A100 (80GB SXM) 在 LLM 推理负载下的典型整机功耗 P_avg 约为 650W (GPU TDP 400W + 系统开销 ~60%)，需对比其 2039 GB/s 带宽带来的高能效优势

## Evidence

先验知识/题面给定，逻辑校验通过：A100 SXM TDP 400W 为官方规格，整机功耗 650W 符合典型服务器配置（CPU+内存+风扇等开销约 60% 合理），带宽 2039 GB/s 为 HBM2e 标准值，数据自洽。
