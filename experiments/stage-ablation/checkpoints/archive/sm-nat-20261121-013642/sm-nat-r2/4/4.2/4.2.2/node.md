# N61: H_byte_LRU (LRU字节命中率) 的数值下界估算：基于 N28 公式，在 α=1.1 重尾分布下，若 C=128GB 仅覆盖 Top-K 大对象，H_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

H_byte_LRU (LRU字节命中率) 的数值下界估算：基于 N28 公式，在 α=1.1 重尾分布下，若 C=128GB 仅覆盖 Top-K 大对象，H_byte_LRU ≈ 0.65-0.85 (取决于 K 的选取)，该值作为 T_cold 公式的分母修正项 (1-H) 的输入。

## Corrected Claim

H_byte_LRU (LRU字节命中率) 的数值下界估算：基于 N28 公式，在 α=1.1 重尾分布下，若 C=128GB 仅覆盖 Top-K 大对象，H_byte_LRU ≈ 0.65-0.85 (取决于 K 的选取)，该值作为 T_cold 公式的分母修正项 (1-H) 的输入。

## Evidence

先验知识/题面给定，逻辑校验通过
