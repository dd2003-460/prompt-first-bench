# N86: H100 对 INT8 (W8A16) 精度的原生计算支持：SM 9.0 支持 INT8 Tensor Cores，标称 INT8 稀疏算力为 1979 TOP

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

H100 对 INT8 (W8A16) 精度的原生计算支持：SM 9.0 支持 INT8 Tensor Cores，标称 INT8 稀疏算力为 1979 TOPS，密集算力约为 989.5 TOPS，支持 vLLM 的 INT8 量化推理内核。

## Corrected Claim

H100 对 INT8 (W8A16) 精度的原生计算支持：SM 9.0 支持 INT8 Tensor Cores，标称 INT8 稀疏算力为 1979 TOPS，密集算力约为 989.5 TOPS，支持 vLLM 的 INT8 量化推理内核。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM5 官方规格中 INT8 稀疏算力确为 1979 TOPS，密集算力为其一半即 989.5 TOPS，且 SM 9.0 架构原生支持 INT8 Tensor Cores，数据自洽且符合硬件事实。

## Search Query

H100 INT8 tensor core performance TOPS dense sparse
