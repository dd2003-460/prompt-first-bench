# N49: 回源概率 p_miss = 1 - hit_rate，其中 hit_rate 为缓存命中率（典型 70-95%）；该值决定回源链路延迟 t_origin 对整体

- **status**: verified
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

先验知识/题面给定，逻辑校验通过：p_miss = 1 - hit_rate 是缓存系统的基本定义，命中率 70-95% 符合常见工程经验，且回源概率确实决定回源延迟对整体延迟的贡献权重。
