# N367: 控制变量遗漏偏误修正：在估计 E_T,exp 时，若未控制卖家主动降价行为（Price_Drop_Flag），可能导致估计值偏误；需加入交互项 E_T,exp 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N116

## Claim

控制变量遗漏偏误修正：在估计 E_T,exp 时，若未控制卖家主动降价行为（Price_Drop_Flag），可能导致估计值偏误；需加入交互项 E_T,exp * Price_Drop_Flag 以分离曝光效应与降价信号效应，偏误大小需通过 2SLS 或 Heckman 模型量化。

## Corrected Claim

在估计 E_T,exp 时，若未控制卖家主动降价行为（Price_Drop_Flag），可能导致估计值偏误；通常需加入交互项 E_T,exp * Price_Drop_Flag 以分离曝光效应与降价信号效应，偏误大小可通过 2SLS 或 Heckman 模型等计量方法尝试量化，具体方法需视内生性来源而定。

## Evidence

[质询]该陈述属于具体的计量经济学方法论建议（经验事实/专业判断），而非第一性原理可推导的数学或逻辑恒等式。具体而言，是否必须使用2SLS或Heckman模型取决于内生性的具体来源和数据结构，并非绝对真理；此外，交互项的加入方式及偏误方向需结合具体模型设定，陈述过于绝对化。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该事实属于专业方法论建议，非第一性原理可推导范畴）

## Search Query

omitted variable bias exposure transaction time seller price drop interaction
