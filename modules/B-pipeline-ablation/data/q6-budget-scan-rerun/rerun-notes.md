# 重跑批观察记录

## 300-r1 落地 (23:48, 37min)
- **n_nodes=252, 停止原因 = max_depth=4 hit** (非 max_nodes=300)
- **★ 停止机制与原批不同**: 原批 300 档三 rep 全 max_nodes=300 hit (精确 300 节点, 预算约束); 重跑批 300-r1 撞深度墙 (252 节点, 深度约束)
- **含义**: 原批"300 档 realized=budget (干净 x 轴)"不是稳健属性, 是 cache 共享展开路径的产物 — 独立检索后 300 档也撞深度墙。深度墙影响比之前认为的大 (不止 719 档, 300 档独立检索也会撞)
- **对 variance 对照的污染**: 原批 300 节点 vs 重跑 252 节点, 树大小不同 → metacog 分不可直接比。variance check 脚本需加 stop 字段, 对照时标注停止机制
- 评分成功: judge total=0.4139 (depth 0.8 顶格, cov 0.0278), metacog=0.2536 (gap 0.0, ret 0.1786, hg 0.9333)
- 对照原批 300 档 metacog [0.1703, 0.1698, 0.2227] — 重跑 r1 0.2536 偏高, 但单点不可比 (停止机制 + 节点数都不同)
- **对 D "不要限制深度" 指令的支撑**: 深度墙在 300 档独立检索下也生效 → 原批所有档的"预算约束"结论都带深度墙混杂, 无深度墙批 (max_depth=10) 是唯一干净的预算测试

## 300-r1 深度形状对照 (23:58) — cache 改变展开形状, 不只共享答案
- **重跑 300-r1 (独立检索)**: n=252, L1:5 L2:26 L3:58 L4:163, 撞 max_depth=4
- **原批 300-r1 (cache 共享)**: n=300, L1:5 L2:29 L3:91 L4:175, 撞 max_nodes=300
- **两批都到 L4 (max_depth=4), 但形状不同**: 独立检索批 L3 更窄 (58 vs 91), 更快撞深度墙 (252 节点); cache 共享批 L3 更宽 (91), 先填满 300 节点才撞预算
- **含义**: cache 不只"共享答案压低方差" — 它改变了展开形状 (宽 vs 深), 从而改变哪个约束先绑定 (max_nodes vs max_depth)。独立检索 → 展开偏深 → 深度墙更早绑定; cache 共享 → 展开偏宽 → 预算更早绑定
- **对 variance 对照的影响**: 两批树形状不同 (L3 58 vs 91), metacog/judge 分对照时树结构是混杂, 不只是"cache 压低方差"一个因素
- **对 D "不要限制深度" 的进一步支撑**: 深度墙在独立检索下 252 节点就绑定 (比原批 300 更早), 深度上限是真实的约束源, 无深度墙批 (max_depth=10) 是唯一干净预算测试
- n=1 (仅 300-r1), 需 r2/r3 确认形状差异是否稳健

## 重跑批覆盖范围正当性: 为什么只重跑 300/719, 不重跑 50/100/150 (00:02)
- **深度墙绑定阈值**: 300-r1 独立检索 252 节点撞 max_depth=4 → 深度墙在 ~250 节点绑定
- **50/100 档**: 节点数 50-100 << 250 (深度墙阈值) → 独立检索几乎肯定还是 max_nodes hit (预算约束), 不受深度墙影响, 不需要重跑
- **150 档**: 150 节点 < 250, 大概率 max_nodes hit, 临界但影响小
- **300 档**: 已确认独立检索撞深度墙 (252 节点) — 深度墙敏感档, 必须重跑
- **719 档**: 原批就撞深度墙, 重跑批覆盖
- **结论**: 重跑批覆盖 300/719 正确 — 50/100/150 档节点数 < 深度墙绑定阈值, 独立检索几乎肯定 max_nodes hit, 预算轴结论稳健, 不需要烧 GPU 重跑
- **对"预算控制"前提的影响**: 预算 (max_nodes) 在独立检索下不是绑定约束 (深度墙先绑定, 300 档 252 节点就停), 预算控制只在 cache 共享下有效 — 预算扫描的"预算是绑定约束"前提依赖 cache 共享。这是方法论级发现, 需 n=6 确认 (300-r2/r3 + 719×3 落地后跑 shape check)

## 300-r1 metacog 单点观察 (00:03) — 判据轴上 rerun 高于原批全部 rep
- rerun 300-r1: metacog=0.2536, gap=0.0, ret=0.1786, hg=0.9333
- 原批 300 档: metacog=[0.1703, 0.1698, 0.2227], gap=[0.0233, 0.0333, 0.03], ret=[0.1367, 0.1467, 0.1467]
- **单点观察**: rerun metacog 0.2536 > 原批全部 3 rep; gap=0 (原批 0.023-0.033); ret 0.1786 > 原批 0.137-0.147
- **两种可能解读** (n=1, 不下结论):
  (a) 独立检索展开更深 (L3 58 vs 91) → 节点更聚焦 → gap 标记更少 (gap=0) + 检索更准 (ret 高) → metacog 高
  (b) 随机方差, r2/r3 会回落
- **若 r2/r3 也高**: 独立检索不是"方差被 cache 压低", 而是"均值偏移" — cache 共享假设的解读方向要改 (从"方差"改"均值")
- **若 r2/r3 回落**: 300-r1 是 outlier, 原方差对照判据不变
- 等 r2/r3 (shape check + variance check 脚本就位, n=6 定论)

## ★ 300-r1 gap_rate=0 核验 (00:05, 正确口径 DEFENSIVE_RE) — 独立检索系统性不写 gap 标记
- **正确口径** (metacog_axis.py: DEFENSIVE_RE 查 claim+evidence+corrected_claim, 非 CUR):
  - 重跑 300-r1: gap_rate=0.0000 (0/252 defensive), metacog=0.2536
  - 原批 300-r1: gap_rate=0.0233 (7/300), metacog=0.1703
- **metacog 高的来源分解**: metacog_total = 0.4*gap + 0.3*ret + 0.3*post
  - rerun: 0.4*0 + 0.3*0.1786 + 0.3*0.667 = 0.2536
  - 原批: 0.4*0.0233 + 0.3*0.1367 + 0.3*0.400 = 0.1703
  - **post_retrieval_accuracy 0.667 vs 0.400** — 独立检索后验证率更高 (检索更准), gap=0 但 metacog 反而高
- **★ 方法论级发现**: gap 标记是 prompt-elicited (prompt 指示模型标不确定 claim)。独立检索下模型系统性不标 (0/252), cache 共享下标 (7/300)。
  可能机制: 独立检索→模型自己搜→对结果更有信心→不标; cache 共享→模型看到"之前查过"→更倾向标"待核验"
- **对论文核心 claim 的影响**: monitoring 轴 (gap_rate) 是 gold-free 跨域 general 的核心组件。如果 gap_rate 受检索模式 (cache 共享 vs 独立) 系统性影响, 则检索模式是 monitoring 轴的隐藏混杂变量 — 原批 83-run 语料全是 cache 共享模式, gap_rate 的"跨域不变性"结论可能带检索模式混杂
- **n=1 (仅 300-r1)**, 需 r2/r3 确认 gap_rate=0 是否稳健。若稳健: monitoring 轴的"不变性"声明需加检索模式限定, 或把检索模式作为新混杂变量进 draft
- 上一段 (00:03) 的"两种解读"修正: 不是 (a) 展开深→gap 少, 是独立检索→信心高→gap 少 + 检索准→post 高

## 300-r2 落地 + judge 区分度红旗 (00:55)
- **r2 分数**: n_nodes=300, **stop=max_nodes=300 hit (非深度墙!)**, judge total=0.4139 (depth 0.8, cov 0.0278), metacog=0.331 (gap 0.01, ret 0.09, hg 1.0, post 1.0)
- **★ 停止机制 rep 间不一致**: r1 撞深度墙 (252 节点), r2 撞预算墙 (300 节点)。之前 00:02 的"独立检索 300 档必撞深度墙 (252 节点绑定)"是 n=1, r2 证伪其稳健性 — 两 rep 一个深度墙一个预算墙, 停止机制本身是 rep 间变量, 不能当"独立检索的稳健属性"
- **★ judge 轴在 300 档无区分度 (方法学级)**: total=0.5×depth+0.5×cov; depth=min(max_depth/5,1.0), 两 rep 都撞深度 4→0.8 饱和; cov=1/36 分辨率 (36 gold unit, 两 rep 各只命中 1 个) → total=0.5×0.8+0.5×(1/36)=0.4139 必然相同。原批 300 档区分度全靠 cov (0/3/2 unit), 重跑两 rep 都 1 unit → 完全相同。**含义**: 300 档 judge 方差对照 (rerun sd vs orig sd) 无意义 — judge 轴饱和, 只有 metacog 轴有区分度 (0.2536 vs 0.331)。46-unit 分辨率饱和问题在重跑批同样出现
- **gap_rate n=2**: r1=0.0000 (0/252), r2=0.01 (~3/300)。独立检索下 gap 标记系统性稀少 (原批 0.023-0.033) 的模式 n=2 支持, 但 r2 非零 (0.01), 非"绝对 0"。post_retrieval r1=0.667 r2=1.0 (独立检索后验证率高)
- **待 r3**: 停止机制是否再变 (深度墙/预算墙), gap_rate 是否继续 ~0, judge total 是否再撞 0.4139 (cov 再命中 1 unit)

## metacog 轴判读修正: 均值偏移, 不是方差回升 (00:58, n=2)
- **数据**: 原批 300 档 metacog [0.1703, 0.1698, 0.2227] (mean 0.1876, sd 0.0304); 重跑 r1/r2 [0.2536, 0.331] (mean 0.2923)
- **关键**: 重跑两点都 > 原批 max (0.2536/0.331 > 0.2227) → 这是**均值偏移**, 不是方差回升。n=2 的 sd=0.0547 只是两点差的一半, 不稳定, 机械判据 (sd>1.3×orig) 碰巧过但判读方向错
- **驱动分解**: post_retrieval r1=0.667 r2=1.0 vs 原批 0.400 (独立检索后验证率系统性高); gap r1=0 r2=0.01 vs 原批 0.023-0.033 (独立检索 gap 标记稀少)
- **与 gap_rate 发现同根因**: 检索模式 (cache 共享 vs 独立) 系统性改变模型行为 — 独立检索→信心高 (gap 少) + 检索准 (post 高) → metacog 系统性高。**两个发现互相印证, 共同指向: 检索模式是 metacog 轴 (含 gap_rate 和 post_retrieval 两个子轴) 的隐藏混杂变量**
- **对论文 claim 的影响升级**: 不只 monitoring 轴 (gap_rate), 整个 metacog 轴的"跨域不变性"声明都带检索模式混杂 — 原批 83-run 语料全是 cache 共享模式。draft 里 metacog 轴的不变性声明需加检索模式限定, 或把检索模式作为新混杂变量进 draft
- **n=2, r3 确认**: 若 r3 metacog 也 > 0.2227 → 均值偏移定论; 若 r3 回落 → n=2 巧合, 判读退回方差假设

## draft 影响定位 (01:02) — 检索模式混杂的具体落点
- **draft 文件**: experiments/stage-ablation/workshop-draft-metacog-20261122.md
- **不变性声明位置**: L9 (findings 段, "the metacognition axis's invariance finding remains scoped to the rep-scan era") + L94 (provenance note, gap_rate ANOVA F(2,12)=0.036 全段)
- **draft 已有的限定** (做得很细): rep-scan era 限定 / 8-pattern vs 22-pattern detector-scoped / realized-compute 回归 (cor=-0.034 ns) / 小分母 artifact 排除
- **draft 没有的限定 = 本轮发现**: 检索模式 (cache 共享 vs 独立检索) 从未被声明为前提, 因为 83-run 语料 + 15 rep-scan 全是 cache 共享模式 — 不变性声明实际是"cache 共享检索模式下"的不变性, 隐含前提未显式化
- **r3 落地后的 draft 动作**: 若 gap_rate 独立检索下持续 ~0 (n=3 确认) → §6 加一条 scope 限定: "the invariance claim is scoped to the cache-shared retrieval mode; independent-retrieval runs show systematically lower gap marking (0.000/0.01 vs 0.023-0.033) and higher post_retrieval (0.667/1.0 vs 0.400) — retrieval mode is a hidden confound for the metacog axis (gap + post components)"。不撤不变性声明, 加限定 (era/detector 先例同型)
