# N31: 工作点C（低成本入门）：1×NVIDIA RTX 4090 24GB，W4精度，TTFT 15-30s，Tokens/s 12-18，单价约$1,600-1,8

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

工作点C（低成本入门）：1×NVIDIA RTX 4090 24GB，W4精度，TTFT 15-30s，Tokens/s 12-18，单价约$1,600-1,800，适合预算受限且能接受较高TTFT的个人开发者场景。

## Corrected Claim

工作点C（低成本入门）：1×NVIDIA RTX 4090 24GB，W4精度，适合预算受限的个人开发者场景。具体TTFT和Tokens/s取决于模型规模（如7B-27B），通常TTFT在秒级至十秒级，Tokens/s在10-20+区间，单价约$1,600-1,800。

## Evidence

父节点级核验未通过：不完备（子节点之间存在严重的逻辑矛盾（非正交）和事实错误（不完备/错误）。父节点声称该配置可行（TTFT 15-30s），但子节点1明确指出32K上下文下显存溢出，子节点2在16K上下文下估算TTFT仅5-8s且Tokens/s高达38，这与父节点的基准数据（15-30s TTFT, 12-18 Tokens/s）严重不符。此外，子节点2的显存带宽计算逻辑有误（通常Prefill是计算瓶颈而非带宽瓶颈，且权重读取次数计算需更严谨），导致推导出的性能指标与父节点描述的场景不匹配。）

## Search Query

RTX 4090 24GB single GPU inference Qwen 27B W4 quantization performance

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2077515232579273386&rut=bdd9c7024d132cde32617e4d144fa0023df952aee6da1f32b270e607843058fd', 'type': 'ddg', 'title': '一张rtx 4090能跑多大的ai模型？2026本地部署指南 - 知乎'}
