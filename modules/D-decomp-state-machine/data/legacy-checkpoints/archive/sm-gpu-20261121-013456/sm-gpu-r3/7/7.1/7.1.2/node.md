# N269: AMD Radeon PRO W7900 在运行 Qwen3-27B BF16 时的实测满载功耗（Watt），需修正 N106 中 '300W' 的估算；该卡 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N104

## Claim

AMD Radeon PRO W7900 在运行 Qwen3-27B BF16 时的实测满载功耗（Watt），需修正 N106 中 '300W' 的估算；该卡 TDP 为 300W，但在持续推理负载下实际功耗可能波动，需确认典型功耗以准确计算 3 年电力成本（公式：Power_W * 8760h * 3 * Price_$per_kWh / 1000）。

## Corrected Claim

AMD Radeon PRO W7900 的 TDP 为 300W，在运行 Qwen3-27B BF16 推理时，实际功耗通常低于或接近 TDP，具体数值需参考官方规格书或实测数据，不能直接假设恒定为 300W 进行成本计算。

## Evidence

[质询]参考来源仅讨论了显卡架构（RDNA 3）和精度支持（FP8/INT8），完全未提及功耗数据（Watt）或TDP，无法提供外部证据支持具体的实测功耗数值或波动范围。 | 逻辑上TDP 300W作为上限是合理的，但具体实测功耗属于经验事实，参考来源[1][2]与功耗主题无关，无法提供直接支持，故降级。

## Search Query

AMD Radeon PRO W7900 power consumption watts AI inference load

## Retrieval Sources

- {'url': 'https://blog.csdn.net/zhangfeng1133/article/details/163222273&rut=8999f32832fe93878fce2ddb6a21ee2c3bf826dcf630e257d4b404e8c661d95b', 'type': 'ddg', 'title': '在单卡amd Radeon Pro W7900上训练Qwen3.6-27B的可行方案 amd免费算力'}
- {'url': 'https://blog.51cto.com/u_16120231/14855916&rut=2f68086e183788d6ca95340044abf2fda2d4a9e1cfe133349db9e0a4df6dc6c0', 'type': 'ddg', 'title': '在单卡amd Radeon Pro W7900上训练Qwen3.6-27B的可行方案 amd免费算力'}
