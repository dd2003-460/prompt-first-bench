# Goal: RV3G6-o3-claim-list — O3 gold 节点转原子 claim 清单

> 创建：2026-10-30 · ralph loop runner（queue 队首）
> 依据：`bench/rubric-v3/AUDIT-report.md` §2-O3（L79，finding #13 处置「采纳」）+ §9.1 R-13 + queue 候选描述

## 【目标】
把 gold-tree 的 31 个节点从「节点 ID 对得上才算命中」（DRAFT v1 L58 / v2 L71 现行判据，AUDIT finding #13 判定**不可执行**）转换为一份**原子 claim 清单** `bench/rubric-v3/o3-claim-list.md`：
1. **逐节点 claim 转换**：每个 gold 节点 → 1-2 句可判真假的实质内容陈述（judge 判「产出是否包含该实质内容」而非「是否出现节点 ID」）。claim 必须满足：(a) 自含——不读 gold-tree 全文也能理解在说什么；(b) 可二值判——yes/no 无中间态；(c) 方向正确性内嵌——错误方向的覆盖不算命中（沿用 TASK-ablation Step 1「方向正确」要求）。
2. **映射一致性指标定义**：定义「claim 级判定 vs 旧节点 ID 级判定」的一致性度量（主口径 = 按 run 聚合的 hit 向量一致率），并给出冻结数据上的基线值（hit-matrix.json 8×31 为唯一可用输入，claim 级重判本身需独立 judge = unverified，见失败降级）。
3. **多判者规则文字化**：AUDIT §2-O3 的「≥2/3 独立判者一致」落为可操作协议（判者数 N=3、tie 处理、与 κ 条目层门禁的关系）。
4. **DRAFT v2 O3 节修订**：L71「命中判据不变」行替换为引用本清单的新判据 + `[batch2: R-13]` 占位标记更新为已落地状态（R-13 是 batch2 项，本 goal 提前落地其核心件，revision-log 登记范围切割理由）。

## 【阶段】
rubric-v3 审计链修订落地环。纯仓库内文本工作 + 机判脚本，不改任何冻结数据（gold-tree.md / hit-matrix.json 只读）。claim 措辞属人工判断项——runner 起草全部 31 条并用冻结数据自检，最终措辞审定留成璐（APPROVALS 登记，不阻塞）。

## 【SOP 索引】
- `sop/arena-loop-pipeline.md`（唯一 SOP 入口）
- `loop/prompt-first/00..04.5`（六阶段定义）
- `bench/rubric-v3/AUDIT-report.md`（上游定稿，§2-O3 L79 / §9.1 R-13 L293 / §9.3 L312 是主要消费对象）
- `bench/rubric-v3/ablation/gold-tree.md`（31 节点源，只读）
- `bench/rubric-v3/DRAFT-rubric-v3-v2.md`（O3 节 L62-82 是修订对象）
- `bench/rubric-v3/ablation/hit-matrix.json`（evidence 字段 = claim 措辞的校准材料，只读）

## 【验收标准】
- [ ] o3-claim-list.md 落盘：31 节点全覆盖，每节点 1-2 句 claim + 判据说明（自含/可二值/方向内嵌三属性逐条可查）
- [ ] 映射一致性指标有正式定义（公式 + 口径 + 分母声明）+ 冻结数据基线值（机算，脚本可复现）
- [ ] ≥2/3 多判者协议文字化（N/tie/与 κ 门禁关系三要素齐全）
- [ ] DRAFT v2 O3 节 L71 判据行更新 + revision-log 追加 R-13 条目（含范围切割说明）
- [ ] 机判脚本 assert-o3-claim-list.py exit 0（结构完整性：31 节点无缺漏 / claim 非空 / 指标基线值复算一致）
- [ ] 冻结数据零修改（git status 验证 gold-tree/hit-matrix/prior-estimates/stats-* 无 diff）
- [ ] 04.5 反方复核 verdict pass

## 【失败降级】
- 某节点无法写出可二值判的 claim（如纯结构性节点）→ 该节点标 NA 档 + 理由，不硬凑（NA 节点在指标分母中显式声明）
- claim 级独立重判需要 fresh-context judge → 工具纪律禁 subagent，标 unverified，用 hit-matrix evidence 字段做措辞校准替代，补数路径导出 queue
- DRAFT v2 修订与其他 batch2 项冲突 → 只动 L71 判据行 + 占位标记，其余不动，冲突登记 APPROVALS