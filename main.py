import argparse
from conver_utils.infer import voice_change

def main():
    parser = argparse.ArgumentParser(description='Change voice using specified parameters')
    parser.add_argument('--voice_model', type=str, required=True, help='Name of the voice model')
    parser.add_argument('--main_vocals', type=str, required=True, help='Path to the main vocals audio file')
    parser.add_argument('--ai_vocals_path', type=str, required=True, help='Path to save the AI-generated vocals audio file')
    parser.add_argument('--pitch_change', type=int, required=True, help='Pitch change value')
    parser.add_argument('--f0_method', type=str, required=True, help='F0 method')
    parser.add_argument('--index_rate', type=float, required=True, help='Index rate')
    parser.add_argument('--filter_radius', type=int, required=True, help='Filter radius')
    parser.add_argument('--rms_mix_rate', type=float, required=True, help='RMS mix rate')
    parser.add_argument('--protect', type=float, required=True, help='Protect value')
    parser.add_argument('--crepe_hop_length', type=int, required=True, help='Crepe hop length')

    args = parser.parse_args()

    voice_change(
        args.voice_model, args.main_vocals, args.ai_vocals_path, args.pitch_change,
        args.f0_method, args.index_rate, args.filter_radius, args.rms_mix_rate,
        args.protect, args.crepe_hop_length
    )

if __name__ == '__main__':
    main()
