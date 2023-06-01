"""
Usage: ``python -m speech_synthesis -m /path/to/model -c /path/to/config -t "text to synthesise" -o /path/to/output.wav``
OR: ``python -m speech_synthesis --model_path /path/to/model --config_path /path/to/config --text "text to synthesise" --output_path /path/to/output.wav``
"""

from argparse import ArgumentParser

from . import load_model, text_to_wav

arg_parser = ArgumentParser()
arg_parser.add_argument(
    "-m", "--model_path", type=str, required=True, help="path to model.pth"
)
arg_parser.add_argument(
    "-c", "--config_path", type=str, required=True, help="path to config.json"
)
arg_parser.add_argument(
    "-t", "--text", type=str, required=True, help="text to synthesise"
)
arg_parser.add_argument(
    "-o", "--output_path", type=str, required=True, help="path to output WAV file"
)

if __name__ == "__main__":
    args = arg_parser.parse_args()

    model = load_model(args.model_path, args.config_path)
    text_to_wav(model, args.text, args.output_path)
