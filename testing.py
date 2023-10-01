from conver_utils.infer import voice_change

voice_model = 'Nagita'
main_vocals = 'richard.mp3'
ai_vocals_path = 'answer_rvc.mp3'
pitch_change = 6
f0_method = 'rmvpe'
index_rate = 0.5
filter_radius = 3
rms_mix_rate = 0.25
protect = 0.33
crepe_hop_length = 128
voice_change(voice_model, main_vocals, ai_vocals_path, pitch_change, f0_method, index_rate, filter_radius, rms_mix_rate, protect, crepe_hop_length)