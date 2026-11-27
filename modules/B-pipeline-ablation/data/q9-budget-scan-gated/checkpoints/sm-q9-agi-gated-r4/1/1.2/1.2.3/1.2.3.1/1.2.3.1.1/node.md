# N89: N41中给出的衰减公式 acceptance_rate = exp(-λ * log2(seq_len/4096)) 在 seq_len=4096 时预测接受率

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

N41中给出的衰减公式 acceptance_rate = exp(-λ * log2(seq_len/4096)) 在 seq_len=4096 时预测接受率为 exp(0)=100%，这与实际~85%不符。修正公式应为 acceptance_rate = base_alpha * exp(-λ * log2(seq_len/4096))，其中 base_alpha 为短上下文基准接受率（~0.85），λ 需重新拟合。

## Corrected Claim

N41中给出的衰减公式 acceptance_rate = exp(-λ * log2(seq_len/4096)) 在 seq_len=4096 时预测接受率为 exp(0)=100%，这与实际~85%不符。修正公式应为 acceptance_rate = base_alpha * exp(-λ * log2(seq_len/4096))，其中 base_alpha 为短上下文基准接受率（~0.85），λ 需重新拟合。

## Evidence

先验知识/题面给定，逻辑校验通过：原公式在seq_len=4096时确实为exp(0)=1，与85%不符；修正公式引入base_alpha后在seq_len=4096时为base_alpha*exp(0)=0.85，逻辑自洽且符合物理直觉。
