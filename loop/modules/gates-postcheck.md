# 模块 gates-postcheck — 三道闸（04 / 04.5 阶段通用 post-check）

> origin: ai · 2026-11-03 · T23 结构并入（任务书：projects/decomp/tasks/T23-merge-pfb-ablation.md；设计源：projects/decomp/tasks/T22-gate-experiment.md，decomp-bench commit 0a8dfc4）
> 定位：**输出后校验**（post-check），不依赖模型有搜索能力。闸管格式合规与事实纪律，不管信息获取（信息获取归 02 阶段 + ego-browser 通道）。
> 状态：SOP 定义已落盘；机器实现（gates.py）**已回填**——2026-11-03 T22 subagent 交付 `decomp-bench: experiments/autoresearch-r2/gates.py`（main commit 8d933b2），拷入本仓 `experiments/stage-ablation/gates.py`，4 个单元测试通过。注意：T22 的 r2 实验本身因 endpoint 当时不可达为 0/12 runs（降级回执见 decomp-bench `experiments/autoresearch-r2/scoring.md`），endpoint 现已恢复，补跑结果出来前 gates.py 只算「可用原型」不算「已验证有效」。

## 挂载点

| 阶段 | 挂哪道闸 | 时机 |
|------|---------|------|
| 04-execution-verification | 闸 1 + 闸 2 | 每条执行记录写入前过闸；不过闸的断言标 `unverified`/`conflict` 冻结，禁止进入结论区 |
| 04.5-final-review | 闸 1 + 闸 2 + 闸 3 | 终审轮末自检，替代语气式防御（「可能/大概」免责话术） |

## 闸 1：数字必溯源

- 正则抽取所有数字型断言（XXX TFLOPS / GB/s / TB / 元 / % / ms / 倍 等，含中文单位与千分位格式）。
- 凡无来源锚点（URL / datasheet 引用 / 核验日期）的一律标 `unverified`，**禁止进入结论区**。
- 指标：**无来源数字率** = 无来源锚点的数字断言数 / 全部数字断言数。
- r1 基线参照：27b 裸奔时具体规格全靠脑补（TFLOPS 编成 395/340），此率应显著高于 0；闸有效判据见 T22 验收标准（R2-B < R2-A 的 50%）。

## 闸 2：矛盾必对质

- 新断言与已有断言库交叉比对；冲突则两条都冻结标 `conflict`，需独立证据仲裁后才能解冻。
- 指标：**矛盾对数** = 同一事实的不同版本共存数。r1 基线 ≥1 对（HBM 带宽「相同 vs 不同」两版共存）；闸生效后应为 0，非 0 则记录矛盾内容分析原因。

## 闸 3：实事求是 checklist（轮末自检）

1. **fact/inference 分离**：每条输出区分 fact（带来源）/ inference（标 conf）；指标 = 标注覆盖率。
2. **限定必须带边界**：「在 X 条件下成立，Y 未验证」，禁止裸「可能/大概」；指标 = 裸语气词率（无边界限定的限定词数 / 全部限定词数）。
3. **坏消息同等显眼**：限制陈述放开头不放结尾免责声明位；指标 = 限制陈述出现在输出前 1/3 的比例。

## 机器接口（待 T22 回填）

预期产物（T22 交付物清单，路径相对 decomp 仓 `experiments/autoresearch-r2/`）：

- `gates.py` — 三道闸实现：数字抽取正则 / 矛盾比对 / checklist 校验
- `run_r2.py` — r1 框架扩展（变体注入 + 闸 post-check 模块）

回填动作：T22 scoring.md 落盘后，把 `gates.py` 拷入 pfb `experiments/stage-ablation/gates.py`（或按 T22 实际路径登记于此），并在此节写死调用方式。S5 臂配置是否保留三道闸，**以 T22 结果为准**（若闸无效 → S5 降级为 04+04.5 无闸版，DESIGN.md 显式依赖节同步改）。

## 归属声明

三道闸对标的是 **pfb 完整流程**（带 02/02.5/04/04.5 的系统），不是 decomp 单模块。decomp（decomp-01 模块）只做分解+标注缺口+留空，不产生需要溯源的事实断言——闸 1/2 主要咬合的是 02 调研产出的下游使用环节。