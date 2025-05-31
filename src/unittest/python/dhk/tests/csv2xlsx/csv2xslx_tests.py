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

import dhk.csv2xlsx.csv2xlsx as csv2xlsx


class Test(TestCase):
    def test_transform_throws_no_exceptions(
        self: typing.Self
    ) -> None:
        'Test that transform function throws no exceptions.'

        paramss = \
            [
                {
                    'csv_iterable': (
                        '"col1","col2"',
                        '"foo",123',
                        '"bar",456',
                    )
                },
                {
                    'csv_iterable': (
                        '"col1 qwer asfd zxvc qwer asfd zxvc qwer asfd zxvc","col2","col3","col4","col5","col6","col7"',
                        '"foo  qwer asfd zxvc qwer asfd zxvc qwer asfd zxvc qwer asfd zxvc qwer asfd zxvc","foo  qwer asfd zxvc qwer asfd zxvc qwer asfd zxvc qwer asfd zxvc qwer asfd zxvc","true","1970-01-01","1970-01-01 12:59:59","1234","1234"',
                        '"1234","foo","false","1970-01-01","1970-01-01 12:59:59","5678.9","5678.9"',
                    ),
                    'workbook_settings': {
                        "workbook_options": {
                        },
                        "workbook_format": {
                            "font_size": 12,
                            "valign": "top"
                        },
                        "worksheet_settings": {
                            "freeze_panes": [
                                1,
                                0
                            ],
                            "autofilter": [
                                0,
                                0,
                                -1,
                                -1
                            ]
                        },
                        "cell_format_settings": {
                            "header": {
                                "valign": "bottom",
                                "bold": True,
                                "text_wrap": True
                            },
                            "date": {
                                "num_format": "yyyy-mm-dd"
                            },
                            "datetime": {
                                "num_format": "yyyy-mm-dd HH:MM:SS.000"
                            },
                            "num0": {
                                "num_format": "0"
                            },
                            "numc0": {
                                "num_format": "#,##0"
                            },
                            "num2": {
                                "num_format": "0.00"
                            },
                            "numc2": {
                                "num_format": "#,##0.00"
                            },
                            "dollar0": {
                                "num_format": "$#,##0"
                            },
                            "dollar2": {
                                "num_format": "$#,##0.00"
                            },
                            "textwrap": {
                                "text_wrap": True
                            }
                        },
                        "column_settings": [
                            {
                                "width": 40,
                                "cell_format": "textwrap"
                            },
                            {
                                "width": 40
                            },
                            {
                                "data_type": "bool",
                                "width": 10
                            },
                            {
                                "data_type": "date",
                                "width": 20,
                                "cell_format": "date"
                            },
                            {
                                "data_type": "datetime",
                                "width": 40,
                                "cell_format": "datetime"
                            },
                            {
                                "data_type": "decimal",
                                "width": 20,
                                "cell_format": "num0",
                                "options": {
                                    "hidden": True
                                }
                            },
                            {
                                "data_type": "decimal",
                                "width": 20,
                                "cell_format": "dollar2"
                            }
                        ],
                        "row_settings": [
                            {
                                "data_type": "string",
                                "cell_format": "header"
                            }
                        ]
                    }
                },
            ]

        for subtest_number in range(0, len(paramss)):
            with self.subTest(
                i=subtest_number
            ):
                params = paramss[subtest_number]

                csv_iterable = params['csv_iterable']

                workbook_settings = params.get('workbook_settings')

                with tempfile.NamedTemporaryFile(
                    mode='w+'
                ) as tmp_file:
                    workbook_path = tmp_file.name

                    try:
                        csv2xlsx.transform(
                            csv_iterable,
                            workbook_path,
                            workbook_settings=workbook_settings
                        )
                    except Exception:
                        self.fail(
                            'Exception raised on csv2xlsx.transform.'
                        )


if __name__ == '__main__':
    main()
