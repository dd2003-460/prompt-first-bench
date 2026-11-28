# N51: Qwen3.8-27B 在 vLLM 中 Decode 阶段的实际 Tokens/s/Worker 净吞吐量 = (Batch Size * 1) / (T_c

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

Qwen3.8-27B 在 vLLM 中 Decode 阶段的实际 Tokens/s/Worker 净吞吐量 = (Batch Size * 1) / (T_compute + T_comm + T_memory)，其中 T_memory 主导，估算值在 8-12 Tokens/s/Worker 区间（考虑 NVFP4 量化带来的访存减少和通信损耗）。

## Corrected Claim

Qwen3.8-27B 在 vLLM 中 Decode 阶段的理论净吞吐量遵循 (Batch Size * 1) / (T_compute + T_comm + T_memory) 规律，其中 T_memory 通常为主导项；在采用 NVFP4 量化等优化措施下，其实际吞吐量受硬件与配置影响显著，需实测确定，不宜直接断定为固定的 8-12 Tokens/s/Worker 区间。

## Evidence

[质询]该陈述包含具体的经验性能数值（8-12 Tokens/s/Worker）和特定的硬件/软件配置假设（NVFP4量化、vLLM实现细节），这些属于经验事实而非第一性原理可推导内容。虽然公式结构符合推理引擎的基本逻辑（吞吐量=并发/延迟），但具体数值高度依赖于硬件型号（如H100/A100）、网络拓扑及vLLM的具体版本优化，缺乏通用性。此外，'Qwen3.8-27B'这一具体模型版本及其在特定量化下的精确性能表现属于动态变化的经验数据，无法仅凭逻辑自洽确认为绝对真理。 | 逻辑自洽：吞吐量公式结构正确，T_memory主导Decode阶段符合大模型推理常识。但作为knowledge节点，虽免于外部来源缺失的惩罚，却因包含具体经验数值且存在‘特定配置下数值可能偏差’的可信攻击点（非硬逻辑错误，而是经验不确定性），根据规则‘challenge若成立且无法排除，同样降档为degraded’，故降级。
