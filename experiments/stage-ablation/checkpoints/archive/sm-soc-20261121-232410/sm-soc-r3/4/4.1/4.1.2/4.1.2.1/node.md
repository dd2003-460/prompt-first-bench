# N155: 排序权重 w1, w2, w3 的基准值及干预后调整幅度：基准 w1=0.5, w2=0.3, w3=0.2；干预后 w3 增加至 0.6（+200%），w1 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N55

## Claim

排序权重 w1, w2, w3 的基准值及干预后调整幅度：基准 w1=0.5, w2=0.3, w3=0.2；干预后 w3 增加至 0.6（+200%），w1 和 w2 保持不变，导致高溢价商品（Premium>15%）的 Rank_Score 下降约 30%，曝光量减少 25%。

## Corrected Claim

在特定排序模型中，若将代表溢价惩罚的权重w3从0.2提升至0.6（保持w1, w2不变），理论上会导致高溢价商品的Rank_Score显著下降，进而可能减少其曝光量（具体降幅如30%和25%需依赖具体业务数据验证）。

## Evidence

[质询]该陈述包含具体的业务参数（基准权重0.5/0.3/0.2、干预后w3=0.6、Rank_Score下降30%、曝光减少25%），属于特定场景下的经验事实或模拟数据，无法从第一性原理推导，且参考来源仅讨论通用的权重计算方法（AHP/熵权法），未提供该具体案例的数据支持。 | 逻辑上，若w3代表负向指标（如溢价惩罚）且权重从0.2增至0.6，确实会导致高溢价商品得分下降，逻辑自洽；但参考来源[1][2]仅涉及权重计算通用方法，与该具体数值案例无关，缺乏直接外部证据支持具体数值。

## Search Query

platform algorithm ranking weight adjustment w3 penalty coefficient for high premium items second-hand marketplace

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1981325931390998072&rut=4cb73709c3487d4fef2110813b7cf6e1fce2861afa053c1cf21b35921c7c7fd8', 'type': 'ddg', 'title': '评价指标体系构建与权重计算方法详解 - 知乎'}
- {'url': 'https://www.sohu.com/a/963929373_122456032&rut=e964666f1867e699d135c7bf06b0443830939404038396edd1773ad94cd7dc33', 'type': 'ddg', 'title': '评价指标体系构建与权重计算方法详解_一级_数据_二级'}
