# N170: 当平均对象大小 s 从 1MB 增至 5MB 时，自建POP的带宽成本 C_bandwidth_self 主要取决于回源流量，若缓存命中率 H_pop 保持 0

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N43

## Claim

当平均对象大小 s 从 1MB 增至 5MB 时，自建POP的带宽成本 C_bandwidth_self 主要取决于回源流量，若缓存命中率 H_pop 保持 0.9 不变，回源流量从 200GB 增至 1000GB，成本从 (200GB * ¥0.1/GB) / 2048000 * 1000 ≈ ¥0.01/1000req 增至 (1000GB * ¥0.1/GB) / 409600 * 1000 ≈ ¥0.24/1000req。

## Corrected Claim

当平均对象大小 s 从 1MB 增至 5MB 时，若总请求数保持不变，回源流量从 200GB 增至 1000GB，成本应从 (200GB * ¥0.1/GB) / 2048000 * 1000 ≈ ¥0.01/1000req 增至 (1000GB * ¥0.1/GB) / 2048000 * 1000 ≈ ¥0.05/1000req；若分母变化为 409600，则需明确总请求数或总流量约束条件的变化。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别针对单价修正、命中率动态变化、综合成本重算三个不同维度进行分解，逻辑上呈递进关系（输入参数修正 -> 中间变量修正 -> 最终结果计算），无内容重复或矛盾。父节点中的核心假设（固定命中率、固定单价）均被子节点挑战并修正，覆盖了父节点计算逻辑中的所有关键变量。）

## Search Query

Self-hosted CDN origin pull bandwidth cost
