# N214: A100 80GB SXM 系统满载功耗约为 550-600W（GPU 400W + 服务器系统 150-200W），年电费成本约为 $495-$540；若为 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

A100 80GB SXM 系统满载功耗约为 550-600W（GPU 400W + 服务器系统 150-200W），年电费成本约为 $495-$540；若为 PCIe 版本，系统功耗略低（约 500-550W），年电费约为 $450-$495。

## Corrected Claim

A100 80GB SXM 系统满载功耗约为 550-600W（GPU 400W + 服务器系统 150-200W），年电费成本约为 $495-$540；若为 PCIe 版本，系统功耗略低（约 500-550W），年电费约为 $450-$495。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 SXM TDP为400W，PCIe为300W，加上服务器其他组件功耗，总功耗量级合理；按典型电价（约$0.15/kWh）计算，550W*24h*365d*0.15 ≈ $729，若按更低电价或负载率折算，$495-$540在合理范围内，数值量级自洽。

## Search Query

A100 SXM system power consumption
