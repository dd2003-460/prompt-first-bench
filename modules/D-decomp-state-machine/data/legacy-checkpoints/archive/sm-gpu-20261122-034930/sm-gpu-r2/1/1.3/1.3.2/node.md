# N53: Activation Buffers 与临时张量开销：在推理框架 (vLLM/TensorRT-LLM) 中，用于存储中间激活值 (Activations) 和

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

Activation Buffers 与临时张量开销：在推理框架 (vLLM/TensorRT-LLM) 中，用于存储中间激活值 (Activations) 和临时计算结果的缓冲区，通常与 Batch_Size * seq_len 成正比。在 Batch=1, seq_len=32K 的长上下文场景下，这部分开销约为 2-4 GB；在短上下文 (4K) 场景下可忽略 (<0.5 GB)。

## Corrected Claim

Activation Buffers 与临时张量开销：在推理框架 (vLLM/TensorRT-LLM) 中，用于存储中间激活值 (Activations) 和临时计算结果的缓冲区，通常与 Batch_Size * seq_len 成正比。在 Batch=1, seq_len=32K 的长上下文场景下，这部分开销约为 2-4 GB；在短上下文 (4K) 场景下可忽略 (<0.5 GB)。

## Evidence

先验知识/题面给定，逻辑校验通过：在主流推理框架中，激活值内存占用确实与 Batch_Size * seq_len 成正比。对于 32K 长上下文，2-4 GB 的估算符合常见模型（如 7B-70B 参数规模）在 FP16/BF16 精度下的中间层激活存储量级；4K 短上下文下 <0.5 GB 亦符合线性缩放规律。
