# N16: 折旧模型：自建策略硬件/网络设备按 5 年直线折旧，年折旧额 = CAPEX/5；公有云 CDN 无折旧，全部计入当期 OPEX；混合策略仅核心自建部分计提折旧

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

折旧模型：自建策略硬件/网络设备按 5 年直线折旧，年折旧额 = CAPEX/5；公有云 CDN 无折旧，全部计入当期 OPEX；混合策略仅核心自建部分计提折旧，长尾部分计入 OPEX

## Corrected Claim

折旧模型：自建策略硬件/网络设备按 5 年直线折旧，年折旧额 = CAPEX/5；公有云 CDN 无折旧，全部计入当期 OPEX；混合策略仅核心自建部分计提折旧，长尾部分计入 OPEX

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上是正交的（分别处理自建、混合、资金成本视角）。但在完备性上存在缺失：父节点明确提到“公有云 CDN 无折旧，全部计入当期 OPEX”，但三个子节点中没有任何一个专门处理或验证“纯公有云策略”下的成本结构（即纯 OPEX 的确认或对比）。子节点 2 虽然提到了混合策略中的 OPEX 部分，但并未独立覆盖纯公有云场景。此外，子节点 3 引入 WACC 属于财务视角的扩展，虽有价值，但父节点主要定义的是会计折旧模型，WACC 并非父节点定义的核心约束，不过作为补充分析是可接受的。主要问题在于遗漏了纯公有云策略的独立分析。）

## Search Query

CAPEX OPEX depreciation model 5-year straight-line CDN infrastructure
