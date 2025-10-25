#!/usr/bin/env python3

import sys
import argparse
from pathlib import Path
import logging

from typing import Protocol, cast

__version__ = "2.0.0"


class Args(Protocol):
    """Type hint for parsed arguments"""

    input: Path
    blast_db: Path
    output_name: Path
    evalue: float


def parse_arguments() -> Args:
    """Parse command line arguments"""

    parser = argparse.ArgumentParser(
        description="GLASSgo - Global sRNA homology search tool",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # required arguments
    parser.add_argument(
        "-i",
        "--input",
        required=True,
        type=Path,
        help="Input sequence in FASTA format"
    )
    parser.add_argument(
        "-d",
        "--blast-db",
        required=True,
        type=Path,
        help="BLAST database to search against",
    )

    parser.add_argument(
        "-o",
        "--output_name",
        help="output file",
        type=Path,
        default="stdout"
    )
    parser.add_argument(
        "-e",
        "--evalue",
        help="maximal excepted E-Value",
        type=float,
        default=1
    )

    return cast(Args, parser.parse_args())  # type: ignore[return-value]


def validate_arguments(args: Args) -> None:
    """Validate command line arguments"""

    if not args.input.exists():
        raise FileNotFoundError(f"Input file {args.input} does not exist")

    if not args.blast_db.exists():
        raise FileNotFoundError(f"BLAST database {args.blast_db} does not exist")


def main():
    """Main function to run GLASSgo"""

    args = parse_arguments()
    validate_arguments(args)


if __name__ == "__main__":
    main()
