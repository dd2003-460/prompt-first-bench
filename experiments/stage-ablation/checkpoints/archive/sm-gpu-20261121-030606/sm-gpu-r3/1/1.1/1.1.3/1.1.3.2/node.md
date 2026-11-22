# N194: 显存碎片与 CUDA 上下文开销 (Overhead) 量化：CUDA 上下文初始化、PyTorch 运行时开销及显存碎片（Fragmentation）通常占用

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

显存碎片与 CUDA 上下文开销 (Overhead) 量化：CUDA 上下文初始化、PyTorch 运行时开销及显存碎片（Fragmentation）通常占用 1-3GB 额外显存。在 34.2GB 理论下限基础上，实际所需显存 = 34.2GB + Overhead。若 Overhead 为 2GB，总需求为 36.2GB。这进一步证实 RTX 4090 (24GB) 在 FP8 下不可行，即使仅存权重+KV (31.7GB) 也超出其物理上限。

## Corrected Claim

显存碎片与 CUDA 上下文开销 (Overhead) 量化：CUDA 上下文初始化、PyTorch 运行时开销及显存碎片（Fragmentation）通常占用 1-3GB 额外显存。在 34.2GB 理论下限基础上，实际所需显存 = 34.2GB + Overhead。若 Overhead 为 2GB，总需求为 36.2GB。这进一步证实 RTX 4090 (24GB) 在 FP8 下不可行，即使仅存权重+KV (31.7GB) 也超出其物理上限。

## Evidence

先验知识/题面给定，逻辑校验通过：CUDA上下文及PyTorch运行时开销在1-3GB范围内符合工程经验，算术推导（34.2+2=36.2）正确，且36.2GB>24GB的结论逻辑自洽。

## Search Query

CUDA context memory overhead pytorch inference fragmentation
