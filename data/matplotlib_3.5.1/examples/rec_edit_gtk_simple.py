{
  "children": [
    {
      "data": {
        "ce_status": "None",
        "entries": [
          [
            "\"\"\"\nLoad a CSV file into a record array and edit it in a gtk treeview\n\"\"\"",
            "",
            "sd"
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
            "gtk",
            null,
            "nn"
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
            "numpy",
            "numpy",
            "nn"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "as",
            null,
            "k"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "np",
            "numpy",
            "nn"
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
            "matplotlib",
            "matplotlib",
            "nn"
          ],
          [
            ".",
            "",
            "nn"
          ],
          [
            "mlab",
            "matplotlib.mlab",
            "nn"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "as",
            null,
            "k"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "mlab",
            "matplotlib.mlab",
            "nn"
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
            "matplotlib",
            "matplotlib",
            "nn"
          ],
          [
            ".",
            "",
            "nn"
          ],
          [
            "cbook",
            "matplotlib.cbook",
            "nn"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "as",
            null,
            "k"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "cbook",
            "matplotlib.cbook",
            "nn"
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
            "mpl_toolkits",
            "mpl_toolkits",
            "nn"
          ],
          [
            ".",
            "",
            "nn"
          ],
          [
            "gtktools",
            null,
            "nn"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "as",
            null,
            "k"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "gtktools",
            null,
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
            "datafile",
            "io.TextIOWrapper",
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
            "cbook",
            "matplotlib.cbook",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "get_sample_data",
            "matplotlib.cbook.get_sample_data",
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
            "demodata.csv",
            "",
            "s1"
          ],
          [
            "'",
            "",
            "s1"
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
            "asfileobj",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "False",
            null,
            "kc"
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
            "r",
            null,
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
            "mlab",
            "matplotlib.mlab",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "csv2rec",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "datafile",
            "io.TextIOWrapper",
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
            "converterd",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "{",
            "",
            ""
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "weekdays",
            null,
            "s1"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            ":",
            "",
            ""
          ],
          [
            "str",
            "builtins.str",
            "nb"
          ],
          [
            "}",
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
            "\n",
            "",
            ""
          ],
          [
            "liststore",
            null,
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
            "treeview",
            null,
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
            "win",
            null,
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
            "gtktools",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "edit_recarray",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "r",
            null,
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
            "win",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "set_title",
            null,
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
            "click to edit",
            "",
            "s1"
          ],
          [
            "'",
            "",
            "s1"
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
            "win",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "connect",
            null,
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
            "delete-event",
            "",
            "s1"
          ],
          [
            "'",
            "",
            "s1"
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
            "lambda",
            null,
            "k"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "*",
            "",
            "o"
          ],
          [
            "args",
            "builtins.tuple",
            ""
          ],
          [
            ":",
            "",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "gtk",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "main_quit",
            null,
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
            "gtk",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "main",
            null,
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
          ]
        ],
        "out": ""
      },
      "type": "Code"
    }
  ],
  "title": null
}