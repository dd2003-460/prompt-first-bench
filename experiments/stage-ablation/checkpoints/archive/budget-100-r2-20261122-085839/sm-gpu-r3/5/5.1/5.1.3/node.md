# N91: ONNX Runtime + NPU 方案部署成本：适配工时为 10-20 人天（需导出 ONNX 模型并处理 NPU 不支持的算子，如 RoPE 和特定 At

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25

## Claim

ONNX Runtime + NPU 方案部署成本：适配工时为 10-20 人天（需导出 ONNX 模型并处理 NPU 不支持的算子，如 RoPE 和特定 Attention 变体），Bug 修复成本为 $5000+（算子覆盖率通常 <80%，需大量 fallback 开发），总成本权重为 1.5-3.0（仅适用于特定硬件锁定场景）。

## Corrected Claim

ONNX Runtime + NPU 方案部署成本较高，通常涉及模型导出及算子适配（如 RoPE 等），需处理算子覆盖率不足导致的 fallback 开发，总成本权重显著高于纯 CPU/GPU 方案（适用于特定硬件锁定场景）。

## Evidence

[质询]具体数值（10-20人天、$5000+、权重1.5-3.0）属于高度依赖具体模型规模、NPU硬件型号及团队效率的经验性估算，缺乏通用标准，存在将特定案例泛化为普遍规律的风险。 | 先验知识/题面给定，逻辑校验通过（量级符合工程常识，但具体数值为经验估算，无外部来源直接支持，故降级为定性表述）

## Search Query

ONNX Runtime NPU operator coverage Qwen3 large language model
