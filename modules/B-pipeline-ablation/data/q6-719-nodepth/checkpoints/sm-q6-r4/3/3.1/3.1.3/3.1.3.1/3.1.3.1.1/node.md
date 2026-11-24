# N638: 工作点A（高缓存命中率）的存储成本增量 ΔC_storage = (N_storage_A - N_storage_base) * C_storage_GB，假

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N213

## Claim

工作点A（高缓存命中率）的存储成本增量 ΔC_storage = (N_storage_A - N_storage_base) * C_storage_GB，假设基准存储2TB，A为3.6TB，C_storage_GB = ¥0.8/GB/月，则 ΔC_storage = (3600 - 2000) * 0.8 = ¥1,280/月；此增量需与回源带宽节省 ΔC_bw = (H_base - H_A) * Traffic_out * P_bw 对比，判断是否经济可行。

## Corrected Claim

工作点A（高缓存命中率）的存储成本增量 ΔC_storage = (N_storage_A - N_storage_base) * C_storage_GB，假设基准存储2TB，A为3.6TB，C_storage_GB = ¥0.8/GB/月，则 ΔC_storage = (3600 - 2000) * 0.8 = ¥1,280/月；此增量需与回源带宽节省 ΔC_bw = (H_base - H_A) * Traffic_out * P_bw 对比，判断是否经济可行。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 (3600-2000)*0.8=1280 正确，量纲与逻辑自洽。

## Search Query

cdn cache storage cost vs bandwidth savings trade-off
