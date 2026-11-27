# N20: Qwen3-27B模型在BF16精度下激活值峰值显存占用约为2.5GB（基于32K上下文长度和batch_size=1估算），FP8/INT8/NVFP4/W4

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

Qwen3-27B模型在BF16精度下激活值峰值显存占用约为2.5GB（基于32K上下文长度和batch_size=1估算），FP8/INT8/NVFP4/W4精度下激活值占用与BF16基本一致或略低

## Corrected Claim

Qwen3-27B模型在BF16精度下激活值峰值显存占用约为2.5GB（基于32K上下文长度和batch_size=1估算），FP8/INT8/NVFP4/W4精度下激活值占用与BF16基本一致或略低

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点1（公式定义）与子节点3、4（具体计算）存在逻辑包含关系，导致冗余；子节点2（定性修正）与子节点3（Flash Attention影响）在“精度与激活值关系”及“2.5GB估算来源”的论述上存在重叠和潜在矛盾（子节点3暗示Flash Attention会显著降低占用，子节点2则侧重精度无关性，未明确区分两者对峰值的不同贡献机制）。）
