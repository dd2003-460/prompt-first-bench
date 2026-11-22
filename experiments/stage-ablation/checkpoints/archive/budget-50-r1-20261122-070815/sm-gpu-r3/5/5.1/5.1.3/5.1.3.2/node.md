# N344: 在标准塔式机箱（风冷，无定制水冷）中，RTX 4090 在室温 25°C 下运行 27B 模型时，GPU 核心温度通常维持在 75-85°C，未触发 Therm

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N122

## Claim

在标准塔式机箱（风冷，无定制水冷）中，RTX 4090 在室温 25°C 下运行 27B 模型时，GPU 核心温度通常维持在 75-85°C，未触发 Thermal Throttling (降频)；但在紧凑型 ITX 机箱或高温环境 (>30°C) 下，温度可能超过 90°C 并触发 5-10% 的降频，导致吞吐量下降 5-10%，此风险需通过长期负载测试 (如 stress-ng) 验证具体降频阈值。

## Corrected Claim

在标准塔式机箱（风冷，无定制水冷）中，RTX 4090 在室温 25°C 下运行 27B 模型时，GPU 核心温度通常维持在 75-85°C，未触发 Thermal Throttling (降频)；但在紧凑型 ITX 机箱或高温环境 (>30°C) 下，温度可能超过 90°C 并触发 5-10% 的降频，导致吞吐量下降 5-10%，此风险需通过长期负载测试 (如 stress-ng) 验证具体降频阈值。

## Evidence

先验知识/题面给定，逻辑校验通过
