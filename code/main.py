import math
import tkinter as tk
from random import randint

class GameWheel:
    
    def __init__( self, root ):
        self.root = root
        self.root.title("大儿帮我选一下")
        
        self.canvas_size = 400
        self.wheel_size = 300
        
        self.canvas = tk.Canvas(root, width = self.canvas_size, height = self.canvas_size, bg = "white")
        self.canvas.pack( )
        
        self.spin_button = tk.Button(root, text = "旋转", command = self.spin_wheel, font = ("仿宋", 12))
        self.spin_button.pack(pady = 10)
        
        # 初始化游戏选项
        self.game_options = ["永劫无间", "台球", "raft", "英雄联盟", "天启派对", "收获日2", "大富翁"]
        
        # 初始化选择的游戏为None
        self.selected_game = None
    
    def draw_wheel( self, active_sector = None ):
        # 绘制一个圆形轮盘
        self.canvas.create_oval((self.canvas_size - self.wheel_size) / 2,
                                (self.canvas_size - self.wheel_size) / 2,
                                (self.canvas_size + self.wheel_size) / 2,
                                (self.canvas_size + self.wheel_size) / 2,
                                outline = "black", width = 2)
        
        # 绘制扇形表示游戏选项
        start_angle = 0
        angle = 360 / len(self.game_options)
        for game_option in self.game_options:
            end_angle = start_angle + angle
            fill_color = "lightblue" if active_sector is None or game_option != self.game_options[
                active_sector] else "yellow"
            self.canvas.create_arc((self.canvas_size - self.wheel_size) / 2,
                                   (self.canvas_size - self.wheel_size) / 2,
                                   (self.canvas_size + self.wheel_size) / 2,
                                   (self.canvas_size + self.wheel_size) / 2,
                                   start = start_angle, extent = angle,
                                   outline = "black", width = 2, fill = fill_color)
            # 计算扇形中心位置
            center_angle = (start_angle + end_angle) / 2
            center_angle %= 360  # 确保角度在合适的范围内
            center_x = (self.canvas_size / 2) + ((self.wheel_size / 2) - 50) * math.cos(
                math.radians(center_angle))
            center_y = (self.canvas_size / 2) - ((self.wheel_size / 2) - 50) * math.sin(
                math.radians(center_angle))
            # 在扇形中心位置显示游戏名称
            self.canvas.create_text(center_x, center_y, text = game_option, font = ("仿宋", 12, "bold"),
                                    fill = "black")
            
            start_angle = end_angle
    
    def spin_wheel( self ):
        # 清空画布
        self.canvas.delete("all")
        
        # 随机选择一个游戏
        self.selected_game = self.game_options[randint(0, len(self.game_options) - 1)]
        
        # 计算选中的游戏在转盘中的位置
        selected_index = self.game_options.index(self.selected_game)
        angle_per_sector = 360 / len(self.game_options)
        target_angle = 360 * 5 + (selected_index + 1) * angle_per_sector  # 5圈再到达目标位置
        current_angle = 0
        
        # 逐渐减速直到停止
        while current_angle < target_angle:
            self.draw_wheel(active_sector = int(current_angle // angle_per_sector) % len(self.game_options))
            self.canvas.update( )
            self.canvas.after(int(50 * current_angle / target_angle) + 1)  # 增加延迟，让速度逐渐减慢
            current_angle += 50  # 旋转速度，可以根据需要调整
        
        # 显示最终结果
        self.canvas.create_text(self.canvas_size / 2, self.canvas_size / 2, text = self.selected_game,
                                font = ("仿宋", 16, "bold"), fill = "red")

if __name__ == "__main__":
    root = tk.Tk( )
    app = GameWheel(root)
    app.draw_wheel( )
    root.mainloop( )