# 阶段 02.5 — RV3G3cdx-m4-independent-source-ops · 交叉核对裁定（r152）

> 方法：S5 三张力点逐条裁定 + 定义条款草案与两打分器 basis 原文互验。裁定原则沿用 r151 契约 §5（多数派 + 最新轮次；矛盾如实登记不强行统一历史）。

## X1 — T1 处置：run1 计分方向分裂（50/45/70）

**裁定**：裁决 70 登记为「口径过渡期人工居中」，**新规则下 run1 判低分侧**。
理由链：(a) 裁决 70 的理由文本「锚点+上轮双源可加」与其自家 E2 key_reasons「锚点≠独立源」、E3 largest_residual_bias「上轮双源回执…过度计入」直接矛盾——同文件族内自相矛盾，按「最新轮次」取 E3/E4（r4 裁决层 reason 是 step2 即时判断，largest_residual_bias 是同文件收尾总结且被 bench.md L67/L29 两轮引用固化）；(b) Claude R5.1（最新轮次）basis 明确「本地双源是同一环境内的两个文件源」不满足收紧口径；(c) 两打分器（50/45）方向一致 vs 裁决（70）孤例 ⇒ 多数派 + 最新轮次双重指向低分侧。
**如实登记**：此即缺陷 #2 的实例化证据——同一事实三种分数，全因「独立源」无操作化定义。本 goal 交付后该分歧应可机判消解。

## X2 — T2 回测口径

**裁定**：计数对象 = P6 `independent_sources` 条目（11 条，schema 锚定可机判）；打分器 basis 引用的原始证据形态仅作对账参照列，不参与计数。
理由：basis 是自由文本，逐字解析不可复现；P6 是结构化字段，正是 packet v2 模板「给足源清单让打分器自己判」的设计意图——操作化定义就是把「自己判」变成「按规则判」。

## X3 — T3 conf=null 条目是否计入

**裁定**：不计入独立源总数。判定规则 = 条目 claim 为**负向通道陈述**（「不可达」「无源」「unverified」类）⇒ 归 channel_status 冗余转录，排除。
理由：两条 null 条目（run1[1]/run3[1]）的 source 分别指向 loop-state 的 chain_steps 记录与 execution-log 的 M4 basis 行——它们记录的是「没有第二源」这一事实本身，不是任何 claim 的第二验证。计入会把「诚实报告无源」反向奖励为「有源」。
**边界登记**：此排除规则当前靠 claim 语义判断（「不可达/无源/unverified」关键词），非纯结构字段——机判规格须标注该局限（见 X5）。

## X4 — 核心判定规则草案（D1-D5，与 basis 原文互验通过）

| 条款 | 规则 | 证据锚点 |
|---|---|---|
| **D1 独立性三维度** | 两个源独立 ⇔ 至少一个维度不同：(i) provider（生成方模型/服务）(ii) 采集通道（web_search / LLM 回执 / 本地实测 / 文件读取）(iii) 信息路径（一手发布 vs 转引链）。三维全同 = 同源。 | E4 run3 basis「同一文件的两种读取方式（同源双读）」= 维度 (iii) 全同实例；E4 run1「同一环境内的两个文件源」= 维度 (ii)(iii) 全同实例 |
| **D2 反例五类（不计入）** | (α) 执行锚点（git hash/退出码/文件存在性）(β) 上轮回执转录（nature=transcription）(γ) 单通道 web_search 多 URL（同通道同检索行为，URL 数 ≠ 源数）(δ) 同源双读（同文件不同读取方式）(ε) 训练知识单源（无 source_path 可锚定的内部知识） | E2 key_reasons 三类 + E3 largest_residual_bias 三类（并集去重 = α β γ）+ E4 run3（δ）+ E4 run1「训练知识单源、标 unverified」（ε）——五类全部有先例原文，零硬造 |
| **D3 转引链折减** | nature=external 但 source 含「转引/经…blog/二手」标记 ⇒ 该条目独立性打折：与转引上游同路径时按 D1(iii) 判同源；无上游可溯时保留计数但 conf 上限 0.7（二手置信封顶）。 | E4 run2「外部源多为二手转引」+ packet run2[2][4][5] source 字段自带转引标记（theaiengineer.substack / arihantdeva blog / parallel.ai 转引 Anthropic） |
| **D4 ≥2 判定** | run 级 M4 达标 ⇔ 计入口中（D2 排除后）存在 ≥2 条 D1 判独立的条目，且至少一条 nature=external 或 local-measured（transcription 永不单独构成独立源，见 D2(β)）。 | E2「web_search 单通道非≥2独立源」+ E4 run2「仍差『不同 provider 的 LLM 回执对』」——两器均要求跨通道/跨 provider 而非数量堆叠 |
| **D5 降级态上限** | channel_status 声明外部通道不可达（degraded-partial / 无网络 / 无 ≥2 LLM 通道）⇒ 该 run M4 不得以「本地双源」顶格：本地双源仅当满足 D1 维度 (ii)/(iii) 差异时按 1 个独立源计，且 run 级结论上限 = mid 档（对应现有打分尺度 ≈ ≤60）。 | E4 run1/run2 basis 均因 channel_status 降级而判 low/mid；E3 run3「无网络无外部交叉=无验证低分」 |

**互验结果**：D1-D5 每条至少一个 basis 原文锚点（表右列），无一条为纯演绎。D3 是唯一含数值参数（0.7 封顶）的条款——参数来源 = packet run2 channel_status 原文「M4 顶格 conf 0.8」之下二手源的合理折减位，**登记为暂定值待成璐确认**（不代裁数值，只定机制）。

## X5 — 机判升级路径预注册（本轮不改脚本）

- **U1 — P6 条目级 lint**（候选脚本 assert-m4-sources.py，未落盘）：(a) nature ∈ {external, local-measured, transcription} 枚举校验；(b) 同 run 内 source 字符串归一（小写 + 去日期括号）后重复 = SIGNAL（疑似同源拆条）；(c) D2 反例关键词扫描（transcription 自动排除 / 「转引|经.*blog|二手」命中 = D3 折减标记）。
- **U2 — schema 扩展需求**（阻塞项，导出候选）：D1(i) provider 维度与 D4 的「不同 provider 回执对」判定**在当前 P6 schema 下不可机判**（无 provider 字段）——需 template v2 → v3 增加 `provider`（必填 str）+ `channel`（枚举：web-search / llm-receipt / local-measured / file-read）两字段。本轮不改 template（改 template = 影响 run5 在途协议，属判定语义级变更）。
- **U3 — 激活条件**：下一轮 run 产出新 packet（含 U2 字段）后，U1 脚本方可实跑回归；在此之前 U1 仅可对 packet v2 做降级运行（provider 维度跳过，仅 D2/D3 可机判部分）。

## verdict

X1-X5 全裁定，零悬置。定义条款 D1-D5 草案定稿（D3 数值参数标暂定）；回测口径 = X2/X3；机判路径 = U1-U3（脚本零改动纪律维持）。进入 03 动作分解。