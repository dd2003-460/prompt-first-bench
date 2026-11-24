# N660: 档位上限工作点（Traffic=50 TB）：Cost_50TB_segment = (50,000 - 10,000) GB * 0.20 CNY/GB = 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N223

## Claim

档位上限工作点（Traffic=50 TB）：Cost_50TB_segment = (50,000 - 10,000) GB * 0.20 CNY/GB = 8,000 CNY；此工作点定义了第二档计费上限，当流量从49.9 TB增至50.1 TB时，边际成本突变为0.16 CNY/GB（假设第三档），对于月均60TB的业务，此临界点决定了剩余10TB流量的计费档位选择及总成本优化空间。

## Corrected Claim

档位上限工作点（Traffic=50 TB）：若第二档单价为0.20 CNY/GB且起算点为10TB，则Cost_50TB_segment = (50,000 - 10,000) GB * 0.20 CNY/GB = 8,000 CNY；此工作点定义了第二档计费上限，当流量从49.9 TB增至50.1 TB时，边际成本突变为0.16 CNY/GB（假设第三档），对于月均60TB的业务，此临界点决定了剩余10TB流量的计费档位选择及总成本优化空间。（注：具体单价及档位规则需依据实际服务商合同确认）

## Evidence

[质询]该陈述包含具体的计费参数（如0.20 CNY/GB、0.16 CNY/GB、50TB档位上限），属于经验事实。参考来源[1]讨论的是AI代码生成工具（Codex）的思考档位选择，与云存储/流量计费完全无关，无法提供外部支持。虽然内部数学计算（40,000 GB * 0.20 = 8,000 CNY）逻辑自洽，但缺乏来源验证具体数值和档位规则的真实性。 | 逻辑推导成立（算术正确），但参考来源[1]与主题无关，且该事实为经验性计费参数，无来源直接支持，依据经验事实排除条款降级。

## Search Query

Alibaba Cloud CDN 50TB traffic tier limit pricing jump

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2038957724638171791&rut=166e3d7a9600e1080dbd9f58e3b4433d6a9f68d0f57d6fa5a2ca906221894617', 'type': 'ddg', 'title': '低、中、高、超高到底怎么选？用 Codex 写代码前，先看懂思考档位和任务风险，别再一上来就开最高档，也别让复杂项目低配硬跑反复返工'}
