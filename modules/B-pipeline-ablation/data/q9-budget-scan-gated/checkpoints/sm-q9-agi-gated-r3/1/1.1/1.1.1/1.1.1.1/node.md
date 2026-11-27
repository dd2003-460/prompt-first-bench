# N33: 修正N18/N21矛盾：基于N20确定的12KB/token开销与N7确定的15.2GB单卡可用显存，扣除13.5GB权重后实际剩余KV空间为1.7GB（174

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N18

## Claim

修正N18/N21矛盾：基于N20确定的12KB/token开销与N7确定的15.2GB单卡可用显存，扣除13.5GB权重后实际剩余KV空间为1.7GB（1740.8MB），计算得单序列最大上下文长度为 1740.8MB / 12KB ≈ 1451 tokens，而非N18声称的4000-5000 tokens。

## Corrected Claim

修正N18/N21矛盾：基于N20确定的12KB/token开销与N7确定的15.2GB单卡可用显存，扣除13.5GB权重后实际剩余KV空间为1.7GB（1740.8MB），计算得单序列最大上下文长度为 1740.8MB / 12KB ≈ 1451 tokens，而非N18声称的4000-5000 tokens。

## Evidence

先验知识/题面给定，逻辑校验通过：1740.8MB / 12KB ≈ 145.06 * 10 = 1450.6，四舍五入为1451 tokens，计算无误且符合显存约束逻辑。
