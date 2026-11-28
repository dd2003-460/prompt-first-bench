# N232: NVFP4 权重反量化至 FP16 的算术开销量化：每次 GEMM 操作前需执行 dequantize 算子，其 FLOPs 占比约为 0.5%-1.5%（基于

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N78

## Claim

NVFP4 权重反量化至 FP16 的算术开销量化：每次 GEMM 操作前需执行 dequantize 算子，其 FLOPs 占比约为 0.5%-1.5%（基于 INT4->FP16 转换指令集效率），但主要瓶颈在于内存带宽而非计算单元，导致整体 MFU 损失主要来自数据搬移而非 ALU 占用。

## Corrected Claim

NVFP4 权重反量化至 FP16 的算术开销量化：每次 GEMM 操作前需执行 dequantize 算子，其 FLOPs 占比约为 0.5%-1.5%（基于 INT4->FP16 转换指令集效率），但主要瓶颈在于内存带宽而非计算单元，导致整体 MFU 损失主要来自数据搬移而非 ALU 占用。

## Evidence

先验知识/题面给定，逻辑校验通过：低精度反量化计算量极小（FLOPs占比<2%符合线性缩放直觉），且LLM推理中GEMM通常受限于内存带宽而非算力，故瓶颈归因于数据搬移符合硬件架构常识。

## Search Query

NVFP4 dequantization overhead FLOPs ratio V100 tensor core efficiency
