{
  "children": [
    {
      "data": {
        "ce_status": "execed",
        "entries": [
          [
            "\"\"\"\n============\nRainbow text\n============\n\nThe example shows how to string together several text objects.\n\nHistory\n-------\nOn the matplotlib-users list back in February 2012, G\u00f6khan Sever asked the\nfollowing question:\n\n  | Is there a way in matplotlib to partially specify the color of a string?\n  |\n  | Example:\n  |\n  | plt.ylabel(\"Today is cloudy.\")\n  |\n  | How can I show \"today\" as red, \"is\" as green and \"cloudy.\" as blue?\n  |\n  | Thanks.\n\nThe solution below is modified from Paul Ivanov's original answer.\n\"\"\"",
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
            "pyplot",
            "matplotlib.pyplot",
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
            "plt",
            "matplotlib.pyplot",
            "nn"
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
            "transforms",
            "matplotlib.transforms",
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
            "Affine2D",
            "matplotlib.transforms.Affine2D",
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
            "rainbow_text",
            "__main__.rainbow_text",
            "nf"
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
            " ",
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
            " ",
            "",
            ""
          ],
          [
            "strings",
            "builtins.list",
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
            "colors",
            "builtins.list",
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
            "orientation",
            "builtins.str",
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "horizontal",
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
            "\n",
            "",
            ""
          ],
          [
            "                 ",
            "",
            ""
          ],
          [
            "ax",
            "builtins.NoneType",
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "None",
            null,
            "kc"
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
            "*",
            "",
            "o"
          ],
          [
            "*",
            "",
            "o"
          ],
          [
            "kwargs",
            "builtins.dict",
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
            "\"\"\"\n    Take a list of *strings* and *colors* and place them next to each\n    other, with text strings[i] being shown in colors[i].\n\n    Parameters\n    ----------\n    x, y : float\n        Text position in data coordinates.\n    strings : list of str\n        The strings to draw.\n    colors : list of color\n        The colors to use.\n    orientation : {'horizontal', 'vertical'}\n    ax : Axes, optional\n        The Axes to draw into. If None, the current axes will be used.\n    **kwargs\n        All other keyword arguments are passed to plt.text(), so you can\n        set the font size, family, etc.\n    \"\"\"",
            "",
            "sd"
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
            "if",
            null,
            "k"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "ax",
            "builtins.NoneType",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "is",
            null,
            "ow"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "None",
            null,
            "kc"
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
            "        ",
            "",
            ""
          ],
          [
            "ax",
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
            "plt",
            "matplotlib.pyplot",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "gca",
            "matplotlib.pyplot.gca",
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
            "t",
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
            "ax",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "transData",
            null,
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
            "canvas",
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
            "ax",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "figure",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "canvas",
            null,
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
            "    ",
            "",
            ""
          ],
          [
            "assert",
            null,
            "k"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "orientation",
            "builtins.str",
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
            "horizontal",
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
            "vertical",
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
            "if",
            null,
            "k"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "orientation",
            "builtins.str",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "==",
            "",
            "o"
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
            "vertical",
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
            "\n",
            "",
            ""
          ],
          [
            "        ",
            "",
            ""
          ],
          [
            "kwargs",
            "builtins.dict",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "update",
            "builtins.dict.update",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "rotation",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "90",
            "",
            "mi"
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
            "verticalalignment",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "bottom",
            null,
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
            "s",
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
            "c",
            null,
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
            "zip",
            "builtins.zip",
            "nb"
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "strings",
            "builtins.list",
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
            "colors",
            "builtins.list",
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
            "        ",
            "",
            ""
          ],
          [
            "text",
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
            "ax",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "text",
            null,
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
            " ",
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
            " ",
            "",
            ""
          ],
          [
            "s",
            null,
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "+",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "\"",
            "",
            "s2"
          ],
          [
            " ",
            "",
            "s2"
          ],
          [
            "\"",
            "",
            "s2"
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
            "color",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "c",
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
            "transform",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "t",
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
            "*",
            "",
            "o"
          ],
          [
            "*",
            "",
            "o"
          ],
          [
            "kwargs",
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
            "\n",
            "",
            ""
          ],
          [
            "        ",
            "",
            ""
          ],
          [
            "# Need to draw to update the text position.",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "        ",
            "",
            ""
          ],
          [
            "text",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "draw",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "canvas",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "get_renderer",
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
            "        ",
            "",
            ""
          ],
          [
            "ex",
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
            "text",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "get_window_extent",
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
            "        ",
            "",
            ""
          ],
          [
            "if",
            null,
            "k"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "orientation",
            "builtins.str",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "==",
            "",
            "o"
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
            "horizontal",
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
            "\n",
            "",
            ""
          ],
          [
            "            ",
            "",
            ""
          ],
          [
            "t",
            "matplotlib.transforms.Affine2D",
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
            "text",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "get_transform",
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
            " ",
            "",
            ""
          ],
          [
            "+",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "Affine2D",
            "matplotlib.transforms.Affine2D",
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
            ".",
            "",
            "o"
          ],
          [
            "translate",
            "matplotlib.transforms.Affine2D.translate",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "ex",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "width",
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
            "0",
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
            "        ",
            "",
            ""
          ],
          [
            "else",
            null,
            "k"
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
            "            ",
            "",
            ""
          ],
          [
            "t",
            "matplotlib.transforms.Affine2D",
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
            "text",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "get_transform",
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
            " ",
            "",
            ""
          ],
          [
            "+",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "Affine2D",
            "matplotlib.transforms.Affine2D",
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
            ".",
            "",
            "o"
          ],
          [
            "translate",
            "matplotlib.transforms.Affine2D.translate",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "0",
            "",
            "mi"
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
            "ex",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "height",
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
            "words",
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
            "\"",
            "",
            "s2"
          ],
          [
            "all unicorns poop rainbows ! ! !",
            "",
            "s2"
          ],
          [
            "\"",
            "",
            "s2"
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "split",
            "builtins.str.split",
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
            "colors",
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
            "red",
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
            "orange",
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
            "gold",
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
            "lawngreen",
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
            "lightseagreen",
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
            "royalblue",
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
            "\n",
            "",
            ""
          ],
          [
            "          ",
            "",
            ""
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "blueviolet",
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
            "\n",
            "",
            ""
          ],
          [
            "plt",
            "matplotlib.pyplot",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "figure",
            "matplotlib.pyplot.figure",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "figsize",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "6",
            "",
            "mi"
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
            "6",
            "",
            "mi"
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
            "rainbow_text",
            "__main__.rainbow_text",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "0.1",
            "",
            "mf"
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
            "0.05",
            "",
            "mf"
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
            "words",
            "builtins.list",
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
            "colors",
            "builtins.list",
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
            "size",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "18",
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
            "rainbow_text",
            "__main__.rainbow_text",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "0.05",
            "",
            "mf"
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
            "0.1",
            "",
            "mf"
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
            "words",
            "builtins.list",
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
            "colors",
            "builtins.list",
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
            "orientation",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "vertical",
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
            "size",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "18",
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
            "plt",
            "matplotlib.pyplot",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "show",
            "matplotlib.pyplot.show",
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
    },
    {
      "data": {
        "value": "ex-rainbow_text.py-0.png"
      },
      "type": "Fig"
    }
  ],
  "title": null
}