# N319: H100 PCIe 80GB 的 FP8 推理吞吐上限修正：理论上限 75 tokens/s，但受 HBM 访问模式限制，实际吞吐在 Batch Size=1 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N108

## Claim

H100 PCIe 80GB 的 FP8 推理吞吐上限修正：理论上限 75 tokens/s，但受 HBM 访问模式限制，实际吞吐在 Batch Size=1 时约为 65-70 tokens/s，在 Batch Size=4 时约为 55-60 tokens/s（因内存带宽瓶颈），需根据实际 Batch Size 选择性能指标。

## Corrected Claim

H100 PCIe 80GB 的 FP8 推理性能受内存带宽和计算能力共同限制。在 Batch Size=1 时，吞吐主要受内存带宽瓶颈影响；随着 Batch Size 增加（如 Batch Size=4），通常系统总吞吐会提升直至计算饱和，而非下降。具体数值需根据模型大小和实际硬件配置实测确定，不宜直接断言 Batch Size=4 时吞吐低于 Batch Size=1。

## Evidence

[质询]数值量级与具体数值缺乏通用基准支持：H100 PCIe 80GB 的 FP8 理论峰值算力约为 1979 TFLOPS，若按典型 LLM 每 token 计算量估算，75 tokens/s 的理论上限及 65-70 tokens/s 的实际吞吐数值过于具体且偏低（通常 H100 在 Batch=1 时 FP8 推理吞吐远高于此，除非模型极大或受特定内存带宽严格限制），且 Batch Size 增加导致吞吐下降（55-60 < 65-70）违背通常的批处理加速直觉（通常 Batch 增加会提升吞吐直至饱和），此处可能混淆了单请求延迟与系统总吞吐，或特定极端场景下的表现被泛化。 | source=knowledge，但陈述中 Batch Size 增加导致吞吐下降的逻辑与常规 GPU 推理性能曲线（Batch 增加通常提升吞吐）存在矛盾，且具体数值缺乏通用基准支持，逻辑自洽性存疑。
