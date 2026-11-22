# N138: 决策权重敏感性分析：若用户对‘首字延迟 (TTFT)’的权重高于‘解码速度 (Decode Speed)’，则 Prefill 算力（FLOPS）成为主导变量，

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

决策权重敏感性分析：若用户对‘首字延迟 (TTFT)’的权重高于‘解码速度 (Decode Speed)’，则 Prefill 算力（FLOPS）成为主导变量，此时 H100 或 RTX 5090 (更高 FLOPS) 的优先级上升；若权重偏向‘持续吞吐’，则显存带宽 (Memory Bandwidth) 成为主导变量，RTX 4090/5090 因带宽/价格比更高而占据优势。需明确用户场景是长文档处理 (TTFT 敏感) 还是长对话生成 (Decode 敏感)。

## Corrected Claim

决策权重敏感性分析：若用户对‘首字延迟 (TTFT)’的权重高于‘解码速度 (Decode Speed)’，则 Prefill 算力（FLOPS）成为主导变量，高FLOPS硬件优先级上升；若权重偏向‘持续吞吐’，则显存带宽 (Memory Bandwidth) 成为主导变量，高带宽/价格比硬件占据优势。需明确用户场景是长文档处理 (TTFT 敏感) 还是长对话生成 (Decode 敏感)。

## Evidence

[质询]该陈述包含具体的硬件性能对比结论（如RTX 4090/5090带宽/价格比优势、H100 FLOPS主导性），属于经验事实。参考来源仅涉及TTFT的工程优化概念，未提供具体硬件参数对比或价格数据，无法直接支持这些具体的硬件选型结论。 | 逻辑上，Prefill阶段计算密集（FLOPS敏感），Decode阶段访存密集（带宽敏感）符合LLM推理的基本原理；但具体硬件（H100/RTX 5090/4090）的性能与价格优势属于经验事实，来源[1]仅覆盖TTFT概念，未提供硬件对比数据，故降级。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2053775002785339097&rut=ebad221a3c2dbd83871b5c88bb7037faa1c8288249a729a552e28ca16ae3e38c', 'type': 'ddg', 'title': 'LLM流式输出深度解析：首字延迟(TTFT)的工程优化全指南'}
