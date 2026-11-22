# N60: 在写回（Write-Back）模式下，有效命中率折损因子 $D_{WB}$ 由脏页淘汰概率决定：$D_{WB} = 1 - P_{evict\_dirty}$，

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N18

## Claim

在写回（Write-Back）模式下，有效命中率折损因子 $D_{WB}$ 由脏页淘汰概率决定：$D_{WB} = 1 - P_{evict\_dirty}$，其中 $P_{evict\_dirty} = \frac{\text{Cache Misses}_{read} \times P_{dirty|miss}}{\text{Total Requests}}$。若缓存未满载（如N24所述），$P_{evict\_dirty} \approx 0$，折损因子接近1；若满载，需估算脏页比例 $P_{dirty|miss}$，通常取决于更新率与访问率之比 $\lambda_{upd}/\lambda_{acc}$。

## Corrected Claim

在写回（Write-Back）模式下，有效命中率折损因子 $D_{WB}$ 由脏页淘汰概率决定：$D_{WB} = 1 - P_{evict\_dirty}$，其中 $P_{evict\_dirty} = \frac{\text{Cache Misses}_{read} \times P_{dirty|miss}}{\text{Total Requests}}$。若缓存未满载（如N24所述），$P_{evict\_dirty} \approx 0$，折损因子接近1；若满载，需估算脏页比例 $P_{dirty|miss}$，通常取决于更新率与访问率之比 $\lambda_{upd}/\lambda_{acc}$。

## Evidence

父节点级核验失败（LLM 错误）：Invalid \escape: line 5 column 78 (char 143)
