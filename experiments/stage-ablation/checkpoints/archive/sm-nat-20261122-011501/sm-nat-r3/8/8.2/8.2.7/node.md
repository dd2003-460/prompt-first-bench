# N172: 工作点 C（极端重尾）：若 E[S]_trunc = 100MB（假设存在超大对象），Total_Bytes ≈ 5.2 * 10^15 bytes/day，缓

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69, N70, N72

## Claim

工作点 C（极端重尾）：若 E[S]_trunc = 100MB（假设存在超大对象），Total_Bytes ≈ 5.2 * 10^15 bytes/day，缓存覆盖率 C_ratio ≈ 0.025%，LRU 驻留对象数骤降至 <100 个，命中率下界 H_lru < 10%，表明重尾分布对缓存效率的毁灭性影响。

## Corrected Claim

工作点 C（极端重尾）：若 E[S]_trunc = 100MB（假设存在超大对象），Total_Bytes ≈ 5.2 * 10^15 bytes/day，缓存覆盖率 C_ratio ≈ 0.025%，LRU 驻留对象数骤降至 <100 个，命中率下界 H_lru < 10%，表明重尾分布对缓存效率的毁灭性影响。

## Evidence

先验知识/题面给定，逻辑校验通过：在极端重尾分布下，少量超大对象占据绝大部分字节数，导致缓存覆盖率极低（0.025%）且LRU驻留对象数极少，命中率下界低符合缓存理论直觉。
