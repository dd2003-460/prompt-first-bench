# idea53 归类入口

> 2026-11-25 建立。本目录只放**指针（软链接）**，实体仍在原位。
> 为什么不搬实体：脚本、arena 任务书、预注册 commit 里都写死了原路径，搬动会打断在跑的任务和可复现锚点。

## 一句话状态

闭式数学论文到「可打磨态」：9 页 PDF、预注册合规（eb1b0598c 17:39 早于数据 718394ece 18:06）、数字审计过、arena 六轮撞车核查 conf 0.7（窄空白，未直接撞车）。**未投**。

## 文件地图

| 指针 | 指向 | 内容 |
|---|---|---|
| `submission/` | `tasks/idea53-goal/submission/` | **投稿包**：paper.tex / paper.pdf（9pp）/ body / header / formalism-skeleton / SHA256SUMS / hds 复算脚本 |
| `paper.md` | `tasks/idea53-goal/paper.md` | 早期 markdown 全文 25KB（投稿版是 tex，这个不是） |
| `audit-final-20261125.md` | 同名 | 11-25 05:42 审计：H(D|S) 口径争议闭合、三待决闭环、复现实跑 |
| `collision-final-paper-firstpass-20261125.md` | 同名 | arena round6 之后的初判：未撞车 conf 0.7 + venue 排序 |
| arena 六轮回执 | 不在工作树，只在 git 分支 `origin/arena/f8477718-prompt-first-bench` | 读法：`git show origin/arena/f8477718-prompt-first-bench:tasks/IDEA-review/result.md`。追加 1–5 节，含最难一击和守法三条件；工作树里的 `tasks/IDEA-review/` 只有 TASK.md |
| `GOAL.md` | `tasks/idea53-goal/GOAL.md` | 目标、验收 5/6 勾（第 6 条实际已做未勾）、venue 概率 |
| `IDEA-INDEX.md` | `modules/IDEA-INDEX.md` | #53 行 = 全部结论演化史（四轮撞车、三源实测、一次证伪） |
| `research-scripts/` | `modules/F-theory/research/` | 27 个 `idea53-*` 脚本与结果 JSON |

## 投稿前真正的缺口（按优先级）

1. **公开 profile 数据 spot-check 未做** —— arena round6 自己列的守法条件 b，用来堵「闭式测量无任何实验验证」这一击。
2. **FP4 proxy 未验证** —— 4090/A100 无原生 FP4，用 0.5×FP16 代理；4090 的 ratio 287.4 有一部分是这个代理造出来的，flip/shift 最高值因此带着 caveat。
3. `submission-staging/merge_references.py` 未跑 —— 补 0 引用到 15 条，幂等脚本，等「投」再执行。
4. `idea53-preprint-ts-v4` 分支未推远程 —— 对外动作，随投稿一起做；v3 已推但过期。
