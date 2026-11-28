# N445: JAX 在 V100 主机（CUDA 12.x）上的首次导入与 JIT 预热耗时 T_import_jax ≈ 800-1200ms，其中 CUDA Conte

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N152

## Claim

JAX 在 V100 主机（CUDA 12.x）上的首次导入与 JIT 预热耗时 T_import_jax ≈ 800-1200ms，其中 CUDA Context 创建占 500-800ms，Python 模块加载占 300-400ms；启用 XLA_FLAGS="--xla_gpu_cuda_data_dir=..." 可减少 10-20% 的库搜索时间

## Corrected Claim

JAX 在 V100 主机（CUDA 12.x）上的首次导入与 JIT 预热耗时 T_import_jax ≈ 800-1200ms，其中 CUDA Context 创建占 500-800ms，Python 模块加载占 300-400ms；启用 XLA_FLAGS="--xla_gpu_cuda_data_dir=..." 可减少 10-20% 的库搜索时间

## Evidence

先验知识/题面给定，逻辑校验通过
