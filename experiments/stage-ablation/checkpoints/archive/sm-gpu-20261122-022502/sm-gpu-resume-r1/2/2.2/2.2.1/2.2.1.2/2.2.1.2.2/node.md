# N580: CUDA Context 和框架缓冲 ~1.5GB 的估计依据：PyTorch 运行时开销 ~0.5GB，CUDA Context 初始化 ~0.5GB，vLL

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N177

## Claim

CUDA Context 和框架缓冲 ~1.5GB 的估计依据：PyTorch 运行时开销 ~0.5GB，CUDA Context 初始化 ~0.5GB，vLLM 内部数据结构 (如 Block Table) ~0.5GB。该估计在 batch_size=1 时成立，若 batch_size 增大，Block Table 和调度器开销将线性增长，需重新评估 OOM 风险。

## Corrected Claim

CUDA Context 和框架缓冲 ~1.5GB 的估计依据：PyTorch 运行时开销 ~0.5GB，CUDA Context 初始化 ~0.5GB，vLLM 内部数据结构 (如 Block Table) ~0.5GB。该估计在 batch_size=1 时成立，若 batch_size 增大，Block Table 和调度器开销将线性增长，需重新评估 OOM 风险。

## Evidence

先验知识/题面给定，逻辑校验通过
