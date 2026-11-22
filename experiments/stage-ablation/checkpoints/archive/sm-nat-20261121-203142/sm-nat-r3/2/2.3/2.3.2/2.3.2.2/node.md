# N111: H_steady 的基准值代入：基于N69典型CDN边缘节点命中率范围85%-95%，取中值 H_steady=0.90，则 ε(1day) ≈ 0.90 * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

H_steady 的基准值代入：基于N69典型CDN边缘节点命中率范围85%-95%，取中值 H_steady=0.90，则 ε(1day) ≈ 0.90 * 0.221 ≈ 0.199，即冷启动第1天命中率比稳态低约19.9个百分点

## Corrected Claim

H_steady 的基准值代入：基于N69典型CDN边缘节点命中率范围85%-95%，取中值 H_steady=0.90，则 ε(1day) ≈ 0.90 * 0.221 ≈ 0.199，即冷启动第1天命中率比稳态低约19.9个百分点

## Evidence

先验知识/题面给定，逻辑校验通过：0.90 * 0.221 = 0.1989 ≈ 0.199，计算无误，且符合CDN冷启动命中率低于稳态的常识。

## Search Query

CDN edge node steady state hit rate typical value
