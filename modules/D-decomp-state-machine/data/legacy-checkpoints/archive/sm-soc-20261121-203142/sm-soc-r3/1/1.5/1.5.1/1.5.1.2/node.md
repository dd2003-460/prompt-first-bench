# N140: 投影1（容量竞争）：高曝光池的有效容量 C_high = N_max * f_active，其中 f_active 为活跃买家比例，需计算 C_high 与当前

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N38, N39, N40

## Claim

投影1（容量竞争）：高曝光池的有效容量 C_high = N_max * f_active，其中 f_active 为活跃买家比例，需计算 C_high 与当前在线高溢价商品数 N_high 的比值 ρ_sat = N_high / C_high 以量化曝光竞争强度。

## Corrected Claim

投影1（容量竞争）：高曝光池的有效容量 C_high 可建模为 N_max * f_active，其中 f_active 为活跃买家比例；通过计算 C_high 与当前在线高溢价商品数 N_high 的比值 ρ_sat = N_high / C_high 来量化曝光竞争强度（注：此为建模假设，需结合具体题目数据验证）。

## Evidence

[质询]该陈述定义了一个具体的数学模型（C_high = N_max * f_active 及 ρ_sat 计算），属于经验性建模假设。参考来源仅提及2026年华数杯C题的宏观解题思路（如需求预测、联合优化），未提供该特定公式或变量定义，无法确认该公式是否为题目给定条件或标准解法，存在口径混淆或模型假设错误的风险。 | 逻辑自洽（量纲合理，竞争强度定义为供给/需求比），但参考来源[1][2]仅涉及题目背景与宏观方法，未直接支持该具体公式定义，属于经验事实/模型假设，缺来源直接支持。

## Search Query

platform concurrent online items capacity estimation saturation ratio

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2069203972380947249&rut=bc7cd2181aa5510c58143bad2de89163100e601f8cd0656078462aba34b57572', 'type': 'ddg', 'title': '2026年华数杯c 题 超详细解题思路 - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/2069420392087922528&rut=114428a1aebca776c962e5b892d2d9724678aff09848f04621151fdbad8bec1a', 'type': 'ddg', 'title': '2026华数杯c题 思路分享 附论文完整版 - 知乎'}
