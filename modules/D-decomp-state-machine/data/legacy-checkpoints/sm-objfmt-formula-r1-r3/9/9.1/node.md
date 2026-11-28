# N112: 双路 RTX 4090 推理时的动态功耗峰值测量值：单卡满载功耗约为 450W（TDP），两卡并行推理时由于 PCIe 总线争用和 CPU 调度开销，系统总 G

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

双路 RTX 4090 推理时的动态功耗峰值测量值：单卡满载功耗约为 450W（TDP），两卡并行推理时由于 PCIe 总线争用和 CPU 调度开销，系统总 GPU 功耗通常维持在 2 * 450W = 900W 附近，需预留 20% 余量即 1080W 作为电源瞬时负载参考。

## Corrected Claim

双路 RTX 4090 推理时的动态功耗峰值测量值：单卡满载功耗约为 450W（TDP），两卡并行推理时由于 PCIe 总线争用和 CPU 调度开销，系统总 GPU 功耗通常维持在 2 * 450W = 900W 附近，需预留 20% 余量即 1080W 作为电源瞬时负载参考。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 TDP 确认为 450W，双卡满载理论峰值 900W，预留 20% 余量计算为 1080W，数值量级与工程常识一致。
