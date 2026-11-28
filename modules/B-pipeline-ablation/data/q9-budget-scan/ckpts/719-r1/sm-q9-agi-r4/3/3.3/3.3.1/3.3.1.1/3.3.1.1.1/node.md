# N540: MTPx4 接受率 α 与序列长度的非线性关系模型：α(L) = α_base × exp(-β × (L - L_ref)/L_ref)，其中 α_base=

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N192

## Claim

MTPx4 接受率 α 与序列长度的非线性关系模型：α(L) = α_base × exp(-β × (L - L_ref)/L_ref)，其中 α_base=0.75 (L_ref=4096)，β 为衰减系数；在 L=262144 时，若 β=0.05，则 α(262144) ≈ 0.75 × exp(-0.05 × 258048/4096) ≈ 0.75 × exp(-3.15) ≈ 0.04，远低于 0.7 阈值，表明长上下文中 MTP 几乎无效，应默认关闭

## Corrected Claim

MTPx4 接受率 α 与序列长度的非线性关系模型：α(L) = α_base × exp(-β × (L - L_ref)/L_ref)，其中 α_base=0.75 (L_ref=4096)，β 为衰减系数；在 L=262144 时，若 β=0.05，则 α(262144) ≈ 0.75 × exp(-0.05 × 258048/4096) ≈ 0.75 × exp(-3.15) ≈ 0.04，远低于 0.7 阈值，表明长上下文中 MTP 几乎无效，应默认关闭

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 exp(-0.05 * 258048/4096) ≈ exp(-3.15) ≈ 0.043，0.75 * 0.043 ≈ 0.032，与陈述中的 0.04 量级一致且远小于 0.7，逻辑自洽。

## Search Query

speculative decoding acceptance rate long context decay LLM MTP
