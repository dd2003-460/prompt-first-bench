# N55: T_hot 的容量约束验证：若前 10% 热门对象总大小为 10^4 * 0.7MB ≈ 7GB，远小于 128GB 缓存，则 T_hot 不受容量驱逐限制，仅

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

T_hot 的容量约束验证：若前 10% 热门对象总大小为 10^4 * 0.7MB ≈ 7GB，远小于 128GB 缓存，则 T_hot 不受容量驱逐限制，仅受更新率 u 限制，T_hot ≈ 1/u * (1/ln(1/(1-P_inval)))。

## Corrected Claim

T_hot 的容量约束验证：若前 10% 热门对象总大小为 10^4 * 0.7MB ≈ 7GB，远小于 128GB 缓存，则 T_hot 不受容量驱逐限制，仅受更新率 u 限制，T_hot ≈ 1/u * (1/ln(1/(1-P_inval)))。

## Evidence

先验知识/题面给定，逻辑校验通过：10^4 * 0.7MB = 7GB < 128GB，容量约束不成立，故仅受更新率限制，推导逻辑自洽。
