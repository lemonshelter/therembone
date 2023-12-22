import keyboard
import time
from math import floor
import random

# プログラムを継続するかどうかのフラグ
running = True

class MIDI_Preprocess:
    def __init__(self):
        self.upper_lim_of_hand = 400.0
        self.lower_lim_of_hand = 20.0
        self.octave_flag = 1
        self.hand_position = 0
        self.raw_hand_distance = 120.0
    
    def set_upper_lim_of_hand(self):
        self.upper_lim_of_hand = self.raw_hand_distance
    
    def set_lower_lim_of_hand(self):
        self.lower_lim_of_hand = self.raw_hand_distance
    
    def set_raw_hand_distance(self, raw_hand_distance):
        self.raw_hand_distance = raw_hand_distance
        
    def set_octave(self, octave):
        self.octave = octave
        
    # 手の距離の生数値をhand_positionへ変換
    def distance2hand_position(self):
        # 変換処理
        self.hand_position = ((self.raw_hand_distance-self.lower_lim_of_hand)/(self.upper_lim_of_hand-self.lower_lim_of_hand))*65536
    # hand_positonの範囲をきめる
    def limit_hand_position_within_range(self,raw_hand_distance):
         # 手の距離（raw_hand_distance）が上限値より大きい場合
        if self.raw_hand_distance > self.upper_lim_of_hand:
            self.hand_position =  65536.0 # hand_positionの最大値を代入

        # 手の距離（raw_hand_distance）が下限値より小さい場合
        elif self.raw_hand_distance < self.lower_lim_of_hand:
            self.hand_position = 0.0 # hand_positionの最小値を代入

    # hand_position, octave_flagをもとに, root_pitch, pitch_bendの値へ変換
    def convet2rootpitch_and_pitchbend(self):
        # 遊びを含めてA#~Dまでの何番目か
        nth_root = self.hand_position // 4096
        pitch_bend_val = floor(self.hand_position - nth_root*4096)
        if self.octave_flag == 0:  # 音量オフ
            root_pitch = 0
            pitch_bend_val = 0
        else:
            root_pitch = int((self.octave_flag+3) * 12 + (nth_root-2))
            
        return root_pitch, pitch_bend_val
    
    def on_key_press(self,key):
        try:
            if key.name == 'u':# uキーが押された際に上限値を設定
                print("Uキーが押されました。")
                if self.raw_hand_distance > self.lower_lim_of_hand:
                    self.set_upper_lim_of_hand()
                    print("上限値", self.upper_lim_of_hand)
                else:# 更新する値が下限値より小さい場合
                    print("上限値を更新できませんでした。")

            elif key.name == 'l':# lキーが押された際に下限値を設定
                print("Lキーが押されました。")
                if self.raw_hand_distance < self.upper_lim_of_hand:
                    self.set_lower_lim_of_hand()
                    print("下限値", self.lower_lim_of_hand)
                else:# 更新する値が上限値より大きい場合
                    print("下限値を更新できませんでした。")

            elif key.name == 't': # 変数情報の表示
                print("手の位置(mm)",self.raw_hand_distance)
                print("上限値", self.upper_lim_of_hand)
                print("下限値", self.lower_lim_of_hand)
                print(f"{root_pitch=}, {pitch_bend_val=},{self.hand_position=}")

            elif key.name == 'i': # 手の位置(raw_hand_distance)をキーボード入力
                raw_hand_distance_input = input("数字を入力してください: ")
                self.set_raw_hand_distance(float(raw_hand_distance_input))

            elif key.name == 'esc': # escでプログラムを終了
                print("ESCキーが押されました。プログラムを終了します。")
                running = False  # ループを終了するためにフラグを変更

        except AttributeError:
            pass  # キーにname属性がない場合の例外処理
    
    def bind_keys(self):
        keyboard.on_press(self.on_key_press)# キー押下イベントに関数をバインド
    
if __name__ == "__main__":
    midi_shori = MIDI_Preprocess()
    midi_shori.bind_keys()
    # メインループ(仮)
    try:
        while running:
            #手の位置をリアルタイムで取得
            #midi_shori.set_raw_hand_distance()
            midi_shori.distance2hand_position()
            midi_shori.limit_hand_position_within_range(midi_shori.raw_hand_distance)
            midi_shori.set_octave(2)
            root_pitch, pitch_bend_val = midi_shori.convet2rootpitch_and_pitchbend()
            time.sleep(0.1) # キーの連続検出を防ぐための遅延
    except KeyboardInterrupt:
        pass    # キーボード割り込みが発生した場合もプログラムを終了