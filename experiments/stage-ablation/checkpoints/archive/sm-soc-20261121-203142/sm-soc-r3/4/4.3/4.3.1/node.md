# N65: 曝光量占比 E_exp = 曝光量 / 总卖家数，需检索二手平台（如闲鱼/转转）针对‘降价’动作的算法响应机制，确定降价后48小时内曝光量的衰减或重置系数，以量

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N17

## Claim

曝光量占比 E_exp = 曝光量 / 总卖家数，需检索二手平台（如闲鱼/转转）针对‘降价’动作的算法响应机制，确定降价后48小时内曝光量的衰减或重置系数，以量化该变量在D_noise公式中的具体数值。

## Corrected Claim

曝光量占比 E_exp = 曝光量 / 总卖家数，需检索二手平台（如闲鱼/转转）针对‘降价’动作的算法响应机制，定性分析降价对曝光量的影响趋势（如是否触发重新推荐或权重调整），以辅助理解该变量在D_noise公式中的作用方向，具体数值需进一步实证数据支持。

## Evidence

[质询]该陈述声称需确定‘降价后48小时内曝光量的衰减或重置系数’的具体数值，但参考来源仅定性描述了闲鱼曝光算法的底层逻辑，并未提供具体的量化系数（如0.8或1.5等），且‘48小时’这一时间窗口在来源中未得到明确验证，属于缺乏具体数据支持的推测性量化需求。 | 来源[1]仅定性解释闲鱼曝光算法逻辑，未提供降价后48小时曝光衰减/重置的具体数值系数，无法直接支持该量化结论，故降级为定性表述。

## Search Query

second hand marketplace algorithm exposure decay price drop 48 hours CTR impact

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2040140817411618585&rut=805dd3524692cb6eb62cd3e58af1e5bed79f212888d55e5a89d40c51c34fc362', 'type': 'ddg', 'title': '闲鱼小白怎么快速获得流量，你一定要了解闲鱼的算法!闲鱼卖货必学! - 知乎'}
