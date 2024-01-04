<!--
 * @Description: 
 * @Author: shadow221213
 * @Date: 2024-01-05 00:41:14
 * @LastEditTime: 2024-01-05 01:37:53
-->
# <div align="center">转盘</div>

最近和朋友游戏选择困难，决定做个转盘免去纠结

## 使用方法

如果没有pyinstaller库，可使用`pip install pyinstaller`下载pyinstaller库

更改`main.py`中的`self.game_options`的值即可更改转盘每个扇区的显示值

更改后使用`pyinstaller -F -i ./code/turnplate.ico ./code/main.py -w --onefile`即可生成新的exe文件（如果不行将build和dist删掉后重新跑一下即可）