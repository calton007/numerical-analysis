# numerical-analysis

数值分析练习脚本集合，已迁移到 Python 3，可在当前环境直接运行。

## 环境要求

- Python 3.14
- NumPy

安装依赖：

```powershell
python -m pip install -r requirements.txt
```

## 运行方式

每个 `NA*.py` 文件都是独立脚本，可以单独运行。

运行单个脚本：

```powershell
python .\NA01_14.py
```

运行全部脚本：

```powershell
Get-ChildItem -Filter NA*.py | Sort-Object Name | ForEach-Object {
    Write-Host "RUN $($_.Name)"
    python $_.FullName
    if ($LASTEXITCODE -ne 0) {
        throw "$($_.Name) failed with exit code $LASTEXITCODE"
    }
}
```

## 脚本说明

| 文件 | 内容 |
|---|---|
| `NA01_14.py` | 追赶法求解线性方程组 |
| `NA01_15_01.py` | 顺序消元法可行性检查 |
| `NA01_15_02.py` | 列主元高斯消元法 |
| `NA02_19_Jacobi.py` | Jacobi 迭代法 |
| `NA02_19_GaussSeidel.py` | Gauss-Seidel 迭代法 |
| `NA02_19_SOR.py` | SOR 迭代法 |
| `NA02_19_Grad.py` | 最速下降法 |
| `NA03_8.py` | 幂法 |
| `NA04_16.py` | 插值公共函数 |
| `NA04_17_01.py` | 对数函数插值示例 |
| `NA04_17_02.py` | Runge 函数插值示例 |
| `NA05_17_01.py` | Romberg 积分示例 1 |
| `NA05_17_02.py` | Romberg 积分示例 2 |
| `NA05_18.py` | 复合求积示例 |

## 注意事项

`NA01_15_01.py` 运行时可能输出“顺数主子式为0”。这是脚本本身的数学判断结果，不是运行失败。
