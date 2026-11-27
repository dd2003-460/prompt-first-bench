# N181: H100 SXM 在 LLM 推理 Prefill 阶段（计算受限）的实测 MFU 范围，基于 SemiAnalysis 或 NVIDIA 白皮书数据，BF16

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N70

## Claim

H100 SXM 在 LLM 推理 Prefill 阶段（计算受限）的实测 MFU 范围，基于 SemiAnalysis 或 NVIDIA 白皮书数据，BF16 模式下通常为 45%-60%，FP8 模式下因 Tensor Core 算力翻倍且激活值精度降低，MFU 通常维持在 50%-65%，具体数值取决于 Batch Size 和序列长度

## Corrected Claim

H100 SXM在LLM推理Prefill阶段（计算受限）的MFU通常较高，BF16模式下因受限于Tensor Core峰值算力，FP8模式下因算力翻倍且精度降低，MFU通常高于BF16模式，具体数值取决于Batch Size和序列长度及软件栈优化程度。

## Evidence

[质询]参考来源仅提供了H100 SXM的硬件规格（如FP8/FP16算力、显存带宽），完全缺失关于LLM推理Prefill阶段实测MFU（Model FLOPs Utilization）的具体数值范围（45%-60%或50%-65%）的数据支持。 | 经验事实，逻辑自洽但缺来源支持。来源[2]和[3]确认了H100 SXM的FP8算力约为FP16的两倍（3958 vs 1979 TFLOPS），支持了'算力翻倍'的前提，但所有来源均未提供具体的MFU实测范围数据，无法验证45%-65%这一具体数值区间。

## Search Query

H100 SXM LLM inference prefill MFU BF16 FP8 SemiAnalysis benchmark

## Retrieval Sources

- {'url': 'https://infervisor.ai/gpus/nvidia-h100&rut=8034e7932c0d6525c6026de93720bb1f125e71add2a6fb7ad8e95c2da8472c36', 'type': 'ddg', 'title': 'NVIDIA H100 SXM for LLM inference: specs and measured results'}
- {'url': 'https://inferencex.semianalysis.com/chips/h100&rut=6288999ef3b04c4335f2b673fee144f9b1eb96492fdfd67f32bbcbb9abd5b818', 'type': 'ddg', 'title': 'NVIDIA H100 SXM Specs: ~$1.17/hr, 80 GB HBM3 | InferenceX'}
- {'url': 'https://gpusmith.com/hardware/gpus/nvidia-h100-sxm&rut=55f709c954c2dc2a5ec2014bee413884cdfa4a5d73d5f2d73b22f9fc76087cfd', 'type': 'ddg', 'title': 'NVIDIA H100 SXM Specs & Procurement | GPU Smith'}
