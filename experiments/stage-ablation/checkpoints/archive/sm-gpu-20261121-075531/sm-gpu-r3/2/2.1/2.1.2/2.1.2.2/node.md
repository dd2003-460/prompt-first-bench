# N170: H100 80GB 在 W4 量化下，拥有原生 FP8/INT4 Tensor Core 加速，计算效率高于 A100；理论 TPS ≈ 3350 / 16.5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

H100 80GB 在 W4 量化下，拥有原生 FP8/INT4 Tensor Core 加速，计算效率高于 A100；理论 TPS ≈ 3350 / 16.5 ≈ 203 TPS；实际受 W4 解码单元利用率限制，实测可能在 150-180 TPS 区间；H100 的优势在于高带宽和高能效，但需对比其每 Token 电力成本与消费级卡的差异。

## Corrected Claim

H100 80GB 在 W4 量化下，拥有原生 FP8/INT4 Tensor Core 加速，计算效率高于 A100；理论 TPS ≈ 3350 / 16.5 ≈ 203 TPS；实际受 W4 解码单元利用率限制，实测可能在 150-180 TPS 区间；H100 的优势在于高带宽和高能效，但需对比其每 Token 电力成本与消费级卡的差异。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 确实支持 FP8/INT4 Tensor Core 且带宽/能效优于 A100；TPS 计算逻辑自洽（3350/16.5≈203），实测区间符合工程经验。

## Search Query

H100 W4 quantized LLM inference throughput native tensor core acceleration efficiency
