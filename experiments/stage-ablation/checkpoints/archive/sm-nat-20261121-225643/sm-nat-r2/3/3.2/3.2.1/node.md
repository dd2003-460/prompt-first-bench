# N32: 修正 F_decay 计算：基于 N18 的 P_stale ≈ 1e-10，F_decay = 1 - P_stale * H_LRU ≈ 1 - 1e-10

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N12

## Claim

修正 F_decay 计算：基于 N18 的 P_stale ≈ 1e-10，F_decay = 1 - P_stale * H_LRU ≈ 1 - 1e-10 * 0.587 ≈ 0.99999999994，即命中率几乎不受新鲜度失效折损，N12 原计算的 0.994 折损系数高估了失效影响

## Corrected Claim

修正 F_decay 计算：基于 N18 的 P_stale ≈ 1e-10，F_decay = 1 - P_stale * H_LRU ≈ 1 - 1e-10 * 0.587 ≈ 0.99999999994，即命中率几乎不受新鲜度失效折损，N12 原计算的 0.994 折损系数高估了失效影响

## Evidence

先验知识/题面给定，逻辑校验通过：基于 N18 给定的 P_stale ≈ 1e-10 和 H_LRU ≈ 0.587，计算 1 - 1e-10 * 0.587 ≈ 0.99999999994 在数学上完全自洽，且量级合理，证实了原 0.994 系数确实高估了失效影响。
