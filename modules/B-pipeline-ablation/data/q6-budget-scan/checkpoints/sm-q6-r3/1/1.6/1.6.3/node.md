# N49: 回源概率 p_miss = 1 - hit_rate，其中 hit_rate 为缓存命中率（典型 70-95%）；该值决定回源链路延迟 t_origin 对整体

- **status**: pending
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

回源概率 p_miss = 1 - hit_rate，其中 hit_rate 为缓存命中率（典型 70-95%）；该值决定回源链路延迟 t_origin 对整体P99延迟的贡献权重。

## Corrected Claim

回源概率 p_miss = 1 - hit_rate，其中 hit_rate 为缓存命中率（典型 70-95%）；该值决定回源链路延迟 t_origin 对整体P99延迟的贡献权重。

## Evidence

父节点级核验未通过：不完备（子节点1聚焦于 hit_rate 的估算逻辑（输入端），子节点2聚焦于 p_miss 对延迟的加权计算（输出端），两者在逻辑上是正交的。然而，父节点核心是解释 'p_miss 决定 t_origin 对 P99 延迟的贡献权重'。子节点2虽然给出了一个近似公式 w_miss = p_miss * (t_origin - t_cache)，但这通常用于平均延迟（Mean Latency）或线性加权，而非 P99 延迟。P99 延迟受长尾分布影响，简单的概率加权无法准确描述 P99 的贡献权重（通常 P99 直接由最慢的那部分请求决定，或者通过分位数计算）。因此，子节点2在理论准确性上存在偏差，未能准确覆盖父节点关于 'P99' 这一特定统计量的核心机制。）
