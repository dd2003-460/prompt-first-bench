# N394: 多卡方案（2x GPU）的系统级MTBF计算：对于2x RTX 4090张量并行方案，系统MTBF = 单卡MTBF / 2（假设故障独立），即约为1.5-2年

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N153

## Claim

多卡方案（2x GPU）的系统级MTBF计算：对于2x RTX 4090张量并行方案，系统MTBF = 单卡MTBF / 2（假设故障独立），即约为1.5-2年；对于2x H100方案，系统MTBF约为2.5-3.5年。此值用于计算C_maint中的故障更换频率。

## Corrected Claim

多卡方案（2x GPU）的系统级MTBF计算：对于2x RTX 4090张量并行方案，系统MTBF = 单卡MTBF / 2（假设故障独立），即约为1.5-2年；对于2x H100方案，系统MTBF约为2.5-3.5年。此值用于计算C_maint中的故障更换频率。

## Evidence

先验知识/题面给定，逻辑校验通过：系统MTBF=单卡MTBF/N符合独立故障假设下的可靠性理论，数值量级（1.5-3.5年）符合高端GPU硬件的典型工程经验值。
