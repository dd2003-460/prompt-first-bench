# N12: NVMe SSD 阵列单位容量功耗（W/TB），基于 7.68TB SSD 典型读写功耗 20-25W 计算

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

NVMe SSD 阵列单位容量功耗（W/TB），基于 7.68TB SSD 典型读写功耗 20-25W 计算

## Corrected Claim

NVMe SSD 阵列单位容量功耗（W/TB），基于 7.68TB SSD 典型读写功耗约 10-15W 估算

## Evidence

[质询]数值量级存疑：7.68TB企业级NVMe SSD在典型读写负载下的功耗通常在10W-15W左右，20-25W更接近于极端满载或特定高性能型号的峰值功耗，作为“典型”值偏高，可能导致单位容量功耗计算结果偏大。 | 参考来源[1]主要讨论1TB消费级SSD，未提供7.68TB企业级SSD的具体功耗数据，无法直接支持该经验参数；但逻辑上功耗与容量成反比关系成立，故保留但降级。

## Search Query

enterprise NVMe SSD power consumption watts per drive 7.68TB

## Retrieval Sources

- {'url': 'https://www.toutiao.com/article/7655910771183862318/&rut=f2e39f748e98464e98a6c1f03612516bd18b8b6f9d9c60ee7400ed9e9fa33558', 'type': 'ddg', 'title': '1TB NVMe SSD完整参数、规格、用途深度解析｜2026装机主力存储实测'}
