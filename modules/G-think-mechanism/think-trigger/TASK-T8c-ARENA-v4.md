# 任务卡 T8c-ARENA-v4：S0 重锚（winner 3090→V100，arena 执行）

# origin: ai · 2026-11-26 · 换路：27b sub 连死 3 次（v1 环境探测 / v2 验证烧输出 / v3 读文件烧输出），
#   根因 = 多文件读 + CFG4 正则族重写（8 变体）+ 6 probe fixture 角色互换 > 27b 输出上限。
#   升级 arena（更强模型 + 更大输出预算 + 仓库绑定 + 执行层）。本卡自包含，arena 读它 + 仓库内 v3 卡。
# 上游: TASK-T8c-FORMAL-RERUN-v3.md（机械步骤 + 已验证数字，本卡继承其数字，扩展正则重写范围）

## 目标（一句话）
把 T8c 实验从「winner = 3090×4/W4/n=2」重锚到「winner = V100×4/W4/n=2」，因为 V100 单价 ③→① 升级
（$2500 题面假设 → $975 实测，gpudojo 2026-10-28），winner 翻转。4 个文件联动改，改完 selftest+probe 全绿。

## 已验证数字（v2 ①类实算，直接用，spot-check 即可不必全重算）
- V100×4/W4/n=2 @ $975 → c_pass **0.4979**（新 winner）
- 3090×4/W4/n=2 @ $1050 → c_pass **0.6807**
- V100×4/W4/n=2 @ $2500（旧题面）→ c_pass **0.7614**
- 盈亏平衡价 ≈ **$2033**（V100 单价 < $2033 时反超 3090 成 winner；$975 远低于此 → 翻转成立）
- 建议：用 calc.py（`bench/rubric-v3/tasks/T0-local-27b/reference/calc.py`）spot-check 翻转点，确认 0.4979 < 0.6807。

## 改动点（4 文件，winner 锚 3090→V100 贯穿）
**1. `modules/G-think-mechanism/think-trigger/exp-results/t8c-spec-final.md`**
- L65 硬件表：V100 单价 $2500 → $975（来源改 gpudojo 2026-10-28 ①类，删「③类假设钉死」措辞）
- L67-71 脆弱性披露：整段重写——现在 V100 更便宜且更快，V100×4/W4/n=2 稳赢；3090 一侧对价格不敏感
- L147 题面正文：V100 单价 $2500 → $975
- L201-205 checklist：「V100 价格假设复核：仍按 $2500」→「已 ①类核验 $975，winner 锚 = V100×4/W4/n=2」
- §2 winner 锚点：3090×4/W4/n=2 → V100×4/W4/n=2（c_pass 0.4979）
- 重冻：对新题面算 sha256，写「冻结版 v2 @ <hash>」

**2. `modules/B-pipeline-ablation/research/correctness_layer_v0.py`**（最难，正则族）
- CFG4 正则族（L29-37，8 变体）：winner 配置从 4×3090 → 4×V100，全部 8 个变体的 3090 → V100（含 `(?:RTX\s*)?3090` → `V100\s*SXM2?` 等格式变体）
- C1e mask（L126）：`re.compile(r"3090")` → V100
- E2 规格行（L138/150）：3090 规格行 → V100 规格行
- selftest fixtures（L336-375）：3090 → V100（V1/V3/V5/V8 等因果探针）
- calc.HARDWARE 引用（L397/406）：`calc.HARDWARE["3090"]` → `["V100"]`，`calc.c_pass("3090",...)` → `("V100",...)`
- **跑 selftest 确认无回归**（11/11 或等价）

**3. `modules/G-think-mechanism/think-trigger/exp-results/t8c_judge_format_probe.py`**
- 6 个 fixture（CORRECT/ERR_A1/ERR_A2/ERR_A3/CORRECT_TBL/ERR_A3_TBL）：winner 角色从 3090 换到 V100
  - CORRECT：V100×4/W4/n=2 被枚举+评估+强推荐 → indeterminate
  - ERR_A1：V100 从未进候选集（只看了 3090）→ A1
  - ERR_A2：V100 多次出现但 4×V100 从未构造/评估 → A2
  - ERR_A3：4×V100 被完整评估但排序垫底，推荐 3090 → A3
  - CORRECT_TBL / ERR_A3_TBL：表格行格式同上角色互换
- **跑 probe 确认 6/6 全对**

**4. `modules/G-think-mechanism/think-trigger/exp-results/run_exp_t8c.py`**
- L33 Q 字符串：V100 单价 $2500 → $975
- MAX_A/MAX_B 保持不变（token-matched 不变量，两臂预算相等 24576）

## 硬约束
- 全程离线，零 LLM 调用（selftest/probe 是纯 python 正则匹配，不调 8787）；不碰 vLLM 推理
- 每个文件改完立即 commit（增量，防丢工作），message 前缀 `T8c-v4:`
- 改完必须跑：`python3 correctness_layer_v0.py`（selftest）+ `python3 t8c_judge_format_probe.py`（6/6），全绿才算 done
- 不留 3090-as-winner 残留：grep 4 文件，winner 锚点相关处全 V100（3090 作为候选集成员可保留，但不能再是 winner）

## 验收（Lead 对照核）
- [ ] selftest 全绿（无回归）
- [ ] probe 6/6 全对
- [ ] spec 内部一致（价格/锚点/checklist 全 V100）+ 新冻结 hash
- [ ] 4 文件 commit 链 ≥4
- [ ] grep 无 3090-as-winner 残留
