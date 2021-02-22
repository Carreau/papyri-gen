{
  "children": [
    {
      "data": {
        "ce_status": "execed",
        "entries": [
          [
            "\"\"\"\n======================\nSet and get properties\n======================\n\nThe pyplot interface allows you to use ``setp`` and ``getp`` to\nset and get object properties respectively, as well as to do\nintrospection on the object.\n\nSetting with ``setp``\n=====================\n\nTo set the linestyle of a line to be dashed, you use ``setp``::\n\n  >>> line, = plt.plot([1, 2, 3])\n  >>> plt.setp(line, linestyle='--')\n\nIf you want to know the valid types of arguments, you can provide the\nname of the property you want to set without a value::\n\n  >>> plt.setp(line, 'linestyle')\n      linestyle: {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}\n\nIf you want to see all the properties that can be set, and their\npossible values, you can do::\n\n    >>> plt.setp(line)\n\n``setp`` operates on a single instance or a list of instances.  If you\nare in query mode introspecting the possible values, only the first\ninstance in the sequence is used.  When actually setting values, all\nthe instances will be set.  For example, suppose you have a list of\ntwo lines, the following will make both lines thicker and red::\n\n    >>> x = np.arange(0, 1, 0.01)\n    >>> y1 = np.sin(2*np.pi*x)\n    >>> y2 = np.sin(4*np.pi*x)\n    >>> lines = plt.plot(x, y1, x, y2)\n    >>> plt.setp(lines, linewidth=2, color='r')\n\n\nGetting with ``getp``\n=====================\n\n``getp`` returns the value of a given attribute.  You can use it to query\nthe value of a single attribute::\n\n    >>> plt.getp(line, 'linewidth')\n        0.5\n\nor all the attribute/value pairs::\n\n    >>> plt.getp(line)\n        aa = True\n        alpha = 1.0\n        antialiased = True\n        c = b\n        clip_on = True\n        color = b\n        ... long listing skipped ...\n\nAliases\n=======\n\nTo reduce keystrokes in interactive mode, a number of properties\nhave short aliases, e.g., 'lw' for 'linewidth' and 'mec' for\n'markeredgecolor'.  When calling set or get in introspection mode,\nthese properties will be listed as 'fullname' or 'aliasname'.\n\"\"\"",
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
            "x",
            "numpy.ndarray",
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
            "np",
            "numpy",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "arange",
            "numpy.arange",
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
            "1.0",
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
            "0.01",
            "",
            "mf"
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
            "y1",
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
            "np",
            "numpy",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "sin",
            "numpy.ufunc",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "2",
            "",
            "mi"
          ],
          [
            "*",
            "",
            "o"
          ],
          [
            "np",
            "numpy",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "pi",
            null,
            ""
          ],
          [
            "*",
            "",
            "o"
          ],
          [
            "x",
            "numpy.ndarray",
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
            "y2",
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
            "np",
            "numpy",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "sin",
            "numpy.ufunc",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "4",
            "",
            "mi"
          ],
          [
            "*",
            "",
            "o"
          ],
          [
            "np",
            "numpy",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "pi",
            null,
            ""
          ],
          [
            "*",
            "",
            "o"
          ],
          [
            "x",
            "numpy.ndarray",
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
            "lines",
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
            "plot",
            "matplotlib.pyplot.plot",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "x",
            "numpy.ndarray",
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
            "y1",
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
            "x",
            "numpy.ndarray",
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
            "y2",
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
            "l1",
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
            "l2",
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
            "lines",
            null,
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
            "setp",
            "matplotlib.pyplot.setp",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "lines",
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
            "linestyle",
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
            "--",
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
            "       ",
            "",
            ""
          ],
          [
            "# set both to dashed",
            "",
            "c1"
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
            "setp",
            "matplotlib.pyplot.setp",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "l1",
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
            "linewidth",
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
            "'",
            "",
            "s1"
          ],
          [
            "r",
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
            "  ",
            "",
            ""
          ],
          [
            "# line1 is thick and red",
            "",
            "c1"
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
            "setp",
            "matplotlib.pyplot.setp",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "l2",
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
            "linewidth",
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
            "'",
            "",
            "s1"
          ],
          [
            "g",
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
            "  ",
            "",
            ""
          ],
          [
            "# line2 is thinner and green",
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
            "Line setters",
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
            "setp",
            "matplotlib.pyplot.setp",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "l1",
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
            "Line getters",
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
            "getp",
            "matplotlib.pyplot.getp",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "l1",
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
            "Rectangle setters",
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
            "setp",
            "matplotlib.pyplot.setp",
            ""
          ],
          [
            "(",
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
            ".",
            "",
            "o"
          ],
          [
            "patch",
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
            "Rectangle getters",
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
            "getp",
            "matplotlib.pyplot.getp",
            ""
          ],
          [
            "(",
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
            ".",
            "",
            "o"
          ],
          [
            "patch",
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
            "title",
            "matplotlib.pyplot.title",
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
            "Hi mom",
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
            "Text setters",
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
            "setp",
            "matplotlib.pyplot.setp",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "t",
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
            "Text getters",
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
            "getp",
            "matplotlib.pyplot.getp",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "t",
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
        "value": "ex-set_and_get.py-0.png"
      },
      "type": "Fig"
    }
  ],
  "title": null
}