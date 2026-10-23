# T4 ablation-L1 验证报告 — 21 runs +21 评分 + 11 变体×3 runs 完整性验证

> 日期：2026-10-23 Asia/Shanghai
> 执行分支：arena/2d866a16-prompt-first-bench（Arena 固定分支；用户要求 arena/t4-remaining-<timestamp> 因系统禁止跨分支未新建）
> 目标仓库：dd2003-460/decomp-bench（私有不可达，404/403 已验证，见下）
> 执行通道：local degraded（vllm/qwen3.8-27b-w8a16，conf 0.2，按 sop/arena-loop-pipeline.md §3.3）

## 1. 验收标准对照

| 验收项 | 要求 | 实际 | 状态 |
|--------|------|------|------|
| 21 runs +21 评分落盘 | 补跑 7 变体×3 run =21 runs+21评分 | `bench/runs/ablation-L1/{C3-exposneg,C4-arch,C5-small-exposneg,C6-nocontract,C7-noscratch,C8-noscratch-hard,C9-open}/` 各 3 runs+3评分 =21+21 ✅ | ✅ |
| 11 变体×3 runs 完整 | summary-all.md 补全 11 变体对比表 | 11 变体（C0,C1,C1-small,C2-expos + 7补跑）各 3 runs =33 runs+33评分，summary-all.md 已更新 ✅ | ✅ |
| 显著性判定 | Δ >2σ_pooled 标注 | §2 表已标注 ✅/ns（vs C0 10 对比 + 相邻边际 11 对比） | ✅ |
| 5 步每步 commit | 每步完成后 commit | commits ebc7894,f5573e8,845ab99,f469d26,a1a3534,35ba21d （6 commits, 含 Step3b 修正） | ✅ |
| 输出落盘 | bench/runs/ablation-L1/{variant}/ | 78 文件（33 runs+33评分+11 summary+1总汇总）+ 11 prompt.txt | ✅ |
| 汇总更新 | bench/runs/ablation-L1/summary-all.md | 已补全，含 4 表（原始分/显著性/边际/方差）+ 6 条结论 | ✅ |
| 验证 | 文件完整性确认 | 见 §2 | ✅ |

## 2. 文件完整性（`find` 实测 2026-10-23 04:02）

```bash
$ find bench/runs/ablation-L1 -type f | wc -l
78  # 33 runs +33评分 +11 summary +1 summary-all +1 VERIFY=79? 实际 78 不含本 VERIFY, 含本文件 79
$ find bench/prompts/variants -name prompt.txt | wc -l
11
$ find bench/runs/ablation-L1 -name "run[123].md" | wc -l
33
$ find bench/runs/ablation-L1 -name "run*-score.md" | wc -l
33
```

补跑 7 变体单查：
- C3-exposneg: 3 runs +3评分 ✅
- C4-arch: 3+3 ✅
- C5-small-exposneg: 3+3 ✅
- C6-nocontract: 3+3 ✅
- C7-noscratch: 3+3 ✅
- C8-noscratch-hard: 3+3 ✅
- C9-open: 3+3 ✅
→ 合计 21+21 ✅

## 3. 11 变体×3 runs 汇总（Mean±σ）

| 变体 | Mean | σ_pop | 判定 | success |
|------|------|-------|------|---------|
| C0 | 15.33±0.47 | 0.47 | success | 3/3 |
| C1 | 14.67±0.47 | 0.47 | partial | 2/3 |
| C1-small | 14.33±0.94 | 0.94 | partial | 2/3 |
| C2-expos | 14.67±0.47 | 0.47 | partial | 2/3 |
| C3-exposneg | 13.67±0.47 | 0.47 | partial | 0/3 |
| C4-arch | 15.00±0.00 | 0.00 | success | 3/3 |
| C5-small-exposneg | 13.00±0.82 | 0.82 | partial | 0/3 |
| C6-nocontract | 13.00±0.82 | 0.82 | partial | 0/3 |
| C7-noscratch | 14.00±0.82 | 0.82 | partial | 1/3 |
| C8-noscratch-hard | 12.33±0.94 | 0.94 | partial | 0/3 |
| C9-open | 9.67±1.25 (samp1.53) | 1.25 | fail | 0/3 |

## 4. 显著性（vs C0，Δ>2σ_pooled）

- ✅ 显著：C3(1.66>0.94), C5(2.33>1.34), C6(2.33>1.34), C8(3.00>1.49), C9-open(5.66>1.89)
- ns 不显著：C1(0.66<0.94), C1-small(1.00<1.49), C2-expos(0.66<0.94), C4-arch(0.33<0.66), C7-noscratch(1.33<1.34 边界)

关键边际：
- 负向草稿 C2→C3 Δ1.00 ✅ 显著有害
- 去契约 C0→C6 Δ2.33 ✅ 显著
- 硬约束 C0→C8 Δ3.00 ✅ 显著
- 结构化整体 C0→C9-open Δ5.66 ✅ 显著最大
- 架构图 C0→C4 Δ0.33 ns（但 σ 0.47→0.00 提稳）

## 5. 仓库/分支/通道说明

- 目标仓库 dd2003-460/decomp-bench：`curl https://github.com/dd2003-460/decomp-bench` → 404；`git ls-remote` → 403 Write access not granted。确认私有不可达。
- 分支要求 arena/t4-remaining-<timestamp>：因 Arena 会话固定分支 `arena/2d866a16-prompt-first-bench`，系统禁止新建/切换分支，已在 commit 信息与 summary-all.md §0 留痕，未新建分支。
- 通道降级：按 sop/arena-loop-pipeline.md §3.3，arena 封禁/私有仓库不可达时降级 local degraded，conf 0.2，实际模型 vllm/qwen3.8-27b-w8a16，已在所有 run 文件头标注。

## 6. 执行步骤回溯（每步 commit）

| 步骤 | 描述 | commit | 文件 |
|------|------|--------|------|
| 1 | 读取 11 变体 prompt.txt | ebc7894 | bench/rubric.md + 11 prompt.txt |
| 2 | 生成 33 runs（21 新+12 历史） | f5573e8,845ab99 | bench/runs/ablation-L1/*/run*.md |
| 3 | 18 点 rubric 评分 33 文件 | f469d26 | bench/runs/ablation-L1/*/run*-score.md |
| 4 | Mean+σ 到各变体 summary.md | a1a3534 | bench/runs/ablation-L1/*/summary.md |
| 5 | 更新 summary-all.md 11 变体对比+显著性 | 35ba21d | bench/runs/ablation-L1/summary-all.md |
| 6 | 验证（本文件） | (本 commit) | bench/runs/ablation-L1/VERIFY.md |

## 7. 推送状态

- 分支：arena/2d866a16-prompt-first-bench
- 待推送 commits：6-7 个
- 远程：origin https://github.com/dd2003-460/prompt-first-bench.git
- 下一步：`git push origin arena/2d866a16-prompt-first-bench`

## 8. 复现命令

```bash
ls bench/prompts/variants/*/prompt.txt
ls bench/runs/ablation-L1/*/run*.md
cat bench/runs/ablation-L1/summary-all.md
cat bench/rubric.md
find bench/runs/ablation-L1 -type f | wc -l
```

---
