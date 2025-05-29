# 使命召唤手游注册表灵敏度修改工具

:warning: **免责声明**  
本工具仅供学习交流使用，严禁用于商业用途。修改注册表存在风险，操作前请自行备份数据。因使用本工具造成的任何损失，作者概不负责。

---

## :gear: 功能说明

- 自动修改《使命召唤模拟器手游》在Windows注册表中的灵敏度相关参数
- 支持动态匹配多种游戏模式（PVE/PVP/TD/Br等）及自定义配置项
- 修改键值首字节为 `0x01`，调整灵敏度逻辑（具体效果因游戏版本可能不同）

---

## :rocket: 下载与使用

### 方式一：直接下载EXE（推荐）

1. 前往 [Release页面](https://github.com/DreamChaserWhatever/regedit_CallofDuty/releases) 下载最新版本
2. 使用前应在游戏里把每一个灵敏度都拖动一下,防止有一些没有改到(只有动过的设置才会生成注册表)
3. **右键以管理员身份运行**（必需系统权限）
4. 按提示完成操作，程序会自动修改注册表

### 方式二：从源码运行（Python 3.13）

1. 克隆仓库：
    ```bash
    git clone https://github.com/DreamChaserWhatever/regedit_CallofDuty.git
    ```
2. 安装依赖库：
    ```bash
    pip install -r requirements.txt
    ```
3. 运行主程序：
    ```bash
    python main.py
    ```

---

## :package: EXE打包指南

### 打包步骤

1. 确保已安装全部依赖：
    ```bash
    pip install -r requirements.txt
    ```
2. 执行打包命令（需提前准备 `app.ico` 图标 或 使用自带的 `main.ico`）：
    ```bash
    pyinstaller --onefile --icon=main.ico main.py -n "CODM_Sensitivity_Tool"
    ```
3. 生成的exe文件位于 `dist` 目录

---

## :mag: 程序细节

- **注册表路径**：`HKEY_CURRENT_USER\SOFTWARE\Tencent\Call-of-Duty`
- **匹配规则**：使用正则表达式筛选目标键值：
  ```regex
  ^CODM_\d+_iMSDK_CN_(PVE|PVP|TD|Br|PVEFiring|PVPFiring|TDFiring|BrFiring)(_(?:RotateSensitive|AimRotate|ReddotHolo|Sniper|Free|ACOG|[\dX]+|SkyVehicle|GroundVehicle|Vertical|Ult).*?)?_h\d+$
---

## :warning: 注意事项

1. **必须使用管理员权限运行**，否则无法修改注册表
2. 游戏更新后可能导致配置失效，需重新运行工具
3. 安全软件处理建议：
    - 临时关闭实时防护
    - 将exe文件添加到白名单
4. 首次使用建议通过注册表编辑器备份相关路径：
   ```reg
   HKEY_CURRENT_USER\SOFTWARE\Tencent\Call-of-Duty

---

:information_source: **重要说明**  
程序运行后若提示`[修改已修改完毕]`，表示所有符合条件的注册表键值已处理完成。建议重启游戏以使修改生效。
---

## :book: 开源协议

本项目基于 **[MIT License](LICENSE)** 开源，您可享有以下权利：

- :white_check_mark: **自由使用**：可无限制用于个人/学习用途
- :white_check_mark: **二次开发**：允许修改源代码并创建衍生版本
- :white_check_mark: **代码分发**：可自由分享源码或编译后的程序

**唯一约束**：  
:information_source: 二次分发时必须包含原始许可证文件及作者声明（见源码文件头部注释）

---

## :sparkles: 支持与贡献

### 问题反馈与建议

[![GitHub Issues](https://img.shields.io/github/issues/DreamChaserWhatever/regedit_CallofDuty?color=blue)](https://github.com/DreamChaserWhatever/regedit_CallofDuty/issues)

1. 遇到BUG?请提交 [Issue](https://github.com/DreamChaserWhatever/regedit_CallofDuty/issues) 并提供：
    - 错误截图/日志
    - 操作系统版本
    - 游戏客户端版本

### 代码贡献

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/DreamChaserWhatever/regedit_CallofDuty/pulls)

1. Fork 本仓库并创建新分支
2. 提交代码变更（请附带测试说明）
3. 发起 Pull Request 至 `dev` 分支

### 开发者联系

- :tv: **Bilibili**：[一面墙的双脚](https://space.bilibili.com/3546759762545419)（这位大佬找到的）
- :tv: **Bilibili**：[DC随便](https://space.bilibili.com/3493117248407780)（我只是写代码的那位）
- :octocat: **GitHub**：[DreamChaserWhatever](https://github.com/DreamChaserWhatever)

> 如果本项目对你有帮助，请点击右上角 :sparkles: **Star** 支持开发者持续更新！