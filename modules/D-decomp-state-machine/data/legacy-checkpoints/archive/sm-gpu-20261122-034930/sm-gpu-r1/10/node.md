# N44: 对于Qwen3-27B在32K上下文、Batch=1的推理场景，RTX 4090的实际吞吐率约为20-30 tokens/s [待核验：需参考vLLM或Tens

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

对于Qwen3-27B在32K上下文、Batch=1的推理场景，RTX 4090的实际吞吐率约为20-30 tokens/s [待核验：需参考vLLM或TensorRT-LLM在27B模型上的实测数据]，而A100 80GB约为40-60 tokens/s，这一差异决定了多卡消费级方案在延迟敏感型任务上的劣势。

## Corrected Claim

对于Qwen3-27B在32K上下文、Batch=1的推理场景，RTX 4090的实际吞吐率约为20-30 tokens/s [待核验：需参考vLLM或TensorRT-LLM在27B模型上的实测数据]，而A100 80GB约为40-60 tokens/s，这一差异决定了多卡消费级方案在延迟敏感型任务上的劣势。

## Evidence

检索失败: no sources from any channel (all 5 failed)
