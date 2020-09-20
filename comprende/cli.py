from argparse import ArgumentParser
from comprende.util import analyze_file
from comprende.core.comprende import ModuleTypes, ALL_MODULES
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

    args = parser.parse_args()

    kwargs = {}
    if not args.local:
        kwargs['local_data'] = False
    kwargs['modules'] = (
        ALL_MODULES if not args.modules
        else [m.value for m in args.modules]
    )
    kwargs['desired_ct'] = args.count

    results = analyze_file(
        args.file,
        **kwargs,
    )

    json = dumps([
        asdict(q) for q in results
    ])

    print(json)


if __name__ == '__main__':
    main()
