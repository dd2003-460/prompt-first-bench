# N182: Tesla P40 (24GB) 不支持 FP8/INT8 硬件加速，仅支持 FP16/INT4 (软件模拟)，在 Qwen3-27B 推理中吞吐量约为 RTX

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N54

## Claim

Tesla P40 (24GB) 不支持 FP8/INT8 硬件加速，仅支持 FP16/INT4 (软件模拟)，在 Qwen3-27B 推理中吞吐量约为 RTX 4090 的 10-15%，且 24GB 显存不足以容纳 32K 上下文下的 KV Cache (需 >30GB)，方案不可行

## Corrected Claim

Tesla P40 (24GB) 无原生 FP8 硬件加速（INT8 有硬件加速但效率较低），在 Qwen3-27B 推理中吞吐量显著低于 RTX 4090（具体比例依量化和引擎而定，通常远低于50%），且 24GB 显存不足以容纳 32K 上下文下的 KV Cache 及模型权重，方案不可行

## Evidence

[质询]吞吐量对比数值（10-15%）缺乏具体基准测试支持，且不同量化方案（如AWQ vs GPTQ）和推理引擎（vLLM vs TGI）下性能差异巨大，该具体百分比可能因配置不同而显著偏离；此外，'不支持FP8/INT8硬件加速'表述略显绝对，P40虽无原生FP8 Tensor Core，但支持INT8 Tensor Core加速，仅FP8需软件模拟或降级为FP16/INT8，此处存在技术细节混淆风险。 | 先验知识/题面给定，逻辑校验通过：P40为Turing架构，确实无原生FP8支持，INT8有硬件加速但效率低于Ampere/Ada；24GB显存确实难以容纳32K上下文下27B模型的KV Cache（估算KV Cache大小：27B模型层数约64，head_dim 128，2*64*128*32768*2bytes ≈ 26GB，加上模型权重本身，总显存需求远超24GB），因此'方案不可行'结论在逻辑上成立。但吞吐量具体数值为经验事实，无来源支持，故降级。

## Search Query

Tesla P40 LLM inference performance FP16 only
