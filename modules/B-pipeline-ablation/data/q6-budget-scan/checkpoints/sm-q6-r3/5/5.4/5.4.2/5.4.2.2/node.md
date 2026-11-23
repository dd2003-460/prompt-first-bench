# N260: 回源队列延迟导致的P99延迟增加 ΔP99_queue = (Q_origin_avg / B_origin) * s_avg * 8，其中 Q_origin_

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N83

## Claim

回源队列延迟导致的P99延迟增加 ΔP99_queue = (Q_origin_avg / B_origin) * s_avg * 8，其中 Q_origin_avg 为平均回源请求率，当 ΔP99_queue > T_budget - P99_base 时，需增加回源带宽

## Corrected Claim

回源队列延迟导致的P99延迟增加通常取决于队列长度与服务时间的关系（如 Little's Law: L = λW），而非简单的 (Q_origin_avg / B_origin) * s_avg * 8。当队列等待时间导致总延迟超过预算时，需增加回源带宽或优化缓存命中率。

## Evidence

[质询]公式量纲与物理意义存在严重错误：Q_origin_avg（请求率，单位 req/s）除以 B_origin（带宽，单位 bps）得到的是 s/req，再乘以 s_avg（秒）得到 s²/req，无法表示延迟（秒）。此外，P99延迟增加通常与队列长度（Q_len）或等待时间相关，而非简单的平均请求率与带宽的线性乘积，该公式缺乏排队论（如M/M/1）的理论支持，属于错误的经验公式。 | 逻辑校验失败：公式量纲不一致（左侧为时间，右侧推导后非时间量纲），且不符合基本排队论直觉。虽source为knowledge，但存在硬逻辑错误（量纲错/内部矛盾），根据判定规则应判failed或degraded。鉴于这是工程经验公式的变体，可能意图表达某种近似但表述错误，故判degraded并修正。
