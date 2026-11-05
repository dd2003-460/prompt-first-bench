# 03 — RV3G6-kappa-formula-adjudicate · 行动分解

> goal: U-K1 κ 公式裁定备料（三方案对照，不代裁）· 分支 ralph/rv3g6-kappa-formula-adjudicate · 2026-10-30
> 输入：02（F1-F6）+ 02.5（X1-X6）。本阶段只分解动作，不执行。

## 动作表

| # | 动作 | 产出 | 验收 | 依赖 |
|---|------|------|------|------|
| A1 | 落盘主材料 `bench/rubric-v3/kappa-u1k1-adjudication-materials.md`，六节结构（对齐 jaccard-m5 先例 + X2 差异修正）：§1 溯源 byte-exact（§4.3 原文 + DRAFT L16/L208/L307 原文 + protocol L71 原文）/ §2 关键发现（**发散型缺口**定性 + F4 精确化：「预注册下限」无数字落点，0.6 是外部推断值 + 判者数错配 + schema 已隐含 Cohen's+2judge 的既成矛盾 X3a）/ §3 三方案对照表（F3.4 八维 × F1/F2/F3 + S2 小例四口径数值行）/ §4 排序 + 适用条件（**非强推荐**，X4 措辞纪律）+ 折中出口（阈值降 SIGNAL，与公式正交）/ §5 裁定后执行清单（D1-D6 × 各方案 diff 面，含 assert-kappa-receipt.py judges 字段放宽项）/ §6 边界声明（零修改冻结件 + unverified 标注 + 不算真实 κ） | 文件落盘 | 五要素齐 + 每格有依据 | 02/02.5 |
| A2 | §1 溯源段 byte-exact 核验：对 §4.3 / DRAFT L16 / L208 / L307 / protocol L71 五处引用逐字 grep 比对（sed 提取 vs 材料内文本 diff） | 核验记录（写入 04） | 5/5 逐字一致（允许登记在案的渲染省略，同 jaccard-m5 先例规则） | A1 |
| A3 | 数值自检终验：S1/S2/S3 全部分数用独立 Fraction 脚本重算一遍（吃矩阵不吃过程），与材料表格逐一比对 | 核验记录（写入 04） | 零 mismatch（−5/27、13/30、1/9、1/4、1/5、1/2、0 全对） | A1 |
| A4 | 冻结面零修改验证：`git status --short` 确认改动面 = 新文件（materials + loop-artifacts）+ queue（收口时），o3-claim-list.md / DRAFT v2 / judge-protocol-batch1.md / assert-kappa-receipt.py / revision-log 零触碰 | git status 输出 | 冻结文件零出现 | A1 |
| A5 | 回归基线维持：跑既有断言脚本确认本 goal 未扰动任何基线——assert-o3-claim-list.py（4/4）、assert-gmr-recompute.py（exit 0）、assert-kappa-receipt.py（FAIL exit 1 常态——kappa-receipt.json 不存在，预期行为不变）、assert-o3-claim-rejudge.py（SIGNAL blocked-on-external exit 0） | 四个 exit code | 与 r142 收口时基线一致 | A1 |
| A6 | 04.5 反方复核（八攻击模板，按 X6 风险声明重点布防：变相代裁 / F4 越界 / 数值抄写 / 先例格式偏离 / 执行清单不可照做） | loop-artifacts/stages/04.5/RV3G6kfa-final-review.md | verdict pass | A1-A5 |
| A7 | 收口：queue 更新（本 goal 划掉 + 结果注记 + 追加新导出候选 ≥1）+ commit + push + merge main | queue diff + main log | 队列状态与实际一致 | A6 |

## 不做的事（边界重申）

- **不代裁**：§4 排序是决策输入；材料落盘即本 goal 完成，裁定 = 成璐的人工动作（同 RV3B1-jaccard-adjudicate 先例）。
- **不改冻结件**：§5 执行清单只描述 diff 面（文件 + 行级位置 + 改写方向），不执行。裁定后由 runner 另开 goal 执行（或成璐直接勾选后并入下次触碰该文件的 goal）。
- **不算真实 κ / 不重标定 0.6**：F4 选项 α（重新标定）需要人-人基线数据（仓库内不存在）→ 如实标注为新增外部依赖，不在本 goal 追。
- **不动 assert-kappa-receipt.py 现状**：A5 只验证其基线行为不变；method 字段收紧 / judges 字段放宽都是裁定后的动作（§5 清单内容）。

## 新导出候选预判（A7 消费，此处预注册）

- **RV3G6-kappa-threshold-recalibrate**（若成璐裁定时选 F4 选项 α）：0.6 阈值对新公式的重标定——需人-人一致性基线（外部）或至少同族多 prompt 敏感性扫描（仓库内可做但工作量另估）。当前仅登记方向，不展开。
- **RV3G4-kappa-gate-execution 联动注记**：U-K1 裁定落盘后，该 goal 的执行协议（怎么算、填什么 method 字符串）即刻闭合——在 queue 条目上加一行联动注记即可，不另立 goal。