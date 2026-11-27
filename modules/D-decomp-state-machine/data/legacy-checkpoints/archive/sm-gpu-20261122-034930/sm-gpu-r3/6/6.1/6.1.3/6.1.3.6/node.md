# N371: 2x RTX 4090 峰值功耗修正：单卡TDP 450W为典型值，但瞬时峰值功耗（Transient Spike）可达 600W-700W（参考NVIDIA官

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N131, N132, N133

## Claim

2x RTX 4090 峰值功耗修正：单卡TDP 450W为典型值，但瞬时峰值功耗（Transient Spike）可达 600W-700W（参考NVIDIA官方规格及PCPartPicker实测），双卡同时峰值时系统总峰值可能超过 1,400W（2*700W + 150W CPU/主板）。因此1600W电源仅留有11%余量，存在过载风险；推荐升级为2000W 80+ Titanium电源（如Corsair AX2000i，$550）以确保稳定性。

## Corrected Claim

2x RTX 4090 单卡TDP为450W，但瞬时峰值功耗可能显著高于TDP（具体数值依负载和驱动而异，部分实测可达600W以上）。双卡同时峰值时系统总功耗可能超过1,400W。1600W电源余量较紧，建议根据具体负载场景评估，或考虑更高功率（如2000W）电源以确保极端负载下的稳定性。

## Evidence

[质询]瞬时峰值功耗（Transient Spike）达到600W-700W的数值缺乏普遍共识，且高度依赖于具体的驱动版本、游戏负载及电源保护机制，将其作为固定事实陈述存在过度简化的风险；此外，1600W电源在双卡4090场景下是否必然存在‘过载风险’取决于电源的瞬态响应能力，而非仅看静态余量。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无法验证具体峰值数值及特定电源型号价格/规格）

## Search Query

RTX 4090 transient power spike maximum wattage Corsair AX2000i price
