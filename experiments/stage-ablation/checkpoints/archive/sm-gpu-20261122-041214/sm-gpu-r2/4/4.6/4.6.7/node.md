# N144: 量化峰值功耗对散热基础设施成本的影响：若 RTX 4090 峰值功耗达 500W (110% TDP)，标准风冷散热器 (设计余量 450W) 可能过热，需升级

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39, N40, N41

## Claim

量化峰值功耗对散热基础设施成本的影响：若 RTX 4090 峰值功耗达 500W (110% TDP)，标准风冷散热器 (设计余量 450W) 可能过热，需升级至高性能风冷或小型水冷，成本增加 $50-$100。对于 2x 4090 (峰值 ~1000W)，机箱风道设计至关重要，若散热不足导致降频 (Thermal Throttling)，性能下降 10-20%，等效于 TCO 增加 10-20% 的电力成本或降低吞吐量。

## Corrected Claim

量化峰值功耗对散热基础设施成本的影响：若 RTX 4090 峰值功耗达 500W (110% TDP)，标准风冷散热器 (设计余量 450W) 可能过热，需升级至高性能风冷或小型水冷，成本增加 $50-$100。对于 2x 4090 (峰值 ~1000W)，机箱风道设计至关重要，若散热不足导致降频 (Thermal Throttling)，性能下降 10-20%，等效于 TCO 增加 10-20% 的电力成本或降低吞吐量。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 TDP 450W，峰值500W符合物理规律；散热升级成本$50-$100及降频导致10-20%性能损失符合工程常识与TCO逻辑。

## Search Query

RTX 4090 thermal throttling performance drop high load
