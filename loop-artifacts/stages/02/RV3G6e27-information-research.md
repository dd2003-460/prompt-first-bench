# 02 — 研究：§3.2 声明 4「27/98」勘误备料

> goal: RV3G6-o3-claim-list-erratum-27 · r144+ · 分支 ralph/rv3g6-o3-claim-list-erratum-27
> 只读事实源：o3-claim-list.md（main @ 404ba7e）/ hit-matrix.json / gold-tree.md / assert-hitmatrix-evidence.py / r142 前序工件

## F1 — 失实数字的原文定位（byte-exact）

`bench/rubric-v3/o3-claim-list.md` **L137**（§3.2 口径声明第 4 条，全文单行）：

```
4. **evidence 文本本身含 gold 数值不构成泄漏通道**（已核：98 个 h=1 cell 中 27 个 evidence 含 gold-tree 数值 token，如「27B」「3 年」——这些是 run 自产文本被冻结进 hit-matrix，属 #13 假命中的证据而非答案注入；§2 claim 文本的防泄漏由 assert 脚本检查②独立保证，两者不混用）。
```

失实点仅一处：**「27」**。同文件内 grep「27」共 2 处命中——L137（本声明）与 L178（「qwen3.8-**27**b 底座」模型名，无关）。改动面 = 1 行内 1 个数字 + 可选注记。

**冻结状态确认**：文件头 L6「判据件冻结——修改 = 新 goal + APPROVALS.md 登记」+ §6 L192-200 冻结声明。本 goal 即该机制预留的勘误通道（开新 goal ✓），但改法选择权在成璐（APPROVALS 登记后裁定）。

## F2 — 三口径定义与 r142 A4 材料复核

r142 (RV3G6-o3-claim-rejudge-evidence-audit) `loop-artifacts/stages/04/RV3G6o3ea-execution-verification.md` A4 节（byte-exact 摘录）：

| 口径 | 定义 | 计数 |
|------|------|------|
| V1 | per-line token − 噪声豁免（assert 现行同源） | **13**/98 |
| V2 | gold-tree 全文件 token − 同豁免 | **34**/98 |
| V3 | per-line token，无豁免 | **35**/98 |

A4 定性原文：「27 = o3-claim-list 起草期不可复现人工计数（或用了未落盘中间口径）。结论方向不受影响……但**数字本身失实**。」

三方案对照所需的关键语义区分：
- **V1 是唯一与既有机判脚本同源的口径**——`assert-hitmatrix-evidence.py` A4 段（L140-154）实现的就是 V1（per-line 节点行 token − noise_exempt），且常态输出「V1 计数 = 13/98 vs 声明值 = 27（MISMATCH）」。**任何回填数字若 ≠ V1，都会与该脚本常态输出再次冲突**（双源漂移风险，同 R-09 D2 双源论证先例）。
- V2/V3 是 r142 02 F3 为溯源而临时定义的对照口径，**无任何脚本持续维护**——写进冻结件会成为新的孤儿数字（下次无人能复现，重演 27 的失败模式）。
- 「27」本身：r142 A4 抽样实证 V1→27 无任何可复现路径（V2-only 额外 21 例几乎全是跨区型号/比例 token；V3−V1=22 例差异来自豁免集 {0,1,ID 分段,31,4,13}）。

## F3 — 下游消费者枚举（谁引用了这个数字）

grep 全仓（排除 .git）「27 个 evidence」/「声明 4」引用面：

| 消费者 | 位置 | 引用方式 | 受勘误影响 |
|--------|------|----------|-----------|
| assert-hitmatrix-evidence.py | ablation/scripts/ L27-29, L152-154 | 硬编码 `declared = 27` 做 mismatch 对照 | **是**——勘误落地后该脚本的 declared 常量需同步（否则 MISMATCH 提示永久失真）；同步动作列入裁定后执行清单 |
| r142 02/04 工件 | loop-artifacts/stages/0{2,4}/RV3G6o3ea-* | 历史审计记录（13/34/35 对照表） | 否——历史工件不改（审计链保留原始发现过程） |
| queue L23 条目 | tasks/goal-queue.md | 描述性引用「三口径均≠27」 | 否——描述的是发现过程，非消费该数字 |
| 其他 bench/ 文档 | — | 未发现引用「27 个 evidence」的数字消费 | 否 |

**关键结论**：数字的实际消费者只有 1 个（assert 脚本的 declared 常量），且该脚本自身就是勘误的验证器——这使「改数字」的执行成本极低（2 文件各 1 行）。

## F4 — 三个候选改法的精确 diff 面

### 方案 A：直接改 13（V1 口径，推荐）

o3-claim-list.md L137 最小 diff（只动数字 + 加口径锚点，机制表述零改动）：

```diff
-4. **evidence 文本本身含 gold 数值不构成泄漏通道**（已核：98 个 h=1 cell 中 27 个 evidence 含 gold-tree 数值 token，如「27B」「3 年」——这些是 run 自产文本被冻结进 hit-matrix，属 #13 假命中的证据而非答案注入；§2 claim 文本的防泄漏由 assert 脚本检查②独立保证，两者不混用）。
+4. **evidence 文本本身含 gold 数值不构成泄漏通道**（已核：98 个 h=1 cell 中 13 个 evidence 含 gold-tree 数值 token【V1 口径 = per-line 节点行 token − 噪声豁免，assert-hitmatrix-evidence.py A4 段机判可复现；r142 勘误：原值 27 为起草期不可复现人工计数】，如「27B」「3 年」——这些是 run 自产文本被冻结进 hit-matrix，属 #13 假命中的证据而非答案注入；§2 claim 文本的防泄漏由 assert 脚本检查②独立保证，两者不混用）。
```

配套：assert-hitmatrix-evidence.py L152 `declared = 27` → `declared = 13` + 注释更新（勘误后常态输出转「一致」）。

### 方案 B：三口径并列呈现

L137 改为：「已核：98 个 h=1 cell 中含 gold-tree 数值 token 的 evidence 数按口径计 V1(per-line−豁免)=13 / V2(全文件−豁免)=34 / V3(per-line 无豁免)=35，机判基准取 V1（assert-hitmatrix-evidence.py A4 段）；原值 27 为起草期不可复现人工计数」。

代价：把两个无脚本维护的孤儿口径（V2/V3）固化进冻结件——未来 gold-tree/hit-matrix 再变时这三个数字都需重算，维护面 ×3。

### 方案 C：删具体数字只留机制表述

L137 改为：「evidence 文本本身含 gold 数值不构成泄漏通道（部分 evidence 含 gold-tree 数值 token，逐格机判见 assert-hitmatrix-evidence.py A4 段——这些是 run 自产文本被冻结进 hit-matrix，属 #13 假命中的证据而非答案注入；§2 claim 文本的防泄漏由 assert 脚本检查②独立保证，两者不混用）。原「已核 27 个」数字经 r142 三口径复算不可复现，已撤除。」

代价：读者失去量级感（13/98 ≈ 13% 这个比例对判断「假命中占比」有参考价值）；但彻底消除孤儿数字复发可能。

## F5 — 推荐排序依据（供成璐消费，非裁定）

三维评估：

| 维度 | A 改 13 | B 三口径 | C 删数字 |
|------|---------|----------|----------|
| 可复现性 | ★★★（与 assert 脚本同源，常态机判守护） | ★（V2/V3 无脚本维护，孤儿数字复发风险） | ★★★（无数字可失实） |
| 信息保留 | ★★★（数字+口径+溯源注记全保留） | ★★★ | ★（量级感丢失） |
| 改动面/维护成本 | 2 文件各 1 行 | 1 文件 1 行但维护面×3 | 1 文件 1 行 |

**推荐 A**。理由：(1) 唯一同时满足「数字可机判复现 + 信息完整 + 改动面最小」的方案；(2) assert 脚本成为常态守护者——未来任何 hit-matrix/gold-tree 变更导致计数漂移都会显式 MISMATCH，27 型静默失实不可能复发；(3) 括号内溯源注记保留了「为什么从 27 改成 13」的审计链，不抹掉历史。折中出口：若成璐认为溯源注记太长破坏可读性，可缩为「（V1 口径，assert-hitmatrix-evidence.py 机判；原值 27 见 r142 勘误）」。