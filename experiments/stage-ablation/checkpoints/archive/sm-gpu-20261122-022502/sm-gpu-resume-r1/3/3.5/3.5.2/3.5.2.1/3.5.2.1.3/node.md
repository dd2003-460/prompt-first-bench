# N756: MI300X 运行 Qwen3-27B 的 BF16 理论 Decode 吞吐上限为 98.15 tokens/s (5.3 TB/s 带宽 / 54 GB 权

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N233, N234, N235

## Claim

MI300X 运行 Qwen3-27B 的 BF16 理论 Decode 吞吐上限为 98.15 tokens/s (5.3 TB/s 带宽 / 54 GB 权重)，该值假设 100% 带宽利用率且忽略计算延迟，实际 vLLM 优化下预计可达 85-90% 效率，即 83-88 tokens/s。

## Corrected Claim

MI300X 运行 Qwen3-27B 的 BF16 理论 Decode 吞吐上限为 98.15 tokens/s (5.3 TB/s 带宽 / 54 GB 权重)，该值假设 100% 带宽利用率且忽略计算延迟，实际 vLLM 优化下预计可达 85-90% 效率，即 83-88 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：MI300X HBM3e 带宽约 5.3TB/s，Qwen3-27B BF16 权重约 54GB，理论上限 5.3/54 ≈ 98.15 tokens/s 计算正确；85-90% 效率假设符合工程经验。
