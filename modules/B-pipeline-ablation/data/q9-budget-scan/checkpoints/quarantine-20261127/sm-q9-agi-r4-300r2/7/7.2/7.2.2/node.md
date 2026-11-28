# N198: 全局摘要桥接（Global Summary Bridge）的实现成本与收益：生成摘要需额外消耗约 512 tokens 输出和 4k tokens 输入，增加单

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N77

## Claim

全局摘要桥接（Global Summary Bridge）的实现成本与收益：生成摘要需额外消耗约 512 tokens 输出和 4k tokens 输入，增加单次处理延迟约 2s；引入摘要后，跨片段推理准确率 Acc_bridge = Acc_local * (1 - P_break * (1 - R_summary))；若摘要召回率 R_summary=80%，则 Acc_bridge ≈ 80% * (1 - 0.3 * 0.2) = 75.2%，恢复至接近单片段水平。

## Corrected Claim

全局摘要桥接（Global Summary Bridge）的实现成本与收益：生成摘要需额外消耗约 512 tokens 输出和 4k tokens 输入，增加单次处理延迟约 2s；引入摘要后，跨片段推理准确率理论上可通过公式 Acc_bridge = Acc_local * (1 - P_break * (1 - R_summary)) 进行估算，其中 R_summary 为摘要召回率。

## Evidence

[质询]数值计算存在严重逻辑错误：公式中 Acc_local 未定义具体数值，却直接得出 75.2% 的结果；且 80% * (1 - 0.3 * 0.2) = 80% * 0.94 = 75.2% 这一算式隐含假设 Acc_local=80%，但前文并未给出此前提，属于无中生有的数值代入，导致推导过程不自洽。 | 先验知识/题面给定，但逻辑校验发现数值推导存在内部矛盾（Acc_local 取值未声明且计算结果依赖未给定的假设），故降级。
