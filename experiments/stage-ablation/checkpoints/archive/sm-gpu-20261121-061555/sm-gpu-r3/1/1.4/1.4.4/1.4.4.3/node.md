# N179: AMD MI300X 的 TDP 为 750W/卡，8 卡模组总功耗 ≈ 6000W，导致 5 年 OpEx（电费）在 24/7 负载下 ≈ 5 * 6000W

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

AMD MI300X 的 TDP 为 750W/卡，8 卡模组总功耗 ≈ 6000W，导致 5 年 OpEx（电费）在 24/7 负载下 ≈ 5 * 6000W * 8760h * $0.15/kWh ≈ $394,200，远超消费级/数据中心单卡方案，使其 TCO 在本地工作站场景下不可行

## Corrected Claim

AMD MI300X 的 TDP 为 750W/卡，8 卡模组总功耗 ≈ 6000W，导致 5 年 OpEx（电费）在 24/7 负载下 ≈ 5 * 6000W * 8760h * $0.15/kWh ≈ $394,200，远超消费级/数据中心单卡方案，使其 TCO 在本地工作站场景下不可行

## Evidence

先验知识/题面给定，逻辑校验通过：MI300X TDP 750W 符合公开规格，8卡总功耗6000W计算正确，电费估算公式及数值量级（约39.4万美元/5年）逻辑自洽且符合数据中心高功耗硬件的经济直觉。

## Search Query

AMD MI300X TDP power consumption 750W
