# T50 B1 新题 Gold Tree（Q8/Q9/Q10）— 阶段 04 执行与结果核对

> 创建：2026-11-07 · 阶段：04 · 依据：`loop-artifacts/stages/03/T50-03-actions.md` A1-A10 + `loop/prompt-first/04-execution-verification.md`
> 分支：`arena/5c63a992-prompt-first-bench`（基线 main @ 89eaee8）

---

## 1. 逐项执行记录（对照阶段 03 验收方式）

| # | 步骤 | 实际执行 | 验收结果 |
|---|------|---------|---------|
| A1 | Q8 题面 | 写入 `bench/questions/Q8-eval-benchmark.txt`（3,233B）；头注释 12 字段对齐 Q6/Q7；preamble 逐字复用；「问题：」行含任务书 Q8 题面方向全部要素（维度/pass@k/测试充分性/泄漏/过拟合/五个参照 benchmark） | ✅ 非空；extract_question() 提取 401 字符核心问题段 |
| A2 | Q9 题面 | 写入 `bench/questions/Q9-vlm-arch.txt`（3,350B）；四对象按任务书冻结（CLIP/SAM/GPT-4V/Gemini），LLaVA/Flamingo 仅作参照架构（阶段 01 登记扩展） | ✅ extract_question() 提取 435 字符 |
| A3 | Q10 题面 | 写入 `bench/questions/Q10-rlhf-align.txt`（3,231B）；题面显式要求"注明是谁、哪个任务的值，不要混用不同实现库的默认值"（C1 裁定前置到题面） | ✅ extract_question() 提取 418 字符 |
| A4 | gold-Q8.md | 写入（15,734B）：结论先行/全树/图例/★×2/黑盒表 B1-B4/OC-1 卡片×3/算例×3/来源表 S1-S11（含 S3'/S5' 二源）/找不到×3 | ✅ grep：36 节点（≥30）、28 leaf（≥10）、最深 N-2.3.1/N-3.2.2 = 深度 4、顶部独立调研声明在位 |
| A5 | gold-Q9.md | 写入（17,281B）：同结构；GPT-4V tiling 叶子 conf 0.8 封顶（三社区源一致）；Gemini 1.0 只采谱系主张不引数值（S11 conf 0.7） | ✅ 34 节点、27 leaf、深度 4（N-1.4.1/N-1.6.2）、声明在位 |
| A6 | gold-Q10.md | 写入（18,697B）：同结构；**C1/C2 裁定落实**——β_KL=0.02（N-2.1，任务书 0.2 标注为 clip ε/TRL 惯例混淆）、对齐税为条件化区间表（N-3.3/N-3.4 分域散点）、任务书 -5~15pp 标 [待核验]（N-3.5 = leaf B1） | ✅ 36 节点、29 leaf、深度 4（N-3.3.1/N-4.3.1）、声明在位；grep 全文无以 "β=0.2" 为 KL 系数的表述（仅出现在"混淆警示"与消融档位扫描语境） |
| A7 | QUESTIONS 注册 | `ablation_harness.py` +20 行：Q8/Q9/Q10 条目（domain/prompt_file/gold_file/search_query，PFB 常量，Q6/Q7 同款注释块） | ✅ ast.parse 通过；keys = [Q1..Q10]；4 字段齐；prompt_file/gold_file 路径实测存在 |
| A8 | research_hook 注册 | ARXIV_QUERIES +3（每题 1 条精准 query，任务书最小集）；**G6 决策落地**：同步补 KNOWN_SITES +3×4（一手 arXiv 论文源，与 gold 来源表对齐）与 FILTER_KEYWORDS +3（保证 S2+ 臂来源过滤行为与 Q6/Q7 一致）——超出任务书最小集的部分已在 04.5 §披露 | ✅ ast.parse 通过；三 dict 均含 Q8/Q9/Q10 key |
| A9 | 验收自查 | 单脚本跑任务书全部机器可查项（输出见下 §2）；另跑 extract_question() 一致性对比（Q6/Q7/Q8 同正则同行为） | ✅ 全过；发现并修复 1 个真缺陷（头注释「问题：」误匹配正则，改回 Q6 的「核心问题」措辞后复测 OK） |
| A10 | commit+push | 见 §3 | 本文件写完后执行 |

## 2. A9 自查脚本输出（关键行）

```
[PASS] ast.parse ablation_harness.py / research_hook.py
[PASS] QUESTIONS contains Q8/Q9/Q10; all keys: [Q1..Q10]
[PASS] Q8/Q9/Q10 entries have 4 standard fields
[PASS] ARXIV_QUERIES / KNOWN_SITES / FILTER_KEYWORDS contains Q8/Q9/Q10
[PASS] gold-Q8: 36 nodes (>=30), 28 leaves (>=10), depth 4 (<=4), independence declaration present
[PASS] gold-Q9: 34 nodes, 27 leaves, depth 4, declaration present
[PASS] gold-Q10: 36 nodes, 29 leaves, depth 4, declaration present
extract_question(): Q8→401 chars / Q9→435 / Q10→418（与 Q6→192 / Q7→213 同行为，均以题面正文起）
```

## 3. 修复记录（诚实记录）

1. **头注释正则误匹配（A1-A3 首版缺陷）**：新题面头注释写了「问题：」字样，被 `extract_question()` 的 `问题[：:]` 正则先于正文命中，提取出注释文本。对照 Q6 发现其头注释用「核心问题」措辞规避了该问题 → 三个文件同式修复，复测提取正确。根因：写头注释时未先跑正则实测；教训已可供后续建题参考（头注释禁用「问题：」裸串）。
2. **头计数自报偏差**：题面头注释与 gold 头部的节点/叶子自报数在写完后与 grep 实测有 ±1~4 偏差（Q8 叶子 24→28、Q9 24→27、Q10 35/25→36/29）→ 已按实测值统一修正（sed），双侧一致。

## 4. 约束遵守核对

- `git status --porcelain`：改动仅限 `ablation_harness.py`（+20）与 `research_hook.py`（+26）两文件；新增仅 6 个指定路径文件 + 6 个 loop-artifacts。**未触碰** Q1-Q5 文件、score.py、score_s10.py、gates.py、gold-tree.md。
- 未创建新目录（loop-artifacts/stages/<N>/ 均为既有目录）。
- 无编造数值：全部叶子带 URL+观察日 2026-11-07；[待核验] 共 2 处（gold-Q8 N-3.5 canary、gold-Q10 N-3.5 MMLU -5~15pp）均按任务书红线处理。

**阶段判定：pass**（A1-A9 全部有实际产出与验收证据；两处缺陷如实记录并修复；A10 待本文件落盘后执行）
**repair_stage：none**
