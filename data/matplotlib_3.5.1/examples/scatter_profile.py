{
  "children": [
    {
      "data": {
        "ce_status": "None",
        "entries": [
          [
            "#!/usr/bin/env python",
            "",
            "ch"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# -*- noplot -*-",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "\"\"\"\nN       Classic     Base renderer    Ext renderer\n20       0.22           0.14            0.14\n100      0.16           0.14            0.13\n1000     0.45           0.26            0.17\n10000    3.30           1.31            0.53\n50000    19.30          6.53            1.98\n\"\"\"",
            "",
            "sd"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "from",
            null,
            "kn"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "__future__",
            "__future__",
            "nn"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "import",
            null,
            "kn"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "print_function",
            "__future__._Feature",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "import",
            null,
            "kn"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "pylab",
            "pylab",
            "nn"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "import",
            null,
            "kn"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "time",
            "time",
            "nn"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "for",
            null,
            "k"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "N",
            "builtins.int",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "in",
            null,
            "ow"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "20",
            "",
            "mi"
          ],
          [
            ",",
            "",
            ""
          ],
          [
            "100",
            "",
            "mi"
          ],
          [
            ",",
            "",
            ""
          ],
          [
            "1000",
            "",
            "mi"
          ],
          [
            ",",
            "",
            ""
          ],
          [
            "10000",
            "",
            "mi"
          ],
          [
            ",",
            "",
            ""
          ],
          [
            "50000",
            "",
            "mi"
          ],
          [
            ")",
            "",
            ""
          ],
          [
            ":",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "    ",
            "",
            ""
          ],
          [
            "tstart",
            "builtins.float",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "time",
            "time",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "time",
            "time.time",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            ")",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "    ",
            "",
            ""
          ],
          [
            "x",
            "builtins.float",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "0.9",
            "",
            "mf"
          ],
          [
            "*",
            "",
            "o"
          ],
          [
            "pylab",
            "pylab",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "rand",
            "numpy.random.mtrand.RandomState.rand",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "N",
            "builtins.int",
            ""
          ],
          [
            ")",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "    ",
            "",
            ""
          ],
          [
            "y",
            "builtins.float",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "0.9",
            "",
            "mf"
          ],
          [
            "*",
            "",
            "o"
          ],
          [
            "pylab",
            "pylab",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "rand",
            "numpy.random.mtrand.RandomState.rand",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "N",
            "builtins.int",
            ""
          ],
          [
            ")",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "    ",
            "",
            ""
          ],
          [
            "s",
            "builtins.int",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "20",
            "",
            "mi"
          ],
          [
            "*",
            "",
            "o"
          ],
          [
            "pylab",
            "pylab",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "rand",
            "numpy.random.mtrand.RandomState.rand",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "N",
            "builtins.int",
            ""
          ],
          [
            ")",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "    ",
            "",
            ""
          ],
          [
            "pylab",
            "pylab",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "scatter",
            "matplotlib.pyplot.scatter",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "x",
            "builtins.float",
            ""
          ],
          [
            ",",
            "",
            ""
          ],
          [
            "y",
            "builtins.float",
            ""
          ],
          [
            ",",
            "",
            ""
          ],
          [
            "s",
            "builtins.int",
            ""
          ],
          [
            ")",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "    ",
            "",
            ""
          ],
          [
            "print",
            "builtins.print",
            "nb"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "%d",
            "",
            "si"
          ],
          [
            " symbols in ",
            "",
            "s1"
          ],
          [
            "%1.2f",
            "",
            "si"
          ],
          [
            " s",
            "",
            "s1"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "%",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "N",
            "builtins.int",
            ""
          ],
          [
            ",",
            "",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "time",
            "time",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "time",
            "time.time",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            ")",
            "",
            ""
          ],
          [
            "-",
            "",
            "o"
          ],
          [
            "tstart",
            "builtins.float",
            ""
          ],
          [
            ")",
            "",
            ""
          ],
          [
            ")",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ]
        ],
        "out": ""
      },
      "type": "Code"
    }
  ],
  "title": null
}