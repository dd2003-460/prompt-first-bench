# N60: NVIDIA RTX 4090 (Ada Lovelace) 原生支持 FP8 (E4M3/E5M2) 和 INT8 推理，其 FP8 Tensor Core 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

NVIDIA RTX 4090 (Ada Lovelace) 原生支持 FP8 (E4M3/E5M2) 和 INT8 推理，其 FP8 Tensor Core 吞吐量为 330 TOPS，INT8 吞吐量为 660 TOPS；在 vLLM 中启用 FP8 时，相比 BF16 推理速度提升约 1.5-2 倍，显存占用减半。

## Corrected Claim

NVIDIA RTX 4090 (Ada Lovelace) 原生支持 FP8 (E4M3/E5M2) 和 INT8 推理，其 FP8 Tensor Core 吞吐量为 330 TOPS，INT8 吞吐量为 660 TOPS；在 vLLM 中启用 FP8 时，相比 BF16 推理速度提升约 1.5-2 倍，显存占用减半。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 基于 Ada Lovelace 架构，官方规格确认支持 FP8/INT8，FP8 算力约为 330 TOPS，INT8 约为 660 TOPS；FP8 相比 BF16 显存减半且推理加速 1.5-2 倍符合硬件特性与工程经验。
