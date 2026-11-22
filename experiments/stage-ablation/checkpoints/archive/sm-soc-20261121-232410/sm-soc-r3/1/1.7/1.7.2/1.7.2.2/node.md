# N141: 预期搜索成本 C_signal_loss 的构成量化：C_signal_loss = C_time * T_extra + C_cognitive，其中 T_e

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N49

## Claim

预期搜索成本 C_signal_loss 的构成量化：C_signal_loss = C_time * T_extra + C_cognitive，其中 T_extra 为因无法区分质量而多出的比较时间（约 5 分钟），C_time 为时间机会成本（10元/小时），C_cognitive 为认知负荷导致的效用损失（约 2 元），合计 C_signal_loss ≈ 6.3 元。

## Corrected Claim

预期搜索成本 C_signal_loss 的构成量化：C_signal_loss = C_time * T_extra + C_cognitive，其中 T_extra 为因无法区分质量而多出的比较时间（约 5 分钟），C_time 为时间机会成本（10元/小时），C_cognitive 为认知负荷导致的效用损失（约 2 元），合计 C_signal_loss ≈ 2.83 元。

## Evidence

先验知识/题面给定，逻辑校验通过：10元/小时 * (5/60)小时 + 2元 = 0.833 + 2 = 2.833元，与陈述中的6.3元存在数值矛盾，但作为knowledge节点，若视为模型内部推导或特定假设下的定性/定量示例，且无外部来源矛盾，通常此类具体数值若逻辑不自洽应判failed。然而，仔细检查：10 * (5/60) = 0.833。0.833 + 2 = 2.833。陈述说合计约6.3元。这里存在明显的算术错误。10元/小时 * 5分钟 = 0.83元。加上2元认知负荷，总共约2.83元。陈述声称6.3元，数值不符。这是一个硬逻辑/算术错误。
