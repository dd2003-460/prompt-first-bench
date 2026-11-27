# N397: Mac Studio M2 Ultra (192GB) 在运行 Qwen3-27B (INT4, 13.5GB) + 32K 上下文 (KV Cache ~2-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N138

## Claim

Mac Studio M2 Ultra (192GB) 在运行 Qwen3-27B (INT4, 13.5GB) + 32K 上下文 (KV Cache ~2-4GB) 时，实际内存占用约为 15-18GB，剩余可用内存 >170GB，因此不存在显存碎片或OOM风险，其‘无显存碎片问题’的优势主要相对于16GB显存的消费级GPU而言，而非相对于其自身的容量瓶颈。

## Corrected Claim

Mac Studio M2 Ultra (192GB) 在运行 Qwen3-27B (INT4, 13.5GB) + 32K 上下文 (KV Cache ~2-4GB) 时，实际内存占用约为 15-18GB，剩余可用内存 >170GB，因此不存在显存碎片或OOM风险，其‘无显存碎片问题’的优势主要相对于16GB显存的消费级GPU而言，而非相对于其自身的容量瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：192GB统一内存远大于15-18GB的模型+KV Cache占用，无OOM风险；对比16GB显存GPU的结论符合硬件常识。

## Search Query

Mac Studio M2 Ultra Qwen3 27B memory usage llama.cpp
