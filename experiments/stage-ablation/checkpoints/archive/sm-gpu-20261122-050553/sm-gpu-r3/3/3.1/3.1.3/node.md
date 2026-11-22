# N65: FP8 (E4M3) 精度下，Qwen3-27B 权重张量在 vLLM 或 PyTorch 后端中的实际存储格式与内存对齐开销：确认是否严格为 1 byte/p

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N16, N17, N18

## Claim

FP8 (E4M3) 精度下，Qwen3-27B 权重张量在 vLLM 或 PyTorch 后端中的实际存储格式与内存对齐开销：确认是否严格为 1 byte/param 或存在 block-wise 缩放因子导致的额外 overhead（如每 128 元素增加 2 bytes），从而影响总显存估算。

## Corrected Claim

FP8 (E4M3) 精度下，Qwen3-27B 权重张量的基础存储为 1 byte/param，但实际显存占用可能因 block-wise 缩放因子（如每 128 元素增加 2 bytes）而略有增加，具体 overhead 取决于 vLLM 或 PyTorch 后端的量化实现细节。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点存在逻辑包含关系导致的冗余（Node 2 是 Node 1 的直接计算结果，Node 3 是 Node 1 的反面假设）；且未覆盖父节点中明确提到的'内存对齐开销'（Memory Alignment Overhead），仅讨论了量化缩放因子（Scale Factor）带来的数据量增加，遗漏了硬件内存分配粒度可能带来的额外浪费。）

## Search Query

FP8 E4M3 quantization memory overhead block scaling vLLM Qwen
