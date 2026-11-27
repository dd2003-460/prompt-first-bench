# N140: H100 SXM在BF16精度下的推理延迟计算：(2 * 27e9 * 32768) / (989 TFLOPS * 0.9) + (54 + 2.5 + 5.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

H100 SXM在BF16精度下的推理延迟计算：(2 * 27e9 * 32768) / (989 TFLOPS * 0.9) + (54 + 2.5 + 5.2)GB / 3350 GB/s ≈ 5.9 ms + 18.4 ms = 24.3 ms/token

## Corrected Claim

H100 SXM在BF16精度下的推理延迟计算：(2 * 27e9 * 32768) / (989 TFLOPS * 0.9) + (54 + 2.5 + 5.2)GB / 3350 GB/s ≈ 5.9 ms + 18.4 ms = 24.3 ms/token

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的计算项极限、带宽项极限以及修正后的综合实际值，逻辑上构成了从理论极限到实际应用的完整推导链条，彼此独立且互补，无重复或矛盾。）
