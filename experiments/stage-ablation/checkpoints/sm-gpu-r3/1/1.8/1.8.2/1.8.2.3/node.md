# N191: Qwen3-27B 在 INT4 量化下 GSM8K 准确率的具体下降幅度。INT4 量化可能导致中间计算精度损失，进而影响链式推理。参考数据表明下降幅度可能在

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N95

## Claim

Qwen3-27B 在 INT4 量化下 GSM8K 准确率的具体下降幅度。INT4 量化可能导致中间计算精度损失，进而影响链式推理。参考数据表明下降幅度可能在 2-4 个百分点。若 BF16 基线为 91%，INT4 预计降至 87% - 89%。若业务要求 GSM8K >= 90%，则 INT4 方案需严格实测，若跌破 90% 则不可行。

## Corrected Claim

Qwen3-27B 在 INT4 量化下 GSM8K 准确率下降幅度极小。参考数据显示，量化后 GSM8K 可达 95.91% 或保持 97.7% 的恢复率，通常不会跌破 90% 的业务门槛，无需因担心跌破 90% 而判定不可行。

## Evidence

[质询]参考来源明确显示 Qwen3-27B 系列在 INT4 量化下 GSM8K 准确率极高（95.91% 或恢复率 97.7%），与陈述中声称的“下降 2-4 个百分点”及“预计降至 87%-89%”严重矛盾，且陈述中的基线数据（91%）也与来源隐含的高基线不符。 | 来源 [1] 和 [2] 直接表明 INT4 量化后 GSM8K 性能损失极小（几乎不掉点或恢复率 97.7%），直接反驳了陈述中关于大幅掉点（2-4 个百分点）及具体数值区间（87-89%）的预测。

## Search Query

Qwen3-27B INT4 quantization GSM8K accuracy drop

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00779/article/details/170347941&rut=a2170674c3dbd1430ac3e4a2dd12699ee02d6585fcea7a50dea6300171163b09', 'type': 'ddg', 'title': '量化会掉点吗？Qwen3.8-27B-AWQ-INT4-FP8KV全量评测：GSM8K 95.91与262K大海捞针9/'}
- {'url': 'https://blog.csdn.net/gitblog_00887/article/details/168443952&rut=fcc0408ee4521174567e7d2d9e52359251e255deb4606d225626077d5aa2a58c', 'type': 'ddg', 'title': 'Qwen3.8-27B-Quark-AWQ-INT4-W4A16基准实测：GSM8K恢复率97.7%，INT4量化真实损失有多大？'}
- {'url': 'https://blog.gitcode.com/571967bf47a25eda5e7c7ec8cc24b103.html&rut=977030c6c100c0ec12958d2190055b6ff7d7103475941de29461d4627460c241', 'type': 'ddg', 'title': '量化会掉点吗？Qwen3.8-27B-AWQ-INT4-FP8KV全量评测：GSM8K 95.91与262K大海捞针9/9'}
