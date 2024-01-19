from recognize_finger import RecognizeFinger
from distance_sensor import DistanceSensor
from MIDI_process import MIDI_Process
from MIDI2sound import MIDI2Sound

recognize_finger = RecognizeFinger()
distance_sensor = DistanceSensor()
midi_process = MIDI_Process()
midi2sound = MIDI2Sound()

midi_process.bind_keys()

while True:
    """
    指のクラス分類
    """
    
    
    """
    距離測定
    """
    # 距離の生データを受け取り
    #midi_process.set_raw_hand_distance(111) # (仮)
    
    
    """
    MIDI処理
    """
    # 距離データをhand_positionに
    midi_process.distance2hand_position()
    # hand_positionをroot_pitchとpitch_bend_valへ変換
    midi_process.convert2rootpitch_and_pitchbend()
    root_pitch = midi_process.get_root_pitch()
    pitch_bend_val = midi_process.get_pitch_bend_val()
    
    
    """
    MIDIから音声合成
    """
    # 音を合成
    midi2sound.play_continuously(root_pitch, pitch_bend_val)