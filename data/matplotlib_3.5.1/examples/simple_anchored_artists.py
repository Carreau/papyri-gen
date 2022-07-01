{
  "children": [
    {
      "data": {
        "ce_status": "execed",
        "entries": [
          {
            "link": {
              "data": "\"\"\"\n=======================\nSimple Anchored Artists\n=======================\n\nThis example illustrates the use of the anchored helper classes found in\n:mod:`matplotlib.offsetbox` and in :mod:`mpl_toolkits.axes_grid1`.\nAn implementation of a similar figure, but without use of the toolkit,\ncan be found in :doc:`/gallery/misc/anchored_artists`.\n\"\"\"",
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
                "anchor": null,
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
                "anchor": null,
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
                "anchor": null,
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.draw_text",
                  "version": "*"
                },
                "value": "draw_text"
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
              "data": "ax",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\"\"\"\n    Draw two text-boxes, anchored by different corners to the upper-left\n    corner of the figure.\n    \"\"\"",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "from",
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
                "anchor": null,
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.offsetbox",
                  "version": "*"
                },
                "value": "offsetbox"
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.offsetbox.AnchoredText",
                  "version": "*"
                },
                "value": "AnchoredText"
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.offsetbox.AnchoredText",
                  "version": "*"
                },
                "value": "at"
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.offsetbox.AnchoredText",
                  "version": "*"
                },
                "value": "AnchoredText"
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
              "data": "\"",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "Figure 1a",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "\"",
              "type": "str"
            },
            "type": "s2"
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
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "                      ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "loc",
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
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "upper left",
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
              "data": "prop",
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
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "builtins",
                  "path": "builtins.dict",
                  "version": "*"
                },
                "value": "dict"
              },
              "type": "Link"
            },
            "type": "nb"
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
              "data": "size",
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
              "data": "8",
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
              "data": "frameon",
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
              "data": ",",
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
              "data": "                      ",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.offsetbox.AnchoredText",
                  "version": "*"
                },
                "value": "at"
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.patches.FancyBboxPatch",
                  "version": "*"
                },
                "value": "patch"
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.patches.FancyBboxPatch.set_boxstyle",
                  "version": "*"
                },
                "value": "set_boxstyle"
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
              "data": "\"",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "round,pad=0.,rounding_size=0.2",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "\"",
              "type": "str"
            },
            "type": "s2"
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
              "data": "    ",
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
              "data": "add_artist",
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.offsetbox.AnchoredText",
                  "version": "*"
                },
                "value": "at"
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
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.offsetbox.AnchoredText",
                  "version": "*"
                },
                "value": "at2"
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.offsetbox.AnchoredText",
                  "version": "*"
                },
                "value": "AnchoredText"
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
              "data": "\"",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "Figure 1(b)",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "\"",
              "type": "str"
            },
            "type": "s2"
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
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "                       ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "loc",
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
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "lower left",
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
              "data": "prop",
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
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "builtins",
                  "path": "builtins.dict",
                  "version": "*"
                },
                "value": "dict"
              },
              "type": "Link"
            },
            "type": "nb"
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
              "data": "size",
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
              "data": "8",
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
              "data": "frameon",
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
              "data": ",",
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
              "data": "                       ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "bbox_to_anchor",
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
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "0.",
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
              "data": "1.",
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
              "data": ",",
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
              "data": "                       ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "bbox_transform",
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
              "data": "transAxes",
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
              "data": "                       ",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.offsetbox.AnchoredText",
                  "version": "*"
                },
                "value": "at2"
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.patches.FancyBboxPatch",
                  "version": "*"
                },
                "value": "patch"
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.patches.FancyBboxPatch.set_boxstyle",
                  "version": "*"
                },
                "value": "set_boxstyle"
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
              "data": "\"",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "round,pad=0.,rounding_size=0.2",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "\"",
              "type": "str"
            },
            "type": "s2"
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
              "data": "    ",
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
              "data": "add_artist",
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.offsetbox.AnchoredText",
                  "version": "*"
                },
                "value": "at2"
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
              "data": "\n",
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.draw_circle",
                  "version": "*"
                },
                "value": "draw_circle"
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
              "data": "ax",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\"\"\"\n    Draw a circle in axis coordinates\n    \"\"\"",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "from",
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "mpl_toolkits",
                  "path": "mpl_toolkits",
                  "version": "*"
                },
                "value": "mpl_toolkits"
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "mpl_toolkits",
                  "path": "mpl_toolkits.axes_grid1",
                  "version": "*"
                },
                "value": "axes_grid1"
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "mpl_toolkits",
                  "path": "mpl_toolkits.axes_grid1.anchored_artists",
                  "version": "*"
                },
                "value": "anchored_artists"
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "mpl_toolkits",
                  "path": "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea",
                  "version": "*"
                },
                "value": "AnchoredDrawingArea"
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "from",
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
                "anchor": null,
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.patches",
                  "version": "*"
                },
                "value": "patches"
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.patches.Circle",
                  "version": "*"
                },
                "value": "Circle"
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "mpl_toolkits",
                  "path": "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea",
                  "version": "*"
                },
                "value": "ada"
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "mpl_toolkits",
                  "path": "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea",
                  "version": "*"
                },
                "value": "AnchoredDrawingArea"
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
              "data": "20",
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
              "data": "20",
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
              "data": "0",
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
              "data": "0",
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
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "                              ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "loc",
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
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "upper right",
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
              "data": "pad",
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
              "data": "0.",
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
              "data": "frameon",
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
              "data": "False",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.patches.Circle",
                  "version": "*"
                },
                "value": "p"
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.patches.Circle",
                  "version": "*"
                },
                "value": "Circle"
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
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "10",
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
              "data": "10",
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
              "data": "10",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "mpl_toolkits",
                  "path": "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea",
                  "version": "*"
                },
                "value": "ada"
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.offsetbox.DrawingArea",
                  "version": "*"
                },
                "value": "da"
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.offsetbox.DrawingArea.add_artist",
                  "version": "*"
                },
                "value": "add_artist"
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
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.patches.Circle",
                  "version": "*"
                },
                "value": "p"
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
              "data": "    ",
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
              "data": "add_artist",
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "mpl_toolkits",
                  "path": "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea",
                  "version": "*"
                },
                "value": "ada"
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
              "data": "\n",
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.draw_ellipse",
                  "version": "*"
                },
                "value": "draw_ellipse"
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
              "data": "ax",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\"\"\"\n    Draw an ellipse of width=0.1, height=0.15 in data coordinates\n    \"\"\"",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "from",
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "mpl_toolkits",
                  "path": "mpl_toolkits",
                  "version": "*"
                },
                "value": "mpl_toolkits"
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "mpl_toolkits",
                  "path": "mpl_toolkits.axes_grid1",
                  "version": "*"
                },
                "value": "axes_grid1"
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "mpl_toolkits",
                  "path": "mpl_toolkits.axes_grid1.anchored_artists",
                  "version": "*"
                },
                "value": "anchored_artists"
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "mpl_toolkits",
                  "path": "mpl_toolkits.axes_grid1.anchored_artists.AnchoredEllipse",
                  "version": "*"
                },
                "value": "AnchoredEllipse"
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "mpl_toolkits",
                  "path": "mpl_toolkits.axes_grid1.anchored_artists.AnchoredEllipse",
                  "version": "*"
                },
                "value": "ae"
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "mpl_toolkits",
                  "path": "mpl_toolkits.axes_grid1.anchored_artists.AnchoredEllipse",
                  "version": "*"
                },
                "value": "AnchoredEllipse"
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
              "data": "transData",
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
              "data": "width",
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
              "data": "height",
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
              "data": "0.15",
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
              "data": "angle",
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
              "data": "0.",
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
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "                         ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "loc",
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
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "lower left",
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
              "data": "pad",
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
              "data": "0.5",
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
              "data": "borderpad",
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
              "data": "0.4",
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
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "                         ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "frameon",
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
              "data": "add_artist",
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "mpl_toolkits",
                  "path": "mpl_toolkits.axes_grid1.anchored_artists.AnchoredEllipse",
                  "version": "*"
                },
                "value": "ae"
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
              "data": "\n",
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.draw_sizebar",
                  "version": "*"
                },
                "value": "draw_sizebar"
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
              "data": "ax",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\"\"\"\n    Draw a horizontal bar with length of 0.1 in data coordinates,\n    with a fixed label underneath.\n    \"\"\"",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "from",
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "mpl_toolkits",
                  "path": "mpl_toolkits",
                  "version": "*"
                },
                "value": "mpl_toolkits"
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "mpl_toolkits",
                  "path": "mpl_toolkits.axes_grid1",
                  "version": "*"
                },
                "value": "axes_grid1"
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "mpl_toolkits",
                  "path": "mpl_toolkits.axes_grid1.anchored_artists",
                  "version": "*"
                },
                "value": "anchored_artists"
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "mpl_toolkits",
                  "path": "mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar",
                  "version": "*"
                },
                "value": "AnchoredSizeBar"
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "mpl_toolkits",
                  "path": "mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar",
                  "version": "*"
                },
                "value": "asb"
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "mpl_toolkits",
                  "path": "mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar",
                  "version": "*"
                },
                "value": "AnchoredSizeBar"
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
              "data": "transData",
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
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "                          ",
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
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "                          ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "r",
              "type": "str"
            },
            "type": "sa"
          },
          {
            "link": {
              "data": "\"",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "1$^",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "{",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "\\",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "prime}$",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "\"",
              "type": "str"
            },
            "type": "s2"
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
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "                          ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "loc",
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
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "lower center",
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
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "                          ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "pad",
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
              "data": "borderpad",
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
              "data": "0.5",
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
              "data": "sep",
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
              "data": "5",
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
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "                          ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "frameon",
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
              "data": "False",
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
              "data": "    ",
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
              "data": "add_artist",
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "mpl_toolkits",
                  "path": "mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar",
                  "version": "*"
                },
                "value": "asb"
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
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
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
                "anchor": null,
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
                "anchor": null,
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
              "data": "set_aspect",
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
              "data": "1.",
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
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.draw_text",
                  "version": "*"
                },
                "value": "draw_text"
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
              "data": "ax",
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.draw_circle",
                  "version": "*"
                },
                "value": "draw_circle"
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
              "data": "ax",
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.draw_ellipse",
                  "version": "*"
                },
                "value": "draw_ellipse"
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
              "data": "ax",
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
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.draw_sizebar",
                  "version": "*"
                },
                "value": "draw_sizebar"
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
              "data": "ax",
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
              "data": {
                "anchor": null,
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
                "anchor": null,
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
          "path": "ex-simple_anchored_artists.py-0.png",
          "version": "3.5.1"
        }
      },
      "type": "Fig"
    }
  ],
  "level": 0,
  "target": null,
  "title": null
}