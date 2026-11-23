# N276: 计费模式切换盈亏平衡点：当流量波动系数K_peak > 1.8且日均流量 > 50TB时，按95分位带宽计费的成本通常低于按流量计费；当K_peak < 1.3

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

计费模式切换盈亏平衡点：当流量波动系数K_peak > 1.8且日均流量 > 50TB时，按95分位带宽计费的成本通常低于按流量计费；当K_peak < 1.3或日均流量 < 10TB时，按流量计费更优。需根据实际流量曲线计算P95带宽与流量成本的交叉点。

## Corrected Claim

计费模式切换盈亏平衡点：当流量波动系数K_peak > 1.8且日均流量 > 50TB时，按95分位带宽计费的成本通常低于按流量计费；当K_peak < 1.3或日均流量 < 10TB时，按流量计费更优。需根据实际流量曲线计算P95带宽与流量成本的交叉点。

## Evidence

先验知识/题面给定，逻辑校验通过：高波动（K_peak>1.8）且大流量场景下，95分位计费确实通常优于流量计费，低波动或小流量场景反之，符合网络计费经济学基本原理。

## Search Query

CDN billing model break-even point traffic vs bandwidth pricing
