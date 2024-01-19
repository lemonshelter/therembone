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
        self.midi_out.set_instrument(57)

    #音を鳴らす
    def play_note(self, root_pitch, pitch_bend_val):
        self.midi_out.pitch_bend(pitch_bend_val)  # ピッチベンドの値を設定
        self.midi_out.note_on(root_pitch, VELOCITY)  # 音を鳴らす（ピッチ、ベロシティ）
    #音を止める
    def stop_note(self, root_pitch):
        self.midi_out.note_off(root_pitch, 0)

    # Pygameの終了
    def quit(self):
        pygame.midi.quit()


if __name__ == "__main__":
    midi2sound = MIDI2sound()

    midi2sound.play_note(48, 0)
    time.sleep(1)
    midi2sound.stop_note(48)

    for i in range(8192):
        midi2sound.play_note(48, i)
        time.sleep(0.001)
        midi2sound.stop_note(48)

    midi2sound.quit()