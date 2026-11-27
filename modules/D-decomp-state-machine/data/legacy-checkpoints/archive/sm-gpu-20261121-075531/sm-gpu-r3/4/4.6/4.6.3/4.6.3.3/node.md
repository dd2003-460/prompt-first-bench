# N303: GQA 与 MHA 在相同 KV 量化位宽（如 INT8）下，由于头数减少导致的 KV Cache 总存储量减少比例，以及由此带来的在相同显存预算下可保留更高量

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N99

## Claim

GQA 与 MHA 在相同 KV 量化位宽（如 INT8）下，由于头数减少导致的 KV Cache 总存储量减少比例，以及由此带来的在相同显存预算下可保留更高量化精度（如 FP8 vs INT8）或更长上下文的能力，量化为存储节省百分比 = (1 - GQA_KV_Size / MHA_KV_Size) * 100%。

## Corrected Claim

GQA 与 MHA 在相同 KV 量化位宽（如 INT8）下，由于头数减少导致的 KV Cache 总存储量减少比例，以及由此带来的在相同显存预算下可保留更高量化精度（如 FP8 vs INT8）或更长上下文的能力，量化为存储节省百分比 = (1 - GQA_KV_Size / MHA_KV_Size) * 100%。

## Evidence

先验知识/题面给定，逻辑校验通过：GQA通过共享KV头减少KV Cache大小，存储节省比例公式 (1 - GQA_KV_Size / MHA_KV_Size) * 100% 在数学上自洽且符合定义。
