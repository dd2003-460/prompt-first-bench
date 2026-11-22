# N330: RTX 4090 运行 Qwen3-27B W4 (AWQ) 精度时，显存占用约 13.5GB 权重 + 1.93GB KV + 1GB 开销 ≈ 16.4GB

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N108

## Claim

RTX 4090 运行 Qwen3-27B W4 (AWQ) 精度时，显存占用约 13.5GB 权重 + 1.93GB KV + 1GB 开销 ≈ 16.4GB，单卡可行；但 W4 相比 INT8 的精度损失在代码生成任务 (HumanEval) 上通常表现为 Pass@1 下降 5-10 个百分点，在通用知识任务 (MMLU) 上下降 2-5 个百分点，需评估该质量损失是否可接受以替代双卡 INT8 方案。

## Corrected Claim

RTX 4090 运行 Qwen3-27B W4 (AWQ) 精度时，显存占用约 13.5GB 权重 + 动态 KV Cache + 1GB 开销，单卡可行；但 W4 相比 INT8 的精度损失在代码生成任务 (HumanEval) 上通常表现为 Pass@1 显著下降，在通用知识任务 (MMLU) 上下降幅度较小，需评估该质量损失是否可接受以替代双卡 INT8 方案。

## Evidence

[质询]W4 (AWQ) 相比 INT8 在 HumanEval 上导致 Pass@1 下降 5-10 个百分点的量化数据缺乏普遍共识，不同模型架构和量化实现下波动较大，且 27B 模型在 4090 上运行时的具体 KV Cache 占用（1.93GB）依赖于具体的上下文长度假设，未明确说明，存在参数依赖风险。 | source=knowledge，逻辑自洽（显存估算量级合理：27B*0.5GB/4bit≈3.4GB? 不对，27B*0.5=13.5GB，计算正确；KV Cache 1.93GB 对应约 4k-8k 上下文合理），但精度损失的具体数值（5-10%）属于经验性统计结论，虽无来源矛盾，但作为 knowledge 节点，若挑战点指出其数值过于具体且缺乏通用性，应降级为定性描述以保严谨。注：根据规则，knowledge 节点逻辑自洽即 verified，但 challenge 若成立且无法排除则降档。此处 5-10% 是一个常见的经验范围，但并非绝对真理，且 KV 数值依赖上下文，故降级为定性表述更稳妥。

## Search Query

Qwen 27B AWQ 4bit vs INT8 benchmark accuracy drop
