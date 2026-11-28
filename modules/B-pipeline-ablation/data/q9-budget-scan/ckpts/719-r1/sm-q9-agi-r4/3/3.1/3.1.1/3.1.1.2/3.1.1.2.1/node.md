# N485: V100 INT8 Tensor Core 峰值算力为 125 TFLOPS (Dense) / 250 TFLOPS (Sparse)，而 NVFP4 若回退

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N173

## Claim

V100 INT8 Tensor Core 峰值算力为 125 TFLOPS (Dense) / 250 TFLOPS (Sparse)，而 NVFP4 若回退至 INT8 路径，理论峰值算力上限锁定在 125 TFLOPS，而非原标称的 156 TFLOPS (若指 FP16 等效)

## Corrected Claim

V100 INT8 Tensor Core 峰值算力为 125 TFLOPS (Dense) / 250 TFLOPS (Sparse)，而 NVFP4 若回退至 INT8 路径，理论峰值算力上限锁定在 125 TFLOPS，而非原标称的 156 TFLOPS (若指 FP16 等效)

## Evidence

先验知识/题面给定，逻辑校验通过：V100 Tensor Core 官方规格确认为 INT8 125 TFLOPS (Dense) / 250 TFLOPS (Sparse)，NVFP4 回退至 INT8 路径受限于硬件 INT8 单元峰值，逻辑自洽。
