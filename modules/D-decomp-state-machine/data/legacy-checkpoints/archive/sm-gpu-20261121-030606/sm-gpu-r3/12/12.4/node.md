# N417: Intel Arc B580 显存容量为 12GB GDDR6，带宽 576 GB/s，远低于 1000 GB/s 下限且无法容纳 21GB 的最小显存需求；即

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N184

## Claim

Intel Arc B580 显存容量为 12GB GDDR6，带宽 576 GB/s，远低于 1000 GB/s 下限且无法容纳 21GB 的最小显存需求；即使考虑双卡（24GB），其 PCIe 互联带宽和驱动支持对 vLLM/llama.cpp 的兼容性存疑，且总功耗和 TCO 无优势，因此应从候选集中完全排除，不纳入后续对比。

## Corrected Claim

Intel Arc B580 显存容量为 12GB GDDR6，带宽 576 GB/s，远低于 1000 GB/s 下限且无法容纳 21GB 的最小显存需求；即使考虑双卡（24GB），其 PCIe 互联带宽和驱动支持对 vLLM/llama.cpp 的兼容性存疑，且总功耗和 TCO 无优势，因此应从候选集中完全排除，不纳入后续对比。

## Evidence

先验知识/题面给定，逻辑校验通过：Intel Arc B580 确实配备 12GB GDDR6 显存，带宽约 576 GB/s，远低于 1000 GB/s 且无法容纳 21GB 模型，排除理由成立。

## Search Query

Intel Arc B580 VRAM capacity bandwidth multi-GPU inference support
