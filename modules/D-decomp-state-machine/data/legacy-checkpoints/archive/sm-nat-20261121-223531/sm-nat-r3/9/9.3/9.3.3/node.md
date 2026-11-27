# N226: 验证 N81 中‘预期增益 2-5 百分点’的来源：该范围可能来自文献中 Zipf(α=1) 分布下 LFU 相对 LRU 的实证数据（如 [待核验] 某 CD

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N81

## Claim

验证 N81 中‘预期增益 2-5 百分点’的来源：该范围可能来自文献中 Zipf(α=1) 分布下 LFU 相对 LRU 的实证数据（如 [待核验] 某 CDN 论文），但本题 β=0.9 比 Zipf(α=1) 更偏斜，理论上 LFU 增益应更大；通过公式 ΔH ≈ k * (β-1)^{-1} * |ρ| 估算，k≈0.1，β=0.9 时 ΔH ≈ 0.1 * 10 * 0.3 = 0.3 百分点，与 2-5 百分点矛盾，需重新校准 k 值。

## Corrected Claim

N81 中‘预期增益 2-5 百分点’的来源尚待核验。基于 β=0.9 的偏斜分布，理论上 LFU 增益可能高于 Zipf(α=1) 场景，但具体数值需依赖实证数据或更严谨的模型校准，当前基于简化公式的估算（ΔH ≈ 0.3 百分点）与 2-5 百分点存在差异，需进一步验证模型参数 k 的合理性。

## Evidence

[质询]该陈述包含大量未经验证的内部推导（如公式 ΔH ≈ k * (β-1)^{-1} * |ρ| 及 k≈0.1 的取值），且声称与 N81 的 2-5 百分点矛盾，但缺乏外部文献支持该特定公式或 k 值的有效性，属于孤立的内部逻辑推演。 | 参考来源 [1] 为百度网盘链接，与缓存算法理论无关，无可用外部证据；该陈述为经验事实/模型推导，逻辑自洽但缺乏来源直接支持，依据经验事实排除条款降级。

## Search Query

LFU vs LRU cache hit rate improvement Zipf distribution beta 0.9

## Retrieval Sources

- {'url': 'https://pan.baidu.com/share/init?surl=U37frr0D6HCxWz5GbbrTCw&rut=bce26ec63f89628fab44746781932a0f0065082be1ada0c7855e9f7851b9339e', 'type': 'ddg', 'title': '百度网盘 请输入提取码'}
