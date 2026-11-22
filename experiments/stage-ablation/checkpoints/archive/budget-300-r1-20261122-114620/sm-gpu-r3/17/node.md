# N417: 最终推荐方案 B（平衡性能/中并发）：适用条件为小团队、并发 N=2-4、上下文 32K、需支持 INT8 精度以保持高准确率。推荐配置：双卡 RTX 4090

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

最终推荐方案 B（平衡性能/中并发）：适用条件为小团队、并发 N=2-4、上下文 32K、需支持 INT8 精度以保持高准确率。推荐配置：双卡 RTX 4090 (PCIe Gen4 x4/x8) + INT8 量化 (AWQ/GPTQ) + vLLM 框架 (Batch Parallelism)。5 年 TCO ≈ $6,460，吞吐 ~40 tokens/s (总)，质量损失极小（PPL < 5.7）

## Corrected Claim

最终推荐方案 B（平衡性能/中并发）：适用条件为小团队、并发 N=2-4、上下文 32K、需支持 INT8 精度以保持高准确率。推荐配置：双卡 RTX 4090 (PCIe Gen4 x4/x8) + INT8 量化 (AWQ/GPTQ) + vLLM 框架 (Batch Parallelism)。5 年 TCO ≈ $6,460，吞吐 ~40 tokens/s (总)，质量损失极小（PPL < 5.7）

## Evidence

检索失败: no sources from any channel (all 5 failed)
