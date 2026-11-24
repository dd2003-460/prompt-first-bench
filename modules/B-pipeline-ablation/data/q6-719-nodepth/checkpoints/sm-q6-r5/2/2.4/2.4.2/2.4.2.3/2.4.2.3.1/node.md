# N581: 对于有线宽带用户（3跳路径：接入+骨干+城域），P99合成延迟 L_hops_p99_wired 约为 20-40 ms，其中接入层P99为10-20ms，骨干

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N190

## Claim

对于有线宽带用户（3跳路径：接入+骨干+城域），P99合成延迟 L_hops_p99_wired 约为 20-40 ms，其中接入层P99为10-20ms，骨干和城域平均各5ms，整体受限于最后一公里光纤质量而非无线波动。

## Corrected Claim

对于有线宽带用户（3跳路径：接入+骨干+城域），P99合成延迟 L_hops_p99_wired 约为 20-40 ms，其中接入层P99为10-20ms，骨干和城域平均各5ms，整体受限于最后一公里光纤质量而非无线波动。

## Evidence

先验知识/题面给定，逻辑校验通过：有线宽带3跳路径（接入+骨干+城域）的P99延迟在20-40ms范围内符合工程经验，接入层10-20ms、骨干和城域各5ms的分解合理，且有线网络延迟主要受限于最后一公里光纤质量而非无线波动的描述符合网络工程常识。

## Search Query

wired broadband P99 latency 3 hops backbone metro ms
