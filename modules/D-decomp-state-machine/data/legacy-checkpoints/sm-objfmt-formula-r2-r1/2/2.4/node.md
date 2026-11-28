# N16: 硬件支持矩阵：各候选显卡（4090/A100/H100/Mac）对目标精度（BF16/INT8/W4）的原生计算单元支持情况及加速比（TFLOPS 对比）。

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

硬件支持矩阵：各候选显卡（4090/A100/H100/Mac）对目标精度（BF16/INT8/W4）的原生计算单元支持情况及加速比（TFLOPS 对比）。

## Corrected Claim

各候选显卡（4090/A100/H100）在推理任务中存在显著的性能差异，其中H100性能优于A100，4090因性价比高成为常见选择，但具体各精度下的TFLOPS加速比需查阅官方规格表。

## Evidence

[质询]陈述要求提供具体的‘原生计算单元支持情况’及‘加速比（TFLOPS 对比）’数值，但参考来源仅提供了定性的性能比较（如H100比A100快数倍）和选型建议，缺乏针对BF16/INT8/W4各精度下的具体TFLOPS数值或硬件单元支持细节，无法验证具体的量化指标。 | 来源[1]和[2]确认了涉及显卡（4090/A100/H100）的存在及相对性能差异（间接支持），但未提供陈述中要求的特定精度下的TFLOPS具体数值或硬件单元支持矩阵，属于经验事实且缺乏直接数据支持。

## Search Query

RTX 4090 INT8 tensor core performance A100 INT8 performance H100 FP8 performance

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2092982765583184739&rut=b56fa34379436317140afcb8a2f86de43067aab066fafcfeb9cc50776fa5eb28', 'type': 'ddg', 'title': '2026年大模型推理GPU怎么选？A100、H800、H20、4090四张卡的真实取舍'}
- {'url': 'https://zhuanlan.zhihu.com/p/15975988730&rut=d923e91103367e2ae83be13851e5ff0ecb42b99837a1b6511e648eeb42c8e338', 'type': 'ddg', 'title': '深度学习"神卡"大揭秘：4090、V100、L40、A100、H100 横评'}
