# N152: 工作点 C (低频冷对象)：当 R_i 极低（如第 10000 名，τ_res(i) ≈ 10000 天）时，LRU 淘汰概率主导，即使对象未更新，P_vali

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

工作点 C (低频冷对象)：当 R_i 极低（如第 10000 名，τ_res(i) ≈ 10000 天）时，LRU 淘汰概率主导，即使对象未更新，P_valid(i) 也受限于 LRU 驻留概率 P_res，需结合 N76 的淘汰概率修正，而非仅考虑更新失效。

## Corrected Claim

工作点 C (低频冷对象)：当 R_i 极低（如第 10000 名，τ_res(i) ≈ 10000 天）时，LRU 淘汰概率主导，即使对象未更新，P_valid(i) 也受限于 LRU 驻留概率 P_res，需结合 N76 的淘汰概率修正，而非仅考虑更新失效。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU机制下，低频访问对象（高排名/长驻留时间）的缓存有效性确实主要受限于LRU淘汰概率而非更新频率，符合缓存替换算法的基本原理。
