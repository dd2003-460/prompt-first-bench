# N147: 有效需求集中时间 T_verify 的操作性定义：定义为从商品上架（t=0）到累计咨询量中价格敏感型买家占比低于 10% 的时间点；该阈值 10% 需通过验证咨

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N44

## Claim

有效需求集中时间 T_verify 的操作性定义：定义为从商品上架（t=0）到累计咨询量中价格敏感型买家占比低于 10% 的时间点；该阈值 10% 需通过验证咨询后成交率与初始报价溢价的负相关性显著性（p<0.05）来确定，若无法确定则标记为 [待核验]。

## Corrected Claim

有效需求集中时间 T_verify 的操作性定义：定义为从商品上架（t=0）到累计咨询量中价格敏感型买家占比低于特定阈值（如10%）的时间点；该阈值需通过验证咨询后成交率与初始报价溢价的负相关性显著性（p<0.05）来确定，若无法确定则标记为 [待核验]。

## Evidence

[质询]该陈述定义了一个特定的商业/统计操作性指标（T_verify），其阈值确定依赖于具体的实证数据（咨询后成交率与溢价的负相关性）。参考来源[1]仅涉及SHL测评（数字/演绎推理）的考试介绍，与商品上架、买家咨询、价格敏感度等商业场景完全无关，无法提供外部支持。此外，10%这一具体阈值缺乏通用理论依据，属于特定场景下的经验参数，若无具体数据集支持，其普适性存疑。 | 逻辑上自洽（定义清晰，统计检验方法合理），但参考来源[1]与事实主题（商业需求分析）完全无关，属于「无可用外部证据」。根据经验事实排除条款，此类特定业务指标的定义若无来源直接支持，应降级为degraded。

## Search Query

operational definition verification time second hand goods buyer filtering threshold

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2003503946728230927&rut=874f7e46ddfe302da7c039cc92d918b69f83aa1b1cd0a092542b5ac9374aaae6', 'type': 'ddg', 'title': '2026时代电服科技SHL测评Verify测评：数字推理+演绎推理真题题库和答案'}
