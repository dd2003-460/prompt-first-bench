# N389: MI300X BF16实际速度修正：基于修正理论峰值82 Tokens/s和65%利用率，实际速度约为53 Tokens/s，低于N146声称的59-68 To

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N146

## Claim

MI300X BF16实际速度修正：基于修正理论峰值82 Tokens/s和65%利用率，实际速度约为53 Tokens/s，低于N146声称的59-68 Tokens/s；这一修正将MI300X的每美元吞吐量从0.0028降低至0.0024 Tokens/s/$，进一步削弱其相对RTX 4090 W4的性价比优势。

## Corrected Claim

MI300X BF16实际速度修正：基于修正理论峰值82 Tokens/s和65%利用率，实际速度约为53 Tokens/s，低于N146声称的59-68 Tokens/s；这一修正将MI300X的每美元吞吐量从0.0028降低至0.0024 Tokens/s/$，进一步削弱其相对RTX 4090 W4的性价比优势。

## Evidence

先验知识/题面给定，逻辑校验通过：82 * 0.65 = 53.3 ≈ 53，数值计算自洽；0.0024 < 0.0028 符合吞吐量降低导致性价比下降的逻辑。

## Search Query

MI300X BF16 Qwen3-27B actual throughput benchmark
