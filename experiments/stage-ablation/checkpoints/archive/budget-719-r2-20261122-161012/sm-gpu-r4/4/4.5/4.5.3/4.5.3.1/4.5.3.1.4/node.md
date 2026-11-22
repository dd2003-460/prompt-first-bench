# N574: 在 Decode 阶段（访存密集型），M3 Ultra 与 M2 Ultra 的内存带宽均为 800 GB/s，因此两者的单 Token 生成延迟（T_deco

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N238, N239, N240

## Claim

在 Decode 阶段（访存密集型），M3 Ultra 与 M2 Ultra 的内存带宽均为 800 GB/s，因此两者的单 Token 生成延迟（T_decode）理论值相同；M3 Ultra 仅在 Prefill 阶段（首字延迟 TTFT）具有优势，若用户场景以长文本生成（Decode 占比 > 80%）为主，M3 Ultra 相比 M2 Ultra 的性价比提升微乎其微，甚至可能因价格溢价而不划算。

## Corrected Claim

在 Decode 阶段（访存密集型），M3 Ultra 与 M2 Ultra 的内存带宽均为 800 GB/s，因此两者的单 Token 生成延迟（T_decode）理论值相同；M3 Ultra 仅在 Prefill 阶段（首字延迟 TTFT）具有优势，若用户场景以长文本生成（Decode 占比 > 80%）为主，M3 Ultra 相比 M2 Ultra 的性价比提升微乎其微，甚至可能因价格溢价而不划算。

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra与M3 Ultra内存带宽均为800GB/s，Decode阶段为访存密集型，带宽相同则理论延迟相同；Prefill阶段M3 Ultra算力更强故有优势；长文本生成Decode占比高，故M3 Ultra性价比提升有限。

## Search Query

Apple M3 Ultra memory bandwidth same as M2 Ultra 800GB/s
