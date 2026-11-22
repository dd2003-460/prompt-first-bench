# N117: 有效驻留对象数 k_eff 在‘高热度集中’场景下的数值：当 ρ=-0.3 时，Top-k 对象平均大小 E[S|Top-k] ≈ 5KB，若缓存容量 C=12

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

有效驻留对象数 k_eff 在‘高热度集中’场景下的数值：当 ρ=-0.3 时，Top-k 对象平均大小 E[S|Top-k] ≈ 5KB，若缓存容量 C=128GB，则 k_eff = C / E[S|Top-k] ≈ 1.28e11 / 5120 ≈ 2.5e7，但受限于对象总数 N=1e5，故 k_eff = N = 100,000，即缓存可容纳所有对象，瓶颈转为请求热度分布。

## Corrected Claim

有效驻留对象数 k_eff 在‘高热度集中’场景下的数值：当 ρ=-0.3 时，Top-k 对象平均大小 E[S|Top-k] ≈ 5KB，若缓存容量 C=128GB，则 k_eff = C / E[S|Top-k] ≈ 1.28e11 / 5120 ≈ 2.5e7，但受限于对象总数 N=1e5，故 k_eff = N = 100,000，即缓存可容纳所有对象，瓶颈转为请求热度分布。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 C/E[S] = 128GB/5KB = 2.5e7 正确，且 2.5e7 > N=1e5，故 k_eff 受限于 N，逻辑自洽。
