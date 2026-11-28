# arXiv + TMLR 的四个硬指标（2026-11-25）

结论口径：只采用官方一手数据（TMLR 2025 Annual Report / 官方 editorial pages）。未公布的数字明确标"未公布"，不用第三方估算冒充官方。

## 1. 四个指标一览

| 指标 | arXiv | TMLR | 对照：顶会主会 |
|---|---|---|---|
| 同行评审 | **无**（预印本） | **有**，open-review + double-blind，≥3  reviewer | 有，双盲或单盲 |
| 接受率 | 不适用（不拒稿，但 moderation 可拒） | **70.6%**（剔除 withdrawn/desk-reject）／**46.3%**（全口径） | NeurIPS/ICML/ICLR 通常 20–35% |
| 审稿周期 | 通常 1–3 天（公告/ moderation） | **短文中位 91 天**；长文 104 天 | NeurIPS 2025 中位 126 天；JMLR >200 天 |
| 发表延迟 | 即时公开 | 决定后交 camera-ready + AE 验证即上线；**rolling，无批次排队**。官方年报有"submission→camera-ready"分布图，但为图片，文本无法提取中位天数——**未公布可引用数值** | 主会按固定日程，录用→正式 proceedings 数月 |
| 费用 | 0 | **0**，无 APC，不要求参会 | 注册 $285–700 + 差旅（NeurIPS 强制到场） |
| 存档/持久性 | 永久，非评审版本 | 永久，ISSN 2835-8856，**Scopus 已收录**，Web of Science 审核中；CC BY 4.0，版权归作者 | 永久 proceedings，但固定页数与时点 |
| 含金量定位 | 锁日期 + 可引用，**不算评审发表** | **正式同行评审期刊发表**，低于顶会主会的筛选稀缺性，明显高于 workshop | 主会 > TMLR > workshop |

## 2. 官方原文证据（TMLR 2025 Annual Report，2025-12 发布）

来源：`https://docs.google.com/document/d/1EsApC9y08bY2Qv2lQ-1NjTgU8QuAT9E30k44QiuSG5c/export?format=txt`（首页链接：`jmlr.org/tmlr/index.html`）

- 接受率："Our acceptance rate is stable at 70.6% compared to 69.4% in 2024." 以及 "Our acceptance rate based on 2025 statistics would be 70.6% if ignoring withdrawn and desk-rejected submissions ... This number would fall to 46.3% if including withdrawn and desk-rejected submissions, a meaningful decrease from 2024 (50.6%)."
- 审稿周期："We've managed to reduce our turn-around time from manuscript submission to decision compared to 2024 (from a median of 113 days to 104 days for long papers, and from 97 to 91 days for short papers)." 以及 "Our median turnaround time for short (i.e., conference length) papers was 91 days, compared to 126 days for NeurIPS 2025 and over 200 days for JMLR."
- 规模："published over 1395 papers (up from 908 papers in 2024 and 550 in 2023), for a total of over 3130 papers since TMLR's launch"；约 250 submissions/month。
- 认证稀缺度：2025 年 Featured Certification **24** 篇（≈1.7% of 1395）、Reproducibility 29、Survey 36、Outstanding **4** 篇（≈0.3%）。这是"TMLR 内部含金量分层"的官方数字。
- 索引："we are now indexed by Scopus. We are still in review for Web of Science."
- 上会通道："TMLR has now joined the NeurIPS / ICML / ICLR Journal-to-Conference (J2C) Track ... selected published TMLR papers will now be eligible for presentation at these conferences."（注意：J2C 是展示机会，不进会议 proceedings）

## 3. 含金量怎么理解（判断，非官方口径）

- **70.6% 不是"水刊"证据，也不是顶会同级证据。** TMLR 官方 acceptance criteria 明文："technical correctness over subjective significance"，且"interest"判据要求 reviewer 不确定时应倾向于认为满足；它刻意不按 significance/novelty 筛人。这正是 modest 前置工作能中的原因，也决定了它不具备顶会主会的稀缺性。
- **它是真期刊，不是 workshop。** 有 ISSN、Scopus 收录、永久存档、rolling、无页数刚性、作者保留版权；对"后续继续引用自己的工作"没有 archival workshop 那种阻塞。
- **分层靠 certification，不靠接受率。** Featured 1.7%、Outstanding 0.3% 才是 TMLR 内部的质量信号；J2C 是拿到后再去顶会做 poster 的通道。
- **路径价值**：arXiv 锁日期 + 可引用 → TMLR 正式评审发表 → 若拿 Featured/Outstanding 可走 J2C 上会。全程 0 元、不参会。

## 4. 一条会直接卡住投稿的硬风险（AI 生成）

TMLR Acceptance Criteria 官方原文（`jmlr.org/tmlr/acceptance-criteria.html`）：

> "If a paper fully is AI generated with little or no human involvement, then at least with current AI systems, it is unlikely to meet this criterion."

TMLR 2025 年报：

> "we have identified more than 20 instances of inappropriate use of LLMs for preparing submissions. We investigate each case and, for cases where we believe there is sufficient evidence of abuse, apply a range of disciplinary actions, including banning authors from submitting to TMLR for 1 year for the most serious infractions."

判定：这是**软门槛**（个案判断），不是 ICLR tiny track 那种硬性禁令，但确实存在且已实际执法。idea53 现稿是 AI 主笔 + arena 审稿，直接投有实质风险。

处理动作（不换投稿地）：
1. 把人工智识贡献显性写进稿：四条裁决、类型偷换的反驳、SSC 切割、闭式模型的构造、精确零负控制的设计与数字口径，这些必须由你复述、核验并承担作者责任。
2. 按 TMLR 要求披露 AI 辅助使用；不要提交"AI 全权代写、无人工介入"的版本。
3. 把 already-generated 的英文稿当作草稿，做一次实质人工重写，而不是格式微调。

## 5. 时间线操作提示

- TMLR 有年末暂停收稿的惯例：2025 年是 12-02 至 01-05 暂停、01-06 恢复；2026 年是否同样暂停**未公布**。当前 11-25，若要赶在年末前投，按 12 月初的窗口倒推。
- 以短篇（conference length，≤12 页）投，审稿中位 91 天；长篇 104 天。中文稿不能作 TMLR 投稿主体（arXiv 同样以英文为主）——英文稿在前，中文稿作为附录/译本另置。

## 6. 决策清单（无需再问）

1. arXiv 传英文稿，免费锁公开日期，拿 ID。
2. 英文稿按上节第 4 点做人工实质重写 + AI 使用披露，再以 TMLR 模板（强制 stylefile）投 short paper。
3. 不投 archival workshop；不为顶会预算差旅。
4. 若被拒，利用 TMLR 的开放评审与 resubmit 通道（新 submission + 链接旧稿 + 变更说明）修订再投。
