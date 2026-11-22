# N117: 延迟容忍度 T_max 需区分解码（Decode）与预填充（Prefill）两个阶段：对于交互式对话，Decode 延迟阈值通常设定为 T_decode < 1

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

延迟容忍度 T_max 需区分解码（Decode）与预填充（Prefill）两个阶段：对于交互式对话，Decode 延迟阈值通常设定为 T_decode < 100ms/token（即 >10 tokens/s），而 Prefill 延迟（首字延迟 TTFT）阈值通常设定为 < 2s（基于 32K 上下文输入长度）。

## Corrected Claim

延迟容忍度 T_max 需区分解码（Decode）与预填充（Prefill）两个阶段：对于交互式对话，Decode 延迟阈值通常设定为 T_decode < 100ms/token（即 >10 tokens/s），而 Prefill 延迟（首字延迟 TTFT）阈值通常设定为 < 2s（基于 32K 上下文输入长度）。

## Evidence

父节点级核验未通过：不完备, 有冗余（1. 正交性合格：三个子节点分别针对三种不同的硬件方案（RTX 4090, H100, M3 Ultra）进行估算，对象互斥，无矛盾。2. 完备性不合格：父节点明确定义了 'Decode' 和 'Prefill' 两个阶段的延迟阈值（T_decode < 100ms/token 和 TTFT < 2s），但所有子节点仅计算了 Prefill (TTFT)，完全缺失对 Decode 延迟的分析，导致未覆盖父节点的关键约束。3. 冗余性存在：三个子节点本质上是同一公式（FLOPs / Throughput）在不同硬件参数下的实例化，结构高度重复，应抽象为通用计算模型并列出硬件参数表，而非展开为三个独立的大段文本。）
