{
  "children": [
    {
      "data": {
        "ce_status": "None",
        "entries": [
          [
            "\"\"\"\ngenerate an editable gtk treeview widget for record arrays with custom\nformatting of the cells and show how to limit string entries to a list\nof strings\n\"\"\"",
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
            "\n",
            "",
            ""
          ],
          [
            "formatd",
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
            "get_formatd",
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
            "formatd",
            null,
            ""
          ],
          [
            "[",
            "",
            ""
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "date",
            null,
            "s1"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "]",
            "",
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
            "FormatDate",
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
            "%",
            "",
            "s1"
          ],
          [
            "Y-",
            "",
            "s1"
          ],
          [
            "%",
            "",
            "s1"
          ],
          [
            "m-",
            "",
            "s1"
          ],
          [
            "%d",
            "",
            "si"
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
            "formatd",
            null,
            ""
          ],
          [
            "[",
            "",
            ""
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "prices",
            null,
            "s1"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "]",
            "",
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
            "FormatMillions",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "precision",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "1",
            "",
            "mi"
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
            "formatd",
            null,
            ""
          ],
          [
            "[",
            "",
            ""
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "gain",
            null,
            "s1"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "]",
            "",
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
            "FormatPercent",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "precision",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "2",
            "",
            "mi"
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
            "# use a drop down combo for weekdays",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "stringd",
            "builtins.dict",
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
            "dict",
            "builtins.dict",
            "nb"
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "weekdays",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "[",
            "",
            ""
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "Sun",
            null,
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
            "'",
            "",
            "s1"
          ],
          [
            "Mon",
            null,
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
            "'",
            "",
            "s1"
          ],
          [
            "Tue",
            null,
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
            "'",
            "",
            "s1"
          ],
          [
            "Wed",
            null,
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
            "'",
            "",
            "s1"
          ],
          [
            "Thu",
            null,
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
            "'",
            "",
            "s1"
          ],
          [
            "Fri",
            null,
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
            "'",
            "",
            "s1"
          ],
          [
            "Sat",
            null,
            "s1"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "]",
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
            "constant",
            "builtins.list",
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
            "[",
            "",
            ""
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "clientid",
            null,
            "s1"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "]",
            "",
            ""
          ],
          [
            "   ",
            "",
            ""
          ],
          [
            "# block editing of this field",
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
            "RecListStore",
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
            "formatd",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "formatd",
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
            "stringd",
            "builtins.dict",
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "stringd",
            "builtins.dict",
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
            "treeview",
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
            "RecTreeView",
            null,
            ""
          ],
          [
            "(",
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
            "constant",
            "builtins.list",
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "constant",
            "builtins.list",
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
            "def",
            null,
            "k"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "mycallback",
            "__main__.mycallback",
            "nf"
          ],
          [
            "(",
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
            "rownum",
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
            "colname",
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
            "oldval",
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
            "newval",
            null,
            ""
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
            "print",
            "builtins.print",
            "nb"
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
            "verify: old=",
            "",
            "s1"
          ],
          [
            "%s",
            "",
            "si"
          ],
          [
            ", new=",
            "",
            "s1"
          ],
          [
            "%s",
            "",
            "si"
          ],
          [
            ", rec=",
            "",
            "s1"
          ],
          [
            "%s",
            "",
            "si"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "%",
            "",
            "o"
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "oldval",
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
            "newval",
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
            "liststore",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "r",
            null,
            ""
          ],
          [
            "[",
            "",
            ""
          ],
          [
            "rownum",
            null,
            ""
          ],
          [
            "]",
            "",
            ""
          ],
          [
            "[",
            "",
            ""
          ],
          [
            "colname",
            null,
            ""
          ],
          [
            "]",
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
            ".",
            "",
            "o"
          ],
          [
            "callbacks",
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
            "cell_changed",
            null,
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
            "mycallback",
            "__main__.mycallback",
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
            "Window",
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
            "add",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "treeview",
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
            "show_all",
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