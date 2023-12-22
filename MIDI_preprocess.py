import keyboard
from math import floor
import random
class MIDI_Preprocess:
    def __init__(self):
        self.upper_lim_of_hand = 400
        self.lower_lim_of_hand = 20
        self.octave_flag = 1
        self.hand_position = 0
        self.raw_hand_distance = 120
    
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
            if key.name == 'u':
                self.set_upper_lim_of_hand()
                print("Uキーが押されました。")
                print("上限値", self.upper_lim_of_hand)
            elif key.name == 'l':
                self.set_lower_lim_of_hand()
                print("Lキーが押されました。")
                print("下限値", self.lower_lim_of_hand)
            elif key.name == 'r':
                self.distance2hand_position()
                print("腕の位置(mm)",)
        except AttributeError:
            pass  # キーにname属性がない場合の例外処理
    
    def bind_keys(self):
      keyboard.on_press(self.on_key_press)
    
if __name__ == "__main__":
    midi_shori = MIDI_Preprocess()
    midi_shori.bind_keys()
    # midi_shori.set_lower_lim_of_hand()
    # midi_shori.set_upper_lim_of_hand()
    # midi_shori.set_upper_lim_of_hand()
    midi_shori.set_octave(2)
    midi_shori.distance2hand_position()
    root_pitch, pitch_bend_val = midi_shori.convet2rootpitch_and_pitchbend()
    print(f"{root_pitch=}, {pitch_bend_val=}")
    keyboard.wait('esc')