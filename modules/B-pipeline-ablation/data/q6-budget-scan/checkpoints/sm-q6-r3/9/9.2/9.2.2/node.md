# N364: 缓存可容纳对象数 K 的计算：$K = \lfloor C_{cache} / s_{avg} \rfloor$，其中 $C_{cache}$ 为单 POP 点

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N136

## Claim

缓存可容纳对象数 K 的计算：$K = \lfloor C_{cache} / s_{avg} \rfloor$，其中 $C_{cache}$ 为单 POP 点或全局缓存总容量（如 1TB），$s_{avg}$ 为加权平均对象大小（1.5MB）；例如 $C_{cache}=1\text{TB}$ 时，$K \approx 700,000$。

## Corrected Claim

缓存可容纳对象数 K 的计算：$K = \lfloor C_{cache} / s_{avg} \rfloor$，其中 $C_{cache}$ 为单 POP 点或全局缓存总容量（如 1TB），$s_{avg}$ 为加权平均对象大小（1.5MB）；例如 $C_{cache}=1\text{TB}$ 时，$K \approx 700,000$。

## Evidence

先验知识/题面给定，逻辑校验通过：1TB / 1.5MB ≈ 700,000，量级与计算逻辑自洽。
