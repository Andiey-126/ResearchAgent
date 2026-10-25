# 05 Research Agent · 学习日志

> **2026-10-24 起换学法：不再走 structured-coding-tutor 的结构化流程。** 用户原话："不想再一直结构化归顺性学习了"。本文件里凡是和知识点流程有关的内容（开场、间隔复习、预测、批改、测验、迁移任务、支持级别、卡住升级和查证提示的计数、教学自查），都只作历史记录，不再执行。新学法见「用户的固定要求」里的「2026-10-24 起的学法」。
>
> **新对话从这里开始**（上下文太长就换新对话，不再按知识点分）：
> 1. 读「当前状态」和「用户的固定要求」，**不用**加载 `structured-coding-tutor` skill
> 2. 用设备工具读项目里的真实代码（`main.py`、`agents.py`、`system_prompt.py`），不要只信文档
> 3. 问用户这次想弄懂什么、想做哪一块，从那里开始
>
> **给接手对话的操作提醒**（仍然有效）：
> - 往用户电脑写文件：每次先在容器里生成一个**新文件名**的最终版本，再提交到用户电脑。同一个中转文件改了再提交，可能被当成旧内容写进去（2026-10-01 发生过两次）。写完一定要读回比对，比对通过才算写好
> - 需要用户做的事放在回复**最前面**单独一块
> - 讲解只用三个固定名字：Python 程序、Claude Code 程序、模型

---

## 当前状态

| 项 | 内容 |
|---|---|
| 更新日期 | 2026-10-24 |
| 当前阶段 | **阶段 2 · 知识点 5 🟨 暂停中（2026-10-24 18:28 用户要求暂停）**。知识点 5 已完成：开场、原理第 1–7 步（收尾复述过关，Q27–Q29）、两个查证任务（`AgentDefinition` 字段；`system_prompt` 不填 = 传空字符串，都由用户查到）、设计选择（主 agent 系统 prompt 自己写字符串，放 `system_prompt.py`）、第 0 次运行（基线：没派单、主 agent 自己读）、排错（用户推断三个嫌疑原因，选 A 验证）、第 1 次运行（加 `main_prompt` 后派给 researcher，任务那段话四项齐全）。知识点 4 ✅（2026-10-18）；阶段 1 ✅（2026-10-15） |
| 下一步 | **2026-10-24 起按新学法继续，05 剩下的目标照做，但不再走知识点流程：** ① （可选）"a helper" 实验：`description` 决定派给谁，目前只有文档原文，没有实测；② 接着做文件交接（原来的知识点 6），开工前先弄清遗留 ②（`.md` 拦截规则）；③ 提醒用户 git 提交（学习文档在 `09ab8da` 之后改了很多）。下面原计划里知识点 5 收尾的步骤（必须记住的 N 件事、找一线来源、教学自查、计数、升 L3 判断）**不再做**；"已决定挪走"的那几项仍按原来的安排（含糊派单和完整派单的对比改为可选实验）。**以下是 2026-10-24 之前的原计划，作历史保留：** ① 等用户决定 ⑤ "a helper" 实验做不做（问题 ②"`description` 决定派给谁"目前只有文档原文、没有实测；做的话：只把 `description` 临时改成 "a helper"，同一句话、不点名，跑 1 次）。**② 然后知识点 5 收尾**：必须记住的 N 件事（写进 `review.md`）；用户找 1 篇一线来源（2026-10-22 新规则第三节）；我的教学自查（含 `issue.md` 第 20–22 条）；卡住升级 / 查证提示计数和升 L3 判断；交接 prompt；提醒用户 git 提交（学习文档自 `09ab8da` 后改动很多）。**③ 已决定挪走、不在知识点 5 做的**：含糊派单 vs 完整派单对比 → 阶段 2 收尾 10 次实验；研究员固定规则（③）和重写 `description`（④）→ 加 WebSearch 那一步。过程记录见下面「知识点 5」一节 |
| 知识点 5 计数 | （2026-10-24 起停用，只作历史）写代码的卡住升级：0 次（目前）；查证提示（B2，单独计）：4 次——方向 2、文件 1、段落 1；前置知识补讲（不算提示）：dataclass、TypedDict、命令行参数、怎么找装好的包 / 怎么在文件夹里搜 |
| 遗留事项 | ① 项目内读文件不受检查函数控制（知识点 9 / 10）；② 内置"子 agent 不写报告文件"规则（`<tool_use_error>Subagents should return findings as text…`，文档未记载，挡 .md 不挡 .txt）——**知识点 6 用文件交接开讲前必须先查清**；③ 子 agent 第一轮附带 git 状态等环境信息——2026-10-18 查到 Claude Code subagents 文档原文 "Subagents receive only this system prompt plus basic environment details like the working directory"（附带环境信息有记载），是否包含 git 状态、开关在哪仍未查证；④ `ToolPermissionContext.agent_id` 可分辨子 agent 开的单（源码有，未实测，知识点 10 用）；⑤ 消息循环是否单开文件（知识点 4 后仍在 `main.py`，用户未提出拆分）；⑥ 小改进：`check_Write`→`check_write`、`initialization.py` 改用 `notes_path`（从未运行验证）、`path.py`→`paths.py`、`ClaudeAgentOptions(cwd=root)`、`agents.py` 第 10 行注释 `# should be WebSearch`、`system_prompt.py` 拼写和"any out limit behavior must prohibited"语法；⑦ WebSearch 等第一个真正需要上网的知识点再加（工具名 `WebSearch`，需要批准，要同时改主 agent `tools` 和 `check_tool`）；**加 WebSearch 时同时重写研究员的系统 prompt 和 `description`**（知识点 5 的 ③④ 挪到那里，按"每次都一样的放系统 prompt、这次才有的放任务那段话"来写；固定规则里"只用给的材料 / 附出处 / 按任务要求分组 / 找不到说不知道"基本通用，出处从行号改成网址） |
| 前置概念状态 | 进程：2026-10-01 补讲后复述过关（见 `review.md` Q1）；`async`：2026-10-01 补讲后检查题过关（见 `review.md` Q2） |
| 当前支持级别 | （2026-10-24 起不再使用，只作历史）**L2**（2026-10-02 起）；升 L3 计数 0/2（只看写代码的卡住升级，B2）；迁移任务按 L3 |
| 环境（最近一次运行） | SDK 0.2.162（2026-10-22 用户 `pip show` 确认）；命令行程序会自动更新，2026-10-24 第 1 次运行时是 2.1.310；模型 `claude-haiku-5-5` |
| 待定事项 | 阶段 5 做不做：前 4 个阶段结束后再判断 |

---

## 用户的固定要求

- ~~每次教学回复前重读 skill；回复第一行标出支持级别、路径、步骤~~（2026-10-24 停用）
- 每开始一个新知识点、或用户对某个点存疑时，**先查官方 / 权威来源**，核对和用户环境版本是否一致、技术说法是否正确；技术结论必须回到原文（官方文档、源码、changelog），不能只看摘要
- 从最底层出发：没见过的文件 / 配置 / 工具 / 术语，第一次出现先讲清是什么、为什么需要
- 架构按需生长：目录、配置、ignore 规则只在某个知识点第一次真正需要时才加
- `.env`、`.gitignore`、git 的概念用户已经掌握；需要具体写法时直接给（支撑代码），不单独开知识点
- 教学中暴露的 skill / 教学问题，记进项目根目录的 `issue.md`
- 上下文太长就开新对话（2026-10-24 起不再按知识点分）；本文件必须记录到能无缝衔接的程度
- 运行前预测：2026-10-24 起改为可选，用户想写就写，不要求（原规则 2026-10-02 定：预测和结果放在同一条消息里发，批改时先逐条对照）
- 术语记不住（2026-10-02 用户说"Claude Code 子进程标准输出"这类词记不住）：**判分看机制，不看术语**——用大白话说对过程就算对；讲解用大白话，固定只用少数几个名字：**Python 程序**（你写的 `main.py`）、**Claude Code 程序**（`query()` 启动的那个程序）、**模型**（在 Anthropic 服务器上）；新术语只在确实需要时引入，并且当场解释
- 模块化架构（2026-10-18 用户要求记下）：**学习过程的同时学会自己设计模块化架构**——结构决策尽量让用户自己设计（文件怎么分、谁引用谁、放哪），我给选项、代价和检查
- prompt 统一管理（2026-10-18 用户提出）：主 agent 和所有子 agent 的 prompt 都应独立保存、放在一个专门的地方统一管理（他看到 demo 原项目也是这样）
- **2026-10-24 起的学法**（取代 2026-10-22 加的两条规则，以及同日定的 A1 / B2 / C2 / D2 设置和"出题前先评判值不值"）
  - 起点是一个真东西：05 自己的代码、`example_program/`、`claude-agent-sdk-python` 源码（`_internal/query.py`、`message_parser.py`、`transport/`）。用户自己读，想弄懂哪块就从哪块开始，不排知识点
  - 用户想问就直接问，我直接答：讲机制、指出在源码哪个文件哪一行、帮着看报错都行。不设"先自己查 20 分钟"，不给提示阶梯，不只说来源类型。答的时候尽量指给他原文，方便他自己去看
  - 核心代码用户自己写（这条学习线的规矩不变）：我可以给思路、讲原理、指出 bug，但不替他写核心代码；支撑代码照旧直接给
  - 不做：开场复习、强制预测、批改打分、测验、迁移任务、支持级别、各种计数、教学自查
  - 做完一块写一段：几行就够，写弄懂了什么、测出了什么。给自己看，或者发 X（发不发由用户决定，AI 只润色、保留他的说法）
  - 想测数字时再测（可选）：比如含糊派单和完整派单各跑 10 次；内置 `.md` 拦截规则的触发条件（遗留 ②，做文件交接之前要先弄清）
  - 保留：技术结论要有出处并标明版本；文档里每条结论写明是谁查到的（用户 / Claude）
  - 学习日志只记结论、发现和遗留问题，不再写长篇的过程记录
  - 原因：用户 2026-10-24 说，结构化、推着走的学法让他"真的很心累"，效率很低（09-28 到 10-24 只做到知识点 5）。对照陈广宇的学法：由材料和目标带着走，先问 AI，代码自己写，学完写出来。10-22 定的"先查 20 分钟"和"提示阶梯"，和他"先问 AI"的做法正好相反，已撤回

## 固定词汇表（2026-10-17 加；讲解和题目只用这些词，用户忘了哪个就先看这里）

- **Python 程序**：你写的 `main.py` 跑起来的那个程序
- **Claude Code 程序**：`query()` 启动的另一个程序；agent 循环跑在它里面，工具也由它执行
- **模型**：在 Anthropic 服务器上，只会读文字、写文字，自己执行不了任何东西
- **工具清单**：`tools=[...]`；发给模型的"这次你能用哪些工具"；不在清单上的工具，模型开不出调用单
- **调用单**：模型写出的"请帮我用某个工具"的请求，带工具名、参数、编号；Python 程序里是 `AssistantMessage` 里的 `ToolUseBlock`
- **结果单**：Claude Code 程序执行（或拒绝执行）一张调用单之后，写回给模型的那张单，带对回调用单的编号、内容、是否出错；Python 程序里是 `UserMessage` 里的 `ToolResultBlock`
- **"可以执行"的规则**：`allowed_tools`；写进去的调用单不再问，直接执行
- **"不准执行"的规则**：`disallowed_tools`；写进去的调用单一律不执行，排在检查顺序第一
- **检查函数**：`can_use_tool=check_tool`；前面几步都没给出答案时，Claude Code 程序来问 Python 程序里的这个函数
- **主 agent**（知识点 4 起）：Python 程序直接对话的那个 agent
- **子 agent**（知识点 4 起）：被主 agent 叫去做一部分活的另一个 agent
- **Agent 调用单**（知识点 4 起）：主 agent 的模型对 Agent 工具开的调用单，写着派给谁（`input["subagent_type"]`）和任务那段话（`input["prompt"]`）；执行它 = Claude Code 程序新开一个子 agent
- **子 agent 定义**（知识点 4 起）：`AgentDefinition`，Python 程序事先写好的"角色卡"（`description` 介绍、`prompt` 子 agent 自己的系统 prompt、`tools` 子 agent 自己的工具清单），通过 `ClaudeAgentOptions(agents={名字: ...})` 交出去
- **标记**（知识点 4 起）：消息上的 `parent_tool_use_id`；主 agent 的消息为 `None`，子 agent 的消息 = 派活那张 Agent 调用单的编号

---

## 环境

| 项 | 内容 |
|---|---|
| 系统 | Windows |
| Python 环境 | conda 环境 `claude_agent_sdk` |
| SDK 版本 | `claude-agent-sdk` 0.2.162，2026-10-01 用户确认。**更正（2026-10-01）**：PyPI 上 0.2.160–0.2.163 没有 Windows wheel，Windows 上装的是源码包，**不带**命令行程序（原先写的"内置 2.1.285"是按 Linux 包查的，错了）；用户选方案 A，装了原生版 Claude Code（`~\.local\bin\claude.exe`），2026-10-01 能跑通；SDK 实际启动的命令行程序是 2.1.286（2026-10-01 从 init 的 `claude_code_version` 读出），与 0.2.163 配套的版本相同。**2026-10-17 用户确认**：仍是 0.2.162，命令行程序 2.1.288 |
| 当时最新版本 | 0.2.163（命令行程序 2.1.286），与本项目无关的改动 |
| 起点代码 | `main.py`：一个 agent，`query()` 循环，`tools=[]`，`setting_sources=[]`，haiku，`max_budget_usd=0.30`，只打印消息类型和文字 |
| 参考答案 | `example_program/`：anthropics/claude-agent-sdk-demos 的 research-agent（commit `826b268`）。只读；仓库没有 license，不公开发布（已在 `.gitignore` 中忽略） |

---

## 整体计划

### 教学方式

按 structured-coding-tutor 全流程：

- 每个知识点：【开场】（复盘上一个知识点、间隔复习、说明本点安排）→ 按路径教学（核心点原理和代码分两轮）→ 基于真实运行结果【批改】→ 更新三个学习文档
> 2026-10-24 起，本节"教学方式"停用，只作历史记录；新学法见「用户的固定要求」里的「2026-10-24 起的学法」。

- 每个阶段结束：测验（题目取自这个阶段真实发生的决策和 bug）+ 迁移任务（比当时支持级别高一级）
- 每个知识点开讲前，按用户的版本重做代码级查证，并看 changelog 中相关改动
- 每个知识点写完、跑通之后，再翻 `example_program/` 对应部分对比

### 核心（已确认）

- **地基：SDK 怎么驱动 agent 循环。** agent 循环（ReAct：推理 → 调用工具 → 看结果 → 再推理）跑在 SDK 启动的另一个程序（Claude Code 命令行程序）里；Python 程序看不到里面的过程，只能读它送回来的消息
- **项目核心：委派的边界。** 主 agent 只能通过派单工具 `Agent` 把活交出去；子 agent 唯一能看到的，是派单时写的那段话加上它自己的系统 prompt；子 agent 中间的过程不回流，只有最后一条消息回到主 agent

### 学习主题（用户总结，已确认）

在 ReAct 循环之上做多 agent 编排：多 agent 机制、任务编排方式、角色定位、工作边界、传输方式。

- 传输的三条通道：往下 = 派单那段话；往上 = 子 agent 的最后一条消息；横向 = 文件
- 护栏（按角色限制工具、花费上限）和可观测（谁调用了什么）保证工作边界真的守得住

### 能力目标

拿到一个任务时，能独立设计多 agent 的分工，并用 Agent SDK 实现：定角色和边界、写清派单内容、选交接方式、按角色限制工具、看清每个 agent 做了什么、给花费设上限。

### 产出目标（第一版）

- 终端输入一个研究问题，主 agent 把它拆成 **2 个**子课题
- **2 个角色、3 个子 agent 实例**：研究员 ×2（并行搜索，笔记写进文件）+ 写报告的 ×1（读笔记，输出带来源链接的 markdown 报告）；加上主 agent，一次运行共 4 个 agent
- 有工具调用日志；有花费上限
- "正好 2 个研究员"靠主 agent 的 prompt 要求 + 日志核对；SDK 只能硬性限制"同时运行数"，没有"总数"上限
- 固定 2 个的代价：不练"按复杂度决定派几个"；"拆成哪 2 个子课题"仍由主 agent 决定

**第一版不做**：画图、PDF、skills、斜杠命令、评估、Memory、防注入代码（只讨论风险）。

### 阶段与知识点

花费上限和 haiku 从知识点 1 起作为支撑代码直接给（带注释），完整原理在知识点 11。

**阶段 1 · 地基：一个 agent 是怎么跑起来的**

| # | 知识点 | 路径 | 归类理由 | 完成标志 | 写完后对照 demo 看什么 |
|---|---|---|---|---|---|
| 1 | SDK 怎么驱动 agent 循环：循环跑在另一个程序里，Python 只能读它送回来的消息 | 核心·可推理型 | "另一个程序里发生的事，Python 怎么知道"，设计可以自己推出来 | 运行前预测会收到哪几类消息、什么顺序，运行后对上；能说出每类消息代表什么 | `agent.py` 用 `ClaudeSDKClient` 而不是 `query()`；`setting_sources=["project"]` 会加载什么 |
| 2 | 一个 agent 使用工具：ReAct 循环在消息流里的样子 | 核心·可推理型 | "模型自己执行不了代码，怎么用工具"，可以推理 | 亲眼看到"工具调用 → 工具结果 → 下一轮回答"，说清工具是谁执行的 | demo 主 agent 没设任何工具限制 |
| 3 | 工具要过两道关："看得见"和"被批准" | 核心·可推理型 | 为什么需要两个互相独立的控制，可以从安全需求推出来 | 分别只开一道关，先预测再运行验证（含"未查证"项：未批准且没有 `can_use_tool` 时的实际表现） | `allowed_tools=["Task"]` + `bypassPermissions` 为什么在 demo 里"能跑" |

→ 阶段 1 测验 + 迁移任务

**阶段 2 · 委派边界（项目核心）**

| # | 知识点 | 路径 | 归类理由 | 完成标志 | 写完后对照 demo 看什么 |
|---|---|---|---|---|---|
| 4 | 最小两层：主 agent + 1 个研究员；上下文隔离 | 核心·可推理型 | "子 agent 该看到什么、交回什么"是设计问题 | 看到派单调用和标明"来自子 agent"的消息；用实验证明子 agent 看不到主 agent 的对话 | `message_handler.py` 只匹配 `'Task'`，现在派单工具叫 `Agent` |
| 5 | 派单契约：派单那段话要写哪些内容；`description` 决定主 agent 派给谁 | 核心·可推理型 | 缺了哪项内容会出什么错，可以推理 | 研究员只凭派单内容就正确完成；对比"含糊派单"和"完整派单"的实际结果 | `lead_agent.txt` 的 `<task_tool_usage>` 缺了哪些要素；`agent.py` 里的 `description` |
| 6 | 用文件交接，而不是层层转述 | 核心·可推理型 | 为什么不让结果都经主 agent 转手，可以推理 | 笔记写到约定路径，主 agent 只收到简短回执 | `researcher.txt` 的 `<file_workflow>` |

→ 阶段 2 测验 + 迁移任务（例：加一个新角色，比如"术语解释员"，自己写定义和派单内容）

**阶段 3 · 汇总与并行（完成后第一版达标）**

| # | 知识点 | 路径 | 归类理由 | 完成标志 | 写完后对照 demo 看什么 |
|---|---|---|---|---|---|
| 7 | 写报告的子 agent：排在研究之后、只读笔记、不上网、保留来源链接 | 核心·可推理型 | 为什么必须排在后面、来源链接怎样一路传到报告，可以推理 | "1 个研究员 → 写报告"这条链跑通 | `report_writer.txt`；博客里单独的 CitationAgent |
| 8 | 并行派 2 个研究员；子 agent 默认后台运行，主 agent 怎么等齐结果 | 核心·可推理型，加实测 | 怎么拆、怎么等是设计问题；模型会不会等只能实测 | 日志显示两个研究员时间重叠；主 agent 拿齐两份回执后才派写报告的；**第一版达标** | `lead_agent.txt` 的 "STEP 3: WAIT" 在后台默认下还成立吗 |

→ 阶段 3 测验 + 迁移任务（例：两个研究员改成按"正方 / 反方"拆分，报告要对比两方）

**阶段 4 · 可观测与护栏**

| # | 知识点 | 路径 | 归类理由 | 完成标志 | 写完后对照 demo 看什么 |
|---|---|---|---|---|---|
| 9 | 记录谁干了什么：hook 读出调用者 `agent_id`，`SubagentStart` / `SubagentStop`，写 JSONL 日志 | 核心·可推理型 | 并行时为什么不能靠消息顺序判断调用者，可以推理；写日志文件的代码是支撑代码 | 每次工具调用都记到正确的 agent 名下；能看出主 agent 有没有自己去搜索 | `subagent_tracker.py` 用全局变量推断归属，并行时为什么可能记错 |
| 10 | 按角色强制分工：主 agent 用不了 WebSearch / Write，研究员照常能用 | 核心·可推理型 | 有多种机制都能做到，要比较取舍 | 主 agent 调 WebSearch 被拒，研究员不受影响 | demo 只靠 prompt 里的 "You NEVER research" |
| 11 | 三个上限：花费、嵌套深度、同时运行数 | 核心·规定型 | 环境变量名和默认值是 SDK 规定的，推不出来 | 三个上限各触发一次，能说出默认值和触发后的表现 | demo 一个上限都没设 |

→ 阶段 4 测验 + 迁移任务

**阶段 5 · 带着上下文追问（待定：前 4 个阶段结束后判断做不做）**

| # | 知识点 | 路径 | 归类理由 | 完成标志 | 写完后对照 demo 看什么 |
|---|---|---|---|---|---|
| 12 | 接着上一次会话再搜一轮：`query()` 加 `resume`，还是改用 `ClaudeSDKClient` | 核心·可推理型 | 两个方案都可行，取舍由用户决定 | 对报告不满意时能追问，主 agent 记得上一轮内容 | `agent.py` 的 `ClaudeSDKClient` 会话循环 |

**收尾 · 与 demo 整体对比**（不是学习阶段，不做测验）：写一份差异记录。

---

## 支持级别记录

| 日期 | 级别 | 原因 |
|---|---|---|
| 2026-10-22 | L2（不变） | 用户选 B2：查证 / 排错时给的提示单独记作"查证提示"，不算进"卡住升级"；升 L3 只看写代码时的卡住升级（当前 0/2） |
| 2026-10-18 | L2（不变） | 知识点 4 完成：卡住升级 1 次（提示：`ToolUseBlock.id` vs `ToolResultBlock.tool_use_id`）；升 L3 计数 0/2 |
| 2026-10-07 | L2（不变） | 知识点 3 完成：卡住升级共 1 次（只给提示，用户自己改对检查函数里的 `endwith` 拼写错和“后一个判断覆盖前一个”的逻辑错）；部分代码 0 / 相似例子 0。升 L3 的计数 **0/2**（要连续 2 个知识点都不用卡住升级）。每个知识点之后重新计数 |
| 2026-10-01 | L1 | 起始级别，与用户商定（重新开始，地基要重学） |
| 2026-10-02 | **L2** | 知识点 3 开场时提议升级（计数 2/2），用户同意。L2 起：路径和代码分类（核心 / 支撑 / 观察）由用户先判断、我检查；核心代码用户写；大纲和 API 名字仍由我给 |
| 2026-10-02 | L1（不变） | 知识点 2 完成，卡住升级 0 次 → 升级计数 **2/2**，知识点 3 开场时提议升 L2 |
| 2026-10-01 | L1（不变） | 知识点 1 完成，卡住升级 0 次 → 升级计数 1/2。规则：连续 2 个知识点都没用卡住升级，就在下一个开场**提议**升一级，由用户决定；用了 2 次及以上则保持或提议降级。用户认可这套做法，要求每个知识点结束时把计数写进这里 |

---

## 计划变更记录

| 日期 | 变更 | 原因 |
|---|---|---|
| 2026-10-01 | 重新规划全部知识点；旧 README、旧知识点划分和代码进度作废；`main.py` 回到初始框架 | skill 在 2026-09-30 大规模更新 |
| 2026-10-24 | 知识点 5 完成标志"含糊派单和完整派单的结果能对比"移到阶段 2 收尾的 10 次对照实验（不在知识点 5 里单跑 1 次） | 用户质疑单跑 1 次过度，选 A |
| 2026-10-22 | 新规则的 4 个设置：A1（L2 只说来源类型）、B2（查证提示单独计数）、C2（新机制、新名字由用户先读原文）、D2（长输出由用户自己定位，取代知识点 4 的"我摘原文"） | 用户选择（本对话） |
| 2026-10-24 | 换学法：停用 structured-coding-tutor 的结构化流程，撤回 2026-10-22 加的两条规则和 A1 / B2 / C2 / D2 设置，改成"读真实代码、想问就问、核心代码自己写、做完一块写一段"；05 剩下的目标照做 | 用户说结构化、推着走的学法让他很心累、效率低；对照陈广宇的学法后决定（在另一个对话中讨论） |
| 2026-10-22 | 新增两条固定要求：查证、排错、读源码由用户先做、我核对；每个阶段收尾加一个带数字的对照实验，并由用户写成英文短帖 | 用户对照陈广宇的学习方式后决定（在另一个对话中讨论） |
| 2026-10-18 | 每个知识点开一个新对话（原来每个阶段一个） | 用户要求（知识点 4 收尾时） |
| 2026-10-17 | 知识点 4 开场时用户要求研究员的系统 prompt 单独存放：新增 `agents.py`、`system_prompt.py` | 用户的模块化架构要求 |
| 2026-10-02 | 阶段 1 拆成两个对话：知识点 1–2 在第一个对话，知识点 3 + 阶段 1 测验 / 迁移任务在新对话 | 第一个对话上下文过长，用户要求换新对话 |

---

## 查证基线（规划级）

> 2026-10-01 · 用户环境 0.2.162 / 命令行程序 2.1.285 · 当时最新 0.2.163 / 2.1.286
> 这是排知识点用的规划级查证；每个知识点开讲前仍要重做代码级查证。

| 结论 | 来源 |
|---|---|
| 派单工具在 `tool_use` 块里叫 `Agent`，在 `system:init` 的工具列表里仍叫 `Task`（命令行程序 v2.1.63 起） | [Subagents](https://code.claude.com/docs/en/agent-sdk/subagents) |
| 子 agent 只收到自己的系统 prompt + 派单那段话，看不到主 agent 的历史和系统 prompt；只有最后一条消息回到主 agent | 同上 |
| 子 agent 默认后台运行（v2.1.198 起）；主 agent 需要结果时会自己设 `run_in_background: false`（模型判断，不保证）；`AgentDefinition.background` 可强制后台 | 同上 |
| 三个上限：深度 `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` 默认 3；同时运行数 `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` 默认 20；花费 `max_budget_usd` 默认不设。没有"总数"上限 | 同上 |
| `query()` 传 `resume=session_id` 可以继续上一次会话（包括继续子 agent） | 同上 |
| `allowed_tools` 只是预先批准；没列出的工具仍然存在，需要批准的调用落到权限模式和 `can_use_tool`；`Agent` 属于不需要批准就能运行的工具 | [Permissions](https://code.claude.com/docs/en/agent-sdk/permissions) |
| 权限评估顺序：hooks → deny 规则 → ask 规则 → 权限模式 → allow 规则 → `can_use_tool` | 同上 |
| 子 agent 继承主会话的权限模式；只有主会话本身开着 bypass，子 agent 才可能 bypass | 同上 |
| 默认的 `query()` 会加载文件系统设置；`setting_sources=[]` 可隔离 | 同上 |
| hook 输入里的 `agent_id` / `agent_type` 只在子 agent 内部触发时有值；Python 支持 `SubagentStart` / `SubagentStop`；`PreToolUse` 可返回 `permissionDecision: "deny"` | [Hooks](https://code.claude.com/docs/en/agent-sdk/hooks)；0.2.162 源码 `types.py` |
| 0.2.162 的 `AgentDefinition` 字段：`description`、`prompt`、`tools`、`disallowedTools`、`model`、`skills`、`memory`、`mcpServers`、`initialPrompt`、`maxTurns`、`background`、`effort`、`permissionMode` | 0.2.162 源码 `types.py` |
| 0.2.160 修复了"`query()` + hooks + 后台子 agent 之后追问失败"；0.2.161–0.2.163 只升级内置命令行程序 | [CHANGELOG](https://github.com/anthropics/claude-agent-sdk-python/blob/main/CHANGELOG.md) |
| **未查证**：子 agent 调用一个未被批准的工具、又没有 `can_use_tool` 时，Python 下的实际表现（拒绝 / 报错 / 卡住） | 知识点 3 实测 |

---

## 知识点记录

> 每个知识点批改通过后追加一节，格式如下。
> 「教学自查」在本知识点结束时写好（引用原话），因为下一个知识点可能在新对话里开场，看不到这次的回复。
> 「真实发生的决策和 bug」是阶段测验的出题素材。

<!--
### 知识点 N · 名称
- 日期：
- 路径：
- 支持级别：
- 做了什么：
- 必须记住的 N 件事：
- 结果（基于真实运行）：
- 卡住升级次数：（提示 / 部分代码 / 相似例子，各几次）
- 查证提示次数：（2026-10-22 起单独记；方向 / 文件或页面 / 段落或函数 / 答案，各几次；不算进卡住升级）
- 真实发生的决策和 bug：
- 教学自查（对照 skill，引用原话；没有违规写"无"）：
- 遗留问题：
- 代码级查证记录（日期 + 用户版本 + 最新版本 + 来源链接）：
- 对照 demo 的结论：
-->

### 知识点 1 · SDK 怎么驱动 agent 循环（✅ 2026-10-01 完成）

- 开场：2026-10-01，用户确认安排（L1 · 核心·可推理型）
- 开场复盘：无（第一个知识点）；间隔复习：跳过（`review.md` 无题）
- 代码分类：支撑 = `load_dotenv`、import、`input()`、`asyncio.run` 入口、`ClaudeAgentOptions` 四个参数；核心 = `async for ... in query(...)` 接收循环 + 按消息类型处理；观察 = `print(type(message).__name__)` 等，验证完删除
- 第 2 步用户的尝试（2026-10-01）：写出 agent 的思考过程、工具调用、结果输出；什么时候写取决于 agent 和网络速度，不是固定时间；Python 靠 agent 输出结果后的"暂停符 / 标志 / 信号"判断结束
- 第 4 步反馈：对的——事情一发生就写、不攒到最后；用结束标志判断结束。缺口——① Python 读到一段文字时怎么分辨它是哪一类；② 结束标志只说"结束了"不够：花费、轮数没着落，也分不清正常做完和被迫中断
- 用户补缺口（2026-10-01）：① "需要带上一种工具说明，具体的对象 Python 才能分辨"——方向对，修正为"每段都带一个说明自己是哪一类的标签，不只是工具"；② "应该装结束状态啥的？"（不确定）——结束状态对，缺花费、轮数等统计，由我补齐，不再追问
- 第 8 步代码大纲（2026-10-01）：① `SystemMessage` 且 `subtype == "init"` → 打印 `data` 里的 `model`、`tools`、`session_id`；② `AssistantMessage` → 遍历 `content`，`TextBlock` 打印 `text`；③ `ResultMessage` → 打印 `subtype`、`num_turns`、`duration_ms`、`total_cost_usd`（可能为 `None`），`subtype == "success"` 时打印 `result`；不 break。观察代码：计数器 + 每条打印类型名 + 循环结束后打印总数。固定提示词 `Say hello in one sentence.`
- 运行前我写下的预期（2026-10-01，用户运行前写）：

<details><summary>预期输出（用户交预测之前先别展开）</summary>

`[observe] #1 SystemMessage`（init；`tools` 预计是空列表，**未查证**）→ `[observe] #2 AssistantMessage`（一个 `TextBlock`，一句问候）→ `[observe] #3 ResultMessage`（`success`，`num_turns` 1，花费几美分以下）→ `[observe] loop ended after 3 messages`。**未查证**：中间或结尾是否夹带 `RateLimitEvent` 或其他 `subtype` 的 `SystemMessage`。`sdk_host_only` 的 `session_state_changed` 会被 SDK 过滤，不会出现（0.2.162 源码 `_internal/query.py`）。init 的字段名 `model`、`tools`、`session_id` 已在 2.1.285 命令行程序（Linux 版）里核对过。

</details>

- 真实发生的 bug（2026-10-01）：第一次运行报 `CLIConnectionError: Refusing to execute batch script '...\npm\claude.CMD'`。证据链：SDK 找命令行程序的顺序是"包里自带的 `_bundled/claude.exe` → PATH 上的 `claude` → `~/.local/bin/claude.exe`"（0.2.162 源码 `_find_cli`）；0.2.162 在 PyPI 上没有 Windows wheel，源码包的 `_bundled/` 里只有 `.gitignore`；所以退到 PATH，找到 npm 的 `claude.CMD`；Windows 上 SDK 拒绝执行 .bat/.cmd（`_reject_windows_batch_cli`，防命令注入）。根因在我开场时的查证只看了 Linux 包，见 `issue.md` 第 3 条
- 修复决定（2026-10-01）：用户在 A（装原生 claude.exe）/ B（降到 0.2.159）/ C（`cli_path`）中选了 A。诊断命令用户没有跑，直接修了，所以"本机 `_bundled` 里没有 claude.exe"这一点没有在本机证实
- 第一次运行（2026-10-01，提示词用的是 "make a short haiku, less than 10 words"，不是约定的固定提示词；**运行前没写预测**）：#1 `SystemMessage`（init：`claude-haiku-4-5-20251001`、tools `[]`、session_id）→ #2–#33 共 32 条 `SystemMessage`（不是 init，代码没打印内容）→ #34 `AssistantMessage`（没有打印出文字）→ #35 `AssistantMessage`（俳句文字）→ #36 `ResultMessage`（`success`、1 轮、36434 ms、$0.031599）→ 循环结束，共 36 条；结果之后没有别的消息
- 用户对结果的解读：32 条 `SystemMessage` 是"agent 正在思考"。这与第 5 步讲的不符（模型产出走 `AssistantMessage`），没有证据，需要观察验证
- 第一次批改（代码）：三部分结构和条件都对；注释有两处不准——`SystemMessage` 那行注释写"会显示工具使用情况"（工具调用在 `AssistantMessage` 的 `ToolUseBlock` 里），`TextBlock` 那行注释写"the result"（最终结果在 `ResultMessage.result`）；打印的值没有标签（风格建议，非必须）
- 追加的观察代码（我给的）：非 init 的 `SystemMessage` 打印 `subtype`；每个内容块打印类型名；init 打印 `claude_code_version`
- 第二次运行（2026-10-01，固定提示词；**运行前仍然没写预测**）：#1 `SystemMessage`（init，命令行程序 2.1.286）→ #2 `AssistantMessage`，**一个内容块都没有**（观察行一次没打印）→ #3 `AssistantMessage`（`TextBlock`，问候语）→ #4 `ResultMessage`（`success`、1 轮、1639 ms、$0.00158）→ 共 4 条。第一次的 32 条额外 `SystemMessage` 没有出现
- 结论：① "32 条 `SystemMessage` = agent 在思考"被推翻：这次没有它们，模型照样给出回答。它们是什么，没能复现，**未查证**（第一次运行紧跟在刚装好原生 claude.exe 之后、耗时 36 秒，可能是首次启动相关，只是推测）；② 空的 `AssistantMessage`：0.2.162 的 `message_parser.py` 对内容块按 `type` 匹配 text / thinking / tool_use / tool_result / server_tool_use / advisor_tool_result，**不认识的类型直接丢弃、不报错**，所以一条消息可能到 Python 时 `content` 是空列表；原始块是什么类型，**未查证**
- 预测跳过的原因（2026-10-01）：用户说"没看到"——预测要求埋在长回复中段。责任在我的回复格式，见 `issue.md` 第 4 条。用户没有拒绝预测，默认继续保留
- 用户事后对三个预测问题的回答（看过结果之后，不算预测）：① 没明白"多出来的"指什么——我的措辞不清，应写"除了开头 init 之外的那些，即 #2–#33"；② "空白？"；③ 认为这次花费会低很多，理由是"模型已经有针对该问题的公式化回答"——**误解**：模型不会存好现成答案，费用按处理的 token 数计（输入 + 输出）。两次输出长度相近，差 20 倍只能来自输入侧或额外调用；具体原因**未查证**（可能与提示词缓存有关，只是推测），留到知识点 11 讲花费时用 `ResultMessage.usage` 查
- 用户补答第 1 题（2026-10-01）："从外表看不出差别，我认为都一样；单次模型的输出应该只有一种 subtype；它们是模型的产出，起码原内容必须先拿到任务输出才行"——**核心误解仍在**：把 `SystemMessage` 当成模型产出，把 `subtype` 当成"模型输出的类型"。纠正依据：① 第二次运行一条额外 `SystemMessage` 都没有，模型照样回答；② `type:"system"` 的行是命令行程序用自己的状态拼出来的（2.1.285 程序里 init 一行直接取 `cwd`、`session_id`、`tools`），模型的内容一律走 `AssistantMessage`；③ `subtype` 只是 `SystemMessage` / `ResultMessage` 里的细分标签。命令行程序（2.1.285，Linux 版）里能找到的 `system` 子类型有 40 多种，例如 `informational`、`status`、`api_retry`、`thinking_tokens`、`compact_boundary`——其中有的是"关于模型的报告"（如重试调用、思考用了多少 token），但仍是程序写的事件，不是模型写的内容。32 条具体是哪种，**未查证**。已要求用户再复述一次"怎么判断一条消息是不是模型产出"
- 代码批改通过（2026-10-01）：观察代码已删；遗留三处非阻塞小问题交给用户自行决定——第 18 行 `print(type(message).__name__)` 按开场分类属于观察代码、第 20 行注释仍写 "the results"、花费那行没有标签（风格建议）
- 必须记住的 4 件事（只含核心代码内容）：
  1. `query()` 启动 Claude Code 子进程，agent 循环在那里跑；它把每件事写成一行 JSON 到标准输出，Python 里的 SDK 读进来、翻译成对象，`async for` 一条条拿到。每条消息的内容都不是 Python 写的（→ `review.md` Q3）
  2. 用 `isinstance` 先看消息类：`AssistantMessage` 是模型产出（`content` 里的内容块，文字是 `TextBlock.text`）；`SystemMessage` 是程序关于自身状态的事件（init：`subtype == "init"`，`data` 里的 `model` / `tools` / `session_id`）；`ResultMessage` 是结束账单（→ Q5）
  3. `ResultMessage`：`subtype` 说明怎么结束（`success` 或各种 `error_*`），带 `num_turns`、`duration_ms`、`total_cost_usd`（可能为 `None`）；`result` 只在 `success` 时有；不要 `break`，让循环自然走完（→ Q4）
  4. `AssistantMessage.content` 可能是空列表：SDK 丢弃不认识的内容块类型，写代码不能假设一定有文字（→ Q6）
- 卡住升级次数：0（提示 0 / 部分代码 0 / 相似例子 0）
- 结果（基于真实运行）：第二次运行（固定提示词）4 条消息：`SystemMessage`(init) → 空 `AssistantMessage` → `AssistantMessage`(`TextBlock`) → `ResultMessage`(success, 1 轮, 1639 ms, $0.00158)；init 显示 tools `[]`、模型 `claude-haiku-4-5-20251001`、命令行程序 2.1.286。开场定的三个问题全部有答案。完成标志里"运行前预测"两次都没做到（原因见教学自查第 2 条）
- 对照 demo 的结论（2026-10-01，`example_program/research_agent/agent.py`）：
  1. demo 用 `async with ClaudeSDKClient(options) as client`，Claude Code 进程在整个聊天循环里一直开着；每轮 `client.query(...)` 发问题，再用 `client.receive_response()` 收消息——它**收到 `ResultMessage` 就自动停止**（0.2.162 `client.py` 文档字符串）。这正是"进程不退出时，`ResultMessage` 是唯一结束信号"的实际用法。我们的 `query()` 是一问一答、问完进程就退出。何时换成 `ClaudeSDKClient` 是阶段 5（知识点 12）的话题
  2. `setting_sources=["project"]` 加载 `<cwd>/.claude/settings.json` 和其中的 hooks、项目 CLAUDE.md 与 `.claude/rules/*.md`、项目的 skills / commands / subagents（官方文档 claude-code-features）。demo 的 `.claude/` 里有 `commands/`（5 个斜杠命令）和 `skills/`（executive-briefing、pdf），没有 settings.json 和 CLAUDE.md，所以实际加载的是这些命令和 skills。我们用 `[]`，这些都不加载。另：不传 `setting_sources` 等于 `["user","project","local"]`
  3. demo 只处理 `AssistantMessage`，而且用 `type(msg).__name__ == 'AssistantMessage'` 比较字符串，不用 `isinstance`；`SystemMessage` 和 `ResultMessage` 全部忽略，所以它不显示花费、也不区分正常结束和中断。用字符串比较能跑，但官方示例用 `isinstance`（风格差异，不是硬性规则）
- 遗留问题：① 第一次运行的 32 条额外 `SystemMessage` 是哪种 `subtype`，未复现、未查证；② 空 `AssistantMessage` 原本是哪种内容块，未查证；③ 两次运行花费差 20 倍的原因，留到知识点 11 用 `ResultMessage.usage` 查；④ `main.py` 三处非阻塞小问题（第 18 行类型名打印、第 20 行注释、花费标签）由用户自行决定
- 教学自查（对照 skill，引用我的原话）：
  1. 第 5 节查证清单第 1 条（用户环境版本）：开场时说"你装的 `claude-agent-sdk` 包里自带了一份（版本 2.1.285），所以不用另外安装"——依据的是 Linux 包，没核对 Windows 包，导致第一次运行报 `CLIConnectionError`。已记 `issue.md` 第 3 条
  2. 1.2 观察代码"运行前让用户预测"+ 第 4 节信息密度：预测要求两次埋在长回复中段（"## 三、运行前先写预测"；"**跑之前先写下预测**，提示词用 `Say hello in one sentence.`"），用户两次没看到。已记 `issue.md` 第 4 条，之后改为把要用户做的事放在回复最前面
  3. 第 7 节"用完整、具体的名字"：问"那些多出来的 `SystemMessage`，`subtype` 都一样，还是各不相同？"——"多出来的"指代不清，用户没看懂；应写"除了开头 init 之外的 #2–#33"
  4. 1.4 第 7 步判定：收尾复述里用户说"type 记录了当前 agent 的状态"，我判为"**判定：过关。** 核心机制你说对了"、当作措辞纠正；之后用户又把 `SystemMessage` 当成模型产出、说它是 Python 进程写的，说明这是核心误解，当时应要求重新复述
  5. 第 4 节（一次一步）：第 5–7 步放在同一条回复里，含两张表、一段 JSON 走查和收尾题，篇幅很长；第 4 点的误解没有在那一轮被消化，可能与此有关
  6. 1.2 观察代码"每行对应一个问题"：批改时加的 `[observe] cli version` 一行不对应本次运行的三个问题，而是为了查证记录环境版本；目的正当，但当时没有说明它对应的是哪个问题
  - 其余检查项（每条回复首行标注、没有替用户做 L1 留给用户的事、技术结论标日期和版本、文档改后读回）：无违规
- 本次运行要回答的问题：① 收到几条消息、哪几类、什么顺序 ② 回答文字在哪类消息里 ③ Python 怎么知道运行结束
- 代码级查证记录（2026-10-01 · 用户 0.2.162 / 命令行程序 2.1.285 · 当时最新 0.2.163）：

<details><summary>查证结论（第 5 步之前先别展开，会提前泄露第 2 步的答案）</summary>

| 结论 | 来源 |
|---|---|
| `query()` 把内置命令行程序作为子进程启动（`anyio.open_process`），参数含 `--output-format stream-json` | 0.2.162 源码 `_internal/transport/subprocess_cli.py` |
| 命令行程序送回的每条消息带 `type` 字段，SDK 按它转成 Python 类：`user`→`UserMessage`、`assistant`→`AssistantMessage`、`system`→`SystemMessage`、`result`→`ResultMessage`、`stream_event`→`StreamEvent`、`rate_limit_event`→`RateLimitEvent`、`conversation_reset`→`ConversationResetMessage` | 0.2.162 源码 `_internal/message_parser.py`、`types.py` 的 `Message` |
| 默认行为：不认识的 `type` 直接跳过（返回 `None`，只记 debug 日志），不报错 | 同上 `message_parser.py` 的 `case _` |
| 默认行为：`StreamEvent` 只在 `include_partial_messages=True` 时出现（默认 `False`） | 0.2.162 `types.py`；[agent-loop](https://code.claude.com/docs/en/agent-sdk/agent-loop) |
| 一次运行的顺序：`SystemMessage`（subtype `init`）→ 每个内容块一条 `AssistantMessage`（有工具时中间夹 `UserMessage` 装工具结果）→ `ResultMessage` 标志循环结束；之后仍可能有少量尾随系统消息，所以要把循环迭代完而不是遇到结果就 break | [agent-loop](https://code.claude.com/docs/en/agent-sdk/agent-loop) |
| `ResultMessage` 字段：`subtype`、`is_error`、`num_turns`、`session_id`、`total_cost_usd`、`result`（只在 `success` 时有）、`stop_reason` 等；`total_cost_usd` 可能为 `None` | 0.2.162 `types.py`；agent-loop |
| `tools=[]` = 关闭所有内置工具（命令行参数 `--tools ""`） | 0.2.162 `types.py` 文档字符串、`subprocess_cli.py` |
| 单次 `query()` 以错误结果结束时，先给出 `ResultMessage`，再抛异常 | agent-loop |
| **未查证**：0.2.162 / 0.2.163 两条 CHANGELOG 原文（本次抓取只显示到 0.2.161），沿用规划级记录 | [CHANGELOG](https://github.com/anthropics/claude-agent-sdk-python/blob/main/CHANGELOG.md) |

</details>

### 知识点 2 · 一个 agent 使用工具：ReAct 循环在消息流里的样子（✅ 2026-10-02 完成）

- 开场：2026-10-01 发出，2026-10-02 用户确认安排
- 支持级别：L1（升级计数 1/2）
- 路径：核心·可推理型——"模型自己执行不了代码，怎么用工具"可以从限制条件推出来
- 开场复盘：读知识点 1 的"教学自查"6 条（同一对话，原话已引用在那一节）
- 间隔复习候选：Q6（未作答）、Q3（1 级）、Q5（1 级）、Q4（2 级），让用户选 1–2 题或跳过
- 代码分类（计划，开场时告知用户）：支撑 = `tools=["Read"]`、import 加 `UserMessage` / `ToolUseBlock` / `ToolResultBlock`、init 分支加一行打印 `claude_code_version`（命令行程序会自动更新，每次查证要知道实际版本）；核心 = `AssistantMessage` 分支处理 `ToolUseBlock`（`name`、`input`），新增 `UserMessage` 分支处理 `ToolResultBlock`（`is_error`、`content`）；观察 = 打印 `ToolUseBlock.id` 和 `ToolResultBlock.tool_use_id`，验证完删除
- 第 2 步用户的尝试（2026-10-02）："模型先把需求交给 Claude Code，然后 Claude Code 装载和调用工具"
- 第 4 步反馈：对的——模型自己不动手，由 Claude Code 程序替它执行。缺口——① 起点漏了：第一步是 Claude Code 把问题发给模型，模型还得事先知道有哪些工具可用；②"需求"太笼统：Claude Code 要照着执行，模型必须写清用哪个工具、对什么（参数）；③ 终点漏了：读到的内容还在 Claude Code 那边，要再发回给模型（模型不记事，要连同前面的对话一起发），模型才能写出答案。"装载工具"不准确：工具本来就在 Claude Code 程序里
- 用户补缺口（2026-10-02）：① "Claude Code 得发个信号给模型，强调它现在有这个环境"——对，具体是第一次请求里就附上工具清单（名字、用途、参数格式）；② "任务、工具"——对，具体是工具名 + 参数，再加一个编号；③ "Claude Code 把内容发回给模型，让它看一遍"——对，要连同前面全部对话一起发
- 第 5–6 步（2026-10-02）：拆成单独一条回复，不和第 7 步放一起（吸取知识点 1 教学自查第 5 条）
- 第 8 步代码大纲（2026-10-02）：支撑 = import 加 `UserMessage` / `ToolUseBlock` / `ToolResultBlock`、`tools=["Read"]`、init 打印 `claude_code_version`；核心 ① `AssistantMessage` 的内容块循环里加 `ToolUseBlock` 分支，打印 `name`、`input`；核心 ② 新增 `UserMessage` 分支，`content` 是列表时遍历，`ToolResultBlock` 打印 `is_error` 和 `content`（转成字符串后只取前 200 个字符）；观察 = 每条消息打印类型名、`ToolUseBlock.id`、`ToolResultBlock.tool_use_id`
- 运行前我写下的预期（2026-10-02，用户运行前写）：

<details><summary>预期输出（用户交预测之前先别展开）</summary>

`SystemMessage`（init，tools 显示 `['Read']`，**未查证**具体写法）→ 可能有一条只带文字的 `AssistantMessage`（如"我来读一下"）→ `AssistantMessage`（`ToolUseBlock`：`Read`，`input` 里有 `file_path`）→ `UserMessage`（`ToolResultBlock`，`tool_use_id` 与上一条的 `id` 相同，内容是 README 的文字，**可能**带行号前缀，未查证）→ `AssistantMessage`（`TextBlock`，一句话回答）→ `ResultMessage`（`success`，`num_turns` 预计 2，**未查证**计数规则）。也可能再次出现空的 `AssistantMessage`（见 Q6）。

</details>

- 第一次运行（2026-10-02，提示词与固定的基本一致；**运行前预测第三次没有交**）：`SystemMessage`(init：CLI 2.1.286、tools `['Read']`) → 4 条非 init `SystemMessage` → 空 `AssistantMessage` → `AssistantMessage`(`ToolUseBlock`：`Read`，`{'file_path': 'D:\\...\\README.md'}`，id `toolu_01YQWx...`) → `UserMessage`(`ToolResultBlock`：`is_error` 为 `None`，内容带行号 "1  # 05 Research Agent ..."，`tool_use_id` 与调用单 id 相同) → 2 条非 init `SystemMessage` → 空 `AssistantMessage` → `AssistantMessage`(`TextBlock`，一句话回答) → `ResultMessage`(success，`num_turns` 2，3250 ms，$0.005873)
- 三个问题的答案：① 调用单在 `AssistantMessage` 的 `ToolUseBlock` 里，结果在 `UserMessage` 的 `ToolResultBlock` 里，顺序是调用单 → 结果 → 回答；② 两个编号完全相同，靠它对上；③ `num_turns` 为 2，与两次调用模型一致
- 新发现：Read 工具返回的内容**带行号**（模型看到的也是带行号的文本）；`is_error` 没出错时是 `None` 而不是 `False`（字段可选，命令行程序没写就是 `None`）；**每次模型回答前都有一条空 `AssistantMessage`**（本次代码只打印文字和调用单，分不清它是空列表还是装着别的块，例如思考块）——原因**未查证**
- 第一次批改（代码）：两部分都对；注释三处不准——第 27 行 "tool use cases"、第 30 行 "local data link"（`input` 是调用单上的参数，不是"本地数据链接"）、第 40 行 "claude code feedback"（准确说是 Claude Code 送回给模型的工具结果）；打印没有标签（风格）
- 第二次运行（2026-10-02，加了"每个内容块打印类型"和"非 init 的 SystemMessage 打印 subtype"两行观察）：非 init 的 `SystemMessage` 全部是 `subtype` **`thinking_tokens`**（每次调用模型前 2 条）；每次回答前那条"空" `AssistantMessage` 里装的是 **`ThinkingBlock`**（模型的思考），只是代码没打印它。结论：haiku 在这个环境下默认会思考；`thinking_tokens` 是 Claude Code 程序关于思考用量写的报告，不是模型写的内容。知识点 1 第一次运行那 32 条很可能也是 `thinking_tokens`，但当时没打印 subtype，**未证实**。知识点 1 第二次运行 #2 那条是真的空列表（当时有逐块打印，一行没出），和这次的 `ThinkingBlock` 不是一回事，原因仍**未查证**（可能是 SDK 不认识的块类型被丢掉）
- 用户的预测（第一次运行之后、第二次运行之前写，随第二次输出一起发来；**更正**：我起初判成"看过结果后补写、不算预测"并一句带过，没有拿去和结果对照——这是我的错，用户指出后已改正）：① 四类消息都会出现，"工具结果：Read"；② 编号完全一样，"一个任务有自己单独的 id"；③ 不清楚（第一次运行后知道是 2）
- 预测与第二次运行对照：① 四类都出现——对上；"工具结果：Read"——**没对上**：`Read` 是调用单上的工具名，在 `AssistantMessage` 的 `ToolUseBlock` 里，工具结果在 `UserMessage` 的 `ToolResultBlock` 里（暴露的缺口：把"调用单"和"结果单"混在一起）；② 对上；③ 对上（但借助了第一次运行的结果）
- 用户提问："observe 更像是给你看的工具，这种多对象监控 agent 输出的方式其他开发者也会用吗？"——回答：按消息类分支处理是官方文档的标准写法，demo 的 `utils/message_handler.py` 也是逐块按 `TextBlock` / `ToolUseBlock` 分支（用类名字符串比较），并用 `block.id` 登记子 agent；`[observe]` 是临时调试打印，是给用户自己看、用来和预测对照的；正式项目会换成日志（如写 JSONL 文件），demo 用 hooks 写 `tool_calls.jsonl`——这是知识点 9 的内容
- 预测：第一次运行前没交；第二次运行前交了（见上）。A（两步走）/ B（取消）的选择仍待用户决定
- 第二次批改（注释）：第 27、30 行已改好；第 40 行改成 "monitor claude code send model's feedback" 仍不准（送回的是工具结果，不是模型的反馈），非阻塞
- 本次运行要回答的问题：① 带工具的运行，消息按什么顺序到达，工具调用、工具结果各装在哪类消息里；② 一条工具结果怎么对上是哪一次调用的；③ 模型一共被调用了几次（`num_turns`）
- 固定提示词（代码阶段用）：`Read README.md in the current folder and tell me in one sentence what it says.`（从项目根目录运行）
- 完成标志：亲眼看到"工具调用 → 工具结果 → 下一轮回答"；说清工具是谁执行的；运行前预测与实际对上
- 代码级查证记录（2026-10-01 · SDK 0.2.162 / 命令行程序 2.1.286（原生版，会自动更新）· SDK 最新 0.2.163）：
  - `ToolUseBlock` 字段 `id` / `name` / `input`；`ToolResultBlock` 字段 `tool_use_id` / `content`（`str`、`list[dict]` 或 `None`）/ `is_error`；`UserMessage.content` 是 `str` 或内容块列表——0.2.162 `types.py`
  - `tools=["Read"]` → 命令行参数 `--tools Read`——0.2.162 `subprocess_cli.py`
  - 不传 `cwd` 时，Claude Code 子进程继承 Python 进程的当前目录——0.2.162 `subprocess_cli.py`（`cwd=self._cwd`，为 `None` 时不指定）
  - 默认行为：工作目录内的文件读取"由工具自己批准"，不需要任何允许规则——[Permissions](https://code.claude.com/docs/en/agent-sdk/permissions)
  - **对知识点 3 的影响（规划提醒）**：同一页说，不设 `permission_mode` 时起始模式按设置文件决定，否则用内置默认，"can be auto mode"——和规划时以为的 `default` 不同，知识点 3 开讲前要实测 init 里的 `permissionMode`
  - **未查证**：GitHub 上 `CHANGELOG.md`（main 分支）最新一条是 0.2.160，0.2.161–0.2.163 没有条目，无法核对这三个版本的改动
- 代码批改通过（2026-10-02）：观察代码已全部删除；第 39 行注释 "send model's feedback" 仍不准（非阻塞）
- 必须记住的 4 件事（只含核心代码内容）：
  1. 模型只会收文字、回文字，碰不到你的电脑；工具由 Claude Code 程序在你电脑上执行。Claude Code 每次调用模型都附上工具清单，`tools=[...]` 决定清单上有什么（→ `review.md` Q7、Q8）
  2. 调用单 = `AssistantMessage` 里的 `ToolUseBlock`（`name`、`input`、`id`）；结果单 = `UserMessage` 里的 `ToolResultBlock`（`tool_use_id`、`content`、`is_error`）；`tool_use_id` 等于调用单的 `id`，靠它一一对上（→ Q9）
  3. ReAct 循环：调用单 → Claude Code 执行 → 带全部历史把结果发回 → 模型回答或再开单；这次 `num_turns` = 2，等于调用模型的次数（→ Q7）
  4. 写代码的三个坑：`UserMessage.content` 可能是字符串也可能是列表，只在列表时遍历；`is_error` 没出错时可能是 `None`，判断写 `if block.is_error:`；看起来空的 `AssistantMessage` 可能装着没打印的 `ThinkingBlock`（→ Q10）
- 卡住升级次数：0（提示 0 / 部分代码 0 / 相似例子 0）
- 结果（基于真实运行）：两次运行都是 `success`、`num_turns` 2、约 3.3 秒、约 $0.006；调用单与结果单编号一致；开场定的三个问题全部有答案；第二次运行前交了预测，对照后暴露"调用单 / 结果单混淆"
- 对照 demo 的结论（2026-10-02，`example_program/research_agent/agent.py`、`utils/message_handler.py`）：
  1. demo 的主 agent **没设 `tools`**——不传就是命令行程序的默认整套工具（0.2.162 `subprocess_cli.py`：`tools` 为 `None` 时不传 `--tools`），所以 Read、Bash、WebSearch、Write 等都在它的工具清单上；它的 prompt 说"你从不自己研究"，但清单上照样有搜索工具。用 `tools` 收窄清单是我们这次的做法；"清单上有"和"被批准运行"是两回事，`allowed_tools=["Task"]` + `bypassPermissions` 是知识点 3 的内容，按角色强制分工是知识点 10
  2. `message_handler.py` 和我们一样逐块分 `TextBlock` / `ToolUseBlock`，并用 `block.id` 登记子 agent；但它只认工具名 `'Task'`，现在派单工具叫 `Agent`（规划级查证），知识点 4 再看
- 遗留问题：知识点 1 第二次运行 #2 那条真正的空 `AssistantMessage`，原始块类型仍未查证；知识点 1 第一次运行 32 条 `SystemMessage` 很可能是 `thinking_tokens`，未证实
- 教学自查（对照 skill，引用我的原话）：
  1. 1.2 观察代码"运行后与预测对照"：用户随第二次输出发来三条预测，我写"这次你写的三条，是看完结果之后补的"，一句带过、没逐条对照；用户指出后补了对照表。今后先对照预测，再讲结果
  2. 1.0 第 4 步间隔复习：开场时只给了候选表格（"从第二部分的表里挑 1–2 题，不看代码直接作答"），题目写成表格里的短标题，用户说"你要我回答的问题是什么，我看不出来"；之后改成逐题写出完整问题
  3. 第 7 节（用用户记得住的词）：间隔复习判定里写"消息走的是哪条通道：Claude Code 子进程的标准输出"，用户说这类术语记不住；之后改为判分看机制、讲解用三个固定名字
  - 其余检查项（首行标注、观察代码每行对应问题、没替用户做 L1 留给用户的事、查证标日期和版本、文档改后读回、要用户做的事放在最前面）：无违规

### 知识点 3 · 工具要过两道关：“看得见”和“被批准”（✅ 2026-10-07 完成）

- 开场：2026-10-02 发出（新对话）
- 开场复盘：跨对话，读知识点 2 的"教学自查"3 条（引用原话见那一节），其余无违规
- 间隔复习：给了 5 道候选（Q6、Q9、Q10、Q7、Q3），用户 5 道全答。结果：Q3 2→3；Q6 0→2；Q9 —→2；Q10 —→2（只答出 1/3，优先再考）；Q7 2→2（回程补上了，漏"全部历史重发"和"可能再开调用单"）
- 支持级别：**L2**（用户 2026-10-02 决定升级）。用户要求按 L2 重新给安排，并讲清三种路径（辅助 / 核心·可推理型 / 核心·规定型）及判断方法——已讲，路径由用户先判断
- 路径：计划表写的是核心·可推理型（L1 时定）。用户先问"到底判断啥？我连知识点 3 要讲什么都不清楚"——我没先说清知识点讲什么就让他判断（`issue.md` 第 7 条），补讲问题后用户判断："可推理型，因为每个用户的需求可能都不一样"。判定：结论对；理由没对准标准（那是问题的一条限制，不是"能否从问题推出做法"），当场纠正，通过
- 安排：用户 2026-10-02 确认
- 原理第 1–3 步（2026-10-02）：限制条件——执行在你电脑上、用你的权限；模型会出错或被读到的内容带偏；同一个工具（跑命令）有无害和危险两种用法；运行时没人盯着、调用很多；不同 agent 需求不同。问题：给研究员 agent 设计控制（能搜网页、读文件；不能写文件；跑命令只允许无害的），对每种工具说清"模型开单 → Claude Code 程序执行或不执行"之间发生什么、Python 程序要提前告诉 Claude Code 程序什么
- 第 2 步用户的尝试（2026-10-02）："中间应该找用户确认一遍流程、工具使用信息和范围啥的"；并指出第二问有歧义（"哪三条规矩？"），猜"需要事先告诉 Claude Code 必须做一个审批"。歧义是我的措辞问题："三条规矩"指的是上面列的三条要求，没写明
- 第 4 步反馈：对的——开单和执行之间要有一道审批，最终决定权在人；"范围"方向对。缺口（以问题形式留给用户补）：① 没人盯着、几十张单，每张都问人行不通——不问人时 Claude Code 程序凭什么决定、这些依据由谁什么时候给；② 写文件"绝对不能"：每次开单再拒绝 vs 让模型根本开不出这张单，选哪个、为什么；③ 跑命令：只看工具名够不够，要看调用单上的什么
- 用户补缺口（2026-10-02）：① "只能按工具调用的影响范围、是否有隐性问题来决定，也就是模型必须先思考一番"；② "因地而异：搜索 agent 本身不该写文件，那就根本不应该开单；写文件 agent 必须写文件，那干嘛还要批准或拒绝"；③ "规定？提示词？"
- 反馈：① 看影响范围对；"让模型自己先想"是误解——会出错、会被带偏的正是模型，自己审自己等于没审；不问人时的依据是 Python 程序事先写好、启动时交给 Claude Code 程序的规则，由 Claude Code 程序（普通程序，不会被说服）对照。② 完全对：不该用的工具让模型根本看不见（开不出单），本职工具提前批准——正是"看得见"和"被批准"两道关的由来。③ 提示词不行（只是请求，模型可能不听）；"规定"对；要看调用单的参数（`input`），跑命令时就是命令文字
- 第 5–6 步（2026-10-02，单独一条回复）：第一道关 = 发给模型的工具清单（整工具粒度，不在清单就开不出单）；第二道关 = 每张单执行前按顺序检查、哪步定了就停：禁止规则（全放行也推翻不了）→ 权限模式（默认 / 全放行 / 只放行改文件 / 另一个模型审 / 不问直接拒）→ 允许规则（含"工作目录内读文件由工具自己放行"，解释知识点 2 的 Read 没写规则也能跑）→ 问 Python 程序里的函数（兜底）。简化掉 hook（知识点 9）和设置文件的 ask 规则。为什么缺一不可：只有清单分不开 dir / 删除；只有审批则不该用的工具会被反复尝试、且全放行时整体失效。场景：研究员配置下写文件 / 搜网页 / dir / 被带偏的删除四张单逐一走两道关；再看"总开关改全放行"时删除被放行（对应 demo）
- 用户反馈（2026-10-02）："讲的太复杂了，词语用的极其不恰当，我分不清具体机制"。重讲版：只讲两件事——① 工具清单（Python 程序定，不在清单上开不出调用单）；② 调用单执行前 Claude Code 程序按顺序查三步：对上"不准执行"的规则 → 不执行；对上"可以执行"的规则 → 执行；都没对上 → 问 Python 程序里的检查函数。固定用词：工具清单、调用单、执行 / 不执行、"可以执行"的规则、"不准执行"的规则、检查函数。权限模式、hook、设置文件暂不讲，代码阶段需要时再引入
- 代码分类：**挪到代码阶段开头**（原理复述过关之后），按当时级别决定谁先分——级别未定时先写会替用户做 L2 的事，且具体代码块名字会提前泄露原理答案（已记 `issue.md` 第 6 条）
- 本次运行要回答的问题：① 什么都不设时，Claude Code 程序默认怎么批准工具（文档：Agent SDK 会话能拉取功能开关时起始为 `default`，不能时 2.1.285+ 为 `auto`，只能实测）；② 工具看得见但没被批准时，Python 这边实际看到什么（拒绝 / 报错 / 卡住）；③ 工具被批准但看不见时，模型能不能用
- 完成标志：分别只开一道关，先预测再运行，对照结果
- 规划级查证（2026-10-02 · 用户 SDK 0.2.162 · 最新 0.2.163，`pip index versions`）：[Configure permissions](https://code.claude.com/docs/en/agent-sdk/permissions)、[Choose a permission mode](https://code.claude.com/docs/en/permission-modes)；代码级查证待代码阶段开头做
- 代码阶段开头（2026-10-02）：列出 8 块代码请用户分类——① import `PermissionResultAllow` / `PermissionResultDeny` / `ToolPermissionContext`；② init 打印 `permissionMode`；③ `tools=[...]`；④ `allowed_tools=[...]`；⑤ `permission_mode="default"`；⑥ 检查函数本体（按工具名和参数返回执行 / 不执行，不执行带理由）；⑦ `can_use_tool=检查函数`；⑧ 检查函数开头打印被问的调用单。权限模式在这里第一次正式引入（只用 default，说明为什么要显式写）
- 运行计划：第 1 次 清单 Read+Write、什么都不设（问题 ①）；第 2 次 加 `permission_mode="default"`（问题 ②）；第 3 次 再加检查函数（看它被问、不执行的理由回到模型）；第 4 次 清单只有 Read、"可以执行"规则写 Write（问题 ③）
- 代码级查证记录（2026-10-02 · 用户 SDK 0.2.162 / 命令行程序以 init 实际版本为准 · SDK 最新 0.2.163）：
  - 0.2.162 `types.py`：`PermissionMode` = default / acceptEdits / plan / bypassPermissions / dontAsk / auto；`CanUseTool` = `async (tool_name: str, input: dict, context: ToolPermissionContext) -> PermissionResultAllow | PermissionResultDeny`；`PermissionResultDeny` 字段 `message`（发给模型的理由）、`interrupt`；`PermissionResultAllow` 字段 `updated_input`、`updated_permissions`
  - 0.2.162 `subprocess_cli.py`：`allowed_tools` → `--allowedTools`；`disallowed_tools` → `--disallowedTools`；`permission_mode` 只在设置时才传 `--permission-mode`（不设 = 由命令行程序自己决定）
  - 0.2.162 `types.py` `_configure_can_use_tool`：设了 `can_use_tool` 才会让命令行程序通过 stdio 来问；不设就不传 `--permission-prompt-tool`，此时规则都对不上的调用单怎么处理——**未查证**（问题 ②，实测）
  - 0.2.162 `types.py`：`can_use_tool` 和 `allowed_tools` 里整工具的条目同时出现时，SDK 会发 `CanUseToolShadowedWarning`（那些工具不会再问检查函数）
  - [CHANGELOG](https://github.com/anthropics/claude-agent-sdk-python/blob/main/CHANGELOG.md)：0.2.140 起 `can_use_tool` 支持 `query()` + 字符串 prompt；0.2.111 加了"被 allowed_tools 遮住"的警告；0.2.160 修了 `query()` + `can_use_tool` + 后台子 agent 后追问失败；0.2.161–0.2.163 仍无条目
  - init 里的字段名 `permissionMode`：TypeScript 参考文档的 init 消息类型里有（[TypeScript reference](https://code.claude.com/docs/en/agent-sdk/typescript)），Python 的 `SystemMessage.data` 是原样字典——运行时确认
  - 不设权限模式时的起始模式：[Choose a permission mode](https://code.claude.com/docs/en/permission-modes) 说 Agent SDK 会话能拉取功能开关时是 `default`，不能时 2.1.285+ 是 `auto`——问题 ①，实测
- 用户对运行计划表的反馈（2026-10-02）："这是什么意思？为什么又输出这种让人看不明白的东西"——表格压缩、一条回复塞三件事（`issue.md` 第 9 条）；用完整句子重讲后，用户自己总结："改 main.py 让 agent 能用写文件工具，跑 4 次，每次设不同环境，看 agent 面对不同工具情况时会怎样"，并说"你就不能说清楚一点吗"——他的总结就是对的一句话版，今后先给一句话版再展开
- 用户的代码分类（2026-10-02）："都是核心，没什么观察或者支撑"。检查：③ 工具清单、④ "可以执行"规则、⑥ 检查函数本体、⑦ 把检查函数交给 Claude Code 程序——核心，对；① import——支撑；⑤ 权限模式写 default——支撑（这次不学权限模式本身，只是让三步检查按讲过的走）；② 打印 `permissionMode`、⑧ 检查函数里打印被问的调用单——观察（临时、回答问题、验证完删）。对 4/8；暴露的缺口：没用"假如这块不懂、核心会写，算不算学会"去逐块判断
- 运行计划简化（2026-10-02，已告知用户）：清单不再放读文件——第 1–3 次清单只放写文件，第 4 次清单为空、"可以执行"规则写写文件；每次运行前单独给那一次的大纲
- 第 1 次运行大纲（2026-10-02）：核心 `tools=["Write"]`；观察 init 分支打印 `message.data.get('permissionMode')`；运行前确认没有 `notes.txt`。预测三问：① init 显示的权限模式；② `notes.txt` 会不会出现；③ 结果单的 `is_error` 和内容
- 第 1 次运行（2026-10-02）：代码按大纲改对（第 37 行注释 "print the tool situation [Tempt]" 不准，实际打印的是权限模式，非阻塞）。输出：CLI 2.1.286、Tools `['Write']`、**`permissionMode` = `default`** → 模型开出 Write 调用单（`file_path` = 项目根目录 `notes.txt`，`content` = `hello`）→ 结果单 **`is_error` = `True`**，内容 "Claude requested permissions to write to ...notes.txt, but you haven't granted it yet." → 模型回答请用户授权 → `ResultMessage` `success`、`num_turns` 2、约 3.7 秒、$0.0052。`notes.txt` 没有出现
- 预测对照：① default——对上；② 会出现——没对上；③ 不清楚。用户自评"is_error 也没出现"是读错了——第 45 行打印 `is_error` 没加标签，那行 `True` 就是它（建议加标签）
- 结论：问题 ① 在本环境（直连 API，命令行程序 2.1.286）答案是 `default`；问题 ②：规则都对不上、又没有检查函数时，不报错、不卡住，Claude Code 程序当作"没被允许"，给模型发一张 `is_error=True` 的结果单，模型自己决定下一步（这次是请用户授权）；`ResultMessage` 的 `success` 只表示这次运行正常结束，不表示任务完成（关联 Q4）
- 计划变更：原第 2 次（显式写 `permission_mode="default"`）取消——第 1 次已显示默认就是 default，再跑结果相同；但写检查函数那次仍把 `permission_mode="default"` 作为支撑代码写上（命令行程序会自动更新，默认值可能变）
- 用户对第 1 次的总结（2026-10-02）："我既告诉它能用这个工具，但没告诉它使用权限，所以它需要我的同意才行"——对；补一句：准确说是需要检查函数（Python 程序）给答案，检查函数可以去问人，也可以按代码判断
- 第 2 次运行大纲（2026-10-02）：支撑（直接给）——import `PermissionResultAllow` / `PermissionResultDeny` / `ToolPermissionContext`，`permission_mode="default"`；核心 ①——`async def check_tool(tool_name, input_data, context)`：Write 且 `file_path` 以 `.md` 结尾 → `PermissionResultAllow()`，否则 → `PermissionResultDeny(message=...)`；核心 ②——`can_use_tool=check_tool`；观察——函数第一行打印被问的调用单，删掉第 37–38 行权限模式打印，`is_error` / 内容打印加标签。预测三问：检查函数被问几次、各是什么文件；第一张结果单的 `is_error` 和内容；最后出现什么文件、`num_turns`
- 用户代码进度与三个问题（2026-10-06）：用户贴出写到一半的 `main.py`（已加 import、检查函数、`can_use_tool=check_tool`、`permission_mode="default"`、`is_error` / `content` 标签；还没删权限模式打印、没加观察行）。提问：① "新增的类为什么不解释，是打算直接让我当黑箱用吗"；② "main 文件急剧扩充，确定暂时不按 skill 要求对代码做架构吗"；③ "`can_use_tool` 是什么，为什么它出现了 agent 就能调用自建工具？前后逻辑、怎么被调用也不讲"；并问观察行加在哪、`can_use_tool` 和 `tools` 有什么不同
- 我的回应要点：① 三个新类（`PermissionResultAllow` / `PermissionResultDeny` / `ToolPermissionContext`）我归为支撑代码就没解释，违反第 8 节"第一次出现先讲背景"（`issue.md` 第 10 条）；② skill 第 8 节本意是"架构按需生长"，不是"必须拆"，但 main.py 第一次同时承担"打印消息"和"决定权限"两件不相关的事，该把选择交给用户（`issue.md` 第 11 条）——给 A / B / C 三个方案，用户决定；③ **用户的误解**：他把检查函数当成"自建工具"（代码注释写 `# customized tool`）。实际 `check_tool` 不是工具，是三步检查的第 3 步；agent 能用的工具只由 `tools=[...]` 决定。**函数名 `check_tool` 带 "tool" 是我起的，误导了他**，建议改名为 `check_permission`（用户决定）。`can_use_tool` 的调用链按 0.2.162 源码（`query.py` 第 577–640 行、`types.py` `_configure_can_use_tool`）讲：设了它，SDK 会给 Claude Code 程序加启动参数 `--permission-prompt-tool stdio`；调用单前两步没结果时，Claude Code 程序通过输出口发来一条"can_use_tool"请求（工具名 + 参数 + 附加信息）；SDK 收到后调用检查函数，把返回的 Allow / Deny 转成回信发回；Allow 则执行，Deny 则把 `message` 放进出错的结果单交给模型
- 观察行位置（用户问）：`check_tool` 函数体第一行（`async def` 下面一行，缩进 4 格），在 `status = False` 之前
- 用户检查函数里我发现的问题（只给提示，等用户自查再批改）：① `endwith` 应为 `endswith`（运行会报错）；② 第二个 `if / else` 总会把 `status` 重新赋值，第一个 `if tool_name == "Write"` 的结果被覆盖——工具名不是 Write 但文件名以 .md 结尾也会被放行
- 查证（2026-10-06，0.2.162 源码）：`query()` 传字符串提示词 + `can_use_tool` 可用（`_internal/client.py` 第 182 行起：字符串提示词先 initialize，再写入用户消息，内部一律走流式）；`ToolPermissionContext` 字段：`signal`、`suggestions`、`tool_use_id`、`agent_id`、`blocked_path`、`decision_reason`、`title`、`display_name`、`description`；`PermissionResultAllow(updated_input, updated_permissions)`；`PermissionResultDeny(message, interrupt)`
- 第 2 次运行（2026-10-06，Claude Code 程序自动更新到 **2.1.288**，上次 2.1.286；行为与之前一致）：用户代码改对（`endswith`；两个状态变量 `tool_status` / `input_status` 双边判断；观察行在函数第一行）。输出顺序：init（Tools `['Write']`，权限模式打印已删）→ 调用单（Write，`notes.txt`，`hello`）→ `[check] asked about: Write {...}` → 结果单 `is_error: True`、`content: Only .md file permitted` → 模型回答“系统只允许写 .md，要不要改成 notes.md” → `ResultMessage` success、`num_turns` 2、约 6.1 秒、$0.0062。`notes.txt` 没出现。另有一行 “⚠ claude.ai connectors are disabled because ANTHROPIC_API_KEY ...” 是 Claude Code 程序打印的提示（设了 API 密钥所以没加载 claude.ai 连接器），与本知识点无关
- 预测对照（用户预测）：① 被问 1 次、写 notes.txt——对；② “会报错，内容是写了其它格式的文件”——报错对（`is_error` True），内容表述大意对（实际就是我们写的 `message` 原文）；③ 没出现文件——对，`num_turns` 不清楚（实际 2）。用户评语“基本如我所料”
- 新发现：① 检查函数被问的时刻在调用单出现之后、结果单出现之前；② `PermissionResultDeny.message` 原文成了结果单的 `content`，模型读到了；③ 模型没有自己改成 notes.md 重试，而是问用户——重不重试是模型自己的决定，所以理由要写得模型能据此行动；④ 检查函数在 Python 程序里跑，不是模型调用，不增加 `num_turns`（仍是 2：开单一次、看结果后回答一次）
- 代码批改（第 2 次）：通过。小问题（非阻塞）：第 9 行注释 `# customized tool` 仍把检查函数当成工具；第 33 行注释还是疑问句；函数名 `check_tool` 仍带 tool（用户未采纳改名建议）
- 用户对结构方案的回答（2026-10-06）：“现在最方便、日后最容易做多文件架构的那个”——没选字母，下一条请他在 A / B / C 里选（A 现在最省事、B 现在花一点力气把检查函数挪出去，日后最顺）
- 用户选结构方案（2026-10-07）：**A，暂不拆**，理由：“主要我担心目前还无法评判如何架构”。**知识点 4 开场要重新提这件事**（那时有两层 agent，再给方案）。`project_tree.md` 不用改
- 第 3 次运行（2026-10-07，提示词换成 notes.md，代码不改，CLI 2.1.288）：输出——调用单（Write，`notes.md`，`hello`）→ `[check] asked about: Write {...}` → 结果单 `is_error: None`、`content: File created successfully at: ...notes.md (file state is current in your context — no need to Read it back)` → 模型回答“我创建了 notes.md，内容是 hello” → `ResultMessage` success、`num_turns` 2、约 3.9 秒、$0.0050。文件出现
- 预测对照：检查函数被问 1 次、可以执行——对；出现 notes.md、内容 hello——对（用户输出里没打印文件内容，看到的是 Write 工具回的“创建成功”）；`is_error` = None、`num_turns` = 2——对。用户评语“正确”。四条全对，其中 `is_error` 为 None（知识点 2 的坑之一）这次是预测对的
- 新发现：① 检查函数在“允许”分支也被问了，顺序同拒绝分支（调用单 → 被问 → 结果单）；② 返回 `PermissionResultAllow()` 后 Write 照常执行，结果单里是 Write 工具自己写的成功说明（不是我们写的），`is_error` 为 None；③ 同一份代码、同一个函数，只是提示词里文件名不同，就走了两条分支——规则按调用单的参数判断，不按提示词
- 第 4 次运行大纲（2026-10-07）：核心 ①——`tools=[]`；核心 ②——`allowed_tools=["Write"]`（三步检查的第 2 步“可以执行”规则）；其余不动，检查函数和观察行保留；预告：设了整工具的 `allowed_tools` 又设 `can_use_tool`，SDK 会发 `CanUseToolShadowedWarning`（0.2.162 `types.py` 第 1863–1923 行：因为命中规则就不会再问检查函数），属预期，印证第 2 步在第 3 步之前。预测三问：init 的 `Tools` 显示什么；模型会不会开 Write 调用单；`notes.md` 会不会出现、模型会说什么。运行前必须确认 `notes.md` 已删
- 第 4 次运行（2026-10-07，`tools=[]` + `allowed_tools=["Write"]` + `can_use_tool` 保留，提示词 notes.md，CLI 2.1.288）：输出——终端先出现 `CanUseToolShadowedWarning`（与预告一致，指向 `types.py` 第 1948 行）→ init `Tools: []` → 模型只回文字：说要创建文件，贴了一段 PowerShell 代码块，然后说 “Done! I created a file named notes.md ...” → **没有调用单、没有 `[check]` 行、没有结果单** → `ResultMessage` success、`num_turns` **1**、约 2.6 秒、$0.0022。`notes.md` **没有出现**。用户已先确认 `notes.md` 被删、其余代码无问题
- 预测对照：用户预测“此次运行会报错，因为根本没有指定可用工具（底层），所以 agent 不知道该用什么”。“agent 不知道该用什么”——对（init 的 `Tools: []`）；“会报错”——**没对上**：没有报错，`success`，模型照常回答。用户读结果时自己发现了关键：“它显示说创建了文档，但根本没有任何新文档出现”
- 结论：问题 ③ 答案——**规则写了“可以执行”、工具却不在清单上，模型不能用**：开不出调用单，规则和检查函数从头到尾没被用上；清单和规则互相独立。新发现：**模型会在没有工具时用文字假装做完**（贴代码块并说 “Done”）——所以判断任务有没有做成，不能看模型说了什么，也不能只看 `ResultMessage` 的 `success`，要看有没有调用单 + 结果单（`is_error` 不是 True），或直接看文件
- 用户提问（2026-10-07）：“请解释 tools、allowed_tools、can_use_tool 三个参数的区别，一直搞不懂”。回答：`tools` = 工具清单（给模型看，开单之前）；`allowed_tools` = “可以执行”的规则（Claude Code 程序用，调用单开出后第 2 步，命中直接执行）；`can_use_tool` = 检查函数（Python 程序里，第 3 步，前面都没结果才问）；强调 `allowed_tools` 不是“允许模型用的工具清单”，名字里的 tool 是 SDK 起的，容易和 `tools` 混。顺带一句 `disallowed_tools` 是“不准执行”的规则，知识点 10 再讲（文档：只写工具名的禁用条目会直接把工具从模型的清单里拿掉，带参数样式的才在第 1 步拦截——知识点 10 开讲前再核对）。四次运行对照表：第 1 次只有清单；第 2、3 次清单 + 检查函数；第 4 次清单为空 + 规则 + 检查函数
- 第 5 次运行大纲（2026-10-07）：核心 ①——`tools=[]` 改回 `tools=["Write"]`；其余不动（保留 `allowed_tools=["Write"]` 和 `can_use_tool`）；提示词用 notes.txt（检查函数会拒绝 .txt，规则会放行 Write，看谁说了算）。预测三问：`[check]` 那行会不会出现；`notes.txt` 会不会出现；结果单的 `is_error`。预期（未实测）：`[check]` 不出现、文件出现、`is_error` 为 None；警告会再出现一次

- 第 5 次运行（2026-10-07，`tools=["Write"]` + `allowed_tools=["Write"]` + `can_use_tool=check_tool`，提示词 notes.txt，CLI 2.1.288）：`[check]` 那行**没有出现**，`notes.txt` **出现了**，结果单 `is_error` 不是 True（写入成功）。检查函数本来会因为 `.txt` 拒绝，但从头到尾没被问到
- 预测对照（用户预测：① `[check]` 会出现；② `notes.txt` 不会出现；③ `is_error` 为 True）：三条**全部没对上**。三条错在同一个地方——默认“检查函数是最后一道关，所有调用单最后都要过它”。用户读完结果自己说明了原因：“allowed_tools 不管三七二十一直接让工具被调用，它的优先级大于 can_use_tool，所以工具被执行，文件也出现了”——结论对
- 我补的细节：① 准确说是“**整个工具名**写进 `allowed_tools`”才会把检查函数遮住；SDK 在启动时就发 `CanUseToolShadowedWarning` 提醒，但只警告、不拦；② 想让检查函数管 Write，就**不要**把 Write 写进 `allowed_tools`；③ 这是最危险的一类错：检查函数看起来写好了、运行也成功，但安全检查实际上从没执行——所以要靠运行时的观察（那行 `[check]`）或结果验证；④ 带范围的写法（例如只允许某个目录下的写入）会不会遮住检查函数——**未实测**，知识点 10 再看
- 对照 demo（2026-10-07，`example_program/research_agent/agent.py`）：
  1. demo 的主 agent 设了 `permission_mode="bypassPermissions"` + `allowed_tools=["Task"]`，**没有**检查函数；按我们学到的顺序，“不准执行”的规则仍排第一，通过之后权限模式这一步把剩下的全部放行。所以 `allowed_tools=["Task"]` 在这里起什么额外作用——**未查证作者意图**（可能只是写明意图）。现在派单工具叫 `Agent`，demo 里的 `Task` 是旧名，知识点 4 再看
  2. demo 主 agent 没设 `tools`，所以工具清单是默认整套（第一道关基本没收窄）；它把约束放在两处：prompt 里的话，以及**每个子 agent 自己的 `tools=[...]`**——子 agent 的清单才是真正的第一道关。这正是知识点 10“按角色强制分工”要做的事
  3. 我们现在的写法（default 模式 + 检查函数，每张单都问 Python 程序）和 demo 的写法（全放行、靠清单收窄）是两种取向：前者每次执行前把关，后者事先把能用的工具缩到最小
- 代码级查证记录补充（2026-10-07 · SDK 0.2.162 · 命令行程序 2.1.288）：`can_use_tool` 与整工具的 `allowed_tools` 同时出现会发 `CanUseToolShadowedWarning`（0.2.162 `types.py` 第 1948 行附近），第 5 次运行实测确认“规则先于检查函数”；带范围的规则会不会遮住检查函数——**未实测**
- 必须记住的 5 件事（只含核心代码内容）：
  1. `tools=[...]` 是工具清单：决定模型能对哪些工具开调用单；`allowed_tools` 不是“模型能用的工具清单”，它是第 2 步的“可以执行”规则；清单上没有的工具，写了“可以执行”规则模型也用不了（→ `review.md` Q11、Q12）
  2. 调用单开出后执行前的检查顺序：“不准执行”规则 → 权限模式 → “可以执行”规则 → 检查函数，哪步有答案就停；一路都没人回答时不执行，结果单 `is_error=True`，这次运行本身仍是 `success`，模型自己决定下一步（→ Q13）
  3. 整个工具名写进 `allowed_tools` 会让 `can_use_tool` 永远不被问：SDK 只警告不拦；想让检查函数管某个工具，就别把它写进 `allowed_tools`（→ Q14）
  4. 检查函数：`async def f(tool_name, input_data, context)`；返回 `PermissionResultAllow()` 执行，或 `PermissionResultDeny(message=...)` 不执行，`message` 会原样变成结果单内容被模型读到；它跑在 Python 程序里；交给 SDK 时写 `can_use_tool=f`，函数名后面不加括号（→ Q15）
  5. 模型没有工具时可能用文字假装做完；`ResultMessage` 的 `success` 和模型说的话都不能证明任务做成，要看调用单 + 结果单（`is_error` 不是 True），或直接看文件（→ Q16）
- 卡住升级次数：1（提示 1：检查函数里 `endwith` 拼写和覆盖逻辑，只给提示、用户自查改对 / 部分代码 0 / 相似例子 0）→ 保持 L2，升 L3 计数 0/2
- 结果（基于真实运行）：5 次运行、开场定的三个问题全部有答案（① 默认模式是 `default`；② 没规则没检查函数时不执行、结果单报错、不崩溃不卡住；③ 清单和规则互相独立，清单上没有就用不了；外加第 5 次：规则先于检查函数）。用户每次运行前都交了预测：第 1 次错 1 条、第 2 次大意对、第 3 次全对、第 4 次错 1 条、第 5 次全错——每次出错都集中在“把清单、规则、检查函数当成同一道关”，这是本知识点最大的收获
- 遗留问题：① `disallowed_tools`——文档说只写工具名的条目会把工具从模型清单里直接拿掉，带参数样式的才在检查第 1 步拦截，知识点 10 开讲前核对；② 带范围的 `allowed_tools` 写法是否遮住检查函数——未实测；③ `main.py` 怎么拆——用户选暂不拆，**知识点 4 开场重新提**；④ `acceptEdits` / `plan` / `dontAsk` / `auto` / `bypassPermissions` 这次只讲了 default，其余模式没实测；⑤ 复习欠账：Q10（只答出 1/3）、Q11（等级 1）；⑥ 函数名 `check_tool` 仍带 tool，容易和“工具”混
- 代码清理（2026-10-07 已完成，读回确认）：`[check]` 观察打印、`allowed_tools=["Write"]`、`notes.txt` 都已删；第 8 行注释改成 `# check tool called function`；函数名 `check_tool` 仍带 tool（用户未采纳改名建议，非阻塞）。`main.py` 当前 `tools=["Write"]` + `can_use_tool` + `permission_mode="default"`
- 收尾复述（2026-10-07）：用户复述 `tools` / `allowed_tools` / `can_use_tool` 各管哪一道关，大意对，记 `review.md` Q12 = 2（缺：“不准执行”规则仍排在 allowed 前面；检查函数只在前几步都没答案时才被问）
- 教学自查（对照 skill，引用事实）：
  1. 1.1 / 第 11 节（L2 先判断路径）：用户回“不是到底判断啥？我连知识点 3 要讲什么都不清楚”——我只给了标题就让他判断；之后先说问题再判断（`issue.md` 第 7 条）
  2. 第 7、8 节（词要一致、一次讲一件事）：用户回“讲的太复杂了，词语用的极其不恰当，我分不清具体机制”——一条回复塞了工具清单、四步检查、5 种模式、规则写法、hook，同一概念换了好几个词；之后只讲两件事、固定用词（`issue.md` 第 8 条）
  3. 1.2（运行计划）：用户回“这是什么意思？为什么又输出这种让人看不明白的东西”——4 次运行压成表格、没说为什么跑 4 次（`issue.md` 第 9 条）
  4. 支撑代码不是黑箱：用户问“新增的类为什么不解释，你是打算直接让我当黑箱用吗”；函数名 `check_tool` 误导他把检查函数当成“自建工具”（`issue.md` 第 10 条）
  5. 架构：用户问“现在 main 文件正在急剧扩充，确定暂时不按照 skill 要求对代码进行架构吗”——我从知识点 1 起没提过文件结构（`issue.md` 第 11 条）
  6. 概念和代码名字没有对照：用户在第 4 次运行时才问“tools、allowed_tools、can_use_tool 的区别，一直搞不懂”——前 3 次运行都是在没分清时做的（`issue.md` 第 12 条）
  7. 做得对的一点：第 5 次运行是用户的三条预测全错，我没有直接给答案，而是让他先自己读结果——他自己说出了“优先级”这个关键词，我只补细节
  - 其余检查项（首行标注、要用户做的事放最前面、运行后先对照预测、没替用户写核心代码、查证标日期和版本）：无违规

---

## 阶段 1 测验（✅ 2026-10-07 通过）

- 第一轮（2026-10-07，6 道选择题，选项等长，题目取自真实运行）：**4/6**。第 1 题（空清单，模型文字假装做完）选 B 对；第 2 题（只有清单、没规则没检查函数，Python 看到什么）选 D 错，正确 C——他的理由“没有限制就代表 agent 默认直接调用”和他自己第 1 次运行后写的“所以它需要我的同意才行”相反；第 3 题（规则盖过检查函数）选 D 对；第 4 题（靠 `tool_use_id` 对上）选项 A 对、理由“子进程会有唯一 id”不准（id 属于每张调用单）；第 5 题（`is_error == False` 判成功）选 A 错，正确 C，他自己写“没太读懂题”，是猜的；第 6 题（研究员不该写文件→清单里不放 Write）选 B 对，理由清楚
- 暴露的缺口：① 把“没设限制”当成“默认放行”（`review.md` Q13 → 0）；② `is_error` 为 `None` 这个坑第二次没答出（Q10 → 1）；③ 不确定时凭感觉选，没读懂题就不该猜，应该问
- 复测（2026-10-07，给提示后）：A“没有任何等待，agent 发现没有权限就跑完就停，文件没写”——过关（起初想成“等我批准”）；B“True 算真，None 算假”——过关。Q13、Q10 都记 1 级（提示后答对）
- 阶段 1 测验：✅ 通过（第一轮 4/6 + 复测过关）。下一步：迁移任务（L3，用户先写大纲，不写代码），见下一节

## 阶段 1 迁移任务（🟨 进行中，2026-10-07 起）

- 支持级别：比知识点 3 高一级（按 L3 的做法）：**用户自己写大纲（不写代码）**，我检查、只指出缺口；大纲通过后用户写代码
- 任务（已发给用户）：“文件整理员”agent——读 `notes/` 文件夹里的 .txt，把总结写进 `output/summary.md`。规则：读文件不用问；写文件只准写 `output/` 下的 .md；绝不允许执行命令。大纲要回答：① 清单放哪些工具；② `allowed_tools` 放什么、为什么；③ 检查函数判断什么、返回什么；④ 怎么证明检查函数真的被问到了（第 5 次运行的教训）；⑤ 至少 3 次运行各想看到什么、先预测什么
- 说明：第 ② 问可能没有标准的“放一样”答案，关键是理由；已验证的事实（可用于批改，不要先说）：知识点 2 里 `tools=["Read"]` + 默认模式 + 工作目录内读文件，不设任何规则也能读成功
- 用户大纲第 1 版（2026-10-13，隔了 6 天才回；他说“第 5 次运行我有点搞忘了”）：① 清单放读、写两个工具；② `allowed_tools` 放 Read 不放 Write（理由：读不改文件，写要先确认位置和目标）；③ 检查函数判断 Write 是否作用在 `output/` 下的 .md，是则允许、否则拒绝；④ 必须有 `can_use_tool`，函数里加输出，第 5 次运行忘了；⑤ 三次运行：普通跑 / 错误写入地址 / “给它无效的信息，判断它能否主动推论出信息问题”
- 批改要点（只给缺口，不给答案）：第 1–3 问方向对，选择“不放 Write”正确，但理由写的是“需要确认”，不是“放了会遮住检查函数”（第 4 问的答案和它是同一件事）；缺：权限模式没提（检查顺序第 2 步）；`allowed_tools=["Read"]` 是整工具规则，读的范围超出 `notes/`；检查函数没说拒绝时的 `message` 和怎么判断“在 output/ 下”；第 5 问太笼统，第 3 次测的是模型聪明与否而不是我们设的两道关，没有预测，“绝不执行命令”没有对应的运行（第 4 次运行的另一个发现）
- 复习信号：隔 6 天后忘了第 5 次运行的细节，但设计上没把 Write 放进 `allowed_tools`，说明结论还在、过程忘了；Q14 保持 2 级，下次间隔复习优先考
- 用户大纲第 2 版（2026-10-13）：① 放了 Write 检查函数不会生效；第 4 问答“检查函数的目标是否在 allowed_tools 里”（是看配置，不是靠运行证明）；② 能读 notes/ 以外的文件，不想让它读，理由只想到“耗费更多费用”（没想到项目里有 `.env`）；③ “它”指什么看不懂——我的措辞问题，“它”指权限模式，没写清；④ 拒绝时告诉错误原因和正确路径；`file_path` 长什么样忘了，并明确说“我不会去查阅之前的遗留信息”；判断在 output/ 下“通过 python 函数”；⑤ “抱歉，我实在忘记测试的原则是什么了”
- 本次处理：把测试原则按他现有的话重述（每条规则一次该成功的、一次该被拒绝的；每次只测一件事；运行前写预测）；告知 `file_path` 是带盘符的绝对路径（环境事实，不是答案）；第 3 问改写成“权限模式在检查顺序的第 2 步……”；第 2 问点出 `.env`。**卡住升级记 1 次（提示）→ 迁移任务算一次提示；知识点 3 的 1 次 + 迁移任务的提示都计入阶段 1，升 L3 计数仍 0/2**
- 观察：隔 6 天后，运行细节（第 5 次运行、`file_path` 样子、测试原则）都忘了；他不愿翻旧记录。建议以后每个阶段新对话开场的间隔复习，优先考“运行里亲眼看到的事实”，并在阶段 1 收尾时做一次整体回顾卡
- 用户大纲第 3 版（2026-10-13）：① 权限模式：放行了的单检查函数“不会”被问（对）；模式写“manual 之类需要人为介入”（不准：没有这个名字，我们用的是 `default`；`default` 不自动放行写文件，接着走规则和检查函数，不是“等人”）；② 读 `.env` 会泄露 api，所以检查函数也要管 Read（对，自己纠正了“没有安全隐患”）；说“需要新的检查函数”（不准：同一个检查函数收到所有被问到的工具，靠 `tool_name` 分支）；③ 判断 output/ 下需要绝对路径（对）；④ 打印在检查函数里，“任何情况都应该出现”（部分对：凡是被问到的工具都会出现；没出现就说明被盖过；Read 会不会被问到要实测）；⑤ “第 5 题我实在写不出来”
- 本次处理（卡住升级第 2 级：部分大纲）：给了第 5 问的运行清单格式和第一行样例（正常写 output/summary.md），其余 4 次（错位置、错类型、执行命令、读 `.env`）由用户填预测和理由。**卡住升级累计：迁移任务 2 次（提示 + 部分大纲）**
- 新增待验证疑问（我提出，不预先回答）：知识点 2 的文档说工作目录内读文件“由工具自己批准”，那么 Read 工作目录内的文件时，检查函数会不会被问到？`.env` 就在项目根目录。靠运行验证（放进运行清单第 5 次），结果决定“让检查函数管 Read”这个设计能不能成立
- 配置要求（等用户复述）：`allowed_tools` 里 Read 也不放（和 Write 同理，放了会遮住检查函数）
- 用户大纲第 4 版（2026-10-13）：配置——清单 Read、Write；`allowed_tools` 空；权限模式 `default`；检查函数管 Read 和 Write（对）。运行清单（他把我列表的第 2–5 行编成他的 1–4）：① 写到 `input/input.md`（预测 Write 被问 1 次、`is_error` True）；② 写 `output/summary.txt`（预测 Write 被问 1 次、文件不出现、True）；③ 读 `notes/a.xtx`（文件名拼错）总结写进 `output/summary.txt` 并且“强制执行”（预测 Write 被问 1 次、不出现、True；理由“检查代码部分是否稳定”）；④ 读 `.env`（预测 Read 被问 1 次、结果有问题、True；理由“Read 不应该读取指定位置之外的内容”）
- 批改要点：①② 对应规则、理由清楚，通过；③ 没有验证“绝不执行命令”（执行命令那一次被换成了重复的写错类型），还把文件名拼错、加“强制执行”，一次测了多件事，理由“检查代码是否稳定”太空；④ 目的对，但真读 `.env` 的话，如果检查函数没被问，**真实的 api key 会被模型读到并显示出来**——要改成读一个内容是假的诱饵文件；另外预测里没有算上读 `notes/a.txt` 本身那次 Read 会不会被问，也没考虑拒绝后模型可能重试（`message` 写得好，它会自己改成 .md）→ 这两点留到每次运行前的预测里处理
- 说明：“绝不执行命令”靠清单里没有 Bash（第一道关），不靠检查函数——已告知用户
- 用户大纲第 5 版（2026-10-13）：第 3 次（命令）预测——不会出现调用单，`[check]` 不会出现，模型会说不应该执行命令；怎么分辨真假“查过往记录”；第 4 次（读假文件）预测——`[check]` 不会出现（改了自己上一版的“被问 1 次”，没写理由，应该是听了“工作目录内读文件由工具自己批准”的提示）。用户问：“我把 check 理解成的是‘通过’的意思，不知道对不对”——**不对**，`[check]` 是检查函数第一行那句观察打印，意思是“检查函数被问到了”，不管后面允许还是拒绝；这是我命名不清的问题（沿用知识点 3 的打印文字，没在这次说明）
- 批改：大纲通过，进入写代码（L3：代码由用户写，我只在卡住时给提示）。待做：建 `notes/`、`output/`、`notes/a.txt`、`fake_secret.txt`；检查函数按 `tool_name` 分支管 Read（只准 `notes/` 下）和 Write（只准 `output/` 下的 .md），其余一律拒绝，拒绝时写清原因和正确路径；`tools=["Read","Write"]`、不设 `allowed_tools`、`permission_mode="default"`；检查函数第一行加 `[check]` 观察打印（用后删）；每次运行前用户先写预测（含 `[check]` 次数、文件、`is_error`）；样例运行（正常写 `output/summary.md`）也要预测，因为它决定 Read 会不会被问到
- 文件结构决定（2026-10-15）：用户提问“检查函数要不要整体转移到专门存放检查函数的空间，还是继续复用 `main.py`，几天前怎么计划的”。我复述：2026-10-07 选 A 暂不拆（理由“担心目前还无法评判如何架构”），约定知识点 4 开场重提；这次检查函数要变大（Read / Write 两支 + 绝对路径），再给 A / B / C 三个方案，我建议 C，用户**选 C**：先在 `main.py` 写完迁移任务并跑通，再单独做一步把检查函数挪到专门的文件，用同样的 5 次运行验证行为没变，然后进知识点 4。这改变了原计划（原计划是知识点 4 开场再提），已记；知识点 4 开场只需确认搬家结果，不必再选方案
- 用户的流程要求（2026-10-15）：运行不要合并预测，每次运行单独预测、单独发；阶段 1 结束后必须换新对话
- 代码第 1 版批改（2026-10-15，迁移任务）：用户写出 `check_Write`、`check_Read` 两个小函数 + 一个入口 `check_tool`（按 `tool_name` 分发）；`tools=["Read","Write"]`、不设 `allowed_tools`、`default`、`[check]` 打印在小函数里；用 `pathlib.Path(...).resolve()`（能处理 `..` 和斜杠写法，做得对）。入口函数 + 小函数的写法正是上一轮讨论的结构。已建 `notes/a.txt`、`fake_secret.txt`、`output/`；根目录有之前测试留下的 `test.md`（内容 hello）
- 发现的三处问题（只给位置和提示，让用户自己改）：① 第 21、39 行：`absolute_path` 已经是 `output/`（`notes/`）文件夹本身，却拿文件的 `parent.parent`（是项目根目录）去比，合法的写 / 读也会被拒绝；② 第 29、44 行：`PermissionResultDeny(f"...")` 位置参数，0.2.162 `types.py` 第 271–273 行字段顺序是 `behavior`、`message`、`interrupt`，所以字符串进了 `behavior`、`message` 为空（`_internal/query.py` 第 632 行发回的是 `response.message`）——不报错，但原因到不了模型；③ 第 49–55 行：工具名既不是 Write 也不是 Read 时 `permission` 没有赋值，会 `UnboundLocalError`，也不符合他自己大纲里的“其余一律拒绝”（清单只有两个工具，所以现在碰不到，但规则要写）
- 非阻塞：绝对路径是写死的（搬家那一步会遇到）；`.endswith(".md")` 区分大小写；`input_data['file_path']` 直接取键，缺键会 KeyError；`[check]` 打印没有工具名
- 代码第 2 版批改（2026-10-15，读回 `main.py` 核对，不只信“都改好了”）：① 路径比较（第 21、39 行）已改对，改成和 `absolute_path.resolve().parent` 比；② `PermissionResultDeny`（第 29、44 行）**还是位置参数**，他只改了文字（去掉绝对路径），没改写法——他的理解是“原因文字有问题”，不是“参数位置”；③ 入口函数加了 `if tool_name in ["Write","Read"]` 把变量未赋值的问题挡住，但其他工具时函数**返回 `None`**，SDK 要求返回 `PermissionResultAllow` / `PermissionResultDeny`（`_internal/query.py` 第 637 行会报错），仍没有“其余一律拒绝”。给了新提示：②让他打开自己装的 SDK 看 `PermissionResultDeny` 字段顺序；③问“其他工具时函数返回什么、SDK 要求返回什么”
- 用户说“绝对路径写死的问题我记着，希望之后靠架构思维改正”——对，搬家那一步（方案 C 第 ④ 步）要处理：路径从一处统一取得；届时他自己想方案
- 复盘提醒：他说“按我的理解改正了”，我没有直接信，读回代码后发现两处没真正改——批改前一律读回
- 代码第 3 版通过（2026-10-15，读回 `main.py` 核对，语法检查通过）：`PermissionResultDeny(message=...)` 两处已改成关键字参数；入口函数加了 `else` 分支返回 `PermissionResultDeny(message="'Write' and 'Read' tool allowed only")`，其他工具一律拒绝。用户共来回 3 次才改对（第 2 处最初只改了文字没改写法，我读回代码才发现）。非阻塞：入口里 `if tool_name in [...]` 里面又判断一次（可合并）；绝对路径写死；`[check]` 打印没有工具名；根目录有之前测试留下的 `test.md`
- 进入运行阶段：每次运行单独预测、单独发；固定提示词；运行前确认 `output/` 里没有上一次的结果。第 1 次（样例，应该成功）提示词：`Read notes/a.txt and write a one-sentence summary into output/summary.md.`；预测要答：`[check]` 出现几行、分别对应哪个工具和路径、`output/summary.md` 出不出现、每张结果单的 `is_error`、读 `notes/a.txt` 那一次检查函数到底被问没被问（附理由）
- 第 1 次运行（样例，2026-10-15，CLI 2.1.288，haiku）：输出——Read 调用单（`notes\a.txt`）→ 结果单 `is_error: None`，内容带行号 → Write 调用单（`output\summary.md`，一句话总结）→ **`[check]` 只出现 1 行，是 Write 的路径** → 结果单 `is_error: None`，文件创建成功 → 模型总结；`success`、`num_turns` 3、$0.0098。**Read 没有触发检查函数**
- 预测对照（用户预测：`[check]` 两行，Read 和 Write，路径是相对路径；两张结果单 `is_error` 都是 None；Read 会被问到，理由“调用了 read 工具，无 allowed_tools 约束”）：① Write 被问到——对；Read 被问到——**没对上**；“相对路径”——**没对上**（实际是带盘符的绝对路径，他前几天自己测到过）；② `is_error` 都是 None——对；③ Read 会被问——没对上，理由链是“没规则就一定问检查函数”，漏了检查顺序里前面的步骤已经有答案的情况。用户提问：“check 只出现了一行，只在 write 中出现了，我不明白为什么 read 不出现，明明调用了的”——把“调用（开出调用单）”和“被问（检查函数被问到）”混在一起
- 解释（2026-10-15）：开单 ≠ 被问；检查顺序里权限模式那一步，`default` 模式对读文件已经有答案（知识点 2 记录的文档说法：工作目录内读文件由工具自己批准、不需要规则），所以前面的步骤已放行，检查函数没被问——和知识点 3 第 5 次运行同一个模式（前面有答案就不再问）。**这是文档说法 + 本次观察一致，不是单独验证的机制**：第 5 次运行（读 `fake_secret.txt`，也在工作目录内）会再验证一次；工作目录之外的读会不会被问，**未测**
- 设计后果（待用户自己推出来）：`check_Read` 对项目内的文件读取可能根本不起作用，“只准读 notes/”实际没人保证——项目内的 `.env`、`main.py` 都读得到。等第 5 次运行后让他说清、再决定怎么办（比如不让模型看到整个项目、换工作目录、禁用规则等，知识点 10 才系统学）
- 第 2 次运行（写错位置，2026-10-15，CLI 2.1.288）：Read（`notes\a.txt`，`is_error` None，Read 仍没触发 `[check]`）→ Write（根目录 `wrong.md`）→ `[check]` 1 行 → 结果单 `is_error: True`，内容正是 `message` 原文 → **模型自己改成 `output\wrong.md` 重试** → `[check]` 第 2 行 → `is_error: None`，创建成功 → 模型最后说“创建在 output/wrong.md”；`success`、`num_turns` 4、$0.0140。根目录没有 `wrong.md`，`output/wrong.md` 有
- 预测对照（用户预测：`[check]` 出现一次、是 Write；根目录不会出现；Write 的 `is_error` 是 True；模型会报出错误原因）：① 一次——没对上，实际 Write 被问 2 次（拒绝后重试，我上一轮提醒过要考虑重试）；② 根目录不出现——对，但 `output/wrong.md` 出现了（模型重试的结果）；③ 第一张 Write 结果单 `is_error` True——对，第二张是 None；④ 模型报错误原因——没对上，模型没有向用户报错，而是照 `message` 里写的位置自己改了
- 用户的解读：“模型还是说任务执行成功，但其实并未出现该文件”——**读偏了**：模型最后一句说的是 `output/wrong.md`，那个文件真的存在；没有出现的是根目录那一个。模型没说谎，但没告诉用户“你要的位置被拦了，我改了位置”。应当用调用单 + 结果单（两次 Write：先 True 后 None）和实际文件夹来判断（知识点 3 必须记住的第 5 件事）。教训：拒绝时 `message` 写清楚正确路径，模型会自己改——这对完成任务是好事，但“被拒绝”不等于“任务失败”，结果文件的位置可能和用户要求的不一样
- 用户读 `output/` 后确认：`output/wrong.md` 存在，自述“没发现模型的自主性”（2026-10-15，第 2 次运行后）
- 第 3 次运行（执行命令，2026-10-15，CLI 2.1.288）：init `Tools: ['Read','Write']`；**没有任何调用单、没有 `[check]`**；模型直接说“I don't have a shell command tool available in my current function set”，并给了几条 PowerShell 命令让用户自己跑；`success`、`num_turns` 1、$0.0073。用户预测三条（没有调用单也没有 check；模型说“无法调用该命令”之类；看调用次数、check 等）全部对上
- 观察：这次模型诚实说没有工具，而知识点 3 第 4 次运行（`tools=[]`）它是用文字假装做完——所以“模型说不说实话”每次不保证，真正保证“不执行命令”的是清单里没有 Bash（第一道关），不是模型的表现；判断看 init 的 `Tools`、有没有调用单、`num_turns`
- 第 4 次运行准备：提示词 `Read fake_secret.txt in the project root folder and tell me what it says.`（读项目内、`notes/` 之外的假文件）；预测：`[check]` 出不出现；模型能不能说出文件内容；`is_error`；理由；之后让他回答“如果项目里读文件不被检查函数问到，‘只准读 notes/’现在是谁在保证”
- 第 4 次运行（读项目内 `fake_secret.txt`，2026-10-15，CLI 2.1.288）：init `Tools: ['Read','Write']`；Read 调用单（`...\\05_ResearchAgent\\fake_secret.txt`）→ **没有 `[check]`** → 结果单 `is_error: None`，内容带行号 → 模型说出内容；`success`、`num_turns` 2、$0.0064。检查函数没被问，读成功
- 预测对照（用户预测：`[check]` 会出现，“因为读的是错误地址的错误文件”；模型能说出内容，“并未限制它”；`is_error` True）：① 没对上；② 对（但和①自相矛盾：如果检查函数被问了，它会拒绝，模型就读不到）；③ 没对上。用户问：“我还是不明白，为什么是 none，为什么 check 不出现？”——他把“这是错误文件”当成了“检查函数一定会被问”，忘了检查函数只在前面步骤没答案时才被问；而读文件在项目内，前面的步骤已放行，所以 `None`（读成功）也很自然
- 证据：第 1、4 次运行，Read 读项目内文件（`notes/` 内和 `notes/` 外）两次都没触发检查函数。机制说法仍来自文档（工作目录内读文件由工具自己批准），**项目外读文件会不会被问：未测**
- 安全后果：这个配置下，模型读得到项目内**任何**文件，包括 `.env`；`check_Read` 对项目内读文件不起作用。怎么办涉及知识点 10 的“不准执行”规则，以及一个没测过的猜想（把 Claude Code 程序的工作目录限制在 `notes/`），不在这次告诉他答案
- 下一步：让用户用自己的话回答“`check_Read` 现在起不起作用、‘只准读 notes/’是谁在保证”，再决定是否加第 5 次运行（读项目外的假文件，验证 `check_Read` 在项目外读文件时是否被问）
- 用户回答（2026-10-15）：① `check_Read` “不起作用，但具体原因我还是不理解”（对，现象判对；原因要讲）；② “只准读 notes/ 是模型本身在做决定，而非检查函数”（对：没有任何程序在保证，只靠模型和提示词；这正是知识点 3 原理里“不能让模型自己审自己”的反例）
- 查证（2026-10-15，官方 [Configure permissions](https://code.claude.com/docs/en/agent-sdk/permissions) 的“How permissions are evaluated”、[Choose a permission mode](https://code.claude.com/docs/en/permission-modes)）：完整顺序是 hooks → 不准执行规则（deny）→ 要问的规则（ask，来自设置文件）→ 权限模式 → 可以执行规则（allow）→ 检查函数（canUseTool）。关键一句：“A call the tool approves on its own is resolved at this step too, with no rule needed: for example a file read inside your working directories”——**工具自己放行的调用（项目内读文件、只读命令）是在“可以执行规则”这一步放行的**，不是权限模式那一步。`default` 模式表格写“Reads only”不用问。文档还写：要对**每一次**工具调用都做检查，用 `PreToolUse` hook（最先执行）；带范围的拒绝规则 `Read(...)`（`disallowed_tools`）在第 2 步，任何模式都拦；这两样分别是知识点 9、10 的内容
- **我的更正（教学自查）**：第 1 次运行批改时我说“检查顺序里权限模式那一步，默认模式对读文件好像已经有答案”——步骤归错了：应该是“可以执行规则”这一步里“工具自己放行”。结论（检查函数没被问）不变，但归因不准。已向用户更正
- 设计后果的出路（只给方向，不预先实现）：要真正把读限制在 `notes/`，需要 hook（知识点 9）或带范围的拒绝规则（知识点 10）；把 `cwd` 限制在 `notes/` 理论上也会让项目根目录在工作目录之外，读它会被问到——**这条没测过**。迁移任务到此接受“项目内读不受检查函数控制”这一发现，写进学习日志和 `review.md`，知识点 9、10 开讲时回收
- 剩余运行：用户原大纲里的“写错类型”还没跑——第 5 次运行：`Read notes/a.txt and write a one-sentence summary into output/summary.txt.`（预期检查函数被问 Write；拒绝后模型可能按 `message` 改成 .md 重试）。是否再加“读项目外假文件”这次，等用户决定（可选）
- 第 5 次运行（写错类型，2026-10-15，CLI 2.1.288）：Read（`notes\\a.txt`，无 `[check]`）→ Write（`output\\summary.txt`）→ `[check]` → 结果单 `is_error: True`，内容是 `message` 原文 → 模型自己改成 `output\\summary.md` 重试 → `[check]` → `is_error: None` 成功 → 模型最后**明确告诉用户**“改成了 .md，因为系统只允许 .md”；`success`、`num_turns` 4、$0.0144。用户预测三条（检查函数 2 次用在 Write；模型会说是文件格式问题；output 里可能变成 .md，取决于模型是否转弯）全部对上，并自己总结“模型发现必须是 .md，于是重新做了一次”
- 对比：第 2 次运行模型改了位置却没告诉用户，第 5 次它说明了——模型是否告知每次不保证，所以仍要看调用单、结果单和文件夹
- 迁移任务总结（2026-10-15）：5 次运行：样例成功；写错位置被拒后模型自行改正；执行命令——清单里没有 Bash，没有调用单，模型说没有该工具；读项目内假文件——检查函数没被问到、读成功；写错类型被拒后模型自行改成 .md。所有设计目标除“只准读 notes/”外都达到；“只准读 notes/”在项目内不受检查函数控制，是本次最大的发现
- 迁移任务必须记住的 5 件事（→ `review.md` Q17–Q20，另有 Q11、Q16）：① 检查函数只在前面都没答案时才被问；工具自己放行的调用（读项目内文件）不会被问，所以 `check_Read` 对项目内读无效，要限制读需 hook（知识点 9）或带范围拒绝规则（知识点 10）（Q17）；② 检查函数必须返回允许或拒绝，不能返回 `None`；拒绝要写 `message=`；不认识的工具一律拒绝（Q18）；③ 被拒绝后模型可能自己改正重试，检查函数会被问不止一次，文件可能落在和要求不同的位置，要看调用单、结果单和文件夹（Q19）；④ `file_path` 是模型写的绝对路径，比较前用 `resolve()` 统一，打印字典的双反斜杠只是显示（Q20）；⑤ “不执行命令”靠清单里没有 Bash，不靠模型自觉（Q11、Q16）
- 卡住升级（迁移任务）：提示 3 次（路径比较 / `message=` / 返回 `None`；另有 `file_path`、`.env` 假文件等信息提示）、部分大纲 1 次（第 5 问运行清单）、相似例子 0。升 L3 的计数不变（0/2）。迁移任务的做法（大纲用户写、我只指出缺口）在 L3 下基本可行，但大纲第 3–4 版仍需较多提示
- 教学自查（迁移任务，引用事实）：
  1. 我在批改第 1 次运行时说“检查顺序里权限模式那一步，默认模式对读文件好像已经有答案”——归错步骤，查官方文档后更正（`issue.md` 第 13 条：原理阶段略去的“工具自己放行”正好成了迁移任务的预测陷阱）
  2. 用户隔 6 天回来说“第 5 次运行我有点搞忘了”“我不会去查阅之前的遗留信息”“我实在忘记测试的原则是什么了”——没有回顾卡（`issue.md` 第 14 条）
  3. 用户说“按我的理解改正了”，我没有直接信，读回代码后发现 `PermissionResultDeny` 位置参数和返回 `None` 两处并没有真改——批改前读回代码是对的
  4. 好的一点：第 4 次运行用假文件而不是真 `.env`，避免了真实密钥被读出
  - 其余检查项（首行标注、要用户做的事放最前面、先对照预测再讲结果、没替用户写核心代码、更正时说明原因、文档改后读回）：无违规
- “搬家”大纲第 1 版（2026-10-15）：① `main.py` 只留 SDK 主体结构，检查函数和小函数扔出去，路径单开文件，消息打印跟随检查函数和小函数；② 除路径外每个文件都用文件夹承接（防止以后出现更多相关文件），代价是路径计算花时间；③ 写死的绝对路径换成相对路径，以根目录为绝对父级。用户要求“作为专业程序员评判，最好上官方说明”
- 评判要点（已用官方文档核对，2026-10-15）：① 按职责拆分对；没说 `main.py` 里那段 40 多行的消息循环放哪；② “每个文件一个文件夹”过早：目录要 `__init__.py` 才是包（[Modules 教程 §6.4](https://docs.python.org/3/tutorial/modules.html)），真正的代价是 import 写法和 `__init__.py`，不是路径计算；先平铺，长大了再升级成包（常见做法：`__init__.py` 重新导出，import 写法不变）；脚本所在目录排在标准库前面（§6.1.2），本地文件名不要和标准库同名；PEP 8 推荐绝对导入，主模块必须用绝对导入；③ “相对路径以根目录为绝对父级”有概念问题：相对路径是相对**当前工作目录**，不是相对项目根（[pathlib](https://docs.python.org/3/library/pathlib.html)：`Path.cwd()`、`rename()` 里“relative to the current working directory”）；应该由放路径的那个文件自己的位置（`__file__`，[数据模型](https://docs.python.org/3/reference/datamodel.html)）算出根，此后一处取得；`.parent` 的层数取决于文件深度，所以放根目录最简单；依赖保持单向：`main → permissions → paths`
- 之后可改进（不属于“只搬家”）：`is_relative_to`（字符串比较、不处理 `..`，所以先 `resolve()`）可替代 `.parent.parent` 加 `.name`，并允许子文件夹；PEP 8：函数名小写加下划线（`check_Write` 应为 `check_write`），`absolute_path` 实际是文件夹，名字有误导
- “搬家”大纲第 2 版（2026-10-15）：① 消息循环留在 `main.py`（理由：属于 SDK 结构、内容不多；想做开关可以用函数包裹；单开文件要对比后才能得结论）——可接受，demo 的 `utils/message_handler.py` 是单开文件的先例，知识点 4 子 agent 消息进循环后再评估；函数包裹属于改行为，搬家后再做；② 文件清单：检查函数文件（含小函数）+ 路径文件；`main` 引用检查文件，`main` / 检查文件引用路径文件——对；**没起文件名，没说是否都放根目录平铺**；③ 根目录“以此次代码打开的文件夹来算”——**仍然是启动时的当前工作目录（cwd），不是文件自己的位置**，上一轮已指出这是错的锚点，他没改。下一步：让他起名 + 确认平铺，并用一个具体例子（从别的文件夹启动 `python AgentLearning\\05_ResearchAgent\\main.py`）让他自己看出 cwd 和文件位置不同
- 记在心里、等他理解锚点之后再提：`ClaudeAgentOptions` 的 `cwd` 参数（0.2.162 `subprocess_cli.py`：不传时 Claude Code 程序继承 Python 的当前目录）——用同一个 `ROOT` 既算路径又传给 `cwd`，两边才一致；这和“项目内读文件由工具自己放行”也相关
- “搬家”大纲第 3 版（2026-10-15）：① `main.py` 现在不需要路径文件，“有可能需要所以算进去”（评判：不用的引用等需要再加，避免未使用的 import）；② 路径锚点：“相对位置是以该文件所在位置进行计算”——**对**（改正了之前的 cwd 说法）；③ 具体问题答：“打开的文件夹是 agentlearning，不一样”——“不一样”对，但答的文件夹错：例子里终端先进到 `D:\\MyProjects`，当前工作目录是 `D:\\MyProjects`，不是 `AgentLearning`；④ **文件名、是否平铺仍没回答**（第二次没答）
- 本轮处理：告诉他正确答案（cwd = `D:\\MyProjects`）；让他起名 + 确认平铺 + 直接动手搬，名字和代码一起发；要求：只搬家不改行为，不改函数名和逻辑；搬完不要运行，先发我检查；路径文件放根目录；验证是从项目根目录重跑 5 次运行（`cwd` 参数、从别处启动的测试留到以后）
- 搬家代码第 1 版（2026-10-15 16:53，读回 `main.py` / `check_tools.py` / `path.py`，三个文件语法检查通过）：新文件名 `check_tools.py`（`check_Write`、`check_Read`、`check_tool`，从 `path` 引用 `notes_path`、`output_path`）和 `path.py`（两个路径，仍是写死的 `Path(r"D:\\MyProjects\\...")`），都平铺在根目录；`main.py` 只留 SDK 主流程，`from check_tools import check_tool`。逻辑、函数名、`[check]` 打印都没改（行为不变）。问题：① `path.py` 路径仍写死——这是搬家目标里的最后一项，没做，也没有根目录那一项；② `main.py` 第 7 行 `ToolPermissionContext, PermissionResultAllow, PermissionResultDeny` 已不再使用（未使用的 import）；③ 文件名 `path.py` 可以改成 `paths.py`（里面是多个路径；不是标准库名，无冲突，可选）
- 用户问：“你的题目要求是现在的 path 必须变成相对路径是吧？”——**不是**：我的要求是“路径只在一处取得、别处不写死”，做法是从路径文件自己的位置（`__file__`）算出项目根，再得到 `notes`、`output`，结果仍然是**绝对路径**；他把自己上一轮提的“相对路径”和我的要求混在一起。验证方法（留给他）：路径文件被直接运行时打印这几个路径，从项目根和从别的文件夹各运行一次，应该一样（[Modules 教程 §6.1.1](https://docs.python.org/3/tutorial/modules.html) 的 `__name__ == "__main__"` 写法）
- 路径文件改写（2026-10-15 17:00 起，L3 + 提示）：
  - 用户第 1 次：“很抱歉，我实在不知道如何做出项目根目录计算，你能提示一下吗”——这是卡住，给提示：`__file__`（文件自己的路径，是文字）、`Path(...)`（变路径对象）、`.resolve()`、`.parent`、用 `/` 或 `.joinpath` 接子文件夹；用不同例子（`C:\demo\app\tool.py`）示范思路；提出 3 个问题（`.parent` 要几级、根目录存变量、改完文件里不应再有 `D:\MyProjects`）。**卡住升级累计：迁移任务 3 次（提示 + 部分大纲 + 路径分步提示）**
  - 用户回答：“得到 05 文件夹，不需要再写 parent”（对）；“root 是 …\path.py”（把文件和文件夹说混，纠正：root 是文件夹）。第 2 版代码：`root = Path(__file__).resolve().parent` 对；`notes_path = Path(root + r"\notes")` 错：路径对象不能用 `+` 加文字（类型错误）
  - 第 3 版：`root + Path(r"\notes")`——路径对象加路径对象，仍然不行；用户没先写预测（提醒后补）。提前讲 Windows 坑：用 `/` 接以反斜杠开头的路径会丢掉 `root`（得 `D:\notes`）。用户预测“出错，因为 \ 让程序丢失了路径”——**混了两个问题**：`+` 报错 和 `/` 配开头反斜杠丢根，分开纠正
  - 第 4 版（读回）：`root / "notes"`、`root / "output"`，文件里再无 `D:\MyProjects`，语法通过
  - 自测：用户预测“一样的，因为无论在哪里打开，path 的父级永远是 05”（对；补充：靠的是文件自己的位置 `__file__`，不是终端所在文件夹）。结果：从 `D:\MyProjects\AgentLearning` 运行 `python 05_ResearchAgent\path.py` 和从 `05_ResearchAgent` 运行 `python path.py`，三个路径完全一样。末尾加了 `if __name__ == "__main__":` 打印。`main.py` 无用导入已删（读回确认）
- 搬家后回归（2026-10-15 17:34–17:37，都从项目根运行）：
  - 用户建议：“就再跑 1 到 2 遍就行了，没必要重新跑 5 遍。我们浪费太多时间在查问题上面了”——采纳。理由：搬家只改了“两个路径值从哪来”，判断逻辑没动，且两个值的打印结果和以前写死的完全一样；只需一次成功路径 + 一次会走到路径比较的失败路径。**有意跳过**：错文件类型、执行命令、读 `fake_secret.txt`（逻辑没改）。`check_Read` 里的 `notes_path` 没被实测用到（项目内读文件不经过检查函数，已知遗留）
  - 回归 1（成功）：`Read notes/a.txt` 并写 `output/summary.md`。预测：`[check]` 出现 1 次在 Write、文件在 output/、两个结果单都成功——全对。结果：Read 无 `[check]`（与搬家前一致）；Write 一次 `[check]`，`is_error=None`；3 轮，成本约 $0.0105
  - 回归 2（写错位置）：写 `wrong.md` 到项目根。预测：`[check]` 2 次（被拒后模型重做）、被拒那次 `is_error=True`、文件不在根目录而在 output/——全对。结果：第 1 次 Write 到根目录被拒（`is_error=True`，消息是 deny 里写的那句），模型自己改到 `output\wrong.md` 成功；4 轮，成本约 $0.0137。**用 `device_list_dir` 核对了实际文件夹**：根目录没有 `wrong.md`，`output/` 里有 `wrong.md`（80 字节），模型最后说的话与文件一致
  - 结论：搬家前后行为一致；路径来源已改成由 `path.py` 自己的位置算出，运行位置不影响结果
- 阶段 1 收尾（2026-10-15）：
  - 本次教学自查补充：① 用户觉得“浪费太多时间在查问题上”，我同意减少回归次数，并说明跳过了什么、为什么（没有悄悄跳过）；② 路径提示给了接子文件夹的符号写法（`某路径 / "data"`），属于卡住后的提示，没有替用户写出 `path.py` 的最终两行；③ 用户把两个报错原因混在一起（`+` 报错和 `/` 配反斜杠丢根），已分开纠正；④ 好的一点：用户的自测预测写了理由，且预测与结果一致；运行结果都用文件夹实际内容核对，而不是只看模型说的话
- 上传 GitHub（2026-10-15 17:41–18:01，用户有教学外的需求：“放进 GitHub，请教我一下”，L2 讲解、用户自己运行命令）：
  - 现状检查：仓库早就有（`main` 分支、2 个存档点），**没有远端**；`git ls-files` 只记录 4 个文件（`.gitignore`、`.vscode/settings.json`、`README.md`、`main.py`），`.env` 从未被记录过（上传前最重要的检查，通过）
  - `.gitignore` 最终 8 条：`example_program/`、`.env`、`issue.md`、`__pycache__/`、`test.md`、`fake_secret.txt`、`output/`、`notes/`。用户的判断：测试文件和程序输出不放进仓库，用 `.gitignore` 管；他对 `.gitignore` 的理解“能控制之后的所有变动”只对一半（只管还没被记录的文件，已记录的要另外处理）；`_learning/` 上传，仓库设公开，作者邮箱不介意公开
  - `notes/` 的取舍：我没替他定；他决定忽略，并写 `initialization.py`（`initialize_notes()`，`mkdir(parents=True, exist_ok=True)`，在 `main.py` 顶层调用）启动时自动创建。第 1 版有两个错：`from initialization` 没写完、`"notes" not in root`（路径对象不能这样问，且 `mkdir` 的 `exist_ok=True` 已含检查）；第 2 版读回通过（语法检查通过，**没有运行验证**）。遗留：`initialization.py` 里 `Path` 没用到、`root / "notes"` 应改用 `path.py` 的 `notes_path`、`initialize_notes()` 更适合放进 `main()` 开头；`Write` 是否自动创建 `output/` 没测过
  - 用户两次说“没太多时间”：一次“不预测了，直接改了”（接受，因为是读回确认的小改动，但提醒过没有运行验证）
  - 提交：`git add .` 后 `git status` 绿色栏正确（没有 `.env`、`notes/`、`output/` 等）；`git commit -m "The first status finish. Prepare second"` → `997f481`，9 个文件；说明太含糊，已告知可用 `git commit --amend -m` 在推送前改写，用户没改；笔误 `--online`（应为 `--oneline`）、`git remote add origin` 漏了地址，都没造成问题
  - 远端：`git remote add origin https://github.com/Andiey-126/ResearchAgent.git`，`git remote -v` 两行正确；`git push -u origin main` 成功（用户说“成功放进去了”，终端输出没有发给我）
  - 推送后学习文档又改了一次（加入 `initialization.py` 与 git 记录），**这部分改动还没提交 / 推送**

---

### 知识点 4 · 最小两层 + 上下文隔离（✅ 2026-10-18 完成；2026-10-17 开场）

- 开场：2026-10-17 发出（新对话）。先给了 5 行回顾卡（`issue.md` 第 14 条），再确认搬家结果
- 搬家结果确认（读回 4 个文件，2026-10-17）：`main.py` / `check_tools.py` / `path.py` / `initialization.py` 平铺在根目录；`path.py` 用 `Path(__file__).resolve().parent` 算 `root`，`notes_path` / `output_path` 从 `root` 接出；`main.py` 上次多余的三个 import 已删；`check_tools.py` 逻辑未变；`initialization.py` 仍用 `root / "notes"`（未改用 `notes_path`），`initialize_notes()` 已在 `main()` 第一行调用；`__pycache__` 里只有 `check_tools`、`path` 的缓存，没有 `initialization` 的——它从未被运行过
- 开场复盘：跨对话，读迁移任务的“教学自查”。违规 4 条：① 归错步骤（原话“检查顺序里权限模式那一步，默认模式对读文件好像已经有答案”）；② 隔 6 天回来没给回顾卡；③ 回归测试先定成“全部 5 次”（`issue.md` 第 15 条）；④ `__file__` 等没教过的小工具没在题面点名（`issue.md` 第 16 条）。其余无违规
- 间隔复习候选（逐题写出完整问题，用户挑 1–2）：Q11（1 级，10-02）、Q13（1 级，10-07）、Q10（1 级，10-07）、Q9（2 级，10-07，和本知识点直接相关）
- 支持级别：L2（知识点 3 用了 1 次卡住升级，升 L3 计数 0/2；迁移任务按 L3 单独算，不计入）
- 路径：计划表写“核心·可推理型”（L1 时定）；按 L2 先请用户判断。开场只说了本知识点要解决的问题，没说答案（`issue.md` 第 7 条）
- 代码分类：按 `issue.md` 第 6 条放到代码阶段开头再做
- 本知识点要回答的 3 个问题：① 主 agent 把活交出去、以及子 agent 自己干活时，Python 程序收到的消息分别是什么样、怎么认出是谁的；② 子 agent 能看到主 agent 这边的哪些内容（用实验回答）；③ 子 agent 开出的调用单还会不会问到我们的检查函数（官方文档没写明，**未查证**，实测）
- 完成标志：3 个问题都有运行结果为证；收尾能用自己的话说出子 agent 看到什么、交回什么、为什么这样设计
- 代码级查证（2026-10-17）：
  - 用户环境：SDK 0.2.162、命令行程序 2.1.288（**2026-10-17 用户确认**，与 10-07 相同）
  - 当时最新：SDK 0.2.168（PyPI，2026-10-15）；0.2.167 内置命令行程序 2.1.300。CHANGELOG 0.2.163–0.2.167 没有与子 agent、`AgentDefinition`、`parent_tool_use_id`、权限相关的改动（0.2.166 只是给 hook 和 init 消息补类型）
  - 0.2.162 源码 `types.py`：`AgentDefinition`（第 108 行）、`ClaudeAgentOptions.agents: dict[str, AgentDefinition] | None`（第 2291 行）、`UserMessage` / `AssistantMessage` 都有 `parent_tool_use_id: str | None = None`（第 1129、1144 行）、`TaskStartedMessage` / `TaskProgressMessage` / `TaskNotificationMessage` 都是 `SystemMessage` 的子类（第 1194、1211、1229 行）
  - 官方文档 Subagents 页（2026-10-17 读原文）：派单工具在调用单里叫 `Agent`、在 init 工具列表里叫 `Task`；子 agent 收到的 = 自己的系统 prompt + 派单那段话（+ 工具定义、项目 CLAUDE.md），收不到主 agent 的历史、工具结果和系统 prompt；只有最后一条消息回到主 agent；子 agent 默认后台运行。来源：https://code.claude.com/docs/en/agent-sdk/subagents
- 用户回复（2026-10-17 15:14）：
  - 回顾卡：没问题
  - 间隔复习：Q11 作答（2 级，"交给谁"没分开）；Q10 没作答，问"什么是结果单？指的是啥？"——固定词汇忘了（记 0 级）。我用回归 2 的真实例子讲了调用单 / 结果单，在本文件顶部加了"固定词汇表"（`issue.md` 第 17 条），请他可选再试 Q10
  - 安排：确认，无修改
  - 路径判断：用户"SDK 规定型。我认为多 agent 应该早就有官方写法了"。判定：结论不对，理由没对准标准（和知识点 3 开场同一类问题）——"有官方写法"每个知识点都成立（知识点 3 的 `can_use_tool` 也有官方写法，但"看得见 / 被批准"是他自己推出来的）；标准是"能不能从问题的限制推出做法"。本知识点的核心问题（子 agent 看到什么、交回什么、怎么交出去）能从限制推出 → 核心·可推理型；其中参数名（`agents`、`AgentDefinition` 等）是规定的，按 L2 在代码阶段直接给。规定型的例子：知识点 11 的环境变量名和默认值 3。等用户接受或反对
- 用户回复（2026-10-17 15:23）：
  - Q10 再试：答不出，"我感觉我根本就没思考过这个问题"（记 0；原因见 `issue.md` 第 18 条；代码阶段在真实数据里重学）
  - 路径：接受核心·可推理型。他的理解"有的已经规定了，但鉴于我们项目的特殊要求，有些需要推出来"——当场纠正一处：要推的部分不是因为项目特殊，任何多 agent 系统都有同样的限制；只有参数名是规定的。不再追问
- 原理第 1–3 步（2026-10-17，单独一条回复）：
  - 用到的前置概念先讲清：系统 prompt（一句话定义）、"每一轮把整份历史重发给模型"（Q7 曾漏答，用回归 2 的真实历史举例）
  - 限制条件（只讲事实）：① 模型不记事，每轮读整份历史；② 历史有长度上限，越长越贵越慢，无关内容多了容易抓不住重点（标明是经验规律）；③ 模型只会写文字和开调用单，想让事情发生只能经过 Claude Code 程序；④ 子 agent 也是一个模型，每轮只看到发给它的那份历史
  - 问题（场景：问"FastAPI 和 Flask 哪个更适合做小项目"，主 agent 派研究员查 FastAPI，研究员会读 10 个网页、开十几张调用单）：① 主 agent 的模型要让研究员开始干活，具体输出什么；② 研究员第一轮的历史里该有什么，主 agent 历史里的说明书 / 你的问题 / 拆分方案哪些给、哪些不给，各给理由；③ 研究员干完后主 agent 的历史里该多出什么，网页、调用单、结果单哪些进主 agent 的历史
- 第 2 步用户的尝试（2026-10-17 15:39）：
  1. "它会输出一个专门给研究员的命令，只告诉它此次任务的内容，其余一律不泄露"
  2. "全都不给：系统 prompt 指的是主 agent 的 prompt，跟研究员不搭；主 agent 应该拆分我的问题，把更精细的对于任务的要求给子 agent；拆分方案更不用说了，这是主 agent 负责的内容，不应泄露给子 agent"
  3. "应该多出研究员的结果，结果单"
- 第 4 步反馈（2026-10-17）：对的——① 专门给研究员、只含这次任务；② 主 agent 的系统 prompt 不给（理由"不搭"对准了事实 2）、拆分方案不给、给加工过的任务要求而不是原样转交；③ 结果以结果单回来（固定词汇用对了）。纠正一处说法："泄露"不对，这里不是保密问题，是长度 / 成本 / 抓重点。缺口（以问题形式留给用户补）：① "命令"是什么形式——用他自己第 3 题的"结果单总是对回某张调用单"反推；单上至少写哪两样；② 只说了不给什么，没说给什么：研究员自己的"你是谁、该怎么做"从哪来、谁什么时候写好；只收到"查 FastAPI 优缺点"、不知道"为了小项目、要和 Flask 比"时会查出什么，这个信息该由谁写在哪；③ 研究员的 10 个网页（约 3 万字）和十几张调用单 / 结果单进不进主 agent 的历史（用事实 2 说理由），"结果"具体是研究员说的哪一部分
- 用户补缺口（2026-10-17 15:57）：
  1. "dict 形式，有 id 和内容的形式。如果只是普通文字：那么脚本会读到；这个东西至少有 id 和命令内容"
  2. "研究员 system prompt 直接由我写好，在固定文件中保存，每次固定调用相同的（在创建它子 agent 的时候就能写了）；它查回来的东西就只有 FastAPI 的优缺点，没有任何比较参照物。这句话应该由主 agent 写进命令中"
  3. "3 万字会造成 agent 消耗增加，更慢、更贵，假如是多轮回 agent，则上下文会很快被占用……所以应该只放结果单或者结果之类的。研究员交给主 agent 的结果应该是最终结果，而非中间的内容，中间内容可以靠 python 代码代为输出，交给用户监控"
- 反馈：① 结论对（是一张调用单，带编号和参数）；普通文字只会被 Python 程序打印出来，没有任何 agent 会照着做——对；缺"派给谁"（编号是 Claude Code 程序自动带的，模型要写的是派给谁 + 任务那段话）。② 全对：研究员的系统 prompt 由他事先写好、启动时交出去；"为了小项目、和 Flask 比"由主 agent 写进任务那段话。③ 全对，并且自己提出"中间过程交给 Python 程序给人看"——这正是要验证的问题 ①
- 原理第 5–6 步（2026-10-17，同一条回复，不含代码、不出现代码名字）：
  - 第 5 步机制：① 工具清单里有一个专门的工具 Agent，主 agent 的模型对它开调用单，参数写"派给谁 + 任务那段话"；② Claude Code 程序执行这张单 = 新开一个子 agent，它第一轮的历史只有：子 agent 定义里的系统 prompt + 任务那段话（+ 它自己的工具清单），没有主 agent 的历史、结果单、系统 prompt；③ 子 agent 在 Claude Code 程序里跑自己的循环；④ 跑完后，只有它的最后一条消息变成主 agent 那张 Agent 调用单的结果单（编号对回），另附一行 agentId（以后续接用，这次不讲）；⑤ 子 agent 中间的消息 Python 程序也能收到，带"属于哪张 Agent 调用单"的标记，主 agent 的模型看不到。为什么别的不行：引用用户自己第 1–3 题的推理。和 Read 对比：同样是调用单 / 结果单，区别是执行的是一整个模型循环
  - 点名没讲但会影响预测的分支（`issue.md` 第 13 条的教训）：子 agent 默认在后台跑，模型需要结果时会自己选择等，消息顺序可能和场景不同，知识点 8 专门讲。另说明"这次不讲"：子 agent 工具清单的默认值、续接、层数上限
  - 第 6 步场景：FastAPI 问题，从主 agent 开 Agent 调用单到结果单回来，逐步说明谁做什么、每一步 Python 程序看到什么
- 用户（2026-10-17 16:14）："读懂了"，没有提问
- 第 7 步收尾复述（2026-10-17）：请他不看前文、用自己的话说 4 点：① 主 agent 怎么把活交出去（是什么、上面写什么）；② 子 agent 第一轮看到什么、看不到什么、为什么这样设计；③ 子 agent 交回什么、怎么回到主 agent；④ Python 程序看到什么、怎么分辨一条消息是主 agent 的还是子 agent 的
- 收尾复述（2026-10-17 16:17）：① "交的是执行单，里面有子 agent 的名称和任务要求，是一个 dict"；② "能看到 system prompt 和任务要求、工具，其余的例如用户提示词、主 agent system prompt 一律看不到，这样防止子 agent 角色混淆以及额外支出"；③ "交回来的是结果单，有 id 和最终结果，通过任务 id 进行比对交回方式"；④ "通过不同编号或者状态（不太知道如何表达）"
- 判定：**过关**。①②③ 机制正确（"执行单"应为"调用单"，"任务 id"应为"Agent 调用单的编号"，当场纠正）；④ 不完整但不是误解——当场补全（Python 程序也能收到子 agent 的中间消息；标记里装 Agent 调用单的编号，主 agent 的消息标记为空），代码阶段运行前的预测会再测。记 `review.md` Q22 = 3、Q23 = 2
- 原理阶段卡住升级：0 次
- 代码阶段·第 1 步：概念 ↔ 代码名字（2026-10-17，按 `issue.md` 第 12 条；用户要求不用表格，逐条写）：
  - 子 agent 定义 → `AgentDefinition`（新类）：本次用 `description`（一句介绍，主 agent 靠它挑人，细讲在知识点 5）、`prompt`（子 agent 自己的系统 prompt）、`tools`（子 agent 自己的工具清单）、`model`（可选）
  - 交出子 agent 定义 → `ClaudeAgentOptions(agents={名字: AgentDefinition(...)})`；字典的键就是调用单上"派给谁"写的名字
  - 主 agent 能派活 → 主 agent 的 `tools` 里加 `"Agent"`；init 的工具列表里显示为 `Task`
  - Agent 调用单 → `ToolUseBlock`，`name == "Agent"`，`input["subagent_type"]` = 派给谁，`input["prompt"]` = 任务那段话（其他字段看运行打印）
  - 结果单 → `ToolResultBlock`，`tool_use_id` = Agent 调用单的 `id`，`content` = 子 agent 最后一条消息 + `agentId` 一行
  - 标记 → `parent_tool_use_id`（`AssistantMessage`、`UserMessage` 都有）：主 agent 的消息为 `None`，子 agent 的消息 = Agent 调用单的 `id`
  - 点出 3 个易混点请用户回答：① `AgentDefinition` 的 `prompt` 和调用单 `input["prompt"]` 的区别（谁写、何时写、给谁看）；② `parent_tool_use_id` 是 `None` 和不是 `None` 各说明什么；③ 主 agent 的 `tools` 和 `AgentDefinition` 的 `tools` 各管谁
- 代码级查证补充（2026-10-17 · SDK 0.2.162 · 命令行程序 2.1.288）：
  - 0.2.162 `types.py`：`AgentDefinition` 字段 `description`、`prompt`、`tools`、`disallowedTools`、`model`、`skills`、`memory`、`mcpServers`、`initialPrompt`、`maxTurns`、`background`、`effort`、`permissionMode`（第 108–126 行）；`ClaudeAgentOptions.tools` 是"可用内置工具的基础集合"
  - Tools reference（2026-10-17 读原文）：`Agent` 的 "Permission required" 为 No；"Launching the subagent doesn't itself prompt for permission. Claude Code checks the subagent's own tool calls against your permission rules as it runs"；`Read` 为 No、`Write` 为 Yes。来源：https://code.claude.com/docs/en/tools-reference
  - Permissions（2026-10-17 读原文）：`Agent` 属于"don't ask before running"的工具；子 agent 继承主会话的权限模式。来源：https://code.claude.com/docs/en/agent-sdk/permissions
  - **未查证**：`tools` 参数里写 `"Agent"` 还是 `"Task"`（按工具参考写 `"Agent"`，运行时看 init 列表核对）；Agent 调用单 `input` 里除 `subagent_type`、`prompt` 外的字段；子 agent 的 Write 调用单是否落到 `can_use_tool`（文档只说"按权限规则检查"）
- 用户回答 3 个易混点（2026-10-17 17:27）：① "AgentDefinition 的 prompt 是 subagent 的 system prompt，而 input 的则是任务内容"；② "如果是 None，说明这是 main agent 的信息，如果有编号，则说明这是 subagent 的信息"；③ "AgentDefinition 的 tools 管的是这个子 agent 使用的工具，而主 agent 的 tools 管的是主 agent 以及 subagent 是否能调用（将 subagent 也看成工具）"
- 判定：① 对，补"谁写、何时写"（系统 prompt：你在运行前写；任务那段话：主 agent 的模型在运行中写；两样都给子 agent 的模型看）；② 对；③ 前半对，后半纠正：工具是 Agent，不是子 agent 本身；主 agent 的 `tools` 里有没有 `"Agent"` 决定主 agent 能不能开 Agent 调用单；子 agent 能不能拿到主 agent 清单之外的工具——**未查证**（`tools` 是会话的"可用内置工具基础集合"，是否同时限制子 agent 没找到原文）
- 词汇表加 3 条：Agent 调用单、子 agent 定义、标记
- 代码分类请求（2026-10-17，L2 由用户先分）：列出 7 块——① import 加 `AgentDefinition`；② 写研究员的子 agent 定义；③ `ClaudeAgentOptions` 加 `agents` 并在主 agent 的 `tools` 里加 `"Agent"`；④ 消息循环遇到 Agent 调用单时打印派给谁和任务那段话；⑤ 每条 `AssistantMessage` / `UserMessage` 打印 `parent_tool_use_id`；⑥ Agent 调用单的结果单打印完整内容（现在截到 200 字）；⑦ 检查函数里已有的 `[check]` 打印（用来看子 agent 的 Write 会不会问到检查函数）
- 用户代码分类（2026-10-18 11:36，隔天回来，没附理由，漏第 7 块）：1 支撑、2 核心、3 观察、4 观察、5 观察、6 观察
- 批改：1、2、6 对；**3 错**→核心（不是临时的，验证完不会删；没有它主 agent 派不了活、研究员定义到不了 Claude Code 程序；判断观察代码就问"验证完会删吗"）；4 接受，但这是**我的失误**——现有代码已经打印每张调用单的 `name` 和 `input`，Agent 调用单会自动打出来，第 4 块不用新写，删掉；5 接受为观察，但判断条件（`parent_tool_use_id` 是否为 None）是本知识点要记住的机制，由用户自己写；7 漏了→观察（已存在，复用到问题 ③ 有答案为止）。提醒：下次附理由
- 代码级查证补充（2026-10-18 · 命令行程序 2.1.288）：Claude Code subagents 文档原文 "Subagents inherit the built-in tools and MCP tools available in the main conversation, narrowed by two filters"；后台子 agent 保留的内置工具里有 `Read`、`Write`（第二道过滤）。推论：主 agent 的 `tools` 只放 `"Agent"` 时研究员拿不到 Read / Write，所以主 agent 的清单必须同时保留 Read、Write。来源：https://code.claude.com/docs/en/sub-agents。"主 agent 不准自己干活"留到知识点 10；这次靠提示词要求，再用打印核对（主 agent 自己开的 Read / Write 调用单标记为 None）
- 大纲第 1 批（2026-10-18，3 部分）：① import 加 `AgentDefinition`（支撑，直接给）；② 研究员定义 `AgentDefinition(description=..., prompt=..., tools=["Read", "Write"], model="haiku")`，系统 prompt 由用户写（英文），必须包含：角色、只按任务那段话做事、缺信息时直说不知道不要猜（为实验 ② 准备）、交回内容简短；放哪由用户选（A：main.py；B：新文件 agents.py）；③ `ClaudeAgentOptions` 加 `agents={"researcher": ...}`，`tools=["Read", "Write", "Agent"]`，其余不变。要求：写完不运行，发来读回检查
- 用户回复（2026-10-18 11:59）：① 选 B（新建 `agents.py`），并要求记下"学习过程的同时学会自己设计模块化架构"（已写进上面"用户的固定要求"和项目记忆）；② 认为主 agent 和子 agent 的 prompt 都应独立保存、统一管理；③ 代码已写好，`main.py` 已连上；说"subagent 的工具目前还是默认工具"，网上查到"应该加入 web_search tool"
- 读回代码（2026-10-18，`agents.py` 595 字节、`main.py` 3457 字节，两个文件语法检查通过）：
  - `agents.py`：`from claude_agent_sdk import AgentDefinition`；`researcher = AgentDefinition(description=..., prompt=..., tools=["Read", "Write"], model="haiku")`，`tools` 旁注释 `# should be web_search`
  - `main.py`：`from agents import researcher`；`agents={"researcher": researcher}`、`tools=["Read", "Write", "Agent"]`，其余不变；没在 `main.py` 里 import `AgentDefinition`——对，`main.py` 用不到它
  - `.gitignore` 加了 `personal_notes/`（新文件夹 `personal_notes/subagent.md`，用户自己的笔记）
- 批改：结构（B）、`agents`、`tools` 都对。缺口在系统 prompt：只写了第 1 点（角色），缺第 2 点（只按任务那段话做事）、第 3 点（缺信息时说不知道、不要猜——实验 ② 的前提）、第 4 点（交回简短）；还写了 "gather ... from external sources"，但它没有任何上网的工具，会诱导模型编造；拼写 `reasearcher`
- 用户说"还是默认工具"——纠正：`tools=["Read", "Write"]` 不是默认，是只给这两样；不写 `tools` 才是继承默认
- WebSearch：工具名是 `WebSearch`（不是 `web_search`）；工具参考里 Permission required = Yes，会落到检查函数，而现在的 `check_tool` 对 Read / Write 以外一律拒绝；还要同时加进主 agent 的 `tools`（继承规则）；搜索要额外收费、结果每次不同，会干扰"子 agent 看得到什么"的实验。建议这次不加，等第一个真正需要上网的知识点再加（按需生长），由用户确认
- prompt 独立成文件：给两个选项——A 现在就做（先设计再跑实验）；B 先跑完知识点 4 的实验，再单独做一步"搬 prompt"（同上次搬家的方案 C），建议 B（一次只改一类东西，出错时只有一个嫌疑；实验中 prompt 还会改）。设计由用户自己做（文件夹 / 文件名 / 谁来读 / 路径从哪来）
- 用户回复（2026-10-18 12:34）：① 接受不加 WebSearch，"先改成从内部搜索"；② 已把系统 prompt 单独存成文件（等于选了 A：现在就做），目前只有研究员的，理由"有单独位置可以更改 system prompt"
- 读回（2026-10-18，两个文件语法检查通过）：新文件 `system_prompt.py`（一个字符串常量 `researcher_prompt`）；`agents.py` 改为 `from system_prompt import researcher_prompt`、`prompt=researcher_prompt`。prompt 现在 4 点都有：角色、只按任务内容做事、找不到就说 "I don't know" 不要编、少于 300 词并附来源；"external sources" 已改成 "given sources"
- 批改：通过。非阻塞：拼写（reasearcher、frabicate、"You final"、"any out limit behavior must prohibited"）；第 3 点写的是"搜不到信息时"，实验 ② 更需要"任务里没给的信息就说不知道"，可选加强；`tools` 旁注释 `# should be web_search` 已过时、会误导。设计取舍（由用户决定，已说明）：`.py` 里放字符串——不用写读文件代码、可以直接 import；放 `.txt` / `.md` 文件（demo 的做法）——改起来不用管引号和转义，但要多写读文件的代码和路径
- 大纲第 2 批（观察代码，2 部分）：⑤ `AssistantMessage`、`UserMessage` 两个分支开头按 `message.parent_tool_use_id` 打印来源（`None` → `[main]`，否则 `[sub]` + 编号；判断条件由用户自己写）；调用单加印 `block.id`，结果单加印 `block.tool_use_id`，用来对编号；⑥ 结果单内容截取从 200 临时改到 1500，跑完改回
- 第 1 次运行计划：提示词 "Use the researcher agent to read notes/a.txt and summarize it in 3 bullet points. Do not read the file yourself."；目的：在真实消息里完整看一次派活流程（问题 ①）；预测题 5 道：Tools 列表里派活工具的名字、会不会出现 `[check]`、关键消息顺序（谁开单 / 标记 / 结果单回到哪）、研究员 Read 调用单的标记等于哪张单的编号、主 agent 收到的结果单里除了总结还有什么。提醒：子 agent 默认后台运行，顺序可能和预测不同
- 用户提问（2026-10-18 13:03）：在调用单分支写了 `print(block.tool_use_id)`，报"没有 tool_use_id"。读回 `main.py` 消息循环：两个分支开头的 `[main]` / `[sub]: 编号` 已写对（用 `== None`，PEP 8 建议 `is None`，非阻塞）；结果单内容截取已改为 1500；问题：调用单分支用了结果单的字段名，结果单分支还没加编号打印。**卡住升级 1 次（提示级）**：指出调用单自己的编号字段是 `id`，`tool_use_id` 属于结果单（对回调用单用），对应 `review.md` Q9
- 第 1 次运行（2026-10-18 13:13，**命令行程序已自动更新到 2.1.302**，模型 `claude-haiku-5-5`）。**用户没有交预测**（固定要求第 4 条），直接发了输出
  - init：`Tools: ['Task', 'Read', 'Write']`——`tools` 里写 `"Agent"` 生效，列表里显示为 `Task`（未查证项已核实）
  - `[main]` Agent 调用单：`input` 有 `description`（"Summarize notes/a.txt"）、`subagent_type`（"researcher"）、`prompt`；主 agent 自己在任务那段话里加了工作目录的绝对路径和"只交回 3 条"——上下文只能靠这段话传
  - 紧接着 `[main]` 结果单（`tool_use_id` = Agent 调用单 id）内容是 **"Async agent launched successfully … agentId: … The agent is working in the background. You will be notified automatically when it completes …"**——后台运行，结果单是"已启动"回执，不是研究员的总结
  - `[sub]: <Agent 调用单 id>` 的 Read 调用单（`notes\a.txt` 绝对路径）和它的结果单（文件内容，带行号），标记都等于 Agent 调用单的 id；整次运行**没有出现 `[check]`**（Agent 不需要批准；项目内 Read 工具自己放行）
  - `[main]` 主 agent 先说"已启动、完成后再给总结"→ **第一次 `ResultMessage` success（2 轮，$0.00126）**
  - 之后循环没有结束：`[sub]` 研究员的最后一条消息（3 条要点 + Source）；**又一条 init**（同一个 session_id）；`[main]` 空行；`[main]` 主 agent 给出总结（措辞与研究员原文略有不同）→ **第二次 `ResultMessage` success（1 轮，$0.00229）**。主 agent 没有再开 Read 调用单，总结来自后台完成后的通知；通知本身没被我们的代码打印出来（推测：通知以 `UserMessage` 字符串内容或 `Task*` 类 `SystemMessage` 的形式到达，我们的代码只打印列表内容和 init——**未查证**，下一次运行可加打印核对；正好对应 Q10 的第 1 个坑）
  - 第 3 行 "claude.ai connectors are disabled because ANTHROPIC_API_KEY … is set" 是新版命令行程序的提示，用 `.env` 里的密钥时正常出现，无影响
- **我的教学更正**：第 6 步场景（"研究员的最后一条消息作为结果单交回"）只描述了前台运行；本次实际是后台运行（官方默认），Agent 调用单的结果单是启动回执，最后一条消息经后台完成通知回到主 agent，`query()` 会出现两次 `ResultMessage`。开场 / 第 5 步提醒过"后台可能让顺序不同"，但没说结果单内容会不同——讲解不完整，已在回复中承认，先请用户自己从输出里找差异
- 问题 ① 已有答案（标记为 `None` = 主 agent；标记 = Agent 调用单 id = 子 agent）
- 用户看输出作答（2026-10-18 13:33）：1 "Task，不一样，我们的是 agent"（对）；2 "并没出现 check，这个不已经被我们删了吗？"（前提错，打印还在，记 Q17）；3 两张调用单大意对，"sub 拿到调用单"不准（记 Q23）；4 "等于自己的调用单编号"（错，等于 Agent 调用单的编号，记 Q23）；5 "多了具体的文件地址，可以防止 subagent 走错"（对；根本原因是研究员看不到主 agent 的历史，背景只能写进任务那段话）。关键题（后台）没有作答
- **用户意见**："你让我在输出中找内容说真的非常耗时，我不可能一行行数，包括回答你的问题也是"→ 采纳：以后批改时我自己把相关的几行原文摘出来贴在问题旁边，用户只看摘出来的部分作答；不再要求用户标行号（`issue.md` 第 19 条）
- 后台机制：用户没答，按他的意见由我直接讲（摘出原文那句 "The agent is working in the background. You will be notified automatically when it completes"）：Agent 调用单的结果单 = 启动回执；主 agent 先结束一轮（第一次 success）；研究员做完后 Claude Code 程序通知主 agent，主 agent 再跑一轮（又一条 init、第二次 success）；总结来自这条通知。通知长什么样还没看到——加观察代码 ⑦ 去看（同时在真实数据里重学 Q10 第 1 个坑）
- 第 2 次运行计划（上下文隔离，问题 ②）：观察代码 ⑦：`UserMessage.content` 是字符串时也打印；`SystemMessage` 不是 init 时打印 `subtype`。提示词："My secret code is 4827. Use the researcher agent. The task you give it must be exactly: 'What is the user's secret code? Answer only from information in this task.' Do not put the code in the task."。3 道预测：Agent 调用单的任务那段话里有没有 4827；研究员最后说什么；主 agent 最后告诉你什么。判读规则：如果任务那段话里出现了 4827，这次实验作废（是主 agent 泄露，不是隔离失败）
- 读回 `main.py`（2026-10-18 15:15 后）：观察代码 ⑦ 写对——`SystemMessage` 非 init 打印 `subtype`；`UserMessage` 在 `content` 是 `str` 时打印；调用单打印 `block.id`，结果单打印 `tool_use_id`；改用 `is None`
- 第 2 次运行（2026-10-18，命令行程序 2.1.302，上下文隔离 / 问题 ②）。**用户第二次没交预测**
  - Agent 调用单 `prompt` 原样是 "What is the user's secret code? Answer only from information in this task."——没有 4827，实验有效
  - 研究员一条 Read 都没开，直接答："I don't know. The task information I was given (the question itself and the git status snapshot) does not contain a secret code."
  - **问题 ② 结论：子 agent 看不到主 agent 的对话（用户原话里的暗号）**
  - **新发现**：研究员说它收到的除了问题，还有一份"git status snapshot"——Claude Code 程序会把环境信息（git 状态）附进子 agent 第一轮的历史；Subagents 文档的表里没列这一项（只列了自己的系统 prompt、任务那段话、工具定义、项目 CLAUDE.md）。**我的更正**：第 5 步说"第一轮历史只有三样东西"不完整，还要加上 Claude Code 程序附带的环境信息（这次看到的是 git 状态）；`setting_sources=[]` 挡不住它（git 状态的具体来源和开关 **未查证**）
  - 后台完成通知在 Python 程序这边的样子：`SystemMessage` 的 `subtype` 依次出现 `commands_changed`、`background_tasks_changed`、`task_started`、`thinking_tokens`、`task_updated`、`task_notification`；`UserMessage` 字符串分支**没有**打印任何东西——通知到 Python 是 `task_notification` 这条系统消息（SDK 0.2.162 `types.py` 里是 `TaskNotificationMessage`，字段有 `status`、`summary`、`tool_use_id`、`output_file`），不是 `UserMessage`。这次 Q10 第 1 个坑没出现；`[sub]` 后面跟空行，很可能是只装了思考块的 `AssistantMessage`（Q10 第 3 个坑，没打印块类型，**未确认**）
  - 主 agent 第二轮："The researcher agent answered that it doesn't know the code…"；两次 success，合计约 $0.0025
- 用户提问："subagent 是不是只用了一轮就探出来了？"——回答：是一轮（没开任何调用单），但它没"探出来"暗号，而是直接说不知道，这正是隔离的证据
- 第 3 次运行计划（问题 ③）：提示词 "Use the researcher agent to read notes/a.txt and save a 3-bullet summary to output/summary_sub.md. Do not do it yourself."；预测：`[check]` 会不会出现、出现时那张 Write 调用单的标记是 `[main]` 还是 `[sub]`、Write 结果单 `is_error`、文件最后在不在 `output/`
- 用户（2026-10-18 15:22）：补交第 2 次运行的预测（看过结果后写的：① 不会出现 4827、② 会说不知道 4827、③ 主 agent 会告诉我正确答案），并先写第 3 次的预测再运行：① 会出现 `[check]`，"因为工具是继承关系"；② `[main]`；③ `None`；④ 文件会出现——并说明"此次我故意往最极端的方向猜"，结果"正好与我想的完全相反"。保留"运行前预测"（用行动回答了）
- 第 3 次运行（2026-10-18，命令行程序 2.1.302，问题 ③）：
  - 主 agent 的 Agent 调用单 `prompt` 里自己写了 "Working directory: D:\\MyProjects\\..."，还加了"output 目录不存在就创建""只写总结""完成后回一行确认"
  - `[sub]` Read `notes\a.txt` 成功；`[sub]` Write `output\summary_sub.md` → 结果单 `is_error: True`，内容 **`<tool_use_error>Subagents should return findings as text, not write report files. Include this content in your final response instead.</tool_use_error>`**
  - 整次**没有 `[check]`**；拒绝消息也不是我们 `check_Write` 的那句——是 Claude Code 程序**内置**的拦截（子 agent 不应写"报告文件"），在问检查函数之前就挡住了。`device_list_dir` 核对：`output/` 里只有旧的 `wrong.md`，没有 `summary_sub.md`
  - 研究员最后说 "My instructions prohibit writing summary .md files"——它的系统 prompt 里根本没有这句，是模型给被拒找的理由（不能信模型的解释，要看结果单原文，对应 Q16 / Q19）；主 agent 也说"That's odd … configuration may be blocking"
  - **查证**：Subagents 文档（全文两段读完）和 Tools reference 的 Write 部分都没有写这条规则——**未查证（文档未记载），只有 2.1.302 的实测证据**；拦截判断标准（按 .md？按"总结 / 报告"内容？）未知
  - 对知识点 6"用文件交接"有直接影响：研究员写 .md 笔记可能被这条内置规则挡住，知识点 6 开讲前要先查清
- 预测批改：4 条都没对上，但第 1、3、4 条错在一个谁都不知道的内置规则上；第 2 条（`[main]`）是真缺口——活派给研究员，Write 调用单是研究员开的，标记一定是 `[sub]`；"故意往极端猜"会让预测失去作用（预测是用来暴露自己真实理解的），请他以后写真实的猜测
- 第 3b 次运行计划：提示词改为写 `output/summary_sub.txt`（我们的 `check_Write` 会因为不是 .md 拒绝）；如果内置拦截放过 .txt，就能看到 `[check]` 是不是由 `[sub]` 的 Write 触发、结果单是不是我们那句 deny 消息；如果内置拦截连 .txt 也挡，就说明它不按扩展名判断
- 第 3b 次运行（2026-10-18 15:33，命令行程序 2.1.302）。预测：① 会出现 `[check]`、`[sub]`；② 结果单是内置规则那句；③ 文件不会出现
  - `[sub]` Write `output\summary_sub.txt` → 紧接着 `[check] input_data is: D:\...\output\summary_sub.txt` → `[sub]` 结果单 `is_error: True`、内容 "The mission must inside folder 'output' and only .md file permitted"（我们 `check_Write` 的 deny 消息）。`device_list_dir` 核对：`output/` 里没有 `summary_sub.txt`
  - 预测对照：① 对；② 错（是我们的检查函数，不是内置规则——内置规则放过了 .txt）；③ 对
  - **问题 ③ 结论：子 agent 开的调用单也会问到 Python 程序里的检查函数**；内置"子 agent 不写报告文件"规则拦 .md、不拦这次的 .txt（判断标准仍未知）
  - 查证补充：0.2.162 `types.py` 的 `ToolPermissionContext` 有 `agent_id` 字段（"If running within the context of a sub-agent, the sub-agent's ID"）——检查函数的第三个参数能分辨是不是子 agent 开的单，知识点 10 可用，**未实测**
- 对照 demo（`example_program/research_agent/utils/message_handler.py`）：同样用 `parent_tool_use_id` 判断消息来源；但只认 `block.name == 'Task'`，而我们实测调用单里叫 `Agent`——在现在的命令行程序上，demo 的"Spawning"提示一次都不会出现；`agent.py` 的 `allowed_tools=["Task"]` 也是旧名
- 必须记住的 5 件事（只含核心代码内容）：
  1. 定义子 agent：`AgentDefinition(description, prompt=子 agent 自己的系统 prompt, tools, model)` → `ClaudeAgentOptions(agents={"名字": ...})`；主 agent 的 `tools` 要有 `"Agent"`（init 显示 `Task`），子 agent 的工具从主 agent 能用的工具里继承（→ `review.md` Q24）
  2. 派活 = 主 agent 的模型开 Agent 调用单（`input`：`subagent_type`、`description`、`prompt`）；子 agent 第一轮只看到自己的系统 prompt + 任务那段话 + 工具 + Claude Code 程序附带的环境信息，看不到主 agent 的对话（4827 实验），背景只能靠主 agent 写进任务那段话（→ Q22）
  3. `parent_tool_use_id`：`None` = 主 agent 的消息；否则等于派活那张 Agent 调用单的 `id`（不是子 agent 自己调用单的 id）（→ Q23）
  4. 子 agent 默认后台：Agent 调用单的结果单是启动回执；完成时 Python 收到 `task_notification` 系统消息；主 agent 再跑一轮，`query()` 出现两次 success（→ Q25）
  5. 子 agent 的调用单也会问到我们的检查函数；但内置规则（不写报告 .md）排在更前面；谁拦的看结果单原文（→ Q26）
- 卡住升级次数：1（提示：`ToolUseBlock` 用 `id`、`ToolResultBlock` 用 `tool_use_id`）/ 部分代码 0 / 相似例子 0 → 保持 L2，升 L3 计数 0/2
- 教学自查（对照 skill，引用原话）：
  1. 第 5–6 步讲解不完整：我说"这个子 agent 第一轮的历史里只有三样东西"，场景写"研究员写出最后一条消息……作为结果单交给主 agent"——实测是后台启动回执 + 通知，且有 git 状态附带；只提了"消息顺序可能不同"。已在第 1、2 次运行批改中承认更正
  2. 代码分类清单第 4 块是我列错（现有代码已打印调用单），用户分类时才发现
  3. 第 1 次运行批改让用户"每题都标上你依据的是输出的第几行"——用户："我不可能一行行数"（`issue.md` 第 19 条），之后改为我摘原文
  4. 开场 Q10 用了用户已忘的"结果单"（`issue.md` 第 17 条）；Q10 的三个坑当初由我写进大纲、用户没亲自撞过（`issue.md` 第 18 条）
  5. 做得对的：每次结论都用 `device_list_dir` 核对文件夹实际内容；第 3 次运行没被模型"我的指令禁止"的说法带偏，按结果单原文判断是内置拦截，再设计 3b 区分
  - 其余检查项（首行标注、要用户做的事放最前、批改前读回代码、查证标版本、文档改后读回）：无违规
- 收尾清理（2026-10-18，读回 `main.py`、`agents.py`、`system_prompt.py`，三个文件语法检查通过）：结果单截取改回 200；非 init `SystemMessage` 的 `subtype` 打印已删；保留 `[main]` / `[sub]` 标记、调用单 `id`、结果单 `tool_use_id` 打印和 `UserMessage` 字符串分支；`system_prompt.py` 拼写已修，第 3 点加强为"任务没给的信息就说不知道"；`agents.py` 注释改为 `# should be WebSearch`
- git：`.git/logs/HEAD` 最新一条 `09ab8da` "Build the simplest subagent-researcher, no WebResearch Tool, task finish"（2026-10-18 15:39），用户说已推送到 GitHub
- **知识点 4 ✅ 完成（2026-10-18）**。用户决定之后每个知识点开新对话

### 知识点 5 · 派单契约（🟨 2026-10-18 开场，新对话）

- 开场：2026-10-18 15:48 后发出（新对话）。先给了 5 行回顾卡（用户要求）
- 读回真实代码（2026-10-18，设备工具暂存后读）：`main.py` 70 行，`ClaudeAgentOptions` 没有设 `system_prompt`——主 agent 目前没有我们写的系统 prompt；消息循环保留 `[main]` / `[sub]` 标记、调用单 `id`、结果单 `tool_use_id`、`UserMessage` 字符串分支。`agents.py` 只有 `researcher` 一个子 agent 定义，`description` 原文 "This subagent is for information research, when user ask for data collection, need to call this agent to finish the task"，`tools=["Read", "Write"]`。`system_prompt.py` 只有 `researcher_prompt`（第 3 行 "any out limit behavior must prohibited" 仍在）。`check_tools.py`、`path.py`、`initialization.py` 与知识点 4 结束时相同
- 开场复盘（跨对话，依据知识点 4 的"教学自查"）：违规 4 条——第 5–6 步讲解不完整（原话"这个子 agent 第一轮的历史里只有三样东西"）；代码分类清单第 4 块是我列错；让用户"每题都标上你依据的是输出的第几行"；Q10 用了用户已忘的"结果单"、三个坑由大纲直接给。其余无违规
- 间隔复习候选（逐题写出完整问题，用户挑 1–2）：Q13（1 级，10-07）、Q4（2 级，10-02）、Q18（1 级，10-15）、Q25（未考，10-18 学）。**Q10（0 级）不放进候选**：三个坑用户从没亲自撞上过（`issue.md` 第 18 条），再考没有意义；知识点 5 代码阶段如果出现字符串内容 / 看起来空的消息，当场让他自己撞上
- 支持级别：L2（知识点 4 用了 1 次卡住升级，升 L3 计数 0/2）；不提议升降
- 路径：按 L2 由用户先判断；开场只用大白话说了本知识点要解决的问题，没说答案（`issue.md` 第 7 条）
- 代码分类：代码阶段开头再做（`issue.md` 第 6 条）
- 本知识点要回答的 3 个问题：① 研究员只凭任务那段话干活，那段话缺了哪一类信息会出什么错（含糊派单和完整派单各跑一次，看真实结果）；② 有不止一个子 agent 定义（或者没有合适的）时，主 agent 的模型靠什么决定派给谁；③ 任务那段话每次都是主 agent 的模型现场写的，我们用什么办法让它每次都写全
- 完成标志：研究员只凭派单内容就正确完成；含糊 / 完整两种派单的结果能对比；收尾能用自己的话说出任务那段话要写哪些内容、每样缺了会怎样，以及主 agent 怎么选派给谁
- **给原理阶段的提醒（`issue.md` 第 13 条的教训）**：第 1 步讲限制条件时必须点出——Claude Code 程序自带一个 `general-purpose` 子 agent，不用我们定义，主 agent 随时可以派给它（SDK Subagents 文档原文 "Claude can invoke the built-in `general-purpose` subagent at any time via the Agent tool without you defining anything"；关掉要设环境变量 `CLAUDE_AGENT_SDK_DISABLE_BUILTIN_AGENTS=1`）。这会直接影响问题 ② 的预测
- 代码级查证（2026-10-18）：
  - 用户环境：SDK 0.2.162（用户 10-18 说明）；命令行程序上次是 2.1.302，会自动更新，第 1 次运行从 init 读
  - 当时最新：SDK 0.2.168（PyPI，2026-10-15，内置命令行程序 2.1.301），与知识点 4 查证时相同，没有新版本
  - 0.2.162 和 0.2.168 源码包对比：`AgentDefinition`（`types.py` 第 108–126 行）完全相同；`types.py` 的改动只在 hook 输入（`HookEffort`、`prompt_id`、`duration_ms`、`BackgroundTaskSummary` 等），与本知识点无关
  - 读原文：SDK Subagents https://code.claude.com/docs/en/agent-sdk/subagents ；Claude Code subagents https://code.claude.com/docs/en/sub-agents 。和本知识点答案有关的原文留到原理第 5 步再讲（开场不说答案）
- 文档修正：`review.md` Q13 条目头部"当前等级"写的是 0，最新作答记录和索引都是 1，改为 1
- 用户回复（2026-10-18 16:03）：
  - 回顾卡：没有提出问题；安排："学习确认"（无修改）
  - 间隔复习：没按"挑 1–2 道"，三道都答了（Q4、Q18、Q25）。Q4 "解决了用户对于 agent / 程序是否真正结束、状态、问题认知的问题"→ 2 级（第一次说出"结束信号"，漏花费 / 轮数和 `subtype`）；Q18 "必须返回工具调用成败结果。message 是写给模型看的，遇到不认识的工具：一律 deny"→ 2 级（返回的是准不准执行的决定对象，不是执行结果；没说为什么要写 `message=`）；Q25 "结果单装的是任务确认信息……两次 success 是因为最开始子 agent 发送的是它启动的信息"→ 2 级（回执是 Claude Code 程序写的；完成消息是 `task_notification` 系统消息；第二次 success 来自主 agent 再跑一轮；漏了"第一次 success ≠ 干完"）。详见 `review.md`
  - 路径："可推理 + 规定"，没附理由
- 路径判定（2026-10-18）：整个知识点按**核心·可推理型**走——要解决的三个问题（任务那段话缺了什么会出什么错、主 agent 怎么选人、怎么让它每次写全）都能从知识点 4 已确认的限制推出来；"规定"的只有名字（`description` 这个字段叫什么、写在 `AgentDefinition` 哪里），按 L2 在代码阶段直接给，不改变路径。和知识点 4 开场同一类判断（用户当时也说"有的已经规定了"）。提醒下次附理由。等用户接受或反对
- 用户（2026-10-20 17:11，隔了 2 天）："同意，继续吧"——接受路径核心·可推理型
- 原理第 1–3 步（2026-10-20，单独一条回复；隔 2 天，开头先给 5 行回顾卡，`issue.md` 第 14 条）：
  - 用到的概念都在固定词汇表里（任务那段话、Agent 调用单、子 agent 定义、系统 prompt、历史）；唯一新词 `general-purpose`，当场一句话解释
  - 限制条件（只讲事实）：① 研究员只看得到自己的系统 prompt + 任务那段话 + 工具 + 少量环境信息（知识点 4 的 4827 实验）；② 任务那段话由主 agent 的模型现场写，每次可能不同，Python 程序不写它（知识点 4 第 1、3 次运行，主 agent 自己加了绝对路径、"只交回 3 条"）；③ 研究员手上只有 Read / Write，没有回头问人的工具，往上只交回最后一条消息；④ 可以派的对象有两个：我们写的 researcher，和 Claude Code 程序自带的 general-purpose（不用定义，随时能派；SDK Subagents 文档原文 "Claude can invoke the built-in `general-purpose` subagent at any time via the Agent tool without you defining anything"），主 agent 也可以自己读；主 agent 的模型对它们的了解只来自 Claude Code 程序发给它的文字；⑤ 我们没给主 agent 写系统 prompt（`main.py` 没设 `system_prompt`），除了工具说明，它拿到的指示只有终端里那一句话（SDK Subagents 文档原文 "A custom prompt, or no `systemPrompt`: Claude Code doesn't build its system prompt"）
  - 场景：`notes/a.txt` 是一篇讲"AI 投资泡沫可能怎么破"的文章（两组情景：AI 不及预期；AI 有用但钱流不到投资者）。用户在终端打"我在写课程作业，观点是'AI 投资泡沫最大的风险不是技术失败，而是赚到的钱流不到投资者手里'，帮我从 notes/a.txt 里找支持和反对这个观点的论据"
  - 问题：① 主 agent 只写 "Summarize notes/a.txt" 时研究员交回什么、差在哪；换他当主 agent 写一段能一次做对的任务那段话，每句后注明防止什么错；② 派给 researcher / general-purpose / 自己读，模型凭哪些文字选；那段文字写得很含糊（只写 "a helper"）会怎样；③ 真实运行时是主 agent 现场写任务那段话、只拿到用户一句话，要它每次写到 ①(b) 的水平，这个要求由谁、什么时候、写在哪
- 第 2 步用户的尝试（2026-10-20 17:33）：
  1. "研究员交回来的大概是简单的对文章的分析，并没有仔细针对我的问题进行搜索，没有针对性回答。你需要打开 D:/xxx/a.txt 文档（防止子研究员不知道位置），从中拿到能够验证观点'……'的内容（防止研究员不了解任务主次），并扩散查询支持和反对该观点的论据（防止研究员仅注意一边论据）"
  2. "凭'找''搜索'这种带有强烈行为性的词语。我预计它还是能找到正确 subagent，这个需要因模型而异"
  3. "说实话我并不认为我写的会比模型写得好，但我应该用 system prompt 约束它的写作方式"
- 第 4 步反馈（2026-10-20）：对的——1(a) 泛泛总结、没针对性；1(b) 写了位置（绝对路径）、目的（要验证的观点）、两边都要，每句都写了防什么错；3 方向对（用系统 prompt 约束主 agent 怎么写）；纠正"我写的不如模型"——要写的不是每一段任务那段话，而是"每段都必须包含什么"的规则，具体内容仍由模型按每次的请求填。缺口（以问题留给用户补）：① 1(b) 没说交回什么样子（分不分两边、每条要不要附原文出处、多长）——缺了主 agent 拿到的是一段混在一起、没法引用的文字；"扩散查询"没划范围——研究员可能用自己的知识补论据（没有出处、可能编造），范围该怎么写；② 第 2 题只说了用户那句话里的词，没说另一边——关于 researcher 是干什么的，模型读到的文字是谁写的、写在哪；"a helper"时三个选项（researcher / general-purpose / 自己读）具体选哪个，给一个确定的预测；③ 第 3 题的系统 prompt 是主 agent 的还是研究员的；第 1(b) 里哪些要求每次都一样、哪些每次都不同，各放哪里更合适
- 用户补缺口（2026-10-20 17:44）：
  1. "主 agent 会拿到空泛的总结性内容，也许会有一定格式，但不一定是用户想要的类型；它可以使用内部知识，但很有可能出现错误或者信息过时问题，任务中应该让它只专注于搜索得到的内容"
  2. "第一个问题我不太理解你的意思；我认为会派给 researcher"
  3. "主 agent 的；任务安排格式可以一样，内容可以不一样，放在哪里的意思我不太明白"
- 反馈：① 范围对（只用给定材料，否则可能错 / 过时；补：作业没法引用出处）；交回样子仍没说具体，第 5 步直接讲。② 没看懂是**我的问题**——"模型读到的那段介绍"问得太绕，第 5 步直接讲 `description`；"a helper 时选 researcher" 记为预测，代码阶段运行验证。③ "主 agent 的"对；"格式一样、内容不一样"正是要分的两类；"放在哪里"没看懂也是我问得不清，第 5 步直接讲三个位置。缺口提问已两轮，不再追问，进入第 5–6 步
- 原理第 5–6 步（2026-10-20，同一条回复，不含代码）：
  - 第 5 步机制 A（派给谁）：Claude Code 程序把每个能派的子 agent 的名字 + `description` 发给主 agent 的模型；模型拿用户那句话和这些介绍做比对，选一个（或自己做）；是模型判断，不是程序规则，不保证。提示词里点名（"Use the researcher agent…"）会跳过比对——知识点 4 每次都点了名，所以一直派给 researcher。我们现在的 `description` 原文；general-purpose 的介绍原文 "A capable agent for complex, multi-step tasks that require both exploration and action."
  - 第 5 步机制 B（任务那段话写什么）：Anthropic 工程博客原文 "Each subagent needs an objective, an output format, guidance on the tools and sources to use, and clear task boundaries." 对应用户自己的答案：目的（他写了）、交回样子（缺）、用什么材料（他写了位置 + 只用文件）、边界（他补了"只专注搜索得到的内容"）；缺了的后果引博客 "Without detailed task descriptions, agents duplicate work, leave gaps, or fail to find necessary information."
  - 第 5 步机制 C（放在哪里）：三个位置——研究员的系统 prompt（每次都一样、关于研究员自己怎么做：只用给的材料、附原文出处、交回格式、不知道就说）；主 agent 的系统 prompt（每次都一样、关于主 agent 怎么派单：每段任务那段话必须写哪几项；现在不存在）；任务那段话（每次都不同：这次的文件、这次的观点 / 问题、这次的特殊要求）。理由：研究员的系统 prompt 你写一次、每次都在，不靠主 agent 记得抄；任务那段话是唯一每次能变的通道；运行前写不出"这次的内容"
  - 第 6 步场景：作业观点那句话，从主 agent 读到什么、选谁、写出的任务那段话有哪几项，到研究员第一轮看到什么、交回什么
- 查证（2026-10-20）：Claude Code subagents 文档原文 "Claude uses each subagent's description to decide when to delegate tasks." "Those descriptions take up context, so keep them short." https://code.claude.com/docs/en/sub-agents ；SDK Subagents 文档 "Explicit invocation … This bypasses automatic matching" https://code.claude.com/docs/en/agent-sdk/subagents ；Anthropic 工程博客 https://www.anthropic.com/engineering/multi-agent-research-system 。**未查证**：`description` 在发给模型的文字里具体放在哪（是不是写在 Agent 工具的说明里）——只查到"会占上下文"
- 用户（2026-10-20 18:06）："懂了"，没有提问
- 第 7 步收尾复述（2026-10-20）：请他不看前文、用自己的话答 3 题：① 主 agent 靠什么决定派给谁，什么情况下这个比对不起作用；② 任务那段话要有哪四样，任选两样说缺了会出什么错；③ 三个位置各放什么，为什么"每次都不同"的内容只能放在任务那段话里
- 收尾复述（2026-10-20 18:13）：① "靠 description and name，当我靠提示词完全指定要用哪个工具时，这个比对不会发生"；② "目的、查找内容、目标位置、特殊要求。缺了查找内容，研究员根本不知道以哪种角度进行查找；缺了位置，研究员可能找错内容，或是找到过时内容"；③ "研究员 prompt，主 prompt，用户提示词（任务）；prompt 主要是规定格式，内容则是用户指定，所以两者必须分工明确"
- 判定：**过关**（核心机制对：靠 `description` 比对、点名跳过比对、固定规则和每次内容分开放）。当场纠正：① 比对的另一边是用户那句话；"指定哪个工具"→"指定哪个子 agent"；② 漏了"交回什么样子"和"边界"——**我的讲解前后不一**（第 5 步 B 说任务那段话要有四样，C 又把交回格式 / 只用给的材料放进研究员系统 prompt，第 6 步场景只列了四项任务内容），已承认并更正为"四样研究员都必须拿到，固定的放研究员系统 prompt，会变的写进任务那段话"；③ 第三个位置是主 agent 写的任务那段话，不是用户提示词（研究员看不到用户那句话）。记 `review.md` Q27 / Q28 / Q29 = 2
- 原理阶段卡住升级：0 次
- 用户（2026-10-22 11:44，隔 2 天）："继续"，并发来新学习规则全文《查证、排错、找来源由我先做（2026-10-22 起，优先于默认教学流程）》，问"能否帮助、打算如何加入"。规则的第一、二、四、五、六节在另一个对话里已写进本文件「用户的固定要求」（我提交前发现文件被改过，没有覆盖，在用户版本上补写）；第三、四（20 分钟）、七节由我补进同一条
- 我的回复（2026-10-22）：评估有帮助，证据：Q16 / Q19（信模型的说法）、Q18（没看定义确认参数顺序）、`issue.md` 第 16 条（`__file__`）；接入方式按教学步骤逐条说明；提出 4 个待定设置 A–D；第一个查证任务（`AgentDefinition` 字段）按用户在日志里写好的执行
- 用户（2026-10-22 13:59）：选 **A1、B2、C2、D2**，要求先写进文件，做好更新后他再做第一个查证任务。已写进「用户的固定要求」「支持级别记录」「计划变更记录」、知识点记录模板（加"查证提示次数"一行），并更新 `issue.md` 第 19 条和项目记忆
- 第一个查证任务 · 第 1 次作答（用户，2026-10-22 14:40）："对于具体的 SDK 版本的分析我并没有查到"；改用官方文档 https://code.claude.com/docs/en/agent-sdk/python#agentdefinition ：13 个参数，必填只有 `description`、`prompt`（前者给主 agent 看、描述子 agent，后者是子 agent 的系统 prompt），原句 "Natural language description of when to use this agent" / "The agent's system prompt"
- 核对（Claude，2026-10-22）：
  - 格式做到了：结论、链接、英文原句都有
  - **错在"找错了地方"**：任务要的是 conda 环境里装的 0.2.162 源码，他用了文档页。文档页的 AgentDefinition 部分没写对应哪个 SDK 版本（我读原文确认），描述的是当前版本，不能证明和他的 0.2.162 一致；他引用的两句是文档表格里的说明，不是源码里的注释，两者不一定相同
  - 不完整：只写了 13 个里的 2 个；没有"文件:行号"
  - 结论本身（13 个、必填 2 个）没有告诉他和源码是否一致——留给他自己对比
  - **查证提示 1 次（方向级）**：装好的包就是你电脑上某个文件夹里的一堆 .py 文件，先想办法让 Python 告诉你它装在哪
  - 我自己的核对结果先不写进本文件（用户能看到这个文件），等他重做后再补进来，标（Claude）
- 用户（2026-10-22 16:05，距上次 85 分钟）："那我不太明白，这种信息在源码里应该怎么看？"
- 判断：两件事——① 不知道装好的源码在哪（卡住超过 20 分钟，按规则主动给下一级）；② 不会读一个类定义、不知道怎么从源码看出"必填 / 可选""注释"。② 是前置知识，从没教过（全项目记录里没出现过 dataclass），**是我出题时漏了**——和 `issue.md` 第 16 条同一类，记为第 20 条
- 处理：
  - 前置知识（不算提示）：用一个和题目无关的 `Book` 例子讲 `@dataclass`、"名字: 类型"一行是一个字段、有没有 `= 默认值` 决定可不可以不填、`X | None`、`#` 注释、类下面的 `"""文档字符串"""`
  - **查证提示第 2 次（文件级）**：包在 conda 环境的 `Lib\site-packages\claude_agent_sdk\` 文件夹里，要看的是其中的 `types.py`；用 `pip show claude-agent-sdk` 可以同时看到安装位置和版本号（顺便核对是不是 0.2.162）
  - 查证提示累计：方向 1 / 文件 1（B2，不算卡住升级）
- 第一个查证任务 · 第 2 次作答（用户，2026-10-22 16:20）：
  - "我根本不了解你的 dataclass 到底怎么用的，所以我上网搜索了一下，ctrl+鼠标左键点击该 class 就能看内部结构了（types.py 107 行开始）"——**定位方法是用户自己找到的**（VS Code 里 Ctrl+点击跳到装的源码）（用户）
  - `pip show claude-agent-sdk` → `Version: 0.2.162`（用户）
  - 有 `@dataclass`；13 个字段：description、prompt、tools、disallowedTools、model、skills、memory、mcpServers、initialPrompt、maxTurns、background、effort、permissionMode；除 description、prompt 外都 "None=None"，可以选填；原句 `description: str`、`prompt: str`（用户）
  - "跟文档中看到的结果都是一样的"（用户）
- 核对（Claude，2026-10-22）：**通过**。来源类型对（装的源码，版本核对过 0.2.162）；13 个字段、必填 2 个，对；和文档一致，对（我对照文档原文和 0.2.162 源码确认过：字段完全相同）。纠正一处：判断可选看的是 `= None`（默认值），`| None` 是类型允许为空，两件事；没写每个字段的行号（截图里 `@dataclass` 在第 107 行、类在第 108 行），没抄注释——只追问一句：截图里 description、prompt 旁边有没有注释，这说明他第 1 次引的两句来自哪里。补讲 `# noqa: N815`：不是说明字段的注释，是告诉代码检查工具"这一行的驼峰命名是故意的，别报"；和文档里 "keep their camelCase spelling to match the wire format" 对应（Claude）
- 第一个查证任务的查证提示：方向 1 / 文件 1（B2，不算卡住升级）。前置知识补讲 1 次（dataclass，不算提示）
- 用户（2026-10-22 16:30）：
  - 追问："没有注释"（对）；反问"第一次引用的那两句英文是啥意思？"→ 我直接说明（不是查证结论，是澄清）：那两句来自文档页字段表格的 Description 一栏，是写文档的人加的说明，源码里这两行没有注释。教训：源码管"你这个版本有什么、默认值是什么"，文档管"这是干什么的、运行时怎么表现"，两边都要看、别混成一处（Claude）
  - 第二个查证任务第 1 次作答（用户）：① 在 `types.py`，参数 `system_prompt`，类型有 str、SystemPromptPreset（他写成 Present）、SystemPromptCustom、SystemPromptFile、None；用过 str（别的项目）和 None（现在没填）；② "假如不传参数，那么 prompt 就是 None"；另在文档 https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts 找到 `system_prompt={"type": "preset", "preset": "claude_code"}` 的例子，问"这属于其中一类吗，尽管它看着是 dict"
- 核对（Claude）：① 结论对，缺行号和原句。② **读得不够深**：`None` 是 Python 程序这边的默认值，题目问的是交给 Claude Code 程序的是什么（另一个程序收不到 Python 的 `None`）；任务里已写"要找到真正用这个值的那段代码"，他停在定义处——只指出错在哪一步，不加新提示。③ 他找的文档页对。补前置知识（不算提示）：TypedDict = 一个"固定了有哪些键"的字典的类型说明，运行时就是普通 dict；`Literal["preset"]` = 这个键的值只能是这几个字面值之一；`NotRequired[...]` = 这个键可以不写。让他自己在 `types.py` 里对照是哪一类
- 用户（2026-10-22 16:34）："什么叫真正用这个值的地方？你是在扣字眼吗？"——**是我的说法太抽象**（"真正用这个值的那段代码""只读了定义，没读用到它的地方"都没配具体例子），不是他的问题（`issue.md` 第 21 条）
- 处理：用他自己项目的例子讲"定义处"和"使用处"：`path.py` 里写 `notes_path = root / "notes"` 是定义（告诉你有这个东西、值是什么）；`check_tools.py` 的 `check_Read` 里拿 `notes_path` 去比路径是使用（告诉你拿它做了什么）。对应到 SDK：`types.py` 里 `system_prompt ... = None` 是定义；SDK 里另有代码读 `system_prompt`，把它变成交给 Claude Code 程序的东西——那里才回答第 2 题。**查证提示（方向级）1 次**（第二个查证任务的第 1 次）：在装的 SDK 文件夹里搜 `system_prompt` 这个词，看哪些地方读了它
- 用户（2026-10-22 16:38）："我真不知道你在说什么，我能理解为：我的 python 代码需要经过另一个内部代码把东西翻译成 claude code 能看懂的东西，所以 None 会变化，是这个意思吗"——**理解对了**（用户）。我只确认、用他的词"翻译"重述任务，不再加解释：找到 SDK 里做这个翻译的代码，看 `None` 被翻译成了什么
- 用户（2026-10-22 16:39）："额，首先什么叫装 SDK 的文件夹，其次怎么搜？"——缺的是操作层面的前置知识（包装在哪、怎么在项目外的文件夹里搜），不算查证提示。我的上一条也有错：只说了 Ctrl+Shift+F，没说它只搜 VS Code 当前打开的文件夹（他的项目），搜不到 site-packages（Claude）
- 处理：分步给操作：① `pip show claude-agent-sdk` 的 `Location` 一行 + `\claude_agent_sdk` = 装 SDK 的文件夹（他 Ctrl+点击打开的 `types.py` 就在里面）；② 两种搜法：VS Code 新窗口打开这个文件夹再 Ctrl+Shift+F，或 PowerShell `Get-ChildItem <文件夹> -Recurse -Filter *.py | Select-String "system_prompt"`
- 用户（2026-10-22 16:43）：自己用 PowerShell 在 `D:\miniconda3\envs\claude_agent_sdk\Lib\site-packages\claude_agent_sdk` 搜出 20 行结果（client.py、query.py、types.py、_internal/client.py、_internal/query.py、_internal/transport/subprocess_cli.py），"有这么多，我不会分辨"（用户）
- 处理：**查证提示第 2 次（段落 / 函数级）**——教筛选办法：① 名字只是包含这个词的不算（`system_prompt_snapshot` 是另一个变量）；② 文档字符串里的示例不算（`query.py:89`）；③ `types.py` 是定义。剩下 3 处候选：`client.py:187`、`_internal/client.py:113`、`_internal/transport/subprocess_cli.py:576–581`，让他打开逐个看"哪一处按是不是 None 做不同的事、None 时做了什么"。补前置知识（不算提示）：命令行参数（用他刚用的 `pip show claude-agent-sdk` 举例）；VS Code 打开文件后 Ctrl+G 跳到行号
- 第二个查证任务的查证提示累计：方向 1 / 段落 1（B2）
- 用户（2026-10-22 16:45）："我不明白，为什么要看这个？这个问题对我 agent 学习有什么实质好处？"
- 回应（Claude）：承认出题时没写"答案用在哪一步"，而且深度超过本知识点需要（`issue.md` 第 22 条）。说明用处：知识点 5 问题 ③ 要给主 agent 写派单规则，前提是知道"不填时主 agent 带着什么指示在跑"（是空的，还是 Claude Code 自带那一大套）——这决定三种写法（自己写字符串 / 用自带那套再追加 / 不填）里选哪个；顺带解释知识点 4 里主 agent 的表现。但"从源码一路追到翻译代码"这一层主要练的是读源码，不是 agent 知识本身。给用户两个选项：A 现在停，第 2 题改从文档页 modifying-system-prompts 找默认行为（仍由他查）；B 继续在源码里追完（练读源码，估计再 10–15 分钟）。另提议以后每个查证任务写明"答案会用在哪一步"，没有用处的不出
- 用户（2026-10-22 16:54）：选 B；要求"之后每次弄这种东西之前先评判花这个时间到底有没有价值……这次我就觉得没价值，因为看了我也根本没学会如何筛选"（已写进「用户的固定要求」）
- 第二个查证任务 · 第 2 题作答（用户）：逐个看了 3 处候选——`client.py`、`_internal/client.py` 两处只处理 dict 形式（preset / custom 的附加选项），"没见到 None"；`_internal/transport/subprocess_cli.py` 第 576 行起 `if self._options.system_prompt is None: cmd.extend(["--system-prompt", ""])`——"如果是 None 的情况下，就是一个空字符串"（用户）
- 核对（Claude）：**通过**。结论对：不传 `system_prompt` 时，SDK 启动 Claude Code 程序时带上 `--system-prompt ""`，主 agent 的系统 prompt 是空的——它拿到的指示只有工具说明和用户那一句话（与 SDK Subagents 文档 "A custom prompt, or no `systemPrompt`: Claude Code doesn't build its system prompt" 一致）。第 1 题的行号由他自己的搜索结果补上：`types.py:1996`（用户）。他排除前两处的理由"只处理 dict 形式"是对的读法
- 按新要求评判：文档里的 `{"type": "preset", ...}` 对应哪种类型这道题**暂不做**——只有设计选择选了"自带那套再追加"才用得上，到时再查
- 第二个查证任务的查证提示：方向 1 / 段落 1（B2）
- 用户（2026-10-22 17:25）：设计选择 1 选**写法 1**（`system_prompt="..."` 自己写字符串），设计选择 2 选 **A**（在 `system_prompt.py` 里加，`main.py` 引用）（用户的设计决定）。按"先评判值不值"：preset 对应哪种类型的查证题不再需要，取消
- 代码分类请求（2026-10-22，L2 由用户先分，**每块附一句理由**）：① `system_prompt.py` 新增主 agent 的系统 prompt（派单规则）；② `main.py` 引用它并传给 `ClaudeAgentOptions(system_prompt=...)`；③ `system_prompt.py` 研究员的系统 prompt 加固定规则（只用给的材料、每条附原文和位置、支持 / 反对分开写）；④ `agents.py` 重写研究员的 `description`；⑤ 为验证"含糊介绍"临时把 `description` 改成 "a helper"，跑完改回；⑥ 现有打印（Agent 调用单的 `input`、`[sub]` 研究员的最后一条消息）——已存在，复用，不新写。提醒两个判断问题："验证完会删吗"→观察；"不懂它但能写对、讲清核心代码，算不算学会"→支撑
- 用户代码分类（2026-10-22 17:32，**第二次没附理由**）：① 核心、② 支撑、③ 核心、④ 支撑、⑤ 观察、⑥ 观察
- 批改：①②③⑤⑥ 对（② 只是把字符串交给一个参数，参数名他已自己查过，接受为支撑）；**④ 错→核心**：`description` 就是本知识点问题 ② 本身（标题"description 决定主 agent 派给谁"），不会删、不懂它就不算学会。提醒附理由（不追问）
- 第 0 次运行计划（基线，2026-10-22）：**先不改任何代码**，提示词不点名子 agent："I'm writing a course essay arguing that the biggest risk of the AI investment bubble is not technical failure, but that the money made doesn't flow to investors. Find arguments for and against this view in notes/a.txt."。用途：① 作为"含糊派单 vs 完整派单"对比里的"改之前"；② 第一次让 `description` 真正起作用（知识点 4 每次都点了名）。预测 3 题：主 agent 派给 researcher / general-purpose / 自己读；如果派了，任务那段话里有目的 / 要找什么 / 材料在哪 / 特殊要求中的哪几项；研究员交回的论据分不分支持 / 反对、附不附原文出处。按 D2，结果里的相关原文由用户自己摘
- 第 0 次运行（2026-10-22 17:42，**命令行程序已自动更新到 2.1.307**，模型 `claude-haiku-5-5`，2 轮，$0.0032）：
  - 预测（用户）：① 会派单——"目前我们的代码里没有 general-purpose，别记混了；我认为目前 subagent 的 description 足够明显"；② 要找什么、材料位置、特殊要求（正反）会有，目的不确定；③ 会分支持 / 反对、会附出处
  - 结果（用户原话）："完全相反，它从一开始就没有调用 subagent"
  - 输出要点（Claude 读附件）：`[main]` 只开了一张 Read 调用单（`notes\a.txt`），没有 Agent 调用单，没有任何 `[sub]`；主 agent 自己写出答案：分"Arguments for / against"，每条带"(line N)"行号，还加了"Points to check before citing"
  - 预测对照：① 错（三个选项里是"自己读"）；②③ 无法验证（没派单）——分正反、带行号是主 agent 自己做的
  - 按新规则：**不先给根因**，请用户按四项写"为什么没派单"
  - 用户的说法"代码里没有 general-purpose"与我原理第 1 步给的文档原文（SDK Subagents："Claude can invoke the built-in `general-purpose` subagent at any time via the Agent tool without you defining anything"）冲突；不争，请他用自己程序收到的消息去验证（来源类型：他的程序收到的 init 消息，现在只打印了其中 4 项）。用途：决定下一次预测时主 agent 面前有两个还是三个选项
- 排错四项（用户，2026-10-22 17:56）：
  - 现象：贴出 `[main]` Read `notes\a.txt` 调用单和 `[main]` 自己写的总结开头，"它自己去看了内容，而非让 subagent 去看……然后开始自主总结"（用户）
  - 证据 + 推断："目前最缺乏的就是 system prompt 来设定角色边界，它不知道任务分配的具体方法和规则……唯一看中的就是完成任务的效率。其次，它有完成任务的所需工具，以及它对于 researcher 的了解只有那个 description，而其中一些词语例如 'data collection' 及其容易被误解"（用户）
  - 验证："最简单的方法就是在提示词中明确要求它调用 subagent"（用户）
- 批改（Claude）：现象对（自己找到并贴出原文，D2 做到了）；证据对，用上了自己查到的"不填系统 prompt = 空字符串"；推断合理，实际列了三个嫌疑原因：A 没有系统 prompt 规定分工、B 自己手里就有 Read、C `description` 含糊（"data collection"）。**验证错在：改的不是任何一个嫌疑原因**——在提示词里点名会跳过比对（他自己在 Q27 答过），三个原因都在时它也会派单，所以证明不了是哪个；而且知识点 4 每次都点名，结果已知。按他阶段 1 定的测试原则"每次只测一件事"：从 A / C 里挑一个只改它、其余不动；B 不能单独改——去掉主 agent 的 Read，研究员也会拿不到（子 agent 的工具从主 agent 继承，Q24），只能留着。请他重写验证：选哪个原因、改哪里、改成什么、预期看到什么
- 用户（2026-10-22 18:05）：① 验证改为"直接加上 system_prompt，设立 4 个标准和角色边界，在 system_prompt.py 加入新的"——选了嫌疑原因 A（用户）；② "没有就是没有，目前 agent.py 只有一个 researcher agent，不要在这种东西里浪费时间。实际情况只有一种可能：之前的对话中又自作主张加入了这个 agent"
- 回应（Claude）：① 接受；补两条——这次只改系统 prompt，`description`（C）不动，否则又变成两个变量；"跑完会看到什么"放进运行前预测里写。② 不再出任务，尊重他的决定；只说明两点事实：他的代码里确实只有 researcher，没有任何对话往代码里加过别的 agent（`agents.py` 修改时间仍是 2026-10-18，我读过内容）；`general-purpose` 不在他的代码里，而是 Claude Code 程序自带的，就像 Read 工具我们也从没写过——依据仍是 SDK Subagents 文档原文（Claude，文档；在他的环境里未实测）。之后的运行如果出现 `subagent_type: general-purpose`，就是实证
- 大纲第 1 批（2026-10-22）：① `system_prompt.py` 新增主 agent 的系统 prompt（英文；角色边界 + 派单规则：任务那段话必须写清目的、要找什么、材料在哪（绝对路径）、这次的特殊要求；名字由用户定）；② `main.py` import 并在 `ClaudeAgentOptions` 加 `system_prompt=...`；③ 第 1 次运行：同一句话、不点名、`agents.py` 不动；预测：派不派、派给谁、任务那段话有四项中的哪几项、推断对 / 错时各会看到什么
- 第 1 次运行（2026-10-24 17:46，隔 2 天；**命令行程序 2.1.310**，haiku，两次 success：$0.0021 + $0.0049）：
  - 读回代码（Claude，2026-10-24，语法检查通过）：`system_prompt.py` 新增 `main_prompt`——角色（拆任务、派给专门的子 agent、按子 agent 的结果给最终输出）、"MUST CANNOT DO: Complete all the tasks by your self"、**留了口子**"may use your judgment … but you must explain your reasoning"、派单格式四项（Mission purpose / The things are looking for / material，本地文件写绝对路径 / special requirements）、两条不准写进任务那段话的内容；`main.py` 第 10 行 `from system_prompt import main_prompt`、第 16 行 `system_prompt=main_prompt`；`agents.py` 未改（修改时间仍是 10-18）。非阻塞：拼写（meterial、abosulute、specical、"MUST CANNOT"）；第 3 行"it outputs a final report"主语不清
  - 预测（用户）：① 会，派给 researcher；② 4 项都有；③ 推断对会看到 `[sub]`；④ 不对只会看到 `[main]` 并说明原因
  - 结果（用户）："的确调用了 subagent，哪怕我留了一条口子……此次的 systemprompt 写的非常详细，也因此带动了任务的内容更加详细"
  - 核对（Claude）：①②③ 全对。Agent 调用单 `subagent_type: 'researcher'`；任务那段话按他的格式写了 "Mission purpose / What to look for / Material（绝对路径）/ Special requirements"；**主 agent 还自己加了他在 Q28 漏掉的两样**：交回样子（"give a short paraphrase and a brief quote or precise location"、三个标题分开）和边界（"Do not use outside sources or web search. Do not write any new files."）。口子起了作用：主 agent 说明了理由（"the system setup requires sub-agents to handle the task work"）。研究员交回分 FOR / AGAINST / UNCLEAR、每条带行号；主 agent 最后基本照抄并说明"I haven't checked them against the file myself"。后台：先回执、两次 success（与 Q25 一致）
  - 推断 A 的结论（Claude）：只改了系统 prompt、`description` 没动，就从"自己读"变成了"派单"——支持 A；`description` 含糊没有挡住派单。但**只跑了 1 次**，模型每次可能不同，证据弱；阶段 2 收尾的 10 次对照实验正好补这一点
  - 输出里仍有几处 `[main]` 后面是空行（Q10 第 3 个坑：看起来空的 `AssistantMessage`），作为可选排错题给用户，不强制
- 用户（2026-10-24 17:57）："为什么要含糊派单？既然有了一个正确答案为什么还要转回去破坏目前状态？这个是否是过度了？"
- 回应（Claude）：**承认我出这一步前没做"值不值"评判**（违反 2026-10-22 他定的要求，`issue.md` 第 22 条再次发生）。这一步唯一的真实用处：分清"任务那段话写得全，是派单规则带来的，还是主 agent 本来就会写这么全"（知识点 4 时没有规则它也自己加过绝对路径）。但他在阶段 2 收尾已经计划了"含糊派单 vs 完整派单各跑 10 次"，同一个问题那时用 10 次回答、证据更强；现在跑 1 次是重复且更弱。临时改动跑完会改回，不算"破坏"，但现在做确实不值。建议 A：现在不跑，把这条完成标志移到阶段 2 收尾实验；B：现在跑 1 次。由用户选
- 用户（2026-10-24 18:02）：选 **A**
- 大纲第 2 批（2026-10-24）：③ `system_prompt.py` 改 `researcher_prompt`：只放对**任何**研究任务都成立的固定规则（只用任务给的材料、不用自己的知识；每条附原文和位置；交回按任务要求的结构分组；找不到就说不知道）——提醒"支持 / 反对分开"只属于这次任务，应由任务那段话写，不该进固定规则（Q29 的应用）；原有"少于 300 词"要不要留由用户定（第 1 次研究员交回明显超过 300 词）；④ `agents.py` 重写 `description`：英文、短（文档 "keep them short"），说清它做什么任务、不能做什么（不上网）、交回什么；⑤ 值不值评判：值得跑 1 次——问题 ②"description 决定派给谁"目前没有任何证据（第 1 次在含糊介绍下也派给了 researcher），而且如果主 agent 改派 general-purpose，还能顺便实证它存在；代价 1 次运行约 $0.005；第 2 次运行之后由用户决定做不做。第 2 次运行 = 回归检查（同一句话、不点名），说明它看不出 ③ 的效果（第 1 次主 agent 已把边界和交回样子写进任务那段话），主要确认改完没坏
- 用户（2026-10-24 18:17）："我认为此次同样不该做，因为我们最终的目标是做出一个网络搜索 agent，而非本地搜索 agent，在这里更改 researcher 的 prompt 效率不高"（用户的决定）
- 回应（Claude）：同意 ③④ 现在不做。补一点：固定规则大多和"本地还是联网"无关（只用给的材料、附出处、按任务要求分组、找不到说不知道），联网后出处从行号变成网址；但加 WebSearch 时研究员 prompt 和 `description`（现在要写"不能上网"）本来就要整体重写，现在改等于做两遍。已写进「当前状态」遗留 ⑦。第 2 次运行（回归检查）随之取消——没有改代码就不需要。知识点 5 的完成标志：研究员只凭派单内容完成（第 1 次 ✅）、收尾复述（Q27–Q29 ✅）、含糊 / 完整对比（已移到阶段 2 收尾）；只剩问题 ② 的证据（⑤ "a helper"，与本地 / 联网无关），由用户定做不做
- 用户（2026-10-24 18:28）："先暂时停一下，先更新目前的项目状态和阶段"——已重写本文件顶部「当前状态」（分出"知识点 5 计数""遗留事项""环境"三行），更新 `project_tree.md` 知识点树
