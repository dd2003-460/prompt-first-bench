# N19: 对象更新率1%/天导致的LRU有效命中率折扣：有效命中率 H_eff ≈ H_LRU * (1 - U * T_residence)，其中U=0.01/day，

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

对象更新率1%/天导致的LRU有效命中率折扣：有效命中率 H_eff ≈ H_LRU * (1 - U * T_residence)，其中U=0.01/day，T_residence为对象平均驻留时间；若热门对象驻留时间较短（因频繁更新），折扣系数约为 0.90-0.95；具体需计算热门对象集合的平均驻留时间，通常更新率直接线性扣减命中率，折扣约为 1 - 0.01 * (平均访问间隔/更新间隔)。

## Corrected Claim

对象更新率会影响 LRU 命中率，但具体折扣系数取决于热门对象的平均驻留时间与更新频率的比值，不存在通用的固定折扣系数（如 0.90-0.95），需根据具体业务负载模型计算。

## Evidence

[质询]公式 H_eff ≈ H_LRU * (1 - U * T_residence) 缺乏严格的理论推导支持，且量纲和物理意义存疑。通常更新率对命中率的影响取决于更新频率与访问频率的相对关系，而非简单的线性乘积。此外，'折扣系数约为 0.90-0.95' 这一具体数值范围缺乏依据，因为 T_residence 未给定，无法得出固定区间。 | 来源 [1] 仅介绍 LRU 及改进策略（LFU, W-TinyLFU, ARC），未涉及更新率对命中率的具体量化折扣公式或数值范围，无法支持该具体经验公式。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2025677845498708639&rut=e4f96d4a68d4df41c2ceedac544257f46a448779d6814ef1193317d0e1d4f6cd', 'type': 'ddg', 'title': '千万 Qps 架构，第 101 讲：「缓存淘汰策略：从lru到自适应」'}
