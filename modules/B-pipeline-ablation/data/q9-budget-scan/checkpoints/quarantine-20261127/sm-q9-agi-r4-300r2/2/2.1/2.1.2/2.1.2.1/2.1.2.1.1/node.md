# N295: HotpotQA 多跳推理中 ReAct 相比 CoT 的增益分解：ΔEM = ΔRetrieval_Accuracy * W_retrieval + ΔRea

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N119

## Claim

HotpotQA 多跳推理中 ReAct 相比 CoT 的增益分解：ΔEM = ΔRetrieval_Accuracy * W_retrieval + ΔReasoning_Consistency * W_reasoning；在 Qwen3-27B 上，ΔRetrieval_Accuracy (因模型更强) 贡献 +3.5%，ΔReasoning_Consistency (因工具调用干扰) 贡献 -1.2%，净增益 +2.3%，低于 GPT-3.5 时代的 +12.4%。

## Corrected Claim

在HotpotQA多跳推理中，ReAct相比CoT通常表现出更高的答案准确率（来源[1][2]），但其具体增益幅度及在不同模型（如Qwen3-27B）上的归因分解需依赖特定实验数据，现有参考来源未提供确切的数值分解。

## Evidence

[质询]具体数值（+3.5%, -1.2%, +2.3%, +12.4%）及特定模型（Qwen3-27B）的归因分解缺乏来源直接支持，且‘GPT-3.5时代’的对比基准模糊，疑似虚构或过度精确的经验数据。 | 来源[1][2]仅定性支持ReAct在HotpotQA上优于CoT，未提供具体的增益分解数值或Qwen3-27B的实验数据；该陈述包含具体经验参数，属经验事实，逻辑自洽但缺来源直接支持，故降级。

## Search Query

Qwen3 27B HotpotQA ReAct vs Chain-of-Thought exact match performance comparison

## Retrieval Sources

- {'url': 'https://blog.csdn.net/g5h6i7j/article/details/149993034&rut=2d54738704cb9db11d1faf63aef6f9724daf5546c5db1414a14fde8c6edac6ed', 'type': 'ddg', 'title': 'ReAct vs CoT：大模型推理框架对比实验报告（含HotpotQA测试数据）-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/149993034&rut=746e0f508d2ef150a42cc369e87560bd786bf2b219930ba2d211b60ee4083ebb', 'type': 'ddg', 'title': 'ReAct vs CoT：大模型推理框架对比实验报告（含HotpotQA测试数据）_g5h6i7j-亚马逊云科技技术品牌专区'}
- {'url': 'https://blog.csdn.net/weixin_29064009/article/details/159144820&rut=8a3ed8adeb44f48745468fd71b42442ab3f9412235be3118a3f766031ed22a03', 'type': 'ddg', 'title': 'ReAct实战：如何用大语言模型实现推理与行动的完美结合（附HotpotQA案例）-CSDN博客'}
