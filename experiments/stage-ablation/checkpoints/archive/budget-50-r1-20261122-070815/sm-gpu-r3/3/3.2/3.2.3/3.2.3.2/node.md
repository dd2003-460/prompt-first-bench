# N266: A100 不支持原生 FP8，FP8 模型在 A100 上运行时需反量化为 BF16 进行计算，导致算力回退至 BF16 水平（312 TFLOPS）且额外增加

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

A100 不支持原生 FP8，FP8 模型在 A100 上运行时需反量化为 BF16 进行计算，导致算力回退至 BF16 水平（312 TFLOPS）且额外增加反量化开销（约 5-10% 延迟），因此 A100 上 FP8 的“有效算力”并非 624 TFLOPS，而是略低于 BF16 有效算力；需对比 A100 上 BF16 与 FP8-Dequant 的实测吞吐以量化该开销。

## Corrected Claim

A100 不支持原生 FP8，FP8 模型在 A100 上运行时需反量化为 BF16 进行计算，导致算力回退至 BF16 水平（312 TFLOPS）且额外增加反量化开销（约 5-10% 延迟），因此 A100 上 FP8 的“有效算力”并非 624 TFLOPS，而是略低于 BF16 有效算力；需对比 A100 上 BF16 与 FP8-Dequant 的实测吞吐以量化该开销。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 (GA100) 架构确实不支持原生 FP8 计算单元，FP8 需反量化为 BF16/FP16 计算，其 BF16 峰值算力为 312 TFLOPS，逻辑自洽且符合硬件事实。
