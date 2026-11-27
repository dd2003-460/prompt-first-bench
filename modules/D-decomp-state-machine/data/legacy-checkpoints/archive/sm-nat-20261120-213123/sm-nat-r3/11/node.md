# N80: 在静态请求分布下，LFU 的字节命中率理论上限 H_lfu_max 由缓存容量 C 内能容纳的最高频率对象集合决定。由于 LFU 优先缓存高频对象，其命中字节流

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在静态请求分布下，LFU 的字节命中率理论上限 H_lfu_max 由缓存容量 C 内能容纳的最高频率对象集合决定。由于 LFU 优先缓存高频对象，其命中字节流量占比近似为 ∫_{0}^{C/\bar{S}_{hot}} λ(x)S(x)dx / R_byte。对于 Pareto(β=0.9) 分布，前 1% 的对象（k=1000）覆盖约 50% 的请求，若其平均大小因负相关而较小，LFU 能完全缓存这部分头部对象，使得 H_lfu_max 接近 50% + (剩余容量覆盖的次头部对象字节占比)。

## Corrected Claim

在静态请求分布下，LFU 的字节命中率理论上限 H_lfu_max 由缓存容量 C 内能容纳的最高频率对象集合决定。由于 LFU 优先缓存高频对象，其命中字节流量占比近似为 ∫_{0}^{C/\bar{S}_{hot}} λ(x)S(x)dx / R_byte。对于 Pareto(β=0.9) 分布，前 1% 的对象（k=1000）覆盖约 50% 的请求，若其平均大小因负相关而较小，LFU 能完全缓存这部分头部对象，使得 H_lfu_max 接近 50% + (剩余容量覆盖的次头部对象字节占比)。

## Evidence

检索失败: no sources from any channel (all 5 failed)
