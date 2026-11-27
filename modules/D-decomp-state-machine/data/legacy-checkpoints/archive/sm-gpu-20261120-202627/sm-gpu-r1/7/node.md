# N30: 候选硬件筛选边界：排除显存带宽 < 1TB/s 且无专用推理引擎支持的架构（如旧款消费卡 GTX 系列），因为 32K 上下文下 KV Cache 读写带宽是主

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

候选硬件筛选边界：排除显存带宽 < 1TB/s 且无专用推理引擎支持的架构（如旧款消费卡 GTX 系列），因为 32K 上下文下 KV Cache 读写带宽是主要瓶颈；同时排除单卡显存 < 16GB 且无法通过多卡互联聚合至 ≥ 30GB 的方案，除非采用激进的 W4 量化且接受 >5% 质量损失。

## Corrected Claim

候选硬件筛选应优先考虑显存带宽和总显存容量，因为32K上下文下KV Cache读写是主要瓶颈；具体阈值（如带宽<1TB/s或显存<16GB需排除）需根据特定模型规模和量化策略进行工程评估，而非绝对固定。

## Evidence

[质询]该陈述包含具体的工程经验阈值（如1TB/s带宽、16GB/30GB显存、5%质量损失），这些并非第一性原理可推导的数学或物理定律，而是依赖于具体模型规模、精度和硬件架构的经验性工程决策。参考来源仅提供了定性方向（带宽是瓶颈、显存限制），未提供这些具体数值阈值的直接支持或一致性验证。 | 来源[1]和[2]定性支持了显存带宽是推理瓶颈以及硬件物理边界的存在，但未提供具体的数值筛选标准（如1TB/s, 16GB等），属于经验事实且缺乏直接来源支持。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_28718345/article/details/166173047&rut=ba30de296786024eeb5ec90bc2ef0aee48b2cb2fea2ae6ef7553af025d98c49e', 'type': 'ddg', 'title': '大模型推理性能优化指南：从显存带宽到推理引擎选型实践-csdn博客'}
- {'url': 'https://blog.csdn.net/weixin_32596893/article/details/164776321&rut=8201a2f5583e1b0a25a1317e3daa3b3ffa35080ca5d44a97a28085cdb47f9bbf', 'type': 'ddg', 'title': 'Llm推理优化的硬件底层逻辑：从hbm带宽到sm调度的四层边界-csdn博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/162349721&rut=d530634f8b796c0e0e2665404664be0f7cbd874a0ab33a08f11d5d7741a3b9a1', 'type': 'ddg', 'title': '本地部署大模型踩坑实录，显卡选型与推理优化全攻略_晨xi的光-AI编程社区'}
