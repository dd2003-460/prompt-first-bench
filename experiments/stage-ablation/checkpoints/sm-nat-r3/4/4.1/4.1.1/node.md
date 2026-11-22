# N68: LRU 队列中对象 i 的等待时间 W_LRU(i) 与更新间隔 T_update 的并联公式 T_eff(i) = (W_LRU(i) * T_update)

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N19

## Claim

LRU 队列中对象 i 的等待时间 W_LRU(i) 与更新间隔 T_update 的并联公式 T_eff(i) = (W_LRU(i) * T_update) / (W_LRU(i) + T_update) 在 W_LRU(i) >> T_update 时退化为 T_eff(i) ≈ T_update，此时更新率主导失效，命中率折损 D_update ≈ T_update / (W_LRU(i) + T_update) ≈ 1 - W_LRU(i)/T_update，量化为 D_update ≈ 0.99 当 W_LRU(i) = 100 * T_update。

## Corrected Claim

LRU 队列中对象 i 的有效时间 T_eff(i) = (W_LRU(i) * T_update) / (W_LRU(i) + T_update)。当 W_LRU(i) >> T_update 时，T_eff(i) ≈ T_update。此时命中率折损率 D_update ≈ T_update / (W_LRU(i) + T_update) ≈ T_update / W_LRU(i)。当 W_LRU(i) = 100 * T_update 时，D_update ≈ 0.01。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 740)
