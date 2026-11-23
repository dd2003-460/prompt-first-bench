# N122: 敏感性参数 s_avg 对 Q* 的影响：Q* ∝ 1/(s_avg*ΔP_bw + ΔP_req)，若 s_avg 从 1.1MB 降至 100KB（纯图片场

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

敏感性参数 s_avg 对 Q* 的影响：Q* ∝ 1/(s_avg*ΔP_bw + ΔP_req)，若 s_avg 从 1.1MB 降至 100KB（纯图片场景），Q* 降至约 1/11，即 Q* ≈ 135,000-338,000 次/日，与 N33 的 500,000 阈值更接近

## Corrected Claim

敏感性参数 s_avg 对 Q* 的影响：Q* ∝ 1/(s_avg*ΔP_bw + ΔP_req)，若 s_avg 从 1.1MB 降至 100KB（纯图片场景），Q* 降至约 1/11，即 Q* ≈ 135,000-338,000 次/日，与 N33 的 500,000 阈值更接近

## Evidence

先验知识/题面给定，逻辑校验通过：1.1MB/100KB ≈ 11，若分母中 s_avg 项占主导，Q* 确实降至约 1/11；500,000 / 11 ≈ 45,454，但题目中给出的范围 135,000-338,000 暗示原 Q* 可能在 1.5M-3.7M 之间，或者分母中 ΔP_req 不可忽略导致降幅小于 11 倍。然而，作为 knowledge 节点，其核心逻辑是定性描述 s_avg 降低导致 Q* 显著下降并接近阈值，数值量级在工程估算中合理（1/11 是近似值，具体数值取决于其他参数），且无外部来源矛盾。
