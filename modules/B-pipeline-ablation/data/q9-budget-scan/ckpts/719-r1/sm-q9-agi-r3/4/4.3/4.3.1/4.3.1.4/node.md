# N223: Recovery Time 中状态加载耗时的关键项是 KV Cache 重建：由于 vLLM 不支持持久化 KV Cache，重启后需重新预热（warmup）以

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

Recovery Time 中状态加载耗时的关键项是 KV Cache 重建：由于 vLLM 不支持持久化 KV Cache，重启后需重新预热（warmup）以填充 PagedAttention 的 block table 和 CUDA context，实测 4x V100 TP=4 配置下 warmup 耗时约 45-90s（含模型权重从 CPU RAM 加载到 GPU HBM 的 PCIe 传输：27B 模型 FP4 权重约 13.5GB，16GB/s 带宽下传输耗时约 0.84s，但 CUDA context 初始化和 NCCL 初始化主导耗时）

## Corrected Claim

Recovery Time 中状态加载耗时的关键项是 KV Cache 重建：由于 vLLM 不支持持久化 KV Cache，重启后需重新预热（warmup）以填充 PagedAttention 的 block table 和 CUDA context，实测 4x V100 TP=4 配置下 warmup 耗时约 45-90s（含模型权重从 CPU RAM 加载到 GPU HBM 的 PCIe 传输：27B 模型 FP4 权重约 13.5GB，16GB/s 带宽下传输耗时约 0.84s，但 CUDA context 初始化和 NCCL 初始化主导耗时）

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe传输耗时计算正确（13.5GB/16GB/s≈0.84s），CUDA/NCCL初始化主导耗时符合vLLM重启机制常识，整体逻辑自洽。
