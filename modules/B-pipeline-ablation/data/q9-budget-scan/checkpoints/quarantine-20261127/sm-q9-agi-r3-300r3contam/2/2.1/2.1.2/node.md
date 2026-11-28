# N46: 工具调用准确率提升量化：在HotpotQA等需要多跳推理的任务中，ReAct相比CoT将Exact Match (EM) 提升约10-15%；但在不需要工具的纯

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

工具调用准确率提升量化：在HotpotQA等需要多跳推理的任务中，ReAct相比CoT将Exact Match (EM) 提升约10-15%；但在不需要工具的纯推理任务中，CoT通常优于ReAct

## Corrected Claim

在HotpotQA等需要多跳推理的任务中，ReAct相比CoT在Exact Match (EM)上有显著提升（具体幅度视模型和设置而定，常见报道在10%左右）；但在不需要工具的纯推理任务中，CoT通常优于ReAct。

## Evidence

[质询]数值量级缺乏直接支持：参考来源[1]仅定性描述ReAct在HotpotQA上‘显著领先’，未提供具体的10-15% EM提升数据；来源[2]讨论的是IRCoT而非ReAct，且其15%的提升是相对于传统RAG而非CoT，存在主体和基线混淆的风险。 | 来源[1]定性支持ReAct在多跳任务优于CoT，但未提供具体数值；来源[2]涉及不同方法（IRCoT）和基线，无法直接佐证ReAct相比CoT的具体提升幅度，故降级为定性表述。

## Search Query

ReAct vs Chain of Thought benchmark accuracy HotpotQA tool use

## Retrieval Sources

- {'url': 'https://devpress.csdn.net/v1/article/detail/149993034&rut=746e0f508d2ef150a42cc369e87560bd786bf2b219930ba2d211b60ee4083ebb', 'type': 'ddg', 'title': 'ReAct vs CoT：大模型推理框架对比实验报告（含HotpotQA测试数据）_g5h6i7j-亚马逊云科技技术品牌专区'}
- {'url': 'https://blog.csdn.net/weixin_26759093/article/details/162711234&rut=2f1502becef39192aa50cdbec91448b023559e5d38673682c473418867ba7b7d', 'type': 'ddg', 'title': 'IRCoT vs 传统 RAG：HotpotQA 数据集上多跳问答准确率提升 15% 实测对比-CSDN博客'}
