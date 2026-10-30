# origin: ai — 当前 goal（r153）

## 【目标】
RV3G3cdx-crossdomain-promptversion-mapping：M1 完整 fail-loud 协议承接（r150 Y2 降级项）——「题面版本↔gold_nodes 映射表」权威源建立 + assert-goldrank-crossdomain.py load_batch2 对照检查实现（prompt_version 声明的题面版本 → 映射表查得 gold 清单 → 与显式 gold_nodes 一致性机判，换题面未声明/错配 = exit 2）。

## 【阶段】
1-loop 六阶段（01→04.5），产出落盘 loop-artifacts/stages/<N>/RV3G3cdx-cdpm-*。

## 【SOP 索引】
loop/prompt-first/01..04.5 + sop/arena-loop-pipeline.md；前序工件 r150 stages/02+04.5（M1-M3 登记处）、assert-goldrank-crossdomain.py docstring D1/Y1/Y2 节、DRAFT-rubric-v3-v2.md §3.2 变体矩阵冻结规则（B10）、revision-log-batch1.md R-10 回填状态（冻结 commit 61416b4）。

## 【验收标准】
1. 映射表 JSON 落盘 bench/rubric-v3/ablation/prompt-version-gold-map.json（含 domain1 既有域条目 + 消费规则文档化）。
2. assert-goldrank-crossdomain.py load_batch2 新增 C-对照检查：prompt_version 在映射表中 ⇒ 显式 gold_nodes 必须与映射表该版本 gold 清单一致（不一致 = exit 2 指名道姓）；prompt_version 不在映射表 ⇒ SIGNAL（不代裁新域建表）；缺省路径（无 gold_nodes 声明）行为零变化。
3. 样例矩阵扩展：正样例 ×2（声明匹配 / 缺省沿用）+ 负样例 ×3（版本未知 / 清单错配 / 映射表 schema 违例）全实证对应出口。
4. byte-exact 回归：无参调用输出与改动前逐字节一致（当前 ablation 面常态 = SIGNAL blocked-on-external exit 0）。
5. 十五脚本基线零漂移 + 冻结面 0 diff + queue-lint exit 0。
6. 04.5 八攻击反方复核 verdict pass。

## 【失败降级】
- 若映射表权威源认定存在仓库内不可消解的二义性（如 V0 归属）→ 登记矛盾 + 选保守口径（fail-safe 方向 = 多报 SIGNAL 不误报 FAIL）+ APPROVALS 登记待成璐裁定，不阻塞收口。
- 若对照检查引入既有样例回归失败 → 回滚脚本改动，仅交付映射表 + 规格文档，检查实现导出下轮候选。
