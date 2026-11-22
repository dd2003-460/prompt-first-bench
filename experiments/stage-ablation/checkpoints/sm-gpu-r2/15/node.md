# N173: 最终推荐的条件性约束示例 1：若用户主要任务为代码辅助且能接受 INT4 量化带来的 <5% 准确率下降，则推荐 RTX 4090 (24GB) + AWQ 量

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

最终推荐的条件性约束示例 1：若用户主要任务为代码辅助且能接受 INT4 量化带来的 <5% 准确率下降，则推荐 RTX 4090 (24GB) + AWQ 量化，3 年 TCO 最低 (~$3,000)；若用户要求 BF16 原生精度或需处理 64K+ 长上下文，则推荐 A100 80GB PCIe，尽管 TCO 较高 (~$13,000)，但消除了量化质量风险和显存瓶颈。

## Corrected Claim

最终推荐的条件性约束示例 1：若用户主要任务为代码辅助且能接受 INT4 量化带来的 <5% 准确率下降，则推荐 RTX 4090 (24GB) + AWQ 量化，3 年 TCO 最低 (~$3,000)；若用户要求 BF16 原生精度或需处理 64K+ 长上下文，则推荐 A100 80GB PCIe，尽管 TCO 较高 (~$13,000)，但消除了量化质量风险和显存瓶颈。

## Evidence

检索失败: no sources from any channel (all 5 failed)
