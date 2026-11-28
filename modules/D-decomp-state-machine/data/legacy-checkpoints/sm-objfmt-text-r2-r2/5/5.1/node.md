# N27: Qwen3-27B 在 BF16 精度下，单卡（如 H100 80GB）的推理吞吐量基准值约为 150 tokens/s [待核验]

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N5

## Claim

Qwen3-27B 在 BF16 精度下，单卡（如 H100 80GB）的推理吞吐量基准值约为 150 tokens/s [待核验]

## Corrected Claim

Qwen3-27B 在 BF16 精度下，单卡（如 H100 80GB）的推理吞吐量基准值约为 150 tokens/s（需进一步验证具体硬件与模型版本的匹配性）

## Evidence

父节点级核验未通过：不完备（子节点正交且无冗余，分别提供了硬件参数、理论计算逻辑和效率修正系数。但存在严重的事实错误和完备性问题：1. Qwen3-27B 并非 MoE 模型，子节点2中提及的'MoE 路由开销'是错误的；2. 子节点2称每 token 读取字节数约为 27.8GB 是错误的，BF16 下 27B 参数量模型权重约为 54GB，但 Decode 阶段主要瓶颈是权重加载，单 token 读取量应接近总权重大小（若未量化）或更少（若量化），但表述混淆了'模型大小'与'每token读取量'的概念，且未考虑 Batch Size 对吞吐的影响，无法直接得出 150 tokens/s 这一特定基准值的推导路径，缺乏对 Batch Size 这一关键变量的覆盖。）

## Search Query

Qwen3-27B H100 inference throughput tokens per second

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2072597504793880030&rut=304ab9b1949db5d068e5f24670c8b7c3dcf1028c44ee8d381a92e4513f6bc363', 'type': 'ddg', 'title': 'Qwen3.8-27B 的 BF16、FP8、MTP、单卡表现，以及与 Qwen3.6 MoE 的差距'}
