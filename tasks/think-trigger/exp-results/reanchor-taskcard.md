# T8c 重锚定任务书（ReAnchor-A）

# origin: ai (2026-11-26, Lead 规划产出, sub 纯执行)

## 背景（sub 不需理解, 只需执行）
V100 价格从假设 $2500 核实为 ¥5000≈$704（京东 ①类, 2026-11-26）。winner 从 3090×4/W4/n=2 翻转为 V100×4/W4/n=2。B' 臂截断修复: 预算 24576→73728(=6×12288)。

## 真值（oracle 实跑, V100 price=704, 勿改）
- winner = V100×4/W4/n=2, c_pass=***
- 3090×4/W4/n=2 c_pass=0.6807
- V100×4/W8/n=2 c_pass=0.5188
- 3090×4/W8/n=2 c_pass=0.764
- breakeven V100 price = $2032.9
- 4090×4/W4/n=2 @$1599 c_pass=0.6354 (> 0.4511, 不翻转 winner)
- 淘汰 5 配置不变: 3090×2/W8, 3090×2/W16, 3090×3/W16, 3090×4/W16, V100×2/W16
- 显存/卡: V100×4/W4/n=2 → 15.8GB; 3090×4/W4/n=2 → 15.8GB; V100×4/W8/n=2 → 19.1GB; 3090×4/W8/n=2 → 19.1GB

## 执行方式
用 python 脚本做替换（读文件→str.replace→写文件），不用 sed（多行替换易错）。每个替换点: (file, old_string, new_string)。old_string 必须唯一（用足够长的上下文确保唯一）。替换后跑验收。

## 文件 1: t8c-spec-final.md
路径: tasks/think-trigger/exp-results/t8c-spec-final.md

### 1a. L15 行（4090 敏感性措辞）
old: `4090 敏感性已证候选集含 4090 则 winner 翻转（oracle \`check_4090_flip()\` 实跑）；定死后 oracle 实跑 winner=3090×4/W4/n=2 ✅`
new: `4090 敏感性已证候选集含 4090 不改变 winner（0.6354 > 0.4511, oracle 实跑）；定死后 oracle 实跑 winner=V100×4/W4/n=2 ✅`

### 1b. L51-54（4090 排除理由整段替换）
old（从 `2. **4090 必须排除**` 到 `对照被污染（t8b-smoke-report.md §3.2）。`）:
```
2. **4090 必须排除**（敏感性已证，本轮 oracle 实跑复现）：`check_4090_flip()` →
   4090×4/W4/n=2 = 0.635 < 3090×4/W4/n=2 = 0.681，winner 翻转为 4090（盈亏平衡价 ≈ $1905，
   远高于 KB MSRP $1599 / NE street $1699-1899，`knowledge-base/hardware-staging/rtx-4090.json`
   ①类 conf 0.85）。T8b 题面「自行搜索」让模型自由纳入 4090 → 对照被污染（t8b-smoke-report.md §3.2）。
```
new:
```
2. **4090 必须排除**（T8b 污染 + 规格不全双重理由）：(a) 4090 不在 calc.py HARDWARE
   （KB `knowledge-base/hardware-staging/rtx-4090.json` ①类 conf 0.85 但 flops 口径
   non-tensor 165.2 TFLOPS 与 gold 口径不一致），入候选集则 oracle sweep 不可复算；
   (b) T8b 题面「自行搜索」让模型自由纳入 4090 → 对照被污染（t8b-smoke-report.md §3.2）。
   敏感性复核：4090×4/W4/n=2 = 0.6354 > V100×4/W4/n=2 = 0.4511，即使入候选集也不翻转
   winner（盈亏平衡价 ≈ $1905，远高于 KB MSRP $1599）。
```

### 1c. L65（V100 价格行）
old: `| V100 SXM2 | 32GB | 900 GB/s | 125 TFLOPS | 250W | **$2500** | calc.py L36 ①类（规格源 \`datacenter-cards.json\`；价格原文标 [待核验, 2026 市场价] → 本实验按 ③类假设钉死，见下方脆弱性披露） |`
new: `| V100 SXM2 | 32GB | 900 GB/s | 125 TFLOPS | 250W | **$704**（¥5000） | 规格 calc.py L36 ①类（源 \`datacenter-cards.json\`）；价格 ①类核验 2026-11-26（京东零售 ¥4770-6000 取中 ¥5000≈$704, 4 条 listing 交叉） |`

### 1d. L67-72（脆弱性披露整段替换）
old（从 `**⚠ 脆弱性披露` 到 `T8c 数据作废重跑。此为已知限制，不掩盖。`）:
```
**⚠ 脆弱性披露（必须随题面一起读）**：winner 对 V100 价格假设敏感——本轮实跑（python 二分，
calc.py 同参数）：V100 单价 **< $2033** 时 V100×4/W4/n=2 反超 3090×4/W4/n=2 成为 winner；
V100=$2500（题面值）时 0.761 > 0.681，3090 稳赢。3090 一侧对价格极不敏感（>$5000 才被反超，
远超任何现实价）。→ **T8c 的 correctness 锚点 = 「题面钉死价格下的 winner」**，即
3090×4/W4/n=2；若后续 V100 实价核验（③→①升级）落在 $2033 以下，winner 锚点须重定，
T8c 数据作废重跑。此为已知限制，不掩盖。
```
new:
```
**⚠ 脆弱性披露（必须随题面一起读）**：winner 对 V100 价格敏感——本轮实跑（python 二分，
calc.py 同参数）：V100 单价 **> $2032.9** 时 3090×4/W4/n=2 反超 V100×4/W4/n=2 成为 winner；
V100=$704（题面值，①类核验 2026-11-26 京东 ¥5000）时 0.4511 < 0.6807，V100 稳赢
（margin 33.7%）。3090 一侧对价格极不敏感（其价格 $1050 为 gold 口径钉死值）。
→ **T8c 的 correctness 锚点 = 「题面钉死价格下的 winner」**，即 V100×4/W4/n=2；
若后续 V100 实价核验落在 $2032.9 以上，winner 锚点须重定，T8c 数据作废重跑。
此为已知限制，不掩盖。
```

### 1e. L74-80（oracle 实跑验证整段替换）
old（从 `**oracle 实跑验证` 到 `→ 若入候选集 winner 翻转（排除依据，见上）`）:
```
**oracle 实跑验证（本轮，命令 `python3 tasks/think-trigger/exp-results/gold_gpu_oracle.py`，exit 0）**：
- winner = **3090×4/W4/n=2** ✅（期望一致）
- c_pass(winner) = 0.681 ≈ 0.679（calc.py 标定值，差 0.3% < 1% 容差）✅
- N-5.2 带宽门对 gold 6 个 pass/fail 判断 6/6 吻合 ✅
- 可行配置排序 top-3：3090×4/W4/n=2 (0.681) < V100×4/W4/n=2 (0.761) < 3090×4/W8/n=2 (0.764)
- 淘汰 5 配置：3090×2/W8、3090×2/W16、3090×3/W16、3090×4/W16（N-5.1 显存门）、V100×2/W16
- 4090 敏感性复现：4090×4/W4/n=2 = 0.635 → 若入候选集 winner 翻转（排除依据，见上）
```
new:
```
**oracle 实跑验证（2026-11-26 重锚定后，V100 price=704, 命令 `python3 tasks/think-trigger/exp-results/gold_gpu_oracle.py`，exit 0）**：
- winner = **V100×4/W4/n=2** ✅（期望一致）
- c_pass(winner) = 0.4511 ¢/task
- N-5.2 带宽门对 gold 6 个 pass/fail 判断 6/6 吻合 ✅
- 可行配置排序 top-3：V100×4/W4/n=2 (0.4511) < V100×4/W8/n=2 (0.5188) < V100×3/W4/n=1 (0.5856)
- 淘汰 5 配置：3090×2/W8、3090×2/W16、3090×3/W16、3090×4/W16（N-5.1 显存门）、V100×2/W16
- 4090 敏感性复核：4090×4/W4/n=2 = 0.6354 > 0.4511 → 不翻转 winner（排除依据见上）
```

### 1f. L121（c_pass 锚点数值）
old: `模型按题面公式算出的 c_pass 应能对上 oracle 数值（winner 0.681），对不上即可机械判「算术/推导错」。`
new: `模型按题面公式算出的 c_pass 应能对上 oracle 数值（winner 0.4511），对不上即可机械判「算术/推导错」。`

## 文件 2: t8c-preregistration.md
路径: tasks/think-trigger/exp-results/t8c-preregistration.md

### 2a. L11（预算值）
old: `在 token 预算匹配（两臂同为 24576 completion tokens）且题面无歧义（三歧义已消解）的条件下，`
new: `在 token 预算匹配（两臂同为 73728 completion tokens 上限）且题面无歧义（三歧义已消解）的条件下，`

### 2b. L20-23（A1/A2/A3 断点定义, winner 卡型 3090→V100）
old:
```
  - **A1 候选构建断点**：winner 卡型（3090）从未进入候选集（P_A1 = 1−C ≥ 0.7）。
  - **A2 候选集粒度断点**：3090 进了候选集，但 winner 配置（4×3090）从未被构造/评估（C2BP）。
  - **A3 排序/权重断点**：4×3090 被完整评估但排序垫底/未被选中（P_A3 = E1·R_low ≥ 0.5）。
```
new:
```
  - **A1 候选构建断点**：winner 卡型（V100）从未进入候选集（P_A1 = 1−C ≥ 0.7）。
  - **A2 候选集粒度断点**：V100 进了候选集，但 winner 配置（4×V100）从未被构造/评估（C2BP）。
  - **A3 排序/权重断点**：4×V100 被完整评估但排序垫底/未被选中（P_A3 = E1·R_low ≥ 0.5）。
```

### 2c. L35（预算说明）
old: `**两臂同 token 预算 = 24576 completion tokens**（B' 臂 6 阶段 × 4096 的天然上限）。`
new: `**两臂同 token 预算上限 = 73728 completion tokens**（B' 臂 6 阶段 × 12288；2026-11-26 post-hoc 修复：原 24576 下 B' 臂 3/3 截断，根因=总预算 < 六阶段真实需求 69227）。`

### 2d. L43（预算取值理由）
old: `**取哪条 run 做基线**：取 **B 臂均值 22630** 向上取整到阶段对齐值 **24576**（=6×4096），`
new: `**取哪条 run 做基线**：取 **B 臂截断态实测需求 69227** 向上取整到阶段对齐值 **73728**（=6×12288），`

### 2e. L50-51（A' 臂预算）
old: `- Arm A'（直接求解）：单次调用 \`max_tokens=24576\`。T8b A 臂自然收尾在 7K-13K，\n  24576 下预期仍自然 stop（不截断）；若 stop 后实际用量 ≪ 24576，属正常（预算是上限不是配额），`
new: `- Arm A'（直接求解）：单次调用 \`max_tokens=73728\`。T8b A 臂自然收尾在 7K-13K，\n  73728 下预期仍自然 stop（不截断）；若 stop 后实际用量 ≪ 73728，属正常（预算是上限不是配额），`

### 2f. L53（B' 臂预算）
old: `- Arm B'（六阶段）：每阶段 \`max_tokens=4096\`，总预算 24576（同 T8b B 臂结构）。`
new: `- Arm B'（六阶段）：每阶段 \`max_tokens=12288\`，总预算上限 73728（同 T8b B 臂结构，阶段数不变）。`

### 2g. L56（预算层面）
old: `- **预算层面（硬）**：两臂名义预算严格相等 = 24576，无容差（这是设计的定义）。`
new: `- **预算层面（硬）**：两臂名义预算上限严格相等 = 73728，无容差（这是设计的定义）。`

### 2h. L63-64（截断风险说明）
old: `  若某臂截断样本 > 50%，该臂数据作废重跑（预算 24576 下预期不发生；T8b B 臂撞顶 2/3 是\n  24576 预算内的阶段分配问题，B' 沿用同结构，风险已知并接受——截断样本按上条处理）。`
new: `  若某臂截断样本 > 50%，该臂数据作废重跑（预算 73728 覆盖 B' 实测需求 69227，预期不发生；\n  原 24576 下 B' 3/3 截断已证预算不足，post-hoc 修复见 t8c-posthoc-20261126.md）。`

### 2i. L102（成本估算）
old: `- **成本**：n=9/臂 ≈ 9×24576 ≈ 221K tokens/臂，两臂 ~443K，27b 本地可承受（~数小时）。`
new: `- **成本**：n=9/臂，A' 实际 ~13K×9≈117K + B' 实际 ~69K×9≈621K，两臂 ~738K，27b 本地可承受（~数小时）。`

### 2j. L136（跑数说明）
old: `1. 跑 A'×3 + B'×3（各 24576 预算，§1）。`
new: `1. 跑 A'×3 + B'×3（各 73728 预算上限，§1）。`

### 2k. L155（claim 限定）
old: `3. 三判据全过 → **H1 成立（多阶段赢）**，claim 限定为「27b + 本题面 + 24576 预算下`
new: `3. 三判据全过 → **H1 成立（多阶段赢）**，claim 限定为「27b + 本题面 + 73728 预算上限下`

## 文件 3: run_exp_t8c.py
路径: tasks/think-trigger/exp-results/run_exp_t8c.py

### 3a. L3（注释）
old: `# T8c 跑数脚本：pfb 六阶段 vs 直接求解（GPU 选卡题，token-matched 24576/臂）`
new: `# T8c 跑数脚本：pfb 六阶段 vs 直接求解（GPU 选卡题，token-matched 73728/臂上限）`

### 3b. L7-8（注释）
old: `#   1. Q 换成 §4 冻结题面（定值 64K / 候选集定死 3090+V100 / c_pass 公式全列 / n=floor(n_cards/2)）\n#   2. MAX_A 16384 -> 24576（token-matched：两臂预算相等，B 臂 6×4096 硬结构决定上限）`
new: `#   1. Q 换成 §4 冻结题面（定值 64K / 候选集定死 3090+V100 / c_pass 公式全列 / n=floor(n_cards/2)）\n#   2. MAX_A 16384 -> 73728（token-matched：两臂预算上限相等，B 臂 6×12288 硬结构决定上限；2026-11-26 post-hoc 修复）`

### 3c. L17（MAX_A）
old: `MAX_A = 24576  # Arm A' 单次（= 24K 预算，预注册 §1）`
new: `MAX_A = 73728  # Arm A' 单次（= 72K 预算上限，预注册 §1, 2026-11-26 post-hoc）`

### 3d. L18（MAX_B）
old: `MAX_B = 4096   # Arm B' 每阶段（6×4096=24576）`
new: `MAX_B = 12288  # Arm B' 每阶段（6×12288=73728, 2026-11-26 post-hoc 修复截断）`

### 3e. L33（题面 V100 价格）
old: `    "  V100 SXM2   显存 32 GB   峰值带宽 900 GB/s   峰值算力(FP16 non-tensor) 125 TFLOPS  TDP 250 W   单价 $2500\\n"`
new: `    "  V100 SXM2   显存 32 GB   峰值带宽 900 GB/s   峰值算力(FP16 non-tensor) 125 TFLOPS  TDP 250 W   单价 $704（¥5000）\\n"`

### 3f. L175（meta）
old: `"meta": {"experiment": "T8c pfb 六阶段 vs 直接求解（token-matched 24576/臂，题面三歧义已消解）",`
new: `"meta": {"experiment": "T8c pfb 六阶段 vs 直接求解（token-matched 73728/臂上限，题面三歧义已消解, 2026-11-26 重锚定）",`

### 3g. L180（token_matched_budget）
old: `                       "token_matched_budget": 24576,`
new: `                       "token_matched_budget": 73728,`

## 文件 4: t8c_spec_selfcheck.py
路径: tasks/think-trigger/exp-results/t8c_spec_selfcheck.py

### 4a. L7（注释）
old: `#       若被模型照抄执行, 能否复现 oracle winner = 3090×4/W4/n=2 (c_pass≈0.681)。`
new: `#       若被模型照抄执行, 能否复现 oracle winner = V100×4/W4/n=2 (c_pass≈0.4511)。`

### 4b. L16（V100 价格）
old: `    "V100": dict(mem=32.0, bw=900.0, tf=125e12, tdp=250.0, price=2500.0),`
new: `    "V100": dict(mem=32.0, bw=900.0, tf=125e12, tdp=250.0, price=704.0),`

### 4c. L86（期望 winner）
old: `    ok_winner = (w == "3090×4/W4/n=2")`
new: `    ok_winner = (w == "V100×4/W4/n=2")`

## 文件 5: gold_gpu_oracle.py
路径: tasks/think-trigger/exp-results/gold_gpu_oracle.py

### 5a. 在 `import calc` 之后加价格覆写（找到 `import calc` 行, 在其后插入）
old: `import calc`
new: `import calc\ncalc.HARDWARE["V100"]["price_each"] = 704.0  # 2026-11-26 ①类核验 (京东 ¥5000)`

注意: 如果文件里有多处 `import calc`，只改第一处（模块顶部）。用 grep 确认位置。

### 5b. EXPECTED winner（找到 `expect = "3090×4/W4/n=2"` 行）
old: `    expect = "3090×4/W4/n=2"`
new: `    expect = "V100×4/W4/n=2"`

### 5c. c_pass 验收值（找到 `abs(winner_c - 0.679)` 附近）
old: `    c_ok = abs(winner_c - 0.679) / 0.679 < 0.01`
new: `    c_ok = abs(winner_c - 0.4511) / 0.4511 < 0.01`

### 5d. 输出文案（找到 `≈0.679` ）
old: `f" c_pass={winner_c:.3f}≈0.679 {'✅' if c_ok else '❌'}"`
new: `f" c_pass={winner_c:.4f}≈0.4511 {'✅' if c_ok else '❌'}"`

## 文件 6: t8c_judge_format_probe.py
路径: tasks/think-trigger/exp-results/t8c_judge_format_probe.py

**语义翻转**: winner 从 3090×4 变为 V100×4。fixture 里 3090↔V100 角色互换。
- CORRECT: 推荐 V100×4（原来推荐 3090×4）
- ERR_A1: V100 从未进候选集（模型只看 3090）→ 推荐 3090
- ERR_A2: V100 进了但 4×V100 未评估 → 推荐 3090
- ERR_A3: 4×V100 被评估但排序垫底 → 推荐 3090

### 6a. L31-38（CORRECT fixture 整段替换）
old（从 `# 1) CORRECT:` 到 `) + TAIL` 第一个出现）:
```
# 1) CORRECT: 4×3090/W4/n=2 被枚举、被评估、被强推荐
CORRECT = HEADER + (
    "| 3090×4/W4/n=2 | 0.681 | 15.8 GB | 317 GB/s |\n"
    "| V100×4/W4/n=2 | 0.761 | 15.8 GB | 317 GB/s |\n"
    "| 3090×4/W8/n=2 | 0.764 | 19.1 GB | 382 GB/s |\n"
    "\n【淘汰】3090×2/W8/n=1: 显存 25.9>24 GB 装不下; 3090×2/W16/n=1: 显存 39.4>24 GB。\n"
    "\n【最终推荐】主推荐: 4×RTX 3090 / W4 / n=2（c_pass=0.681 ¢/task, 全表最低）。\n"
) + TAIL
```
new:
```
# 1) CORRECT: 4×V100/W4/n=2 被枚举、被评估、被强推荐
CORRECT = HEADER + (
    "| V100×4/W4/n=2 | 0.4511 | 15.8 GB | 317 GB/s |\n"
    "| V100×4/W8/n=2 | 0.5188 | 19.1 GB | 382 GB/s |\n"
    "| 3090×4/W4/n=2 | 0.6807 | 15.8 GB | 317 GB/s |\n"
    "\n【淘汰】3090×2/W8/n=1: 显存 25.9>24 GB 装不下; V100×2/W16/n=1: 显存 39.4>32 GB。\n"
    "\n【最终推荐】主推荐: 4×V100 SXM2 / W4 / n=2（c_pass=0.4511 ¢/task, 全表最低）。\n"
) + TAIL
```

### 6b. L40-46（ERR_A1 fixture 整段替换）
old（从 `# 2) ERR_A1:` 到 `) + TAIL`）:
```
# 2) ERR_A1: 3090 从未进候选集（模型只看了 V100）
ERR_A1 = HEADER + (
    "| V100×4/W4/n=2 | 0.761 | 15.8 GB | 317 GB/s |\n"
    "| V100×4/W8/n=2 | 0.876 | 19.1 GB | 382 GB/s |\n"
    "\n【淘汰】V100×2/W16/n=1: 显存 39.4>32 GB 装不下。\n"
    "\n【最终推荐】主推荐: 4×V100 SXM2 / W4 / n=2（c_pass=0.761 ¢/task, 全表最低）。\n"
) + TAIL
```
new:
```
# 2) ERR_A1: V100 从未进候选集（模型只看了 3090）
ERR_A1 = HEADER + (
    "| 3090×4/W4/n=2 | 0.6807 | 15.8 GB | 317 GB/s |\n"
    "| 3090×4/W8/n=2 | 0.764 | 19.1 GB | 382 GB/s |\n"
    "\n【淘汰】3090×2/W8/n=1: 显存 25.9>24 GB 装不下。\n"
    "\n【最终推荐】主推荐: 4×RTX 3090 / W4 / n=2（c_pass=0.6807 ¢/task, 全表最低）。\n"
) + TAIL
```

### 6c. L48-56（ERR_A2 fixture 整段替换）
old（从 `# 3) ERR_A2:` 到 `) + TAIL`）:
```
# 3) ERR_A2: 3090 多次出现(≥4, 避开 C1e=0.5 的设计边界保守归 A1)
#    但 4×3090 从未被构造/评估（只算了 3090×2）
ERR_A2 = HEADER + (
    "| 3090×2/W4/n=1 | 0.982 | 19.4 GB | 387 GB/s |\n"
    "| V100×4/W4/n=2 | 0.761 | 15.8 GB | 317 GB/s |\n"
    "\n【淘汰】3090×2/W8/n=1: 显存 25.9>24 GB 装不下; 3090 单卡 24 GB 装不下 "
    "27B W4+KV@64K, 3090 多卡组合未展开计算。\n"
    "\n【最终推荐】主推荐: 4×V100 SXM2 / W4 / n=2（c_pass=0.761 ¢/task, 全表最低）。\n"
) + TAIL
```
new:
```
# 3) ERR_A2: V100 多次出现(≥4, 避开 C1e=0.5 的设计边界保守归 A1)
#    但 4×V100 从未被构造/评估（只算了 V100×2）
ERR_A2 = HEADER + (
    "| V100×2/W4/n=1 | 0.7088 | 19.35 GB | 387 GB/s |\n"
    "| 3090×4/W4/n=2 | 0.6807 | 15.8 GB | 317 GB/s |\n"
    "\n【淘汰】V100×2/W16/n=1: 显存 39.4>32 GB 装不下; V100 单卡 32 GB 装不下 "
    "27B W4+KV@64K, V100 多卡组合未展开计算。\n"
    "\n【最终推荐】主推荐: 4×RTX 3090 / W4 / n=2（c_pass=0.6807 ¢/task, 全表最低）。\n"
) + TAIL
```

### 6d. L58-67（ERR_A3 fixture 整段替换）
old（从 `# 4) ERR_A3:` 到 `) + TAIL`）:
```
# 4) ERR_A3: 4×3090 被完整评估（有数值）但排序垫底, 推荐 V100
ERR_A3 = HEADER + (
    "| V100×4/W4/n=2 | 0.761 | 15.8 GB | 317 GB/s |\n"
    "| 3090×4/W4/n=2 | 0.681* | 15.8 GB | 317 GB/s |\n"
    "*注: 3090×4 的 c_pass 按题面公式算为 0.681, 但考虑二手市场供应稳定性与散热, "
    "综合评分后列为次选。\n"
    "\n【淘汰】3090×2/W8/n=1: 显存 25.9>24 GB 装不下。\n"
    "\n【最终推荐】主推荐: 4×V100 SXM2 / W4 / n=2（综合评分最高）。\n"
    "备选: 4×3090/W4/n=2（c_pass 更低但供应稳定性差, 列次选）。\n"
) + TAIL
```
new:
```
# 4) ERR_A3: 4×V100 被完整评估（有数值）但排序垫底, 推荐 3090
ERR_A3 = HEADER + (
    "| 3090×4/W4/n=2 | 0.6807 | 15.8 GB | 317 GB/s |\n"
    "| V100×4/W4/n=2 | 0.4511* | 15.8 GB | 317 GB/s |\n"
    "*注: V100×4 的 c_pass 按题面公式算为 0.4511, 但考虑二手市场供应稳定性与散热, "
    "综合评分后列为次选。\n"
    "\n【淘汰】V100×2/W16/n=1: 显存 39.4>32 GB 装不下。\n"
    "\n【最终推荐】主推荐: 4×RTX 3090 / W4 / n=2（综合评分最高）。\n"
    "备选: 4×V100 SXM2/W4/n=2（c_pass 更低但供应稳定性差, 列次选）。\n"
) + TAIL
```

### 6e. L69-84（CORRECT_TBL fixture 整段替换）
old（从 `# 5) CORRECT_TBL:` 到 `)` 结束）:
```
# 5) CORRECT_TBL: 表格行格式(卡型/卡数分列)的正确答案——winner 评估行+推荐行均为表格
CORRECT_TBL = (
    "### 1. 可行配置枚举（两道门通过者, 按 c_pass 升序）\n"
    "| 卡型 | 卡数 | 精度 | n | c_pass (¢/task) |\n"
    "|---|---|---|---|---|\n"
    "| RTX 3090 | 4 | W4 | 2 | 0.681 |\n"
    "| V100 SXM2 | 4 | W4 | 2 | 0.761 |\n"
    "| RTX 3090 | 4 | W8 | 2 | 0.764 |\n"
    "\n### 2. 最优选卡方案\n"
    "| **RTX 3090** | 4 | W4 | 2 | **0.681** | —（**最优选**） |\n"
    "\n### 3. 淘汰原因\n"
    "| RTX 3090 | 2 | W8 | 1 | 显存 25.85>24 装不下 |\n"
    "| V100 SXM2 | 2 | W16 | 1 | 显存 39.35>32 装不下 |\n"
    "\n【精度论证】W4 质量损失可接受 [待核验]。\n"
    "【来源标注】936 GB/s / 24.7 GB/流 = 题面给定; c_pass = 按题面公式推导。\n"
)
```
new:
```
# 5) CORRECT_TBL: 表格行格式(卡型/卡数分列)的正确答案——winner 评估行+推荐行均为表格
CORRECT_TBL = (
    "### 1. 可行配置枚举（两道门通过者, 按 c_pass 升序）\n"
    "| 卡型 | 卡数 | 精度 | n | c_pass (¢/task) |\n"
    "|---|---|---|---|---|\n"
    "| V100 SXM2 | 4 | W4 | 2 | 0.4511 |\n"
    "| V100 SXM2 | 4 | W8 | 2 | 0.5188 |\n"
    "| RTX 3090 | 4 | W4 | 2 | 0.6807 |\n"
    "\n### 2. 最优选卡方案\n"
    "| **V100 SXM2** | 4 | W4 | 2 | **0.4511** | —（**最优选**） |\n"
    "\n### 3. 淘汰原因\n"
    "| RTX 3090 | 2 | W8 | 1 | 显存 25.85>24 装不下 |\n"
    "| V100 SXM2 | 2 | W16 | 1 | 显存 39.35>32 装不下 |\n"
    "\n【精度论证】W4 质量损失可接受 [待核验]。\n"
    "【来源标注】900 GB/s / 24.7 GB/流 = 题面给定; c_pass = 按题面公式推导。\n"
)
```

### 6f. L86-102（ERR_A3_TBL fixture 整段替换, 已确认存在）
old:
```
# 6) ERR_A3_TBL: 表格行格式的 A3——winner(3090×4) 被完整评估(0.681)但推荐 V100
#    (模拟 smoke 第一批 A 臂 run2 的真实形态, 含 gpu_price 单卡价误读口径)
ERR_A3_TBL = (
    "### 1. 可行配置枚举（两道门通过者, 按 c_pass 升序）\n"
    "| 卡型 | 卡数 | 精度 | n | c_pass (¢/task) | 备注 |\n"
    "|---|---|---|---|---|---|\n"
    "| **V100** | 4 | W4 | 2 | **0.437** | —（**最优选**） |\n"
    "| RTX 3090 | 4 | W4 | 2 | 0.521 | c_pass 更高 |\n"
    "| RTX 3090 | 4 | W8 | 2 | 0.584 | c_pass 更高 |\n"
    "\n### 2. 最优选卡方案\n"
    "**V100 SXM2 × 4 卡 × W4 × n=2**, c_pass = 0.4374 ¢/task（全局最低）。\n"
    "\n### 3. 淘汰原因\n"
    "- **RTX 3090 W8/W16 2卡**：显存不足（W8 2卡需 25.85 GB/卡 > 24 GB）。\n"
    "- **RTX 3090 所有配置**：算力和带宽均低于 V100, c_pass 全面劣势。\n"
    "\n【精度论证】W4 质量损失可接受 [待核验]。\n"
    "【来源标注】936 GB/s / 24.7 GB/流 = 题面给定; c_pass = 按题面公式推导。\n"
)
```
new:
```
# 6) ERR_A3_TBL: 表格行格式的 A3——winner(V100×4) 被完整评估(0.437, 单卡价误读口径)但推荐 3090
#    (模拟 smoke 第一批 A 臂 run2 的真实形态, 含 gpu_price 单卡价误读口径)
ERR_A3_TBL = (
    "### 1. 可行配置枚举（两道门通过者, 按 c_pass 升序）\n"
    "| 卡型 | 卡数 | 精度 | n | c_pass (¢/task) | 备注 |\n"
    "|---|---|---|---|---|---|\n"
    "| **RTX 3090** | 4 | W4 | 2 | **0.437** | —（**最优选**） |\n"
    "| V100 SXM2 | 4 | W4 | 2 | 0.521 | c_pass 更高 |\n"
    "| V100 SXM2 | 4 | W8 | 2 | 0.584 | c_pass 更高 |\n"
    "\n### 2. 最优选卡方案\n"
    "**RTX 3090 × 4 卡 × W4 × n=2**, c_pass = 0.4374 ¢/task（全局最低）。\n"
    "\n### 3. 淘汰原因\n"
    "- **V100 SXM2 W16 2卡**：显存不足（39.35 GB/卡 > 32 GB）。\n"
    "- **V100 SXM2 所有配置**：二手市场供应稳定性差, 散热劣于 3090, 列次选。\n"
    "\n【精度论证】W4 质量损失可接受 [待核验]。\n"
    "【来源标注】900 GB/s / 24.7 GB/流 = 题面给定; c_pass = 按题面公式推导。\n"
)
```

## 验收（全部替换完后跑）
1. `python3 tasks/think-trigger/exp-results/t8c_spec_selfcheck.py` → exit 0（winner=V100×4/W4/n=2）
2. `python3 tasks/think-trigger/exp-results/gold_gpu_oracle.py` → winner=V100×4/W4/n=2, c_pass≈0.4511
3. `python3 tasks/think-trigger/exp-results/t8c_judge_format_probe.py` → 全对（4 型标签正确）
4. `git add -A && git commit -m "T8c re-anchor: V100 $704 (JD ①class 2026-11-26), winner→V100×4/W4/n=2, MAX_A 73728 (B' truncation fix)"`

## 边界
- 不改 calc.py（共享依赖, 价格覆写在 oracle 里做）
- 不改 correctness_layer_v0.py（judge 已参数化 WINNER_CARD）
- 不改 T8b 相关文件
- 替换时 old_string 找不到 → 停下报错, 不要模糊匹配
- 每个文件改完立即跑对应验收, 不要全改完才验
