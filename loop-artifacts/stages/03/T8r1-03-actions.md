# T8-matrix-run-r1 团队文件协作/网盘选型 — 阶段 03 行动分解（stage-gate: file-collab-actions）

> 创建：2026-10-30 · 阶段：03（行动分解）· 依据：`loop/prompt-first/03-action-decomposition.md` + 02.5 证据边界 A/B/C/D
> 执行通道：Lead 本地自答（conf-0.2，E1 降级）
> **只使用已通过 Reviewer 的证据**（02.5 边界 A/B），不把猜测写成行动前提。

---

## 1. 行动步骤

### A1 修正 cost-model.json 计算 bug（U1）— owner: agent
- **输入**：02 §2 G1 定价表（修正后）+ S22 汇率 6.680538
- **动作**：重写 `experiments/T8-matrix/runs/tselect-vfull-filecollab/cost-model.json`，USD 项正确 ×12 月换算年度
- **依赖**：无（可立即执行）
- **预期产出**：cost-model.json（16 项年度 TCO，CNY）
- **验收**：python3 重算 exit 0；Dropbox Standard = ¥36,075（非 ¥3,006）；M365 BS = ¥30,062；所有 USD 项 = 单价×人数×12×汇率
- **替代路径**：若 open.er-api.com 不可达 → 用 T7.1 的 6.68 基准值（S53/S54 先例）

### A2 硬约束合规矩阵 — owner: agent
- **输入**：02 §2 G4/G5/G6 功能核验表 + 01 §2 硬约束（版本管理+权限+三端+预算≤¥30,000）
- **动作**：对冻结候选集 C1-C5 内每个被考察对象逐项判定 pass/fail/N-A，落报告 §1
- **依赖**：A1（成本数据）
- **预期产出**：合规矩阵表（对象 × 约束，格子非空）
- **验收**：全部被考察对象出现（含"未核验"对象标 N-A）；Syncthing 版本管理=fail；语雀 Pro/Enterprise 预算=fail
- **并行**：可与 A3 并行

### A3 年度 TCO 汇总与分层 — owner: agent
- **输入**：A1 修正后 cost-model.json + 02.5 边界 B（钉钉扩容区间/Confluence 区间/自托管运维区间）
- **动作**：
  - 每候选给 TCO 点估计 + 不确定度（区间或 ±）
  - 按 F4/F5 分三层：**成本优先层**（Nextcloud 自托管 / 坚果云 Standard / 钉钉专业版）/ **能力优先层**（飞书标准版 / Box Business / M365 BS）/ **自主可控层**（Seafile Pro on-prem / Nextcloud）
  - 超预算项单列淘汰理由
- **依赖**：A1
- **预期产出**：TCO 分层表（落报告 §2）
- **验收**：每层 ≥1 候选；超预算项有明确淘汰理由；区间项标注不确定度来源
- **并行**：可与 A2 并行

### A4 推荐方案 + 备选 + 淘汰理由 — owner: agent
- **输入**：A2 合规矩阵 + A3 TCO 分层 + 02.5 攻击轮 4（飞书存储下沿风险）
- **动作**：
  - D1 推荐方案 ×1：产品名 + 计价模型 + 年度成本 + 满足约束逐条证据
  - D2 备选 ≥2：分层（成本优先/能力优先/自主可控）
  - D3 淘汰理由：冻结候选集内每一类/每一个被考察对象
  - D4 成本明细：TCO 含隐藏费用（存储超额/带宽/运维工时）+ 汇率处理说明
- **依赖**：A2 + A3
- **预期产出**：选型报告核心内容（落报告 §3-§5）
- **验收**：D1-D4 全齐；推荐方案有逐条约束证据；备选分层清晰；淘汰理由可追溯到硬约束
- **关键前提标注**：飞书标准版 1500GB 存储下沿风险（02.5 攻击轮 4）→ 若人均 >50GB 则需升专业版

### A5 证据链完整性检查 — owner: agent
- **输入**：02 S1-S38 + 02.5 X1-X4/A1-A10 + 本报告引用
- **动作**：核对每条关键主张在报告中有对应来源编号；无来源的主张显式标"存在性断言-未核验"
- **依赖**：A4
- **预期产出**：证据链对照表（报告 §6）
- **验收**：抽查 5 条关键主张，来源编号可追溯到 02 S 索引；零"无来源当事实"
- **并行**：无（必须在 A4 后）

### A6 M8 计分表 — owner: agent
- **输入**：本 run 全部六阶段工件 + M8 口径（design.md §M8 口径）
- **动作**：
  - 列出全部核验条目（V1-Vn），每条标通道 conf + 过三测判定
  - 计算 M8 = Σ(通过权重) / Σ(全部权重)
  - 表演型质疑单列（预期 0 条）
  - 落 `experiments/T8-matrix/runs/tselect-vfull-filecollab/m8-scorecard.md`
  - design.md 表格第 3 行回填
- **依赖**：A5（全部工件就绪后）
- **预期产出**：m8-scorecard.md + design.md 更新
- **验收**：M8 数值可复算；design.md 第三行域=file-collab、M8=数值、verdict=pass/revise
- **注意**：U1（cost-model bug）修正前不得计分——A1 是前置

### A7 commit + push + ls-remote 验证 — owner: agent
- **输入**：全部新工件（stages/02/02.5/03/04/04.5 + runs/tselect-vfull-filecollab/ + design.md）
- **动作**：git add + commit（含全部 loop-artifacts/）+ push origin + `git ls-remote origin` 验证落点
- **依赖**：A6
- **预期产出**：远程分支 HEAD = 本地 commit hash
- **验收**：ls-remote 输出含本次 commit hash
- **失败处理**：push 失败 → 记录原因，不阻塞（本地 commit 已保存）

---

## 2. 依赖关系图

```
A1 (fix cost model) ──┬──> A2 (compliance matrix) ──┐
                      │                              ├──> A4 (recommendation) ──> A5 (evidence check) ──> A6 (M8) ──> A7 (push)
                      └──> A3 (TCO layers) ──────────┘
```

- A2/A3 可并行（都只依赖 A1）
- A4 必须等 A2+A3
- A5→A6→A7 严格串行
- **无 user 步骤**（本 run 全程 agent 可离线执行；国内可达性 U7 以风险项标注，不需用户确认）

---

## 3. 关键失败情况与替代路径

| # | 失败场景 | 影响 | 替代路径 | 停止条件 |
|---|----------|------|----------|----------|
| F1 | open.er-api.com 不可达 | A1 无法取汇率 | 用 T7.1 先例 6.68（S53/S54） | 两个源都不可达 → 标"汇率未核验"，TCO 给 USD+CNY 双币 |
| F2 | 某候选定价页 bot-wall 拦截 | 该候选价格只能靠二手源 | 标 lead-unverifiable + 用搜索元数据值 | 无任何来源 → 该候选标"价格未核验"，不作成本结论 |
| F3 | git push 失败（网络/auth） | A7 无法完成 | 本地 commit 保留，记录失败原因 | 重试 2 次仍失败 → 标"push 未完成"，下次唤醒补推 |
| F4 | 04 执行中发现 02 证据有误 | 需回退 02 | 登记到 04 执行日志，标 repair_stage=02 | 仅当错误改变推荐方案时才回退；否则在 04.5 登记为残余风险 |

---

## 4. 阶段判定

- 行动步骤覆盖目标 ✅（D1-D5 全有对应步骤）
- 每步有明确产出和验收方式 ✅
- 依赖关系完整且无循环 ✅（DAG 结构）
- 关键未知未被当成已知前提 ✅（U1-U10 全部显式标注）
- 另一执行者可直接依据本工件行动 ✅（每步有输入/动作/依赖/产出/验收）
- owner 标注 ✅（全 agent，无 user 步骤——本 run 无需用户交互）

**判定：pass → 进入 04。**（conf-0.2，E1 降级）