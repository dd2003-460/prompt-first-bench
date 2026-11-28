# N147: Decode 阶段单步时长 (T_step) 的构成：T_step = T_compute + T_comm + T_memory_io。对于 27B 模型 F

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

Decode 阶段单步时长 (T_step) 的构成：T_step = T_compute + T_comm + T_memory_io。对于 27B 模型 FP16，每层 FLOPs ≈ 2 * params_per_layer * batch_size。Params/layer ≈ 27e9 / 64 ≈ 421M。Batch=1 时，每层 FLOPs ≈ 842 MFLOPs。64 层 ≈ 54 GFLOPs。V100 FP16 Tensor Core 峰值 125 TFLOPS，4 GPU 聚合 500 TFLOPS (理论)，实际利用率 30-40%，有效算力 ~150-200 TFLOPS。T_compute ≈ 54 GFLOPs / 175 TFLOPS ≈ 0.3 ms。

## Corrected Claim

Decode 阶段单步时长 (T_step) 的构成：T_step = T_compute + T_comm + T_memory_io。对于 27B 模型 FP16，每层 FLOPs ≈ 2 * params_per_layer * batch_size。Params/layer ≈ 27e9 / 64 ≈ 421M。Batch=1 时，每层 FLOPs ≈ 842 MFLOPs。64 层 ≈ 54 GFLOPs。V100 FP16 Tensor Core 峰值 125 TFLOPS，4 GPU 聚合 500 TFLOPS (理论)，实际利用率 30-40%，有效算力 ~150-200 TFLOPS。T_compute ≈ 54 GFLOPs / 175 TFLOPS ≈ 0.3 ms。

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型64层每层参数量约421M，Batch=1时单层FLOPs约为2*421M=842M，64层总FLOPs约为54G；V100 FP16 Tensor Core峰值125 TFLOPS，4卡聚合500 TFLOPS，按35%利用率估算有效算力175 TFLOPS，计算耗时54G/175T≈0.3ms，数值量级与逻辑推导均合理。

## Search Query

V100 FP16 tensor core utilization LLM inference compute time estimation
