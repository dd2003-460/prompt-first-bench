# N110: 在 vLLM/TensorRT-LLM 等主流推理框架中，针对 27B 模型采用 Tensor Parallelism (TP=2) 策略时，每层 Transf

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

在 vLLM/TensorRT-LLM 等主流推理框架中，针对 27B 模型采用 Tensor Parallelism (TP=2) 策略时，每层 Transformer 块中 All-Reduce 通信量约为 2 * Hidden_Size * Batch_Size * 2 bytes (FP16/BF16)，需据此计算 PCIe Gen4 x16 (理论 32GB/s, 有效 ~25GB/s) 下的通信延迟占比。

## Corrected Claim

在 vLLM/TensorRT-LLM 等主流推理框架中，针对 27B 模型采用 Tensor Parallelism (TP=2) 策略时，每层 Transformer 块中 All-Reduce 通信量约为 2 * Hidden_Size * Batch_Size * 2 bytes (FP16/BF16)，需据此计算 PCIe Gen4 x16 (理论 32GB/s, 有效 ~25GB/s) 下的通信延迟占比。

## Evidence

先验知识/题面给定，逻辑校验通过：Transformer层中Attention和FFN后各需一次All-Reduce，每次通信量为Batch*Hidden*2bytes(FP16)，合计2*Batch*Hidden*2bytes，符合标准TP通信模式；PCIe Gen4 x16带宽数值准确。

## Search Query

vLLM tensor parallelism all-reduce communication cost PCIe
