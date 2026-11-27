# N140: AMD ROCm 对 RX 7900 XTX 的支持现状：ROCm 6.1.0 及以上版本才提供稳定的 PyTorch 2.3+ 支持；Qwen3-27B 在 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N45, N46, N47

## Claim

AMD ROCm 对 RX 7900 XTX 的支持现状：ROCm 6.1.0 及以上版本才提供稳定的 PyTorch 2.3+ 支持；Qwen3-27B 在 ROCm 上的 INT8 量化推理存在已知 Bug (Issue #12345)，导致部分层计算错误，需使用社区补丁或回退至 FP16 (显存占用增加 100%)。

## Corrected Claim

AMD ROCm 6.1.2 版本已在 RX 7900 XTX 上成功部署 Qwen3.8-27B 模型，支持量化推理（如IQ4），但关于 INT8 量化存在特定 Bug (Issue #12345) 的说法在现有来源中未获证实。

## Evidence

[质询]陈述中提到的具体Bug编号（Issue #12345）及“ROCm 6.1.0及以上才提供稳定PyTorch 2.3+支持”的硬性版本门槛在参考来源中无据可查，且来源[2]和[3]明确显示在ROCm 6.1.2环境下成功部署并运行了Qwen3.8-27B（注意：来源中模型名为Qwen3.8-27B，与陈述中的Qwen3-27B存在细微差异，但即便假设指代同一类模型，来源也未提及INT8量化存在导致计算错误的已知Bug，反而展示了量化部署的成功案例），陈述中的具体技术故障描述与来源提供的成功部署事实相矛盾或至少无法被支持，且Bug编号疑似虚构。 | 来源[2]和[3]证实了在ROCm 6.1.2环境下成功部署Qwen3.8-27B（含量化），未提及INT8量化存在导致计算错误的已知Bug，且来源中未出现Issue #12345，陈述中的具体故障细节与来源展示的成功实践不符。

## Search Query

AMD ROCm 6.1 RX 7900 XTX Qwen3-27B INT8 bug PyTorch compatibility

## Retrieval Sources

- {'url': 'https://smeltcore.com/recipes/qwen3-8-27b-on-rx-7900-xtx-128k-context-vision-chat-on-rocm-with-llama-cpp/&rut=a27ab7fd8a93df0768b34b3c20459d287613ebd6b7196394dcebc8fd986c3453', 'type': 'ddg', 'title': 'Qwen3.8-27B on RX 7900 XTX: 128K-context vision chat on ROCm with llama.cpp'}
- {'url': 'https://blog.csdn.net/weixin_26861329/article/details/167112489&rut=0c94a8837d0b1c3adc239ea522ca74eb50b90cb3910de1fe849d0139e38d752e', 'type': 'ddg', 'title': 'AMD 7900 XTX本地跑Qwen3.8-27B实战：hipEngine+ROCm部署全解析-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_26808439/article/details/167112488&rut=e9b797d7c0e72ffa62958992135c540765b11092441cab04dddab427667ecab1', 'type': 'ddg', 'title': 'AMD 7900 XTX跑Qwen3.8大模型：hipEngine调优深度实录 - CSDN博客'}
