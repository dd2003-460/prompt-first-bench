# idea53 · 加性树解析稿发布包（2026-11-25）

## 这个包是什么

以「加性树 + 微扰 + 级数信息增益」为数学核心的新稿及其全部支撑材料。它**替换**旧的「测量协议」叙事（`../submission/`，v4 时间戳锁包）——旧稿把树当列联表附属观察，只做两层枚举；本稿把可分解加性树放到中心，把「深层主导」升级为可推导、可证伪的解析命题。

定位始终是**前置工作**：树 / GPU 公式 / 四平台都是玩具模型；不解决对齐问题，不声称首次，不主张 ID3 / roofline / PID 是新的。

## 与旧 `submission/` 的关系

- `../submission/` 是 **11-24 的预注册时间戳锁**（v4，8 文件 SHA256SUMS，commit e8754392a）。它锁定的是**旧稿**，其 hash 在该 commit 内自洽、未被改动，作为历史优先级证据原样保留。
- 本包是 **11-25 的新稿**，与旧稿数字口径不同，**不可混算**：
  - 旧稿 flip = 43–56%（速率全 1 → 真实速率的「大跳跃」修正量）
  - 新稿 flip = 4–5%（真实速率 +15% 小扰动的局部稳定性）
  - 新稿额外给出闭式 $P(\mathrm{flip})$ 与 $I_2$，以及有效域 $\alpha\beta\sigma\le0.4$
- 两版都有效的判据在旧稿积压档；本包只承载解析版。

## 目录

```
manuscript/   paper-zh-additive-tree.{tex,md,pdf}  中文稿（7 页，xelatex 编译）
              fig1-scoring-protocol.tex            结构图 TikZ 源
recompute/    idea53-additive-tree-perturbation.{py,json}
                                                   全部数字的复算脚本与结果
reviews/      arena 两轮报告+回执、轻量 review SOP（对抗审查记录）
decisions/    投稿策略三份决策文档（费用/复用/周期/零成本路径）
SHA256SUMS.txt  本包全部交付文件的内容哈希（完整性锁，非预注册）
```

## 复现

```bash
cd manuscript && xelatex paper-zh-additive-tree.tex && xelatex paper-zh-additive-tree.tex
cd ../recompute && python3 idea53-additive-tree-perturbation.py   # 无 LLM、无实测
sha256sum -c SHA256SUMS.txt                                       # 完整性校验
```

## 边界（写进稿里的硬结论）

1. 对角弹性只在**加性**公式成立；分母含求和的非加性形式破坏闭式——可证伪点。
2. 硬 argmax 不可微，级数失效；须软化，且 $\alpha\beta\sigma\lesssim0.4$ 才保留 85–92% 信息量。
3. 「深层在哪层主导」按翻转率 / 信息量 / 修正量三口径结论不同，任何单口径断言都必须先声明口径。
4. 换指数 $\alpha:1\to2$ 不改变主导层面（负面结果）——是结构而非参数决定记账方式。

## 状态

中文稿定稿；英文版待中文确认后再写。`reviews/` 与 `decisions/` 是工作文档，不进正式投稿。
