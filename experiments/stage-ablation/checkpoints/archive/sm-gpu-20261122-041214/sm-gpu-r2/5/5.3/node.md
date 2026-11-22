# N42: 性能基准测试偏差声明：公开基准（如 MLPerf、LLM Benchmark）通常使用特定优化栈（如 TensorRT-LLM、vLLM），不同推理引擎（Hug

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

性能基准测试偏差声明：公开基准（如 MLPerf、LLM Benchmark）通常使用特定优化栈（如 TensorRT-LLM、vLLM），不同推理引擎（Hugging Face Transformers vs vLLM vs TensorRT-LLM）对同一硬件的吞吐量差异可达 2-5 倍。推荐方案需假设使用最优推理引擎，否则实际性能可能低于预期 50% 以上。

## Corrected Claim

性能基准测试偏差声明：公开基准（如 MLPerf、LLM Benchmark）通常使用特定优化栈（如 TensorRT-LLM、vLLM），不同推理引擎（Hugging Face Transformers vs vLLM vs TensorRT-LLM）对同一硬件的吞吐量差异可达 2-5 倍。推荐方案需假设使用最优推理引擎，否则实际性能可能低于预期 50% 以上。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

vLLM vs TensorRT-LLM vs Hugging Face transformers throughput comparison 27B model
