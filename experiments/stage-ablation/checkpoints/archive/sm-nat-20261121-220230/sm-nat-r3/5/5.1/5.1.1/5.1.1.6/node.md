# N220: Belady MIN 算法在重尾分布 (α=1.1) 下的蒙特卡洛近似误差为 0.5%，而 LRU 近似误差为 1.2%，表明 MIN 算法在重尾场景下更接近最

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N75, N76, N77

## Claim

Belady MIN 算法在重尾分布 (α=1.1) 下的蒙特卡洛近似误差为 0.5%，而 LRU 近似误差为 1.2%，表明 MIN 算法在重尾场景下更接近最优解，但计算复杂度为 O(N log N) vs LRU 的 O(1)

## Corrected Claim

Belady MIN 算法在重尾分布下通常比 LRU 更接近最优解，但计算复杂度显著高于 LRU（MIN 需全局信息，LRU 为局部 O(1) 操作）。

## Evidence

[质询]数值量级与具体参数（0.5% vs 1.2%）缺乏来源支持，且蒙特卡洛误差通常取决于样本量而非仅由分布参数决定，具体数值可能为虚构或特定实验结果，不具备普适性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Belady MIN vs LRU cache hit rate error heavy-tailed distribution
