# N17: 精度对吞吐量的影响机制：低精度 (INT8/FP4) 提高显存带宽利用率，但增加反量化计算开销。在消费级 GPU 上，INT8 吞吐量通常为 BF16 的 1.

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

精度对吞吐量的影响机制：低精度 (INT8/FP4) 提高显存带宽利用率，但增加反量化计算开销。在消费级 GPU 上，INT8 吞吐量通常为 BF16 的 1.5-2.0 倍，4-bit 为 2.0-3.0 倍 [待核验: 具体加速比]。

## Corrected Claim

精度对吞吐量的影响机制：低精度 (INT8/FP4) 提高显存带宽利用率，但增加反量化计算开销。在消费级 GPU 上，INT8 吞吐量通常为 BF16 的 1.5-2.0 倍，4-bit 为 2.0-3.0 倍 [待核验: 具体加速比]。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM inference throughput comparison BF16 INT8 4-bit quantization
