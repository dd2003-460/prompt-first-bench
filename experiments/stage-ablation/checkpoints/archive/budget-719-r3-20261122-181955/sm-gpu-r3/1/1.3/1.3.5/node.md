# N56: RX 7900 XTX TDP 为 315W，RX 7900 XT 为 300W，RX 7800 XT 为 263W，MI300X 为 750W

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

RX 7900 XTX TDP 为 315W，RX 7900 XT 为 300W，RX 7800 XT 为 263W，MI300X 为 750W

## Corrected Claim

RX 7900 XTX TDP 为 315W，RX 7900 XT 为 300W，RX 7800 XT 为 263W，MI300X 为 750W

## Evidence

父节点级核验未通过：非正交, 不完备（1. 正交性失败：子节点1主要关注TDP修正与平均功耗计算，子节点2基于平均功耗计算成本，二者存在明显的逻辑依赖和数值重叠（子节点2直接使用了子节点1计算的P_avg），且子节点1中关于A100的修正与父节点（仅列出RX/MI300X TDP）主题不一致，属于越界内容。2. 完备性失败：父节点明确列出了RX 7900 XTX和RX 7900 XT的TDP，但两个子节点均未包含这两款GPU的功耗计算或成本分析，导致信息缺失。）
