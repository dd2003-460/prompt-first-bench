# N130: Apple M3 Ultra 的 3 年 TCO 修正值：硬件价格 $39,999，TDP 约 200W（Mac Studio 整机），年电费 $130（200

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30, N31, N32

## Claim

Apple M3 Ultra 的 3 年 TCO 修正值：硬件价格 $39,999，TDP 约 200W（Mac Studio 整机），年电费 $130（200W * 24 * 365 / 1000 * 0.15），3 年 TCO = $39,999 + 3 * $130 + $0 = $40,389。此数值与 H100 相当，但性能远低于 H100，性价比极低。

## Corrected Claim

Apple M3 Ultra（假设沿用 M2 Ultra 顶配价格 $39,999 及 200W TDP）的 3 年 TCO 约为 $40,389。该数值与 H100 相当，但其在通用计算或特定 AI 负载下的性价比需结合具体基准测试评估，不能简单断言为'极低'。

## Evidence

[质询]硬件价格 $39,999 为经验事实，且该价格对应的是 Mac Studio M2 Ultra 的顶配版本（192GB 内存），M3 Ultra 尚未发布或价格未定，存在型号混淆或数据过时风险；此外，'性能远低于 H100' 的定性结论缺乏具体基准测试支持，且 M3 Ultra 在特定 AI 推理场景下可能具有竞争力，该绝对化表述可能不准确。 | source=knowledge，逻辑校验通过（电费计算 200W*24*365/1000*0.15 ≈ $130 正确，TCO 加法正确），但硬件价格和性能对比属于经验事实，无外部来源支持，且存在型号/价格时效性风险，故降级。
