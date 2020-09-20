from argparse import ArgumentParser
from comprende.util import analyze_file
from comprende.core.comprende import ModuleTypes, ALL_MODULES
from comprende.core.types import Question
from attr import asdict
from json import dumps


def main():
    parser = ArgumentParser()
    parser.add_argument(
        'file', help="the file to analyze",
    )

    parser.add_argument(
        '-l',
        '--local',
        help="look for the file in comprende/tests/data",
        action='store_true',
    )

    parser.add_argument(
        '-m',
        '--modules',
        nargs='+',
        choices=list(ModuleTypes),
        type=ModuleTypes.from_string,
    )

    parser.add_argument(
        '-c',
        '--count',
        type=int,
        default=1
    )

    parser.add_argument(
        '-d',
        '--debug',
        action='store_true',
    )

    args = parser.parse_args()

    kwargs = {}
    if not args.local:
        kwargs['local_data'] = False
    kwargs['modules'] = (
        ALL_MODULES if not args.modules
        else [m.value for m in args.modules]
    )
    kwargs['desired_ct'] = args.count
    kwargs['debug'] = args.debug

    results = analyze_file(
        args.file,
        **kwargs,
    )

    return Question.as_json(*results)


if __name__ == '__main__':
    print(main())
