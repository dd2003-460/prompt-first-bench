# N290: PagedAttention 机制下，KV Cache 的读取并非连续大块，而是分散的页表查找，实际有效带宽利用率可能下降 10-20% [待核验]，需引入效率

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N95

## Claim

PagedAttention 机制下，KV Cache 的读取并非连续大块，而是分散的页表查找，实际有效带宽利用率可能下降 10-20% [待核验]，需引入效率因子 η_page ≈ 0.8-0.9 修正理论 ITL，使得实际 ITL 比理论值高 10-25%。

## Corrected Claim

PagedAttention 机制下，KV Cache 的读取并非连续大块，而是分散的页表查找，实际有效带宽利用率可能下降 10-20% [待核验]，需引入效率因子 η_page ≈ 0.8-0.9 修正理论 ITL，使得实际 ITL 比理论值高 10-25%。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

PagedAttention memory access efficiency overhead inference
