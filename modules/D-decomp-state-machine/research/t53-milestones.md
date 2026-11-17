# T53 状态机里程碑时间线

> 来源: git log (pfb repo) + sm-thinking-sop.md (31 Decisions) + v17-hier-decomposition-blowup.md
> 整理: 2026-11-17, 补 D 质询"pfb 研究里居然没有这些里程碑记载"

## 一句话

v17 用 1930 个节点证明了"只奖多不罚重"的目标函数必然被 Goodhart 刷穿; T53 用 31 个 Decision 把目标函数从"可刷的公式"改造成"不可见的机器侧验收 + 不可计算的终点判据", 正交完备从外加规则变成压缩目标的自然推论。

## 时间线

### Phase 0: v17 爆炸 (2026-11-09)

| 事件 | 关键数字 | 来源 |
|------|---------|------|
| v17 hier 分解跑完 | 1930 节点 / 10 轮 / 有效维度仅 6-8 | v17-hier-decomposition-blowup.md |
| 膨胀轨迹 | r1:+24 → r7:+313 → r9:+560 (指数尾巴) | 同上 |
| D 质询修正判断 | "这是 Goodhart 刷分, 不是模型没读懂" | commit d5bb7d06 |
| 根因三叠加 | 无限预算 + 前40字符弱去重 + BFS 宽度指数增长 | 同上 |
| S_α 公式 | Σₙ[n·ln(kₙ) + α·kₙ·ln(n)] 只奖规模不罚冗余 | 同上 |

**教训**: 任何可机械计算的代理指标近似语义质量 → 必然被刷。精确性和抗刷分性矛盾: 越精确可算, 模型越能针对它优化。

### Phase 1: 止血 + 元规则 (2026-11-11, Decision 1-16)

| # | Decision | 核心内容 | 来源 |
|---|----------|---------|------|
| 1 | 停止判据 | necessary-judge (语义级"引入新变量?") 替代 n-gram gain | sm-thinking-sop.md §决策1 |
| 2 | 泄漏检查 | 查产出侧回显, 不查 prompt 输入 (题目原文进 prompt 是任务定义不是泄漏) | §决策2 |
| 7 | TCO 正交展开 | 成本类父节点必须展开 CapEx/OpEx/可靠性/不确定性 四兄弟 | §决策7 |
| 8 | 微架构下钻 | 硬件对比必须到一手机制参数, 营销规格只是入口 | §决策8 |
| 9 | L1 纯目录层 | 禁止拍平多层 | §决策9 |
| 10 | 元规则纪律 | prompt 只加"怎么判断够不够"的通用判据, 不加"该有什么维度" | §决策10 |
| 11 | L1 维度分类学 | 约束(过滤门) vs 度量(排序键) 必须分开; 横切维度(不确定性/成本/时间)独立成兄弟 | §决策11 |
| 12 | 公式vs文字 | 公式给精确优化方向(易hack), 文字只给模糊倾向; "压缩即智能"路线提出 | §决策12 |
| 14 | 冗余项全量化 | β 0.3→3.0 (罚项从 0.5%→5%); 外生离散事实豁免 [待设计] | §决策14 |
| 15 | 正交完备缺口 | S_α' 不含正交性项; 数值变化伪装正交扩展无法区分; 登记 G8 | §决策15 |
| 16 | 反Goodhart切分 | 真目标(终点判据)进 prompt, 公式(S_α')降级为机器侧监控; 代理与目标分离 | §决策16 |

**关键转折**: Decision 16 是 v17→T53 的分水岭。v17 把 S_α 公式写进 prompt 让模型逐字优化; T53 把公式从 prompt 里删掉, 只留"完整详尽准确的最终答案"这个不可计算的终点。模型面对不可刷的目标, 只能靠真的把树做对来间接提升。

### Phase 2: 理论深化 (2026-11-12, Decision 17-30)

| # | Decision | 核心内容 | 来源 |
|---|----------|---------|------|
| 17 | E12 FATAL ckpt | 崩溃时落盘当前树状态 | commit 575a7784 |
| 18 | 终点目标函数 | U(T)=C·A·S−λ·cost 形式化 | commit 43cca15f |
| 19 | 模型自估终点 | 目标函数先于分解 (模型自己估"做到什么程度算完") | commit df48b22c |
| 20 | judge 解析修复 | 全文 finditer + isinstance 防御 (r9/r10 真根因) | commit de378939 |
| 21 | Lead-teamer 文件总线 | 持久交流协议 | commit 142dbed5 |
| 22 | U(T) 正交完备性审计 | 完备侧强/冗余侧弱; Levin-K 视角; S_α' 是 K(T) 上界松弛 | §Decision22 |
| 23 | ICL-as-training | 目标函数+收敛+防hack = 训练三要素; bench=held-out test set; Goodhart 是结构性必然 | §Decision23 |
| 24 | 三边分类 + 代理锥 | **笛卡尔积边**(独立取值,可展开) / **商边**(trade-off,frontier采样) / **随机耦合边**(公共因子,记录共享源不复制); S_α' 保留为过程监控 | §Decision24 |
| 25 | junk-detector | 提前触发 web_llm 兜底 (三问, 未落代码) | commit e1fbc65b |
| 26 | 条件 MDL | Levin-K 从审计落成可算项 (desc_len/cond_gain); 冗余树自动掉分 | §Decision26 |
| 27 | 压缩-智能可测命题 | compression_ratio × answer_quality, H1-H3 falsifiable | commit 681eafc1 |
| 28 | 命题1 | 覆盖-复杂度下界; I(T)=cov·exp(−Δ/H*) | commit 58be53f2 |
| 29 | 反Goodhart元指令 | ~80字声明进 prompt (无数字无指标名); B(T) 计算预算比机器侧验收; A/B 消融设计 | §Decision29 |
| 30 | 双约束耦合 J(T) | **正交=压缩性别名** (条件熵就是正交度量, 消解 D15 三选一); 命题2 (完备性饱和单调递减); 边际均衡方程 | §Decision30 |

**关键洞察链**:
- D22: S_α' 被 hack 不是"度量错了东西", 是"度量的东西(结构规模)和真正要的东西(正交完备)之间没有保序关系"
- D24: 随机耦合边 = 任何结构化理论的残差项 (解释掉的是结构, 解释不掉的就是噪声); LLM 生成天然自带 (temp>0 的 seed 流); 错误动作=当独立维度展开, 正确动作=记录共享源不复制
- D26: 条件 MDL 补上 cost(T) "罚得均一不分冗余与否"的缺口
- D30: **正交性不需要独立度量, 它就是压缩性的别名**。H_M(ℓ₂|ℓ₁) 小 ↔ ℓ₁ℓ₂ 不正交 ↔ ℓ₂ 是冗余的。D15 纠结的三种度量 (n-gram/embedding/LLM-judge) 都是条件熵的粗糙近似

### Phase 3: 工程落地 (2026-11-12, D31-D33)

| # | 事件 | 来源 |
|---|------|------|
| D31 | LLM info-gain 首组区分度验证 (gpu 13% vs drb2 48% 冗余率) | commit ad9ebcb5 |
| D32 | 信息获取基础设施修复 + H* gold oracle + 首组 I/J 绝对值 + 涌现测试设计 | commit 94b094eb |
| D33 | 落文 | commit 303e9b66 |

## 当前状态 (2026-11-17)

- **状态机**: s5_state_machine.py (1518行), 目标函数驱动, 状态集合 {IDLE, DECOMPOSE, VERIFY, REWORK, STOP}
- **检索**: research_hook.py, GPU 规格表通道 (Wikipedia HTML via ego-browser) + Bing 兜底; webllm 全挂
- **评分**: judge_v2_depth.py, GPU_RUBRIC 22 要点 × 3-4 层深度 × k·ln(k+1) 加权
- **T53 重跑**: 35 节点, ver=9/29 (PID 81336)
- **nat 题**: r11 depth=0.8617 (26节点, 17verified); r46 同时含"随机"+"正交" (CDN 缓存题, 热度-大小相关性分解)
- **gpu 题**: v13 最高 0.4874 (r1); v14 重跑中

## 未闭合缺口

| 缺口 | 来源 | 状态 |
|------|------|------|
| G8: 正交度量选型 | D15 | D30 消解 (条件熵=正交度量), 但代码未实现 |
| 三边分类进 s5_state_machine.py | D24 | idea #43, 未实现 |
| 外生离散事实豁免 (redundancy 只对 derived 算) | D14 | [待设计] |
| A/B 消融 (D29 反Goodhart声明) | D29 | 设计完成, 未跑 |
| 命题2 实验验证 (I vs n_nodes 单调递减) | D30 | 未跑 |
| G 独立性缺口 (参考系侧 vs 答案侧) | D21补充 | 已登记 |

## 文件索引

| 文件 | 内容 |
|------|------|
| modules/D-decomp-state-machine/research/sm-thinking-sop.md | 31 个 Decision 全文 (641行) |
| modules/C-objective-goodhart/research/v17-hier-decomposition-blowup.md | v17 爆炸诊断 + Goodhart 本质 |
| experiments/stage-ablation/s5_state_machine.py | 状态机实现 (1518行) |
| experiments/stage-ablation/research_hook.py | 检索 hook |
| experiments/stage-ablation/judge_v2_depth.py | 深度加权评分 |
| experiments/stage-ablation/INDEX.md | 实验分层索引 |
| lit-survey/IDEA-INDEX.md | 33+ 条 idea 索引 |
