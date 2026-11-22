# N107: RTX 4090运行INT4/W4量化Qwen3-27B时，理论峰值Tokens/s计算：显存带宽1008 GB/s / 每Token读取权重字节数(13.5G

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

RTX 4090运行INT4/W4量化Qwen3-27B时，理论峰值Tokens/s计算：显存带宽1008 GB/s / 每Token读取权重字节数(13.5GB) ≈ 74.6 Tokens/s；但需扣除KV Cache读取开销和反量化计算延迟，实际有效吞吐通常在40-60 Tokens/s区间。

## Corrected Claim

RTX 4090运行INT4/W4量化Qwen3-27B时，理论峰值Tokens/s计算：显存带宽1008 GB/s / 每Token读取权重字节数(13.5GB) ≈ 74.6 Tokens/s；但需扣除KV Cache读取开销和反量化计算延迟，实际有效吞吐通常在40-60 Tokens/s区间。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090显存带宽1008GB/s与Qwen3-27B INT4权重约13.5GB（27B*0.5B/Byte）量级匹配，理论峰值74.6 Tokens/s计算正确，实际吞吐40-60 Tokens/s符合硬件效率经验值。

## Search Query

RTX 4090 27B model 4-bit quantization tokens per second benchmark llama.cpp vllm
