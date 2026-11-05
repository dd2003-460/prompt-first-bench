# §3.2 声明 4「27/98」数字勘误裁决材料 — RV3G6-o3-claim-list-erratum-27

> 状态：**材料已备，待成璐裁定**（runner 不代裁——同 jaccard-m5-adjudication-materials.md 先例）
> 依据：r142 (RV3G6-o3-claim-rejudge-evidence-audit) A4 节三口径独立复算 + 本 goal 02.5 X1 二次独立复算（双源一致）
> 冻结件：`bench/rubric-v3/o3-claim-list.md` L137（§6 红线：修改 = 新 goal + APPROVALS 登记；本文件即该通道备料）

## 1. 溯源：失实数字原文（byte-exact）

`o3-claim-list.md` **L137**（§3.2 口径声明第 4 条）：

```
4. **evidence 文本本身含 gold 数值不构成泄漏通道**（已核：98 个 h=1 cell 中 27 个 evidence 含 gold-tree 数值 token，如「27B」「3 年」——这些是 run 自产文本被冻结进 hit-matrix，属 #13 假命中的证据而非答案注入；§2 claim 文本的防泄漏由 assert 脚本检查②独立保证，两者不混用）。
```

失实点仅一处：**「27」**。同文件 grep「27」另一命中在 L178（「qwen3.8-27b 底座」模型名，无关）。

## 2. 关键发现：27 不可复现，三口径均 ≠ 27

| 口径 | 定义 | 计数 | 维护状态 |
|------|------|------|----------|
| V1 | per-line（节点 ID 所在行）token − 噪声豁免（ID 分段 + 一级前缀 + {0,1,31,4,13}） | **13**/98 | **assert-hitmatrix-evidence.py A4 段常态机判**（与 assert-o3-claim-list.py 同源） |
| V2 | gold-tree 全文件 token − 同豁免 | **34**/98 | 无脚本维护（r142 临时对照口径） |
| V3 | per-line token，无豁免 | **35**/98 | 无脚本维护（r142 临时对照口径） |

- 双源验证：r142 A4 首算 13/34/35 + 本 goal 02.5 X1 从原始数据二次独立复算 13/34/35，逐格一致（V1 全 13 例清单比对通过）。
- r142 A4 抽样实证：V2-only 额外 21 例几乎全是跨区型号/比例 token（'3090' GPU 型号 / '90:9:1' 缓存比例 / '100' A100 型号段）；V1→27 无任何可复现路径。**定性：27 = 起草期不可复现人工计数（或用了未落盘中间口径）**。
- **结论方向不受影响**：声明 4 论证的是机制（evidence 含 gold 数值 ≠ 泄漏通道），对 13/27/34 任一计数都成立；失实的只是数字本身。
- 下游消费者只有 1 个：assert-hitmatrix-evidence.py（docstring L26 + `declared = 27` 常量 L151 + 输出文案 L154）——该脚本常态输出 MISMATCH 提示即为勘误信号源。

## 3. 三方案对照表

| | A · 直接改 13（V1） | B · 三口径并列 | C · 删数字留机制 |
|---|---|---|---|
| L137 改法 | 「27 个」→「13 个」+ 括号内加口径锚点注记（V1 定义 + 机判脚本指向 + r142 勘误溯源） | 「27 个」→「V1=13 / V2=34 / V3=35（机判基准取 V1）」+ 原值 27 溯源注记 | 删「已核：…27 个…」整段数字表述，改「部分 evidence 含 gold-tree 数值 token，逐格机判见 assert-hitmatrix-evidence.py A4 段」+ 撤除说明 |
| 配套改动 | assert 脚本 3 处同步（L26 docstring / L151 declared=13 / L154 文案）→ 常态输出转「一致」 | assert 脚本 declared=13 + 注释「文中并列值仅历史溯源，机判基准=V1」 | assert 脚本 A4 段降级为纯计数报告（移除 mismatch 对照逻辑） |
| 可复现性 | ★★★ 数字有常态机判守护，未来漂移显式 MISMATCH | ★ V2/V3 成孤儿数字（无脚本维护，重演 27 失败模式风险） | ★★★ 无数字可失实 |
| 信息保留 | ★★★ 数字+口径+审计链全保留 | ★★★ | ★ 量级感丢失（13/98≈13% 对判断假命中占比有参考价值） |
| 改动面 | o3-claim-list 1 行 + assert 3 处 + revision-log 1 条目 | o3-claim-list 1 行 + assert 2 处 + revision-log 1 条目 | o3-claim-list 1 行 + assert A4 段重写 + revision-log 1 条目 |
| 主要风险 | 括号注记略长（可缩为短注记折中） | 维护面×3，gold-tree/hit-matrix 再变时三口径都要重算 | 读者失去量级感 |

## 4. 推荐（供成璐消费，非裁定）

**推荐 A**。理由：(1) 唯一同时满足「数字可机判复现 + 信息完整 + 改动面最小」；(2) assert 脚本成为常态守护者——hit-matrix/gold-tree 任何变更导致计数漂移都会显式 MISMATCH，27 型静默失实不可能复发；(3) 括号内溯源注记保留「为什么从 27 改成 13」的审计链，不抹掉历史。

**折中出口**：若认为 A 的括号注记太长破坏可读性 → 缩为「（V1 口径，assert-hitmatrix-evidence.py 机判；原值 27 见 r142 勘误）」；若连短注记都不要 → 退到 C。

## 5. 裁定后执行清单（成璐勾选后由 runner 执行）

### 方案 A 执行序列（推荐）

1. `APPROVALS.md` 追加登记条目（模板见下）
2. `o3-claim-list.md` L137 diff：
   ```diff
   -4. **evidence 文本本身含 gold 数值不构成泄漏通道**（已核：98 个 h=1 cell 中 27 个 evidence 含 gold-tree 数值 token，如「27B」「3 年」——
   +4. **evidence 文本本身含 gold 数值不构成泄漏通道**（已核：98 个 h=1 cell 中 13 个 evidence 含 gold-tree 数值 token【V1 口径 = per-line 节点行 token − 噪声豁免，assert-hitmatrix-evidence.py A4 段机判可复现；r142 勘误：原值 27 为起草期不可复现人工计数】，如「27B」「3 年」——
   ```
   （行尾「这些是 run 自产文本……两者不混用）。」零改动）
3. `ablation/scripts/assert-hitmatrix-evidence.py` 3 处同步：L26 docstring「27 个」→「13 个（原 27 已勘误）」/ L151 `declared = 27` → `declared = 13` / L154 MISMATCH 文案改为「（MISMATCH——计数漂移，查 hit-matrix/gold-tree 变更）」
4. `revision-log-batch1.md` 追加条目（模板见下）
5. 回归：`python3 ablation/scripts/assert-hitmatrix-evidence.py` 预期末行「V1 计数 = 13/98 vs …声明值 = 13（一致）」+ VERDICT PASS exit 0；四脚本基线回归（assert-o3-claim-list 4/4 · assert-goldrank-threshold 31 PASS · assert-gmr-recompute 11 PASS · assert-o3-claim-rejudge SIGNAL blocked-on-external）
6. queue L24 `[~]` → `[x]` + 结果注记

### 方案 B 执行序列

步骤 1/4/5/6 同上；步骤 2 替换为：L137「27 个」→「按口径计 V1(per-line−豁免)=13 / V2(全文件−豁免)=34 / V3(per-line 无豁免)=35，机判基准取 V1（assert-hitmatrix-evidence.py A4 段）；原值 27 为起草期不可复现人工计数」；步骤 3 替换为：assert 脚本 L151 declared=13 + 注释「文中 V2/V3 并列值仅历史溯源，无脚本维护」。

### 方案 C 执行序列

步骤 1/4/5/6 同上；步骤 2 替换为：L137 整句改为「**evidence 文本本身含 gold 数值不构成泄漏通道**（部分 evidence 含 gold-tree 数值 token，逐格机判见 assert-hitmatrix-evidence.py A4 段——这些是 run 自产文本被冻结进 hit-matrix，属 #13 假命中的证据而非答案注入；§2 claim 文本的防泄漏由 assert 脚本检查②独立保证，两者不混用。原『已核 27 个』数字经 r142 三口径复算不可复现，已撤除）」；步骤 3 替换为：assert 脚本 A4 段移除 declared 对照，改为纯计数报告行。

### APPROVALS.md 登记模板

```markdown
## 2026-10-30 · RV3G6-o3-claim-list-erratum-27（r14x）— §3.2 声明 4 数字勘误

**操作**：`bench/rubric-v3/o3-claim-list.md` L137 单行修改（「27 个」→「13 个」+ V1 口径注记）+ `ablation/scripts/assert-hitmatrix-evidence.py` 3 处同步（docstring/declared 常量/输出文案）。

**理由**：r142 A4 + 本 goal 02.5 X1 双源独立复算证实原值 27 不可复现（三口径 13/34/35 均≠27）；结论方向不受影响，仅数字失实。改法 = 成璐裁定方案 A/B/C。

**影响面声明**：o3-claim-list.md 改动面限 L137 单行（§2/§4/§6 零触碰）；assert 脚本改动面限 A4 段 3 处（C1-C5 判定逻辑零触碰）；hit-matrix.json / gold-tree.md / runs-C0-* 冻结数据零修改。

**回退方式**：`git revert <收口 commit>` 单步还原。

**状态**：已执行（成璐裁定方案 X 后 runner 落地）。
```

### revision-log-batch1.md 条目模板

```markdown
## §3.2 声明 4 数字勘误（RV3G6-o3-claim-list-erratum-27 · r14x · 2026-10-30）

**范围**：o3-claim-list.md §3.2 口径声明 4 的「27」勘误为「13」（V1 口径）——数字失实修正，机制表述零改动。

| 项 | 落点 | 验证 |
|----|------|------|
| 勘误本体 | o3-claim-list.md L137 | assert-hitmatrix-evidence.py 常态输出转「一致」 |
| 脚本同步 | assert-hitmatrix-evidence.py L26/L151/L154 | 回归 exit 0 + 四脚本基线维持 |
| 溯源 | 本登记 + APPROVALS.md 条目 | — |

**诚实保留**：V2/V3 口径（34/35）不写入冻结件（无脚本维护的孤儿数字风险）；若未来需要三口径并报，另开 goal 并配维护脚本。
```

## 6. 边界声明

- **runner 只备料不代裁**：三个方案的精确 diff 已预写，但 o3-claim-list.md / assert 脚本 / revision-log / APPROVALS 四个文件在本 goal 全程**零触碰**（git status 验证）。裁定是成璐的人工动作。
- 本材料不改 r142 历史工件（loop-artifacts/stages/0{2,2.5,4}/RV3G6o3ea-*）——审计链保留原始发现过程（「当时发现 27 失实」的记录不因后续勘误而改写）。
- web-llm 交叉验证：unverified 降级（三 provider 登录态失效，沿用 r124 起惯例）——本 goal 证据链仓库内闭合（双源独立复算 + 既有 assert 脚本常态输出），外部第二意见边际贡献 ≈ 0。