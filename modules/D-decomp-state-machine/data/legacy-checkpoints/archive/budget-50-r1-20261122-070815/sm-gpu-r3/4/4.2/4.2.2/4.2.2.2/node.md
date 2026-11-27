# N306: A100 80GB SXM 方案的整机 P_avg 估算为 500W-650W，其能效优势需通过对比 (A100_Tokens/s / A100_Watts) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N106

## Claim

A100 80GB SXM 方案的整机 P_avg 估算为 500W-650W，其能效优势需通过对比 (A100_Tokens/s / A100_Watts) 与 (4090_Tokens/s / 4090_Watts) 的比值来量化，而非仅看绝对功耗

## Corrected Claim

A100 80GB SXM 方案的整机 P_avg 估算为 500W-650W，其能效优势需通过对比 (A100_Tokens/s / A100_Watts) 与 (4090_Tokens/s / 4090_Watts) 的比值来量化，而非仅看绝对功耗

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB SXM 整机功耗 500-650W 符合工程常识（GPU TDP 400W + 系统开销），且能效比（Tokens/s/W）确实是衡量不同功耗平台性能优势的正确指标，逻辑自洽。

## Search Query

A100 vs RTX 4090 energy efficiency tokens per watt LLM inference
