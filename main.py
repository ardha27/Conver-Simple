import argparse
from conver_utils.infer import voice_change

def main():
    parser = argparse.ArgumentParser(description='Change voice using specified parameters')
    parser.add_argument('--voice_model', '-vm', type=str, required=True, help='Voice model name')
    parser.add_argument('--main_vocals', '-mv', type=str, required=True, help='Main vocals audio file path')
    parser.add_argument('--ai_vocals_path', '-ap', type=str, help='AI-generated vocals audio file path', default='output.mp3')
    parser.add_argument('--pitch_change', '-pc', type=int, required=True, help='Pitch change value')
    parser.add_argument('--f0_method', '-f0', type=str, help='F0 method', default='rmvpe')
    parser.add_argument('--index_rate', '-ir', type=float, help='Index rate', default=0.5)
    parser.add_argument('--filter_radius', '-fr', type=int, help='Filter radius', default=3)
    parser.add_argument('--rms_mix_rate', '-rmr', type=float, help='RMS mix rate', default=0.25)
    parser.add_argument('--protect', '-p', type=float, help='Protect value', default=0.33)
    parser.add_argument('--crepe_hop_length', '-chl', type=int, help='Crepe hop length', default=128)

    args = parser.parse_args()

    voice_change(
        args.voice_model, args.main_vocals, args.ai_vocals_path, args.pitch_change,
        args.f0_method, args.index_rate, args.filter_radius, args.rms_mix_rate,
        args.protect, args.crepe_hop_length
    )

if __name__ == '__main__':
    main()
