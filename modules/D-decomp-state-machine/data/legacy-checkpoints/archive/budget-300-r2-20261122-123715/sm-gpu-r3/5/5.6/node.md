# N102: AMD MI300X ROCm 生态兼容性：vLLM 对 MI300X 的支持在 ROCm 6.0+ 中达到 90% 的 CUDA 性能水平 (基于公开 ben

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N23, N24, N25

## Claim

AMD MI300X ROCm 生态兼容性：vLLM 对 MI300X 的支持在 ROCm 6.0+ 中达到 90% 的 CUDA 性能水平 (基于公开 benchmark)，但 TensorRT-LLM 不支持，需使用 vLLM 或 SGLang；性能损失系数 k_rocm ≈ 0.9，主要源于算子优化不足。

## Corrected Claim

AMD MI300X ROCm 生态兼容性：vLLM 对 MI300X 有良好支持（基于 ROCm 6.0+ 公开 benchmark），性能接近但略低于同级 NVIDIA GPU（具体比例视模型和负载而定，通常认为在 80%-90% 区间）；TensorRT-LLM 不支持 MI300X，需使用 vLLM 或 SGLang；性能差异主要源于算子优化程度不同。

## Evidence

[质询]陈述中具体的数值指标（90% CUDA性能水平、k_rocm ≈ 0.9）属于经验事实，参考来源仅提供了vLLM在MI300X上的基准测试文档链接和一般性优化指南，并未直接给出与CUDA对比的具体百分比数值或性能损失系数，存在来源未直接支持具体数值的风险。 | 来源[1][2][3]确认了vLLM在AMD MI300X上的支持及基准测试存在，间接支持了生态兼容性部分，但缺乏对'90%性能'和'k_rocm=0.9'的直接数值证据，且TensorRT-LLM不支持MI300X为已知事实（逻辑自洽），故降级为定性表述。

## Search Query

AMD MI300X vLLM performance benchmark ROCm vs CUDA

## Retrieval Sources

- {'url': 'https://rocm.docs.amd.com/en/docs-6.2.0/how-to/performance-validation/mi300x/vllm-benchmark.html&rut=0028ce4a70255e9c900930c113e9673e8d4f4aa946af85ae650af2fc6469155c', 'type': 'ddg', 'title': 'LLM inference performance validation on AMD Instinct MI300X'}
- {'url': 'https://rocm.docs.amd.com/en/docs-6.4.0/how-to/rocm-for-ai/inference/vllm-benchmark.html&rut=4897bacb8292c26ee06ba52ff5460e7ff591eb8e78edc4920f20291f889d671d', 'type': 'ddg', 'title': 'vLLM inference performance testing — ROCm Documentation'}
- {'url': 'https://rocm.blogs.amd.com/artificial-intelligence/LLM_Inference/README.html&rut=857345f61464929e5ff52405bfd84b63e98604c0925231347b2bc1c3e08def65', 'type': 'ddg', 'title': 'Best practices for competitive inference optimization on AMD Instinct ...'}
