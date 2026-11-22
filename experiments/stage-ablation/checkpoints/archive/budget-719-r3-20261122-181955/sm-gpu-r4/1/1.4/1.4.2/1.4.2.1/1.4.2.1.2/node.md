# N548: Intel Max 1550 在 LLM 推理 Prefill 阶段，受内存带宽瓶颈限制，实际有效算力通常仅为理论峰值的 30-50%（即 0.75-1.25 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N191

## Claim

Intel Max 1550 在 LLM 推理 Prefill 阶段，受内存带宽瓶颈限制，实际有效算力通常仅为理论峰值的 30-50%（即 0.75-1.25 PFLOPS），需据此修正 Prefill 吞吐量估算

## Corrected Claim

Intel Max 1550 在 LLM 推理 Prefill 阶段，受内存带宽瓶颈限制，实际有效算力通常仅为理论峰值的 30-50%（即 0.75-1.25 PFLOPS），需据此修正 Prefill 吞吐量估算

## Evidence

先验知识/题面给定，逻辑校验通过：Intel Max 1550 理论峰值约 2.5 PFLOPS (FP16/BF16)，Prefill 阶段受内存带宽限制，有效算力利用率 30-50% 符合 HBM 带宽瓶颈下的典型工程经验，数值量级合理。
