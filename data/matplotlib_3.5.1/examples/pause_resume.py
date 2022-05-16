{
  "children": [
    {
      "data": {
        "ce_status": "execed",
        "entries": [
          {
            "link": {
              "data": "\"\"\"\n=================================\nPausing and Resuming an Animation\n=================================\n\nThis example showcases:\n\n- using the Animation.pause() method to pause an animation.\n- using the Animation.resume() method to resume an animation.\n\"\"\"",
              "type": "str"
            },
            "type": "sd"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "import",
              "type": "str"
            },
            "type": "kn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib",
                  "version": "*"
                },
                "value": "matplotlib"
              },
              "type": "Link"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.pyplot",
                  "version": "*"
                },
                "value": "pyplot"
              },
              "type": "Link"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "as",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.pyplot",
                  "version": "*"
                },
                "value": "plt"
              },
              "type": "Link"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "import",
              "type": "str"
            },
            "type": "kn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib",
                  "version": "*"
                },
                "value": "matplotlib"
              },
              "type": "Link"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.animation",
                  "version": "*"
                },
                "value": "animation"
              },
              "type": "Link"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "as",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.animation",
                  "version": "*"
                },
                "value": "animation"
              },
              "type": "Link"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "import",
              "type": "str"
            },
            "type": "kn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "numpy",
                  "path": "numpy",
                  "version": "*"
                },
                "value": "numpy"
              },
              "type": "Link"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "as",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "numpy",
                  "path": "numpy",
                  "version": "*"
                },
                "value": "np"
              },
              "type": "Link"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "class",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation",
                  "version": "*"
                },
                "value": "PauseAnimation"
              },
              "type": "Link"
            },
            "type": "nc"
          },
          {
            "link": {
              "data": ":",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "def",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation.__init__",
                  "version": "*"
                },
                "value": "__init__"
              },
              "type": "Link"
            },
            "type": "fm"
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation",
                  "version": "*"
                },
                "value": "self"
              },
              "type": "Link"
            },
            "type": "bp"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ":",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "builtins",
                  "path": "builtins.int",
                  "version": "*"
                },
                "value": "fig"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "ax",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.pyplot",
                  "version": "*"
                },
                "value": "plt"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.pyplot.subplots",
                  "version": "*"
                },
                "value": "subplots"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "ax",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "set_title",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "Click to pause/resume the animation",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "builtins",
                  "path": "builtins.tuple",
                  "version": "*"
                },
                "value": "x"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "numpy",
                  "path": "numpy",
                  "version": "*"
                },
                "value": "np"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "numpy",
                  "path": "numpy.core.function_base.linspace",
                  "version": "*"
                },
                "value": "linspace"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "-",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "0.1",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "0.1",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "1000",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# Start with a normal distribution",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation",
                  "version": "*"
                },
                "value": "self"
              },
              "type": "Link"
            },
            "type": "bp"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "builtins",
                  "path": "builtins.int",
                  "version": "*"
                },
                "value": "n0"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "1.0",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "/",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "4",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "numpy",
                  "path": "numpy",
                  "version": "*"
                },
                "value": "np"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "pi",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "2e-4",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "0.1",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "0.5",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "                   ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "numpy",
                  "path": "numpy",
                  "version": "*"
                },
                "value": "np"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "numpy",
                  "path": "numpy.ufunc",
                  "version": "*"
                },
                "value": "exp"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "-",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "builtins",
                  "path": "builtins.tuple",
                  "version": "*"
                },
                "value": "x"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "2",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "/",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "4",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "2e-4",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "0.1",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation",
                  "version": "*"
                },
                "value": "self"
              },
              "type": "Link"
            },
            "type": "bp"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "p",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "ax",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "plot",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "builtins",
                  "path": "builtins.tuple",
                  "version": "*"
                },
                "value": "x"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation",
                  "version": "*"
                },
                "value": "self"
              },
              "type": "Link"
            },
            "type": "bp"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "builtins",
                  "path": "builtins.int",
                  "version": "*"
                },
                "value": "n0"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation",
                  "version": "*"
                },
                "value": "self"
              },
              "type": "Link"
            },
            "type": "bp"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.animation.FuncAnimation",
                  "version": "*"
                },
                "value": "animation"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.animation",
                  "version": "*"
                },
                "value": "animation"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.animation.FuncAnimation",
                  "version": "*"
                },
                "value": "FuncAnimation"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "            ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "fig",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation",
                  "version": "*"
                },
                "value": "self"
              },
              "type": "Link"
            },
            "type": "bp"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation.update",
                  "version": "*"
                },
                "value": "update"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "frames",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "200",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "interval",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "50",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "blit",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "True",
              "type": "str"
            },
            "type": "kc"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation",
                  "version": "*"
                },
                "value": "self"
              },
              "type": "Link"
            },
            "type": "bp"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "builtins",
                  "path": "builtins.bool",
                  "version": "*"
                },
                "value": "paused"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "False",
              "type": "str"
            },
            "type": "kc"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "fig",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "canvas",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "mpl_connect",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "button_press_event",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation",
                  "version": "*"
                },
                "value": "self"
              },
              "type": "Link"
            },
            "type": "bp"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation.toggle_pause",
                  "version": "*"
                },
                "value": "toggle_pause"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "def",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation.toggle_pause",
                  "version": "*"
                },
                "value": "toggle_pause"
              },
              "type": "Link"
            },
            "type": "nf"
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation",
                  "version": "*"
                },
                "value": "self"
              },
              "type": "Link"
            },
            "type": "bp"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "builtins",
                  "path": "builtins.tuple",
                  "version": "*"
                },
                "value": "args"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "builtins",
                  "path": "builtins.dict",
                  "version": "*"
                },
                "value": "kwargs"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ":",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "if",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation",
                  "version": "*"
                },
                "value": "self"
              },
              "type": "Link"
            },
            "type": "bp"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "builtins",
                  "path": "builtins.bool",
                  "version": "*"
                },
                "value": "paused"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ":",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "            ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation",
                  "version": "*"
                },
                "value": "self"
              },
              "type": "Link"
            },
            "type": "bp"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.animation.FuncAnimation",
                  "version": "*"
                },
                "value": "animation"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.animation.Animation.resume",
                  "version": "*"
                },
                "value": "resume"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "else",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": ":",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "            ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation",
                  "version": "*"
                },
                "value": "self"
              },
              "type": "Link"
            },
            "type": "bp"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.animation.FuncAnimation",
                  "version": "*"
                },
                "value": "animation"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.animation.Animation.pause",
                  "version": "*"
                },
                "value": "pause"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation",
                  "version": "*"
                },
                "value": "self"
              },
              "type": "Link"
            },
            "type": "bp"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "builtins",
                  "path": "builtins.bool",
                  "version": "*"
                },
                "value": "paused"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "not",
              "type": "str"
            },
            "type": "ow"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation",
                  "version": "*"
                },
                "value": "self"
              },
              "type": "Link"
            },
            "type": "bp"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "builtins",
                  "path": "builtins.bool",
                  "version": "*"
                },
                "value": "paused"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "def",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation.update",
                  "version": "*"
                },
                "value": "update"
              },
              "type": "Link"
            },
            "type": "nf"
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation",
                  "version": "*"
                },
                "value": "self"
              },
              "type": "Link"
            },
            "type": "bp"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "i",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ":",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation",
                  "version": "*"
                },
                "value": "self"
              },
              "type": "Link"
            },
            "type": "bp"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "builtins",
                  "path": "builtins.int",
                  "version": "*"
                },
                "value": "n0"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "+",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "i",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "/",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "100",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "%",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "5",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation",
                  "version": "*"
                },
                "value": "self"
              },
              "type": "Link"
            },
            "type": "bp"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "p",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "set_ydata",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation",
                  "version": "*"
                },
                "value": "self"
              },
              "type": "Link"
            },
            "type": "bp"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "builtins",
                  "path": "builtins.int",
                  "version": "*"
                },
                "value": "n0"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "%",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "20",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "return",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation",
                  "version": "*"
                },
                "value": "self"
              },
              "type": "Link"
            },
            "type": "bp"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "p",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation",
                  "version": "*"
                },
                "value": "pa"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.PauseAnimation",
                  "version": "*"
                },
                "value": "PauseAnimation"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.pyplot",
                  "version": "*"
                },
                "value": "plt"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.pyplot.show",
                  "version": "*"
                },
                "value": "show"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          }
        ],
        "out": ""
      },
      "type": "Code2"
    },
    {
      "data": {
        "value": {
          "kind": "assets",
          "module": "matplotlib",
          "path": "ex-pause_resume.py-0.png",
          "version": "3.5.1"
        }
      },
      "type": "Fig"
    }
  ],
  "title": null
}