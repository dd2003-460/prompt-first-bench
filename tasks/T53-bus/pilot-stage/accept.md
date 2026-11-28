# origin: ai (2026-11-28 pilot-stage 05-accept · 验收 + 完成)
# 验收对象: pilot-stage goal (sm-run6 预注册草案) · 验收标准来源: TASK.md "产出" 节 (5 项必含)

## 1. 对照 TASK.md 验收标准逐项检查 (不抽样)

| # | 验收标准 (TASK.md 产出节) | 判定 | 证据 (handle) |
|---|---|---|---|
| A1 | 方向选择 (a/b/混合) + 理由引 sm-run5 具体数字 | 达标 | 草案 §1 (line 5-16): 混合, 引 Δ=+0.67/mean(A)=2.0/mean(B)=1.33/B 臂 2/3 自发命中; 数字与 sm-run5-scoring.md line 36-40 逐项一致 (verify.md V2) |
| A2 | 植入缺陷设计: 每条缺陷 + 为什么比 sm-run5 更难自驳 | 达标 | 草案 §2 (line 18-31): H3/H4/H5 各带"为什么更难"论证 + 难度排序 + B 臂预期; H3 跨节不一致经 sm-run5-ref-status.md line 17-18 vs line 21 实测成立 (verify.md V3) |
| A3 | 样本量与判决阈值: n/臂 + 预注册判决标准 (成立/不显著/负结果) + 方差估计来源 | 达标 | 草案 §3 (line 34-44): n=5/臂, 三档阈值 Δ≥1.5/0≤Δ<1.5/Δ<0, 方差估计=sm-run5 6 run pilot (A σ²=0 天花板伪零, 只用于敏感性不用于判决) |
| A4 | 臂定义 (A/B 任务卡差异) + 判分方法 (binary, 谁判分, 盲判否) | 达标 | 草案 §4 (line 46-54): A=任务卡+质疑前置段, B=同卡无质疑段; binary per 缺陷, Lead 机械判分, 盲判=否 (已知污染预先声明) + 判据收紧条款 |
| A5 | 风险与边界声明 (同 sm-run5 诚实标注要求) | 达标 | 草案 §5 (line 56-63): 条件性收益边界声明 + 4 项新增风险 (内生质疑/小样本/模型状态/判分者) |
| A6 | 边界 (硬): 只写指定产出文件, 不跑实验/不调 8787/不碰 sm-run5 收口文件; git 只 add 产出文件 | 达标 | git show --stat: c69fa38aa = 1 file (草案), 77a98d307 = 2 files (design/verify); `git status -- modules/G-think-mechanism/rsi-pilot/` 空; cc-state.json/cc-to-lead.md 未 add (verify.md V6) |

**6/6 达标** (5 项必含产出 + 1 项硬边界)。

## 2. 工件完整性 (本任务 stage 模式, 非 arena 6 阶段 loop)

本任务走 stage 状态机 (02-design → 04-verify → 05-accept), 非 arena 1-loop 六阶段 → 无 loop-artifacts/ 01..04.5 工件要求 (goal-template.md §2 适用于 arena 外包链路, 本试点不适用)。stage 工件齐全:
- TASK.md (任务卡) / design.md (02) / verify.md (04) / accept.md (05, 本文件) / sm-run6-preregistration-draft.md (产出)
- cc-state.json history: 02-design (c69fa38aa) + 04-verify (verify.md 6/6) 两条 evidence 均带可验证 handle

## 3. pfb goal 额外检查 (实验发现 → 生产路径)

问题: "这次验证出的东西, 有没有哪条该写进 loop/prompt-first/ 或 harness 引导式臂?"
**答: 不落地, 记录原因:**
1. 本任务产出是**预注册草案** (sm-run6 实验设计), 不是已验证的机制结论 — 判决要等 sm-run6 数据生成后才有, 现在没有任何"验证出的东西"。
2. 草案 §4 的判据收紧 (只认植入具体维度, 排除同方向不同维度宽判) 是**评分仪器侧改进** (判分方法), 按 scoring.md 判断标准属"纯 scorer 侧改进 (评分仪器的事, 不是 prompt 的事)" → 不落地。
3. 若 sm-run6 跑出 Δ≥1.5 成立, 届时"假设层质疑前置段写入任务卡模板"才进入落地评估 (sm-run5 预注册已预写此路径: "成立→写回任务卡模板"), 由 sm-run6 验收时处理。

## 4. Gate 自检

- [x] 验收标准全部达标 (A1-A6, 6/6)
- [x] 工件齐全 (stage 模式 4 工件 + 产出; arena 6 阶段工件不适用, 原因见 §2)
- [x] goal complete (cc-state.json current_index → 3 = len(stages), 全部阶段走完)
- [x] 下一个 goal: **不 create** (goal-template.md §3 硬规则: 不凭空立项, 新 goal 只从讨论结论/用户明确任务发现)。已识别的可执行待办 = 汇报 Lead (cc-to-lead.md), 由 Lead 决定 sm-run6 是否立项执行。

## 5. 留痕

- commit c69fa38aa (草案) + 77a98d307 (design/verify), 已 push origin thinkmech-review (9dd75445c..77a98d307)
