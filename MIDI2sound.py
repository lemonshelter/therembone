import pygame.midi
import time

VELOCITY = 127

class MIDI2sound:
    def __init__(self):
        # MIDIデバイスの初期化
        pygame.midi.init()

        # MIDIデバイスの取得
        self.device_id = pygame.midi.get_default_output_id()
        self.midi_out = pygame.midi.Output(self.device_id)

        # トロンボーンの音色に設定
        self.midi_out.set_instrument(57, channel=0)
        self.midi_out.set_instrument(57, channel=1)
        
        # play_continuouslyでnote_stopするためにnoteを保持
        self.retained_note = 48

    #音を鳴らす
    def play_note(self, root_pitch, pitch_bend_val, channel):
        self.midi_out.pitch_bend(pitch_bend_val, channel=channel)  # ピッチベンドの値を設定
        self.midi_out.note_on(root_pitch, velocity=VELOCITY, channel=channel)  # 音を鳴らす（ピッチ、ベロシティ）
    #音を止める
    def stop_note(self, root_pitch, channel):
        self.midi_out.note_off(root_pitch, velocity=0, channel=channel)
    
    # 連続で音を鳴らす
    def play_continuously(self, root_pitch, pitch_bend_val):
        self.play_note(root_pitch, pitch_bend_val, channel=0)
        time.sleep(0.05)
        self.stop_note(self.retained_note, channel=1)
        time.sleep(0.2)
        self.play_note(root_pitch, pitch_bend_val, channel=1)
        time.sleep(0.05)
        self.stop_note(root_pitch, channel=0)
        time.sleep(0.2)
        self.retained_note = root_pitch
    
    # 連続演奏を止める
    def stop_continuos_play(self):
        self.stop_note(self.retained_note, channel=1)

    # Pygameの終了
    def quit(self):
        pygame.midi.quit()


if __name__ == "__main__":
    midi2sound = MIDI2sound()

    midi2sound.play_note(48, 0, channel=0)
    time.sleep(1)
    midi2sound.stop_note(48, channel=0)

    # for i in range(10):
    #     midi2sound.play_note(60, 0, channel=0)
    #     time.sleep(0.05)
    #     midi2sound.stop_note(60, channel=1)
    #     print(0)
    #     time.sleep(0.2)
    #     midi2sound.play_note(60, 0, channel=1)
    #     time.sleep(0.05)
    #     midi2sound.stop_note(60, channel=0)
    #     print(1)
    #     time.sleep(0.2)
    
    time.sleep(3)
    
    for i in range(100):
        midi2sound.play_continuously(60, 0)

    midi2sound.quit()