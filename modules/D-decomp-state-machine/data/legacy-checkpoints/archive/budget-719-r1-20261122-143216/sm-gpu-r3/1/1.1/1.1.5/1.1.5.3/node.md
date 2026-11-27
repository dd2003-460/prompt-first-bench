# N162: vLLM 和 TensorRT-LLM 的框架内部缓冲（如输入/输出队列、中间张量缓存）在 32K 上下文、batch_size=1 时的额外显存占用约为 50

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

vLLM 和 TensorRT-LLM 的框架内部缓冲（如输入/输出队列、中间张量缓存）在 32K 上下文、batch_size=1 时的额外显存占用约为 500 MB-1 GB，需结合具体版本和配置实测。

## Corrected Claim

vLLM 和 TensorRT-LLM 的框架内部缓冲（如输入/输出队列、中间张量缓存）在 32K 上下文、batch_size=1 时的额外显存占用约为 500 MB-1 GB，需结合具体版本和配置实测。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

vLLM TensorRT-LLM internal buffer memory overhead 32K batch 1
