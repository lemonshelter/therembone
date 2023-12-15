import keyboard
class MIDI_Preprocess:
    def __init__(self):
        self.upper_lim_of_hand = 100
        self.lower_lim_of_hand = 0
        self.octave_flag = 0
        self.hand_position = 0
    
    def set_upper_lim_of_hand(self):
        self.upper_lim_of_hand = self.hand_position
    
    def set_lower_lim_of_hand(self):
        self.lower_lim_of_hand = self.hand_position
    
    def set_octave(self, octave):
        self.octave = octave
        
    # 手の距離の生数値をhand_positionへ変換
    def distance2hand_position(self, raw_hand_distance):
        pass  # 変換処理
        nanika = 0
        self.hand_position = nanika
    
    # hand_position, octave_flagをもとに, root_pitch, pitch_bendの値へ変換
    def convet2rootpitch_and_pitchbend(self):
        # 遊びを含めてA#~Dまでの何番目か
        nth_root = self.hand_position // 4096
        pitch_bend_val = self.hand_position - nth_root*4096
        if self.octave_flag == 0:  # 音量オフ
            root_pitch = 0
            pitch_bend_val = 0
        else:
            root_pitch = (self.octave_flag+3) * 12 + (nth_root-2)
            
        return root_pitch, pitch_bend_val
    
    def bind_keys(self):
        keyboard.on_press_key("u", lambda _: self.set_upper_lim_of_hand())
        keyboard.on_press_key("l", lambda _: self.set_lower_lim_of_hand())
    
if __name__ == "__main__":
    midi_shori = MIDI_Preprocess()
    midi_shori.bind_keys()
    midi_shori.set_lower_lim_of_hand()
    midi_shori.set_upper_lim_of_hand()
    midi_shori.set_upper_lim_of_hand()
    midi_shori.set_octave(2)
    midi_shori.distance2hand_position(126)
    root_pitch, pitch_bend_val = midi_shori.convet2rootpitch_and_pitchbend()