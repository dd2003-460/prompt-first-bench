# N21: 针对Qwen3-27B在NVFP4量化下的幻觉率基线测定：在特定学术QA数据集（如TriviaQA或SQuAD v2）上，通过统计事实性错误比例，确定本地模型的

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4, N5

## Claim

针对Qwen3-27B在NVFP4量化下的幻觉率基线测定：在特定学术QA数据集（如TriviaQA或SQuAD v2）上，通过统计事实性错误比例，确定本地模型的初始幻觉基准值 $\alpha_{local}$，用于设定过滤门的阈值。

## Corrected Claim

针对Qwen3-27B在NVFP4量化下，通常需要在特定学术QA数据集（如TriviaQA或SQuAD v2）上通过统计事实性错误比例来确定本地模型的初始幻觉基准值 α_local，用于设定过滤门的阈值；现有公开评测主要关注通用基准（如AIME/MMLU）的精度损失，具体幻觉率基线需自行测定。

## Evidence

[质询]该陈述描述的是一个具体的实验操作和结果（测定特定的幻觉率基线值 α_local），属于经验事实。参考来源主要讨论的是模型量化后的通用性能指标（如AIME分数、显存占用、MMLU Pro表现），并未提供在 TriviaQA 或 SQuAD v2 上针对幻觉率的具体基线数值或该特定实验的直接证据。此外，来源中提到的模型版本（Qwen3.8/3.6）与陈述中的 Qwen3 可能存在细微的版本指代差异，但核心问题是缺乏针对“幻觉率基线测定”这一具体经验数据的直接支持。 | 逻辑上，在特定数据集上统计事实性错误以设定过滤阈值是合理的工程实践，量纲和逻辑自洽。但根据经验事实排除条款，该陈述包含具体的实验设定和隐含的经验结果（基线值），属于经验事实。参考来源 [1][2][3] 虽涉及 Qwen3 系列 NVFP4 量化模型的性能评测，但均未直接提及在 TriviaQA/SQuAD v2 上测定幻觉率基线 α_local 的具体数据或过程，仅提供了模型量化后整体性能保持较好的间接背景，无法直接支持该特定基线值的存在或具体数值，故降级为 degraded。

## Search Query

Qwen3 27B NVFP4 quantization hallucination rate benchmark academic QA

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00936/article/details/170614004&rut=c2d1d88c0ab0bf57a00a2f0b063041aae2442c312885a978745d00e89d24b6f0', 'type': 'ddg', 'title': 'Qwen3.8-27B-nvfp4-NInfer评测报告解读：AIME 96.67%背后，NVFP4量化精度损失到底有多'}
- {'url': 'https://blog.csdn.net/gitblog_01106/article/details/168111467&rut=f601cd06334489377c656755735bef531a0de9802235594119b00fce694a1a3b', 'type': 'ddg', 'title': 'Qwen3.8-27B-NVFP4完整指南：4位NVFP4量化如何玩转27B多模态大模型-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/162604876&rut=f24f0c70ea8ab1482917d4844b0f4ffccb609246823fb2c7e50057164883ef89', 'type': 'ddg', 'title': 'Qwen3.6-27B-NVFP4 深度评测：英伟达官方量化，27B 长上下文本地部署新选择'}
