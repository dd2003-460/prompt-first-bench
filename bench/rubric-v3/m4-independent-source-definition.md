# M4「独立源」操作化定义（r152 · RV3G3cdx-m4-independent-source-ops）

> 状态：生效（2026-10-30 落盘）。本文件是 bench M4 指标中「独立源」一词的**唯一成文判定规则源**——此前该词由打分器主观裁量（bench.md L75 已知缺陷 #2）。
> **边界声明**：本文件不改变 M4 指标语义（「≥2 独立源对关键 claim 的验证质量」，bench.md L13「固定落点，下轮引用不重定」）——只把「独立源」从裁量词变为可判据。M4 权重、打分尺度、conf 标注义务均不动。
> 消费方：后续轮次打分器（按 D1-D5 判定而非自由裁量）+ U1 机判脚本（未来落地时以本文件为判定语义权威源，同 r151 queue-format-contract §2 关系范式）。
> 证据索引：每条规则标注先例原文锚点（file + 字段/行号）。取证全文见 `loop-artifacts/stages/02/RV3G3cdx-m4-ops-scan.md` S2 节。

## §1 核心判定条款

### D1 — 独立性三维度（强制）

两个源**独立** ⇔ 在以下至少一个维度上不同；三维全同 = 同源：

| 维度 | 含义 | 判据 |
|---|---|---|
| (i) provider | 生成/发布方（模型服务 / 网站主体 / 实测执行环境） | 当前 P6 schema **不可机判**（无 provider 字段）——人工判定时看 source 字符串中的主体名；机判待 U2 schema v3 |
| (ii) 采集通道 | web_search / LLM 回执 / 本地实测 / 文件读取 | 可由 nature 字段部分推断（external≈web 或 llm / local-measured=本地实测 / transcription=转录） |
| (iii) 信息路径 | 一手发布 vs 转引链深度 | source 字符串含「转引/经…blog/二手」标记 ⇒ 路径 ≥2 跳 |

- 证据：E4 run3 basis「同一文件的两种读取方式（同源双读），非独立源」（维度 iii 全同实例，`r5/scoring-claude-r1.json` scores.run3.M4.basis）；E4 run1 basis「本地双源是同一环境内的两个文件源」（维度 ii+iii 全同实例，同文件 scores.run1.M4.basis）。
- **澄清**（r152 回测 M2 处置）：同一文件的多种读取方式（sed / read / grep…）不构成维度 (ii)/(iii) 差异——读取方式是通道 (ii) 内的子行为，不是独立维度。即 D2(δ) 在 D1 侧的锚定：单文件多读 = 至多 1 个独立源。
- **降级运行态归簇规则**（04.5 W1 补）：U2 schema v3 落地前维度 (i) 不可机判——条目归簇按可判维度 (ii)/(iii) 执行：同采集通道 + 同信息路径的条目组 = 1 簇（至多计 1 个独立源），即使 source 字符串中的主体名互异。人工判定可用维度 (i) 拆簇，机判不得。

### D2 — 反例五类（强制排除，不计入独立源总数）

| 类 | 形态 | 证据锚点 |
|---|---|---|
| α 执行锚点 | git hash / 命令退出码 / 文件存在性——证明「做过」不证明「claim 为真」 | E2 key_reasons「锚点≠独立源」（`r4/independent-scoring-deepseek.json` key_reasons["run1 M4=50 / run2 M4=45 / run3 M4=35"]）；bench.md L29 |
| β 上轮回执转录 | nature=transcription 条目——引用即不重查，零新增验证 | E3 largest_residual_bias「上轮双源回执…过度计入」（`r4/adjudication-step2.json`）；packet run1[0] nature=transcription 实例 |
| γ 单通道多 URL | 同一 web_search 通道的多个结果 URL——URL 数 ≠ 源数（同检索行为同通道） | E2「web_search 单通道非≥2独立源」；E3 run2_M4 reason「web_search 单通道=单源低分」 |
| δ 同源双读 | 同一文件的 sed/read/grep 等不同读取方式 | E4 run3 basis（D1 同锚点） |
| ε 训练知识单源 | 无 source_path 可锚定的模型内部知识（常标 unverified/conf≤0.3） | E4 run1 basis「仅训练知识单源、标 unverified conf 0.3」 |

### D3 — 转引链折减（强制机制，数值参数暂定）

> ⚠ **数值未裁定**：本条机制（转引折减）已定并生效；conf 上限数值 **0.7 为暂定值，待成璐确认**——消费方在数值裁定前只执行机制（标记折减），不得把 0.7 当硬阈值写入判分。

nature=external 且 source 含转引标记（「转引」「经 <X> blog」「二手」）⇒：
- 与转引上游可溯且同路径 ⇒ 按 D1(iii) 判同源，归入上游条目计数；
- 上游不可溯 ⇒ 保留计数，但该条目 conf 上限 **0.7**（暂定值）。
- **暂定参数登记**：0.7 封顶为本轮设定的机制参数（依据 = packet run2 channel_status 原文「M4 顶格 conf 0.8」之下二手源的折减位），**待成璐确认**——机制（转引折减）有 E4 run2「外部源多为二手转引」实证，数值本身无先例锚点，不代裁。
- 证据：packet run2[2]/[4]/[5] source 字段自带转引标记（`r5/evidence-packet-r4-v2.json` runs.run2.P6_cross_validation.independent_sources）。

### D4 — run 级 ≥2 判定（强制）

run 达标 ⇔ D2 排除后计入口中存在 **≥2 条 D1 判独立**的条目，且其中至少一条 nature ∈ {external, local-measured}（transcription 永不单独构成独立源——D2(β) 的直接推论）。
- 数量堆叠不达标：6 条同通道 external（如 run2 E1-E6 若全同 web_search 通道）= 1 个独立源，不是 6 个。
- 证据：E4 run2 basis「三 run 中最接近收紧口径者，仍差『不同 provider 的 LLM 回执对』」——达标要求跨 provider/通道，非条目数。

### D5 — 降级态上限（强制）

channel_status 声明外部通道不可达（degraded-partial / 无网络 / 无 ≥2 LLM 通道）⇒ 该 run 不得以本地双源顶格：本地源仅当满足 D1 维度 (ii)/(iii) 差异时按 1 个独立源计，run 级结论上限 = low-mid 区间（实跑参照 30-50——三 run 历史判分除 X1 登记的过渡期人工居中 70 外全部 ≤50，本条是该既成事实的形式化，非新造阈值）。
- 证据：E4 run1/run2 basis 均因 channel_status 降级判 low/mid；E3 run3_M4 reason「无网络无外部交叉=无验证低分」。

## §2 回测基线（packet v2 既有数据，实跑值）

11 条 independent_sources（run1×2 / run2×7 / run3×2）逐条分类 + 每 run 计数 + 两打分器方向对账 = `loop-artifacts/stages/04/RV3G3cdx-m4-ops-backtest.md`。
**性质声明**（04.5 W4）：该回测是**完备性验证**（历史判分理由是否被 D 条款覆盖——缺陷 #2 的直接消解检验），不是预测验证；规则的外推效力须待 U3 激活轮对新 run 新 packet 的首次盲判才能检验。
**预期方向**（回测须复现，否则如实登记 mismatch）：三 run 全部不达 D4 达标线 ⇒ 与「两打分器收敛点：M4 三项全 low/mid」（bench.md L117）一致。

## §3 机判升级路径（预注册规格，本轮零脚本改动）

- **U1 — assert-m4-sources.py 规格**（未落盘）：(a) nature 枚举校验 ∈ {external, local-measured, transcription}；(b) 同 run 内 source 归一（小写 + 去日期括号）重复 = SIGNAL（疑似同源拆条）；(c) D2/D3 关键词扫描：transcription 自动排除、「转引|经.*blog|二手」命中 = D3 折减标记输出。**X3 负向通道陈述排除 = 双条件并联**（04.5 W2）：conf=null **且** 关键词命中才自动排除，单独任一 = SIGNAL 人工复核。
- **U2 — schema v3 扩展需求**（阻塞项）：template v2 → v3 增加 `provider`（必填 str）+ `channel`（枚举 web-search / llm-receipt / local-measured / file-read）两字段——D1(i) 与 D4「不同 provider 回执对」在此之前不可机判。改 template 属判定语义级变更，走独立候选，本轮不动。
- **U3 — 激活条件**：新 run 产出含 U2 字段的 packet 后 U1 方可完整实跑；此前 U1 仅降级运行（跳过 provider 维度，D2/D3 部分可机判）。
- **否决项登记**：「按 URL 数计源」= 否决（D2(γ) 直接冲突）；「transcription 折半计入」= 否决（D2(β)：引用不产生新验证，折半仍是奖励复读）。

## §4 矛盾与张力登记

1. **run1 计分分裂（50 / 45 / 70）**：DeepSeek 50 / Claude 45 / 裁决 70（winner=self-direction，理由「锚点+上轮双源可加…居中」）。裁决理由与其自家 key_reasons「锚点≠独立源」+ largest_residual_bias「上轮双源回执过度计入」自相矛盾——按「多数派 + 最新轮次」（r151 契约 §5 原则）取低分侧；裁决 70 登记为**口径过渡期人工居中**（缺陷 #2 未修复时的必然产物），历史分数不重写。
2. **X3 排除规则的语义依赖局限**：conf=null 负向通道陈述条目的排除当前靠 claim 关键词（「不可达/无源/unverified」）判断，非纯结构字段——U1 落地时该规则只能做关键词近似，误排/漏排风险登记在案。
3. **D3 数值参数暂定**：见 §1 D3 末段（待成璐确认，机制已定数值未定）。

## §5 修订规则

沿用 r151 契约 §5 两级制：**判定语义级变更**（增删 D 条款 / 改强制级 / 改 D3 数值）= 新 goal 走 1-loop；**条款级澄清**（措辞 / 证据补充 / 行号修正）= 直接 Edit 本文件 + commit message 注明条款号。本文件非冻结件（判定规则文档不是数值冻结对象），但每次修订须列出受影响条款号。