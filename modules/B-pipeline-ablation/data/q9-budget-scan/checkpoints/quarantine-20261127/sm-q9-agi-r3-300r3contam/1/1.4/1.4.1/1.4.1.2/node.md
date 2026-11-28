# N108: 关键事实提取任务的 Recall 计算公式：R_extraction = (N_retrieved_correct / N_gold_total) * 100%

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N38

## Claim

关键事实提取任务的 Recall 计算公式：R_extraction = (N_retrieved_correct / N_gold_total) * 100%，其中 N_retrieved_correct 为模型成功提取且正确的关键事实数，N_gold_total 为 Gold Standard 中定义的关键事实总数；对于 27B 模型，R_extraction 受限于上下文窗口内信息的注意力分布，预期在长文档（>8k tokens）场景下降至 60%-75%。

## Corrected Claim

关键事实提取任务的 Recall 计算公式：R_extraction = (N_retrieved_correct / N_gold_total) * 100%，其中 N_retrieved_correct 为模型成功提取且正确的关键事实数，N_gold_total 为 Gold Standard 中定义的关键事实总数。

## Evidence

[质询]陈述后半部分关于“27B模型在长文档（>8k tokens）场景下Recall预期降至60%-75%”属于具体的经验性能数据，缺乏通用性，且不同架构、训练数据及具体任务难度会导致极大差异，无法作为普适事实成立。 | 来源[1][2]直接支持Recall的标准定义（TP/(TP+FN)），与公式逻辑一致；但所有来源均未提供特定模型（27B）在特定长度（>8k）下的具体性能数值，该部分为无来源支持的经验断言。

## Search Query

LLM information extraction recall long document attention decay

## Retrieval Sources

- {'url': 'https://blog.csdn.net/baidu_38225647/article/details/158326183&rut=3e433ab3a3d6267a278ab3879c7945d75f434e112640e3d79b3daa6001c3f960', 'type': 'ddg', 'title': '精确率(Precision)、召回率(Recall) 超详细图解-CSDN博客'}
- {'url': 'https://blog.csdn.net/W1995S/article/details/114988637&rut=189b79cbc325f5b31125d6181a1a9bf1d675962f37520debede07d3b24847ffd', 'type': 'ddg', 'title': '召回率（recall）和精度（precision）_recall precision-CSDN博客'}
- {'url': 'https://cloud.tencent.com/developer/article/2658116&rut=6a01bc017c0700cc94ed8b76b95eb139712a6ad713993cde54ad00fbeb6e6e2d', 'type': 'ddg', 'title': 'RAG评估必备 | Recall@K、MRR、NDCG 三指标，一文彻底讲透-腾讯云开发者社区-腾讯云'}
