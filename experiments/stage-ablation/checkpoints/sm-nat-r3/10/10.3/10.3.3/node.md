# N187: W_waste 的解析近似：假设 LRU 栈中冷对象占比 p_cold（基于访问频率分布），则 W_waste ≈ p_cold * K_LRU * E[S|C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

W_waste 的解析近似：假设 LRU 栈中冷对象占比 p_cold（基于访问频率分布），则 W_waste ≈ p_cold * K_LRU * E[S|Cold]。需估算 p_cold：在 Zipf 分布下，访问频率低于中位数的对象占比约为 50%，但其在 LRU 栈中的驻留概率与频率成正比，需通过积分 ∫_{i_min}^{N} i^{-β} di / ∫_{1}^{N} i^{-β} di 计算。

## Corrected Claim

W_waste 的解析近似：假设 LRU 栈中冷对象占比 p_cold（基于访问频率分布），则 W_waste ≈ p_cold * K_LRU * E[S|Cold]。需估算 p_cold：在 Zipf 分布下，访问频率低于中位数的对象占比约为 50%，但其在 LRU 栈中的驻留概率与频率成正比，需通过积分 ∫_{i_min}^{N} i^{-β} di / ∫_{1}^{N} i^{-β} di 计算。

## Evidence

先验知识/题面给定，逻辑校验通过
