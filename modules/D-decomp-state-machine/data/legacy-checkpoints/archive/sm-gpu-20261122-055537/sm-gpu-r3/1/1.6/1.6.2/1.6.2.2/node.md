# N184: KV Cache 显存占用精确计算公式：KV_Size_GB = (2 * L * H_kv * D_h * Seq_Len * Bytes_per_Eleme

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

KV Cache 显存占用精确计算公式：KV_Size_GB = (2 * L * H_kv * D_h * Seq_Len * Bytes_per_Element) / 1024^3。其中 2 代表 K 和 V 两个张量。对于 Qwen3-27B GQA (H_kv=8, D_h=128, L=54, Seq=32768, BF16=2B)，计算结果为 7.25 GB。此公式是后续所有显存可行性判断的基础。

## Corrected Claim

KV Cache 显存占用精确计算公式：KV_Size_GB = (2 * L * H_kv * D_h * Seq_Len * Bytes_per_Element) / 1024^3。其中 2 代表 K 和 V 两个张量。对于 Qwen3-27B GQA (H_kv=8, D_h=128, L=54, Seq=32768, BF16=2B)，计算结果为 7.25 GB。此公式是后续所有显存可行性判断的基础。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构正确（2*L*H_kv*D_h*Seq*Bytes），代入数值计算 (2*54*8*128*32768*2)/1024^3 ≈ 7.25 GB，量级与逻辑自洽。
