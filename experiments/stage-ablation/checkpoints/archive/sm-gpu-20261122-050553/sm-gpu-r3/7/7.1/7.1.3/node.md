# N301: 工作点C（FP8 权重 + INT8 KV, 16K ctx）：显存占用 = 27GB (Weights) + 4GB (KV) = 31GB < 32GB，方

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N102

## Claim

工作点C（FP8 权重 + INT8 KV, 16K ctx）：显存占用 = 27GB (Weights) + 4GB (KV) = 31GB < 32GB，方案可行；这是 RTX 5090 单卡运行 Qwen3-27B 的最大稳定上下文长度，若需 32K 上下文必须升级至 2×RTX 5090 或 1×A100/H100。

## Corrected Claim

工作点C（FP8 权重 + INT8 KV, 16K ctx）：显存占用 = 27GB (Weights) + 4GB (KV) = 31GB < 32GB，方案可行；这是 RTX 5090 单卡运行 Qwen3-27B 的最大稳定上下文长度，若需 32K 上下文必须升级至 2×RTX 5090 或 1×A100/H100。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8权重(27B*1B=27GB)与INT8 KV(16K ctx估算约4GB)之和31GB小于RTX 5090的32GB显存，且32K上下文KV翻倍将导致显存溢出，需双卡或更大显存卡，推导自洽。
