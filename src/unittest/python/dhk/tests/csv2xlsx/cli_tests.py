#   -*- coding: utf-8 -*-

##############################################################################
# copyrights and license
#
# Copyright (c) 2025 David Harris Kiesel
#
# Licensed under the MIT License. See LICENSE in the project root for license
# information.
##############################################################################

import tempfile
import typing
from unittest import (
    main,
    TestCase,
)

import dhk.csv2xlsx.cli as cli


class Test(TestCase):
    def test_get_parser(
        self: typing.Self
    ) -> None:
        'Test get_parser function.'

        argparser = cli.get_parser()

        with tempfile.NamedTemporaryFile(
            mode='w+'
        ) as csv_file:
            args = \
                argparser.parse_args(
                    [
                        csv_file.name
                    ]
                )

            self.assertEqual(
                args.csv_fd.name,
                csv_file.name
            )


if __name__ == '__main__':
    main()
